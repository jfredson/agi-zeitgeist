#!/usr/bin/env python3
"""A first sort of the claims search's candidates against the admission rule, before a session
checks them (docs/claims-ledger-method.md, "Which claims get in").

The year-by-year search (scripts/claims_search.py) left a candidates file for each of the
fifteen figureheads. Altman's and Musk's were checked by sessions on 2026-11-17
(<speaker>-checked.csv); the other thirteen were not. For each unchecked candidate this script
sends one request to the Claude API with the web fetch tool: the model opens the source page,
says whether the quoted words are on it, and reads the candidate against the four parts of the
admission rule, quoted to it from the method document as it stands when the script runs.

This script sorts; it admits nothing. Its output is a worksheet in the shape of the checked
files, so the session that does the real check starts from it:

  data/claims-search/<speaker_id>/prescreen/<row>.json   the model's reply, the pages it opened,
                                                         the token counts and the cost
  data/claims-search/<speaker_id>-prescreen.csv          one row per candidate

A session still opens every source, checks every word and makes every admission, as the method
requires. A "pass" here means only that the model read it as passing.

The key is read at run time from ~/.config/sentient-horizons/agi-zeitgeist.env
(ANTHROPIC_API_KEY, the `zeitgeist-coder` key); never printed or written anywhere. The run
draws on the monthly Anthropic API credits; enter its cost in the project's spending record.

    .venv/bin/python scripts/claims_prescreen.py [--speakers amodei,huang] [--limit N]
        [--model claude-opus-5-5] [--ceiling 25] [--workers 4] [--tables-only]

With no --speakers, every speaker that has a candidates file and no checked file. A candidate
already saved is skipped, so a stopped run can be started again. --ceiling stops new requests
once the money spent in this run passes that many dollars. --limit takes the first N unsaved
candidates in all (for a trial). --tables-only rebuilds the worksheets from saved replies.
"""

import argparse
import csv
import json
import re
import sys
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import date
from pathlib import Path

import anthropic

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
OUT = DATA / "claims-search"
METHOD = ROOT / "docs" / "claims-ledger-method.md"
CREDENTIALS = Path.home() / ".config" / "sentient-horizons" / "agi-zeitgeist.env"

# Dollars per million tokens (platform.claude.com/docs/en/about-claude/pricing, as read for
# claims_search.py on 2026-11-16): input, output, 5-minute cache write, cache read.
PRICES = {
    "claude-opus-5-5": (4.00, 20.00, 5.00, 0.20),
    "claude-sonnet-5-5": (2.00, 10.00, 2.50, 0.10),
}

PAGE_CHECKS = ("words found on the page", "words NOT found on the page as fetched",
               "page would not open")
ADMISSIONS = ("pass", "pass, coverage only", "out", "borderline", "recorded")


def rule_text():
    """The admission rule and the readings ruled under it, quoted from the method document."""
    text = METHOD.read_text()
    m = re.search(r"^## Which claims get in.*?(?=^## Order of work)", text, re.S | re.M)
    if not m:
        raise SystemExit("stopped: the admission rule was not found in docs/claims-ledger-method.md")
    return m.group(0).strip()


SYSTEM_HEAD = """You are giving a first reading of one candidate claim for the AGI Zeitgeist's \
claims ledger. A person will check your reading against the page afterwards, so say plainly what \
you saw, and say "borderline" rather than guess.

The candidate was found by an earlier search run, by a model, and its quote has not yet been \
checked against its source. Your two jobs:

1. Open the source page with web fetch and say whether the quoted words are on it, exactly or \
with only trivial differences (punctuation, a dropped "um"). If the page will not open, say so; \
do not judge the words from memory or from a search snippet. If the words are on the page but \
the page is a news report rather than the speaker's own post, a transcript or a printed \
question-and-answer, note that: it decides "pass" against "pass, coverage only".

2. Read the candidate against the admission rule below, all four parts, as written. Use the \
person's role history to judge part 1 (the role held on the date the words were said). If the \
candidate is the same claim as one of the person's recorded claim files listed, the admission is \
"recorded".

The admission rule and the readings ruled under it, quoted from the method document:

"""

SYSTEM_TAIL = """

Finish with one fenced json block and nothing after it, in this shape:
{
  "page_check": "words found on the page | words NOT found on the page as fetched | page would not open",
  "page_note": "one sentence: what the page is, and, if the words differ, what it actually says",
  "date_on_page": "the date the page gives for the words, YYYY-MM-DD or YYYY-MM or YYYY, or empty",
  "role_at_the_time": "the qualifying role held when the words were said, or none",
  "admission": "pass | pass, coverage only | out | borderline | recorded",
  "failed_part": "the number of the rule's part that fails (1, 2, 3 or 4), or empty",
  "reason": "one or two plain sentences giving the reason, in the style: said before OpenAI existed, so no qualifying role"
}"""


def api_key():
    for line in CREDENTIALS.read_text().splitlines():
        if line.startswith("ANTHROPIC_API_KEY="):
            return line.split("=", 1)[1].strip().strip('"').strip("'")
    raise SystemExit("stopped: ANTHROPIC_API_KEY not found in the credentials file")


def speakers():
    with open(DATA / "speakers.csv", newline="") as f:
        return {r["speaker_id"]: r for r in csv.DictReader(f)}


def unchecked_speakers():
    return sorted(p.name[: -len("-candidates.csv")] for p in OUT.glob("*-candidates.csv")
                  if not (OUT / p.name.replace("-candidates.csv", "-checked.csv")).exists())


def candidates(speaker_id):
    with open(OUT / f"{speaker_id}-candidates.csv", newline="") as f:
        return list(csv.DictReader(f))


def recorded(speaker_id):
    return sorted(p.name for p in (DATA / "claims").glob(f"*-{speaker_id}-*.toml"))


def cost(usage, model):
    p_in, p_out, p_write, p_read = PRICES[model]
    return (usage.input_tokens * p_in + usage.output_tokens * p_out
            + (usage.cache_creation_input_tokens or 0) * p_write
            + (usage.cache_read_input_tokens or 0) * p_read) / 1_000_000


def prompt(sp, row, have):
    have_text = "\n".join(f"- {n}" for n in have) if have else "(none)"
    fields = "\n".join(f"{k}: {row.get(k, '')}" for k in (
        "year_searched", "date_said", "quote", "what_is_predicted", "date_or_span", "occasion",
        "source_url", "source_kind", "already_recorded"))
    return (f"Person: {sp['name']}\nRole history: {sp['role_summary']}\n\n"
            f"The candidate, as the search run reported it:\n{fields}\n\n"
            f"This person's recorded claim files (the names carry the date and the gist):\n{have_text}")


def run_one(client, system, sp, n, row, have, args):
    tools = [{"type": "web_fetch_20260209", "name": "web_fetch", "max_uses": 2,
              "max_content_tokens": 8000}]
    messages = [{"role": "user", "content": prompt(sp, row, have)}]
    content, spent, usages, stop = [], 0.0, [], None
    for _ in range(3):  # a fetch turn can pause; send it back so the server carries on
        reply = None
        for attempt in range(3):
            try:
                with client.messages.stream(model=args.model, max_tokens=8000, system=system,
                                            tools=tools, messages=messages,
                                            output_config={"effort": "medium"}) as stream:
                    reply = stream.get_final_message()
                break
            except Exception as e:  # the stream's read timeout is not one of the SDK's own errors
                if "Timeout" not in type(e).__name__ or attempt == 2:
                    raise
        spent += cost(reply.usage, args.model)
        usages.append(reply.usage.model_dump())
        content.extend(reply.content)
        stop = reply.stop_reason
        if stop != "pause_turn":
            break
        messages = [messages[0], {"role": "assistant", "content": content}]

    pages, text = [], ""
    for b in content:
        if b.type == "server_tool_use":
            pages.append(b.input.get("url", json.dumps(b.input)))
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
    if parsed and (parsed.get("page_check") not in PAGE_CHECKS
                   or parsed.get("admission") not in ADMISSIONS):
        problem = "a value outside the allowed labels"
    record = {"speaker_id": sp["speaker_id"], "row": n, "model": args.model,
              "date_run": date.today().isoformat(), "stop_reason": stop, "problem": problem,
              "cost_usd": round(spent, 4), "pages_opened": pages, "usage": usages,
              "candidate": row, "result": parsed, "reply_text": text}
    folder = OUT / sp["speaker_id"] / "prescreen"
    folder.mkdir(parents=True, exist_ok=True)
    (folder / f"{n:03d}.json").write_text(json.dumps(record, indent=2, ensure_ascii=False) + "\n")
    return record


def write_table(speaker_id):
    """Rebuild the worksheet from every saved reply, so it always matches them."""
    folder = OUT / speaker_id / "prescreen"
    rows = []
    for path in sorted(folder.glob("*.json")):
        rec = json.loads(path.read_text())
        c, r = rec["candidate"], rec["result"] or {}
        rows.append({"row": rec["row"], "date_said": c.get("date_said", ""), "quote": c.get("quote", ""),
                     "source_url": c.get("source_url", ""),
                     "already_recorded": c.get("already_recorded", ""),
                     "page_check": r.get("page_check", ""), "page_note": r.get("page_note", ""),
                     "date_on_page": r.get("date_on_page", ""),
                     "role_at_the_time": r.get("role_at_the_time", ""),
                     "admission": r.get("admission", ""), "failed_part": r.get("failed_part", ""),
                     "reason": r.get("reason", ""), "problem": rec["problem"],
                     "sorted_by": f"{rec['model']}, {rec['date_run']} (not checked)"})
    if rows:
        with open(OUT / f"{speaker_id}-prescreen.csv", "w", newline="") as f:
            w = csv.DictWriter(f, fieldnames=list(rows[0]))
            w.writeheader()
            w.writerows(rows)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--speakers", help="comma-separated ids; default every unchecked speaker")
    ap.add_argument("--model", default="claude-opus-5-5", choices=sorted(PRICES))
    ap.add_argument("--ceiling", type=float, default=25.0)
    ap.add_argument("--limit", type=int)
    ap.add_argument("--workers", type=int, default=4)
    ap.add_argument("--tables-only", action="store_true")
    args = ap.parse_args()

    ids = args.speakers.split(",") if args.speakers else unchecked_speakers()
    if args.tables_only:
        for s in ids:
            write_table(s)
        return

    sps = speakers()
    jobs = []
    for s in ids:
        if s not in sps:
            raise SystemExit(f"stopped: {s!r} is not in data/speakers.csv")
        have = recorded(s)
        for n, row in enumerate(candidates(s), 1):
            if not (OUT / s / "prescreen" / f"{n:03d}.json").exists():
                jobs.append((sps[s], n, row, have))
    if args.limit:
        jobs = jobs[: args.limit]
    print(f"{len(jobs)} candidates to sort, across {len({j[0]['speaker_id'] for j in jobs})} people")

    system = [{"type": "text", "text": SYSTEM_HEAD + rule_text() + SYSTEM_TAIL,
               "cache_control": {"type": "ephemeral"}}]
    client = anthropic.Anthropic(api_key=api_key(), timeout=600.0)
    lock, total, stopped = threading.Lock(), [0.0], threading.Event()

    def work(job):
        sp, n, row, have = job
        if stopped.is_set():
            return None
        with lock:
            if total[0] >= args.ceiling:
                stopped.set()
                return None
        rec = run_one(client, system, sp, n, row, have, args)
        with lock:
            total[0] += rec["cost_usd"]
        r = rec["result"] or {}
        print(f"{sp['speaker_id']} {n}: {r.get('admission', '?')} / {r.get('page_check', '?')}"
              f"  ${rec['cost_usd']:.3f}" + (f"  PROBLEM: {rec['problem']}" if rec["problem"] else ""))
        sys.stdout.flush()
        return rec

    try:
        with ThreadPoolExecutor(max_workers=args.workers) as pool:
            futures = [pool.submit(work, j) for j in jobs]
            for f in as_completed(futures):
                try:
                    f.result()
                except anthropic.APIStatusError as e:
                    print(f"a request failed: the API answered {e.status_code}: {e.message}")
                except anthropic.APIConnectionError as e:
                    print(f"a request failed: could not reach the API ({e})")
    finally:
        for s in ids:
            if (OUT / s / "prescreen").exists():
                write_table(s)
    if stopped.is_set():
        print(f"stopped at the ceiling of ${args.ceiling:.2f}; run again to carry on")
    print(f"this run: ${total[0]:.2f}")


if __name__ == "__main__":
    main()
