#!/usr/bin/env python3
"""Year-by-year search for one leader's dated predictions (docs/claims-ledger-method.md,
"Verdicts as small notes, and no rate": the year-by-year search stays).

For each year asked for, one request to the Claude API with the web search and web fetch tools.
The model runs the fixed searches below, may add a few of its own, opens the most promising
pages, and reports any forward-looking, dated words about AI by that person in that year.

This script proposes; it records nothing in the ledger. It writes, per person:

  data/claims-search/<speaker_id>/<year>.json   the model's reply, the tool calls it really
                                                made, the token counts and the cost
  data/claims-search/<speaker_id>-search-rows.csv   one row per search or page opened, in the
                                                columns of data/search_log.csv, with no ids
  data/claims-search/<speaker_id>-candidates.csv    one row per candidate claim

A session then opens each candidate's source, checks the words on the page, and only then
writes the claim file and the search-log rows, as the method requires. Quotes in the candidate
file are the model's reading of a page and are not yet checked.

A year already saved is skipped, so a stopped run can be started again. --redo runs it afresh.

The key is read at run time from ~/.config/sentient-horizons/agi-zeitgeist.env
(ANTHROPIC_API_KEY, the `zeitgeist-coder` key); never printed or written anywhere. The run
draws on the monthly Anthropic API credits; enter its cost in the project's spending record.

    .venv/bin/python scripts/claims_search.py --speaker altman --years 2015-2026
        [--model claude-opus-5-5] [--searches 12] [--pages 6] [--page-tokens 8000]
        [--ceiling 25] [--redo]

--ceiling stops the run before the next year once the money spent passes that many dollars.
"""

import argparse
import csv
import json
import re
import sys
from datetime import date
from pathlib import Path

import anthropic

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
OUT = DATA / "claims-search"
CREDENTIALS = Path.home() / ".config" / "sentient-horizons" / "agi-zeitgeist.env"

# Dollars per million tokens (platform.claude.com/docs/en/about-claude/pricing, read 2026-11-16):
# input, output, 5-minute cache write, cache read. Web search is $10 per 1,000 searches.
PRICES = {
    "claude-opus-5-5": (4.00, 20.00, 5.00, 0.20),
    "claude-sonnet-5-5": (2.00, 10.00, 2.50, 0.10),
}
SEARCH_PRICE = 0.01

# The fixed searches, run for every person and every year, in this order.
FIXED = [
    '"{name}" AI prediction {year}',
    '"{name}" {year} interview AGI "years"',
    '"{name}" {year} AI "by 20" OR "next year" OR "within" OR "end of the decade"',
]

SYSTEM = """You are searching the public record for dated predictions about AI made by one \
named person in one calendar year. Your findings go to a person who will open every source and \
check every word, so accuracy matters more than volume, and "nothing found" is a good answer \
when it is true.

What counts as a candidate. All four must hold:
1. The person said or wrote it in the given year. A later retelling of older words does not \
count for this year; a statement from another year is noted under other_years, not here.
2. The words look forward and are about AI: AI will do, reach or ship something, or will not \
by a stated date. A company's spending, revenue, headcount, chips or data-centre plans are \
business forecasts and stay out. A line framed as a hypothetical ("suppose", "let's imagine") \
stays out.
3. The words carry a date or a length of time: a year, a span ("in five years", "the next \
decade"), or a stage with its own end ("by the end of this decade"). "Soon", "a few years", \
"we are close" are undated: list them under undated only if they are about when AGI or \
superintelligence arrives.
4. You opened a page that carries the words. Prefer the person's own post, essay or filing, \
an official transcript or recording, or a printed question-and-answer interview. If you saw \
the words only in a news report, say so in source_kind.

How to work. Run the fixed searches you are given first, each exactly as written and each \
once. You are told how many searches and page openings you have; every call counts, including a \
repeat, so never run the same search twice. A plain search with a year in it mostly returns \
recent news, so spend your remaining searches on that year's own occasions: the interviews, \
podcasts, conference talks, essays, posts and hearings the person gave that year, by name. Open the pages most likely to hold the \
person's own words. Quote only words you read on a page you opened, exactly as printed; never \
quote from a search snippet or from memory. If a page will not open, say so and do not quote it.

Finish with one fenced json block and nothing after it, in this shape:
{
  "candidates": [{"date_said": "YYYY-MM-DD or YYYY-MM or YYYY", "quote": "exact words", \
"what_is_predicted": "one plain sentence", "date_or_span": "the year or span the words name", \
"occasion": "where it was said", "source_url": "the page you opened", \
"source_kind": "own_words | transcript | printed_qa | coverage_only", \
"already_recorded": "the file name from the recorded list if this is the same claim, else empty"}],
  "undated": [{"date_said": "...", "quote": "...", "source_url": "..."}],
  "other_years": [{"year": "YYYY", "note": "what was seen and where"}],
  "searches": [{"query_or_url": "exactly as run or opened", "what_found": "one sentence"}],
  "quiet_year": true or false,
  "summary": "two or three plain sentences on what this year held"
}
quiet_year is true only when the fixed searches all ran and no candidate was found."""


def api_key():
    for line in CREDENTIALS.read_text().splitlines():
        if line.startswith("ANTHROPIC_API_KEY="):
            return line.split("=", 1)[1].strip().strip('"').strip("'")
    raise SystemExit("stopped: ANTHROPIC_API_KEY not found in the credentials file")


def speaker(speaker_id):
    with open(DATA / "speakers.csv", newline="") as f:
        for r in csv.DictReader(f):
            if r["speaker_id"] == speaker_id:
                return r
    raise SystemExit(f"stopped: {speaker_id!r} is not in data/speakers.csv")


def recorded(speaker_id, year):
    return sorted(p.name for p in (DATA / "claims").glob(f"{year}-*-{speaker_id}-*.toml"))


def prompt(sp, year, args):
    fixed = "\n".join(f"{i}. {q.format(name=sp['name'], year=year)}" for i, q in enumerate(FIXED, 1))
    have = recorded(sp["speaker_id"], year)
    have_text = "\n".join(f"- {n}" for n in have) if have else "(none)"
    return (f"Person: {sp['name']}\nRole over time: {sp['role_summary']}\nYear to search: {year}\n\n"
            f"You have {args.searches} searches and {args.pages} page openings in all.\n\n"
            f"Fixed searches, to run first and exactly as written:\n{fixed}\n\n"
            f"Claims from {year} already recorded for this person (file names carry the date and "
            f"the gist); report them again only if you meet them, marked in already_recorded:\n"
            f"{have_text}")


def cost(usage, model):
    p_in, p_out, p_write, p_read = PRICES[model]
    searches = (usage.server_tool_use.web_search_requests if usage.server_tool_use else 0) or 0
    tokens = (usage.input_tokens * p_in + usage.output_tokens * p_out
              + (usage.cache_creation_input_tokens or 0) * p_write
              + (usage.cache_read_input_tokens or 0) * p_read) / 1_000_000
    return tokens + searches * SEARCH_PRICE, searches


def run_year(client, sp, year, args):
    """One person-year. Returns the saved record."""
    tools = [
        {"type": "web_search_20260209", "name": "web_search", "max_uses": args.searches},
        {"type": "web_fetch_20260209", "name": "web_fetch", "max_uses": args.pages,
         "max_content_tokens": args.page_tokens},
    ]
    messages = [{"role": "user", "content": prompt(sp, year, args)}]
    content, spent, searches, usages, stop = [], 0.0, 0, [], None
    for _ in range(4):  # a long search turn can pause; send it back so the server carries on
        reply = None
        for attempt in range(3):  # a reply can stall mid-stream; the cost of a stalled try is not reported
            try:
                with client.messages.stream(model=args.model, max_tokens=32000, system=SYSTEM,
                                            tools=tools, messages=messages,
                                            output_config={"effort": "medium"},
                                            cache_control={"type": "ephemeral"}) as stream:
                    reply = stream.get_final_message()
                break
            except Exception as e:  # the stream's read timeout is not one of the SDK's own errors
                if "Timeout" not in type(e).__name__ or attempt == 2:
                    raise
                print(f"{year}: the reply timed out, trying again")
        c, s = cost(reply.usage, args.model)
        spent += c
        searches += s
        usages.append(reply.usage.model_dump())
        content.extend(reply.content)
        stop = reply.stop_reason
        if stop != "pause_turn":
            break
        messages = [messages[0], {"role": "assistant", "content": content}]

    calls, text = [], ""
    for b in content:
        if b.type == "server_tool_use":
            calls.append({"tool": b.name, "input": b.input})
        elif b.type == "text":
            text += b.text
    found = re.findall(r"```json\s*(\{.*?\})\s*```", text, re.S)
    parsed, problem = None, ""
    if stop == "refusal":
        problem = "the model declined the request"
    elif not found:
        problem = f"no json block in the reply (stop reason {stop})"
    else:
        try:
            parsed = json.loads(found[-1])
        except json.JSONDecodeError as e:
            problem = f"the json block did not parse: {e}"
    record = {"speaker_id": sp["speaker_id"], "year": year, "model": args.model,
              "date_run": date.today().isoformat(), "stop_reason": stop, "problem": problem,
              "cost_usd": round(spent, 4), "web_searches": searches, "usage": usages,
              "tool_calls": calls, "result": parsed, "reply_text": text}
    folder = OUT / sp["speaker_id"]
    folder.mkdir(parents=True, exist_ok=True)
    (folder / f"{year}.json").write_text(json.dumps(record, indent=2, ensure_ascii=False) + "\n")
    return record


def write_tables(speaker_id):
    """Rebuild the two tables from every saved year, so they always match the saved replies."""
    rows, cands = [], []
    for path in sorted((OUT / speaker_id).glob("*.json")):
        rec = json.loads(path.read_text())
        notes = {s.get("query_or_url", "").strip(): s.get("what_found", "")
                 for s in (rec["result"] or {}).get("searches", [])}
        for call in rec["tool_calls"]:
            if call["tool"] not in ("web_search", "web_fetch"):
                continue  # the model's own filtering code, not a search or a page
            what = call["input"].get("query") or call["input"].get("url") or json.dumps(call["input"])
            where = "Claude API web search" if call["tool"] == "web_search" else "Claude API web fetch"
            rows.append({"search_id": "", "speaker_id": speaker_id, "year": rec["year"], "query": what,
                         "where_searched": where,
                         "what_found": notes.get(what.strip(), "(no note from the model for this call)"),
                         "date_searched": rec["date_run"]})
        for c in (rec["result"] or {}).get("candidates", []):
            cands.append({"year_searched": rec["year"], **{k: c.get(k, "") for k in (
                "date_said", "quote", "what_is_predicted", "date_or_span", "occasion",
                "source_url", "source_kind", "already_recorded")}, "checked_on_page": ""})
    for name, table in ((f"{speaker_id}-search-rows.csv", rows), (f"{speaker_id}-candidates.csv", cands)):
        if table:
            with open(OUT / name, "w", newline="") as f:
                w = csv.DictWriter(f, fieldnames=list(table[0]))
                w.writeheader()
                w.writerows(table)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--speaker", required=True)
    ap.add_argument("--years", required=True, help="one year, or first-last")
    ap.add_argument("--model", default="claude-opus-5-5", choices=sorted(PRICES))
    ap.add_argument("--searches", type=int, default=12)
    ap.add_argument("--pages", type=int, default=6)
    ap.add_argument("--page-tokens", type=int, default=8000)
    ap.add_argument("--ceiling", type=float, default=25.0)
    ap.add_argument("--redo", action="store_true")
    args = ap.parse_args()

    first, _, last = args.years.partition("-")
    years = range(int(last or first), int(first) - 1, -1)  # most recent year back, as the method says
    sp = speaker(args.speaker)
    client = anthropic.Anthropic(api_key=api_key(), timeout=900.0)
    total = 0.0
    try:
        total = run_years(client, sp, years, args)
    finally:
        write_tables(args.speaker)
    print(f"this run: ${total:.2f}")


def run_years(client, sp, years, args):
    total = 0.0
    for year in years:
        saved = OUT / args.speaker / f"{year}.json"
        if saved.exists() and not args.redo:
            print(f"{year}: already saved, skipped")
            continue
        if total >= args.ceiling:
            print(f"stopped before {year}: ${total:.2f} spent, at the ceiling of ${args.ceiling:.2f}")
            break
        try:
            rec = run_year(client, sp, year, args)
        except anthropic.RateLimitError as e:
            print(f"stopped at {year}: rate limited ({e.message}); run again later to carry on")
            break
        except anthropic.APIStatusError as e:
            print(f"stopped at {year}: the API answered {e.status_code}: {e.message}")
            break
        except anthropic.APIConnectionError as e:
            print(f"stopped at {year}: could not reach the API ({e})")
            break
        total += rec["cost_usd"]
        n = len((rec["result"] or {}).get("candidates", []))
        print(f"{year}: {n} candidates, {rec['web_searches']} searches, "
              f"{len(rec['tool_calls'])} tool calls, ${rec['cost_usd']:.2f}"
              + (f"  PROBLEM: {rec['problem']}" if rec["problem"] else ""))
        sys.stdout.flush()
    return total


if __name__ == "__main__":
    main()
