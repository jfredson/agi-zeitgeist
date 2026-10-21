"""Two checks the weekly reading prints in its report (amendment A32, John's ruling of 2026-10-21).

1. Freshness: for every panel member (and every industry leader on the claims page), the latest day they
   were searched for this year's words, and anyone not searched in the last eight days. A comparison of
   people is not shared while anyone in it is overdue (docs/weekly-reading.md, part 4).
2. Tip spread: how many statements and claims came in by tip, per person, and what share of each
   person's rows that is, so John can see whether his own reading tilts the record.

Reads only data/; writes nothing. Standard library only, so the scheduled reading can run it as is.

    python3 scripts/panel_status.py            # both sections
    python3 scripts/panel_status.py --json     # the same, as JSON
"""
import csv
import json
import sys
import tomllib
from collections import Counter
from datetime import date, timedelta
from pathlib import Path

DATA = Path(__file__).resolve().parent.parent / "data"
PANEL_TIERS = ("core", "cohort_2020s")
OVERDUE_DAYS = 8  # a weekly search, with a day's grace


def read(name):
    with (DATA / name).open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def tags(notes):
    return {part.strip().split(":")[0].strip() for part in (notes or "").split(";")}


def main():
    today = date.today()
    year = str(today.year)
    speakers = read("speakers.csv")
    people = {r["speaker_id"]: r for r in speakers if r["tier"] in PANEL_TIERS or r["tier"] == "claims_only"}
    latest = {}
    for r in read("search_log.csv"):
        if r["speaker_id"] in people and r["year"] == year and r.get("date_searched"):
            latest[r["speaker_id"]] = max(latest.get(r["speaker_id"], ""), r["date_searched"])
    cutoff = (today - timedelta(days=OVERDUE_DAYS)).isoformat()
    overdue = sorted((sp for sp in people if latest.get(sp, "") < cutoff), key=lambda sp: (latest.get(sp, ""), sp))
    panel = [sp for sp in people if people[sp]["tier"] in PANEL_TIERS]
    through = min((latest.get(sp, "") for sp in panel), default="") or None

    rows = read("statements.csv")
    total = Counter(r["speaker_id"] for r in rows)
    tip = Counter(r["speaker_id"] for r in rows if "tip" in tags(r["notes"]))
    missed = Counter(r["speaker_id"] for r in rows if "tip_missed" in tags(r["notes"]))
    claims = [tomllib.loads(p.read_text(encoding="utf-8"))["claim"] for p in sorted((DATA / "claims").glob("*.toml"))]
    tip_claims = Counter(c["speaker_id"] for c in claims if c.get("from_tip"))
    tipped = sorted(set(tip) | set(tip_claims), key=lambda sp: (-tip[sp], sp))

    out = dict(
        date=today.isoformat(),
        panel_searched_through=through,
        overdue=[dict(speaker_id=sp, last_searched=latest.get(sp)) for sp in overdue],
        tips=dict(statements=sum(tip.values()), of_statements=len(rows), claims=sum(tip_claims.values()),
                  people_with_tips=len(tipped), panel_size=len(panel),
                  by_person=[dict(speaker_id=sp, statements=tip[sp], missed_by_searches=missed[sp],
                                  share_of_their_statements=round(tip[sp] / total[sp], 3) if total[sp] else None,
                                  claims=tip_claims[sp]) for sp in tipped]),
    )
    if "--json" in sys.argv:
        print(json.dumps(out, indent=2))
        return
    print(f"Freshness ({today}): every panel member searched for {year} words through {through or 'never'}.")
    if overdue:
        print(f"  Overdue, last searched before {cutoff} ({len(overdue)}): "
              + ", ".join(f"{sp} ({latest.get(sp) or 'never'})" for sp in overdue))
    else:
        print("  Nobody is overdue.")
    t = out["tips"]
    print(f"Tips: {t['statements']} of {t['of_statements']} statements and {t['claims']} claims came in by tip, "
          f"for {t['people_with_tips']} {'person' if t['people_with_tips'] == 1 else 'people'} (the panel has {t['panel_size']}).")
    for p in t["by_person"]:
        share = f"{p['share_of_their_statements']:.0%} of their statements" if p["share_of_their_statements"] is not None else "no statements"
        print(f"  {p['speaker_id']}: {p['statements']} statements ({share}; the searches missed {p['missed_by_searches']}), {p['claims']} claims")


if __name__ == "__main__":
    main()
