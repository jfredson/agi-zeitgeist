#!/usr/bin/env python3
"""Search the Guardian and New York Times archives for a panel candidate (amendment A14,
ruling 7; A15 step 2).

For each person, searches both archives for the name together with AI-future terms, in
two windows:
  C3  pieces dated on or before 2017-12-31 (the three-national-pieces test)
  C2  pieces dated on or after 2024-01-01 (leads for a 2024-or-later statement)
and appends every hit to docs/panel-evidence-2026-10/archive-checks.csv with the outlet,
date, headline, link, and whether the person is named in the headline or the abstract.

A hit counts toward C3 only if the person's full name is in the headline or the abstract
AND the headline or abstract carries an AI-future term. A hit where the name is only in
the headline and the archive gives no abstract is recorded with the flag `headline_only`
and not counted. A hit where the name is in neither is recorded with the flag
`named_in_text_only` and not counted. Abstracts are used for the check but not stored.

API keys are read at run time from ~/Documents/.agi-zeitgeist/credentials.env
(GUARDIAN_API_KEY, NYT_API_KEY). They are never printed or written anywhere; error
messages have them removed. Rate limits: Guardian about one request a second; New York
Times about five a minute (one request every 12.5 seconds). If either archive refuses a
request (HTTP 401, 403 or 429), the run stops at once and keeps what it has.

    python3 scripts/archive_check.py "Geoffrey Hinton" ["Yann LeCun" ...]
    python3 scripts/archive_check.py --file names.txt
"""

import csv
import json
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import date
from pathlib import Path

CREDENTIALS = Path.home() / "Documents" / ".agi-zeitgeist" / "credentials.env"
OUT = Path(__file__).resolve().parent.parent / "docs" / "panel-evidence-2026-10" / "archive-checks.csv"
FIELDS = ["person", "window", "archive", "date", "headline", "url", "named_in_headline",
          "named_in_abstract", "ai_term_in_headline_or_abstract", "counts_toward_c3",
          "flag", "query", "retrieved"]
WINDOWS = {"C3": (None, "2017-12-31"), "C2": ("2024-01-01", None)}
AI_TERMS = re.compile(
    r"artificial intelligence|\bA\.?I\.?\b|robot|machine learning|deep learning|neural net"
    r"|superintelligen|singularity|\bAGI\b|intelligent machine|thinking machine|automation"
    r"|smarter than|human-level|chatbot|language model|ChatGPT|OpenAI|DeepMind", re.I)
# Spelling variants the archives use.
VARIANTS = {"Jürgen Schmidhuber": ["Juergen Schmidhuber", "Jurgen Schmidhuber"],
            "François Chollet": ["Francois Chollet"],
            "Kai-Fu Lee": ["Kai-fu Lee", "Kaifu Lee"],
            "Ilya Sutskever": [], "Andrew Ng": []}
GUARDIAN_GAP, NYT_GAP = 1.1, 12.5


class Refused(Exception):
    pass


def load_keys():
    keys = {}
    for line in CREDENTIALS.read_text().splitlines():
        if "=" in line and not line.lstrip().startswith("#"):
            k, v = line.split("=", 1)
            keys[k.strip()] = v.strip().strip('"').strip("'")
    missing = [k for k in ("GUARDIAN_API_KEY", "NYT_API_KEY") if not keys.get(k)]
    if missing:
        sys.exit(f"missing in {CREDENTIALS}: {', '.join(missing)}")
    return keys


def get_json(url, secrets):
    def scrub(text):
        for s in secrets:
            text = text.replace(s, "<key>")
        return text
    req = urllib.request.Request(url, headers={"User-Agent": "agi-zeitgeist archive check"})
    try:
        with urllib.request.urlopen(req, timeout=40) as r:
            return json.loads(r.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        if e.code in (401, 403, 429):
            raise Refused(f"HTTP {e.code} from {urllib.parse.urlsplit(url).netloc}") from None
        raise RuntimeError(scrub(f"HTTP {e.code}: {url}")) from None
    except (urllib.error.URLError, ConnectionError, TimeoutError, OSError) as e:
        # A dropped or timed-out connection is treated like a refusal: stop, don't retry.
        reason = getattr(e, "reason", e)
        raise Refused(scrub(f"connection dropped by {urllib.parse.urlsplit(url).netloc} ({reason})")) from None


def names_for(person):
    return [person] + VARIANTS.get(person, [])


def named(text, person):
    t = (text or "").lower()
    return any(n.lower() in t for n in names_for(person))


def guardian(person, window, key, secrets):
    lo, hi = WINDOWS[window]
    q = f'"{person}" AND ("artificial intelligence" OR AI OR robots OR superintelligence OR singularity)'
    params = {"q": q, "page-size": 50, "order-by": "relevance", "api-key": key,
              "show-fields": "headline,trailText"}
    if lo:
        params["from-date"] = lo
    if hi:
        params["to-date"] = hi
    data = get_json("https://content.guardianapis.com/search?" + urllib.parse.urlencode(params), secrets)
    time.sleep(GUARDIAN_GAP)
    for r in data.get("response", {}).get("results", []):
        f = r.get("fields", {})
        yield {"archive": "Guardian", "date": r.get("webPublicationDate", "")[:10],
               "headline": f.get("headline") or r.get("webTitle", ""),
               "abstract": re.sub(r"<[^>]+>", "", f.get("trailText") or ""),
               "url": r.get("webUrl", ""), "query": q}


def nyt(person, window, key, secrets, pages=2):
    lo, hi = WINDOWS[window]
    q = f'"{person}" artificial intelligence'
    for page in range(pages):
        params = {"q": q, "sort": "relevance", "page": page, "api-key": key}
        if lo:
            params["begin_date"] = lo.replace("-", "")
        if hi:
            params["end_date"] = hi.replace("-", "")
        data = get_json("https://api.nytimes.com/svc/search/v2/articlesearch.json?"
                        + urllib.parse.urlencode(params), secrets)
        time.sleep(NYT_GAP)
        docs = (data.get("response") or {}).get("docs") or []
        for d in docs:
            yield {"archive": "New York Times", "date": (d.get("pub_date") or "")[:10],
                   "headline": (d.get("headline") or {}).get("main", ""),
                   "abstract": d.get("abstract") or d.get("snippet") or "",
                   "url": d.get("web_url", ""), "query": q}
        if len(docs) < 10:
            break


def classify(person, window, hit):
    in_head = named(hit["headline"], person)
    in_abs = named(hit["abstract"], person)
    ai = bool(AI_TERMS.search(hit["headline"] + " " + hit["abstract"]))
    flag, counts = "", False
    if in_head and not hit["abstract"].strip():
        flag = "headline_only"
    elif not (in_head or in_abs):
        flag = "named_in_text_only"
    elif not ai:
        flag = "no_ai_term_in_headline_or_abstract"
    elif window == "C3":
        counts = True
    return {"named_in_headline": "yes" if in_head else "no",
            "named_in_abstract": "yes" if in_abs else "no",
            "ai_term_in_headline_or_abstract": "yes" if ai else "no",
            "counts_toward_c3": "yes" if counts else "no", "flag": flag}


def main():
    args = sys.argv[1:]
    if args[:1] == ["--file"]:
        args = [l.strip() for l in Path(args[1]).read_text().splitlines() if l.strip()]
    if not args:
        sys.exit(__doc__)
    keys = load_keys()
    secrets = [keys["GUARDIAN_API_KEY"], keys["NYT_API_KEY"]]
    OUT.parent.mkdir(parents=True, exist_ok=True)
    new_file = not OUT.exists()
    today = date.today().isoformat()
    with OUT.open("a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS, lineterminator="\n")
        if new_file:
            w.writeheader()
        for person in args:
            summary = {}
            for window in WINDOWS:
                for source in (guardian, nyt):
                    try:
                        hits = list(source(person, window, keys[
                            "GUARDIAN_API_KEY" if source is guardian else "NYT_API_KEY"], secrets))
                    except Refused as e:
                        f.flush()
                        sys.exit(f"stopped: {e} while checking {person} ({window}); "
                                 f"results so far are in {OUT}")
                    seen = set()
                    for h in hits:
                        if h["url"] in seen:
                            continue
                        seen.add(h["url"])
                        row = {"person": person, "window": window, "archive": h["archive"],
                               "date": h["date"], "headline": h["headline"], "url": h["url"],
                               "query": h["query"], "retrieved": today}
                        row.update(classify(person, window, h))
                        w.writerow(row)
                        if row["counts_toward_c3"] == "yes":
                            summary["C3"] = summary.get("C3", 0) + 1
                        if window == "C2" and row["flag"] == "":
                            summary["C2 leads"] = summary.get("C2 leads", 0) + 1
                    f.flush()
            print(f"{person}: C3 counted {summary.get('C3', 0)}, C2 leads {summary.get('C2 leads', 0)}")


if __name__ == "__main__":
    main()
