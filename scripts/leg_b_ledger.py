#!/usr/bin/env python3
"""Score the 2016 survey's milestone forecasts against when each milestone arrived.

Reads data/leg_b_ledger.csv, checks each row against docs/leg-b-ledger-method.md, and
prints one line per milestone plus the counts the method asks for, under both the strict
reading (only "arrived" counts) and the generous one ("arguably arrived" counts too).
Standard library only: python3 scripts/leg_b_ledger.py [--as-of YYYY-MM-DD]
"""

import csv
import sys
from datetime import date
from pathlib import Path

LEDGER = Path(__file__).resolve().parent.parent / "data" / "leg_b_ledger.csv"
SURVEY_CLOSED = date(2016, 6, 28)  # the forecast date (method: "The forecast date")
VERDICTS = {"arrived", "arguably arrived", "not arrived", "left for John"}
BANDS = [("under 5 years", 0, 5), ("5 to 10 years", 5, 10), ("10 years or more", 10, 1e9)]


def years(d):
    return (d - SURVEY_CLOSED).days / 365.25


def check(rows):
    problems = []
    for r in rows:
        mid, v = r["milestone_id"], r["verdict"]
        if v not in VERDICTS:
            problems.append(f"{mid}: verdict {v!r} is not one of the method's four")
        has_demo = v in ("arrived", "arguably arrived")
        for col in ("demonstration", "demonstration_date", "date_basis", "demonstration_source"):
            if has_demo and not r[col]:
                problems.append(f"{mid}: {v} but {col} is blank")
            if not has_demo and r[col]:
                problems.append(f"{mid}: {v} but {col} is filled in")
        if has_demo:
            date.fromisoformat(r["demonstration_date"])
        if v != "arrived" and not r["gap_or_nearest"]:
            problems.append(f"{mid}: {v} needs a gap or nearest demonstration recorded")
        float(r["forecast_years"])
    if len(rows) != 32:
        problems.append(f"expected the survey's 32 milestones, found {len(rows)}")
    return problems


def score(r, as_of, generous):
    """Return (status, actual_lead_or_floor, ratio_or_floor)."""
    f = float(r["forecast_years"])
    v = r["verdict"]
    counted = v == "arrived" or (generous and v == "arguably arrived")
    if v == "left for John":
        return "not scored", None, None
    if counted:
        a = years(date.fromisoformat(r["demonstration_date"]))
        return ("early" if a < f else "late"), a, a / f
    elapsed = years(as_of)
    if elapsed > f:
        return "late (not arrived)", elapsed, elapsed / f
    return "not yet due", elapsed, None


def main():
    as_of = date(2026, 10, 9)
    if "--as-of" in sys.argv:
        as_of = date.fromisoformat(sys.argv[sys.argv.index("--as-of") + 1])
    with LEDGER.open(newline="", encoding="utf-8") as fh:
        rows = list(csv.DictReader(fh))
    problems = check(rows)
    if problems:
        print("FAILED:")
        for p in problems:
            print("  " + p)
        sys.exit(1)

    print(f"Forecast date {SURVEY_CLOSED}; as of {as_of} ({years(as_of):.2f} years later)\n")
    print(f"{'milestone':<44} {'fcst':>5}  {'verdict':<16} {'arrival':<10} {'actual':>6} "
          f"{'early(-)/late(+)':>16} {'ratio':>6}")
    for r in rows:
        f = float(r["forecast_years"])
        _, a, ratio = score(r, as_of, generous=True)
        v = r["verdict"]
        if v in ("arrived", "arguably arrived"):
            arr, act = r["demonstration_date"], f"{a:6.2f}"
            diff, rat = f"{a - f:+16.2f}", f"{ratio:6.2f}"
        elif v == "not arrived" and ratio is not None:
            arr, act = "-", f">{a:5.2f}"
            diff, rat = f"{'at least ' + format(a - f, '+.2f'):>16}", f">{ratio:5.2f}"
        else:
            arr, act, diff, rat = "-", "", "", ""
        print(f"{r['table_s5_name'][:44]:<44} {f:5.1f}  {v:<16} {arr:<10} {act:>6} {diff:>16} {rat:>6}")

    for generous in (False, True):
        name = "generous reading (arguably arrived counts)" if generous else "strict reading (only arrived counts)"
        print(f"\n{name}")
        print(f"  {'forecast lead':<18} {'early':>5} {'late':>5} {'late, not arrived':>18} "
              f"{'not yet due':>12} {'not scored':>11} {'within x2':>10}")
        for label, lo, hi in BANDS + [("all", 0, 1e9)]:
            c = {"early": 0, "late": 0, "late (not arrived)": 0, "not yet due": 0, "not scored": 0}
            within = 0
            for r in rows:
                if not lo <= float(r["forecast_years"]) < hi:
                    continue
                st, _, ratio = score(r, as_of, generous)
                c[st] += 1
                if st in ("early", "late") and 0.5 <= ratio <= 2:
                    within += 1
            print(f"  {label:<18} {c['early']:>5} {c['late']:>5} {c['late (not arrived)']:>18} "
                  f"{c['not yet due']:>12} {c['not scored']:>11} {within:>10}")


if __name__ == "__main__":
    main()
