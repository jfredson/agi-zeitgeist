#!/usr/bin/env python3
"""The backward test for the singularity-entry definition, 1995 to 2019.

Method: docs/backward-test-method.md. Frozen values: docs/singularity-entry-thresholds.json
(read, never changed). Standard library only.

    python3 scripts/backward_test.py                  # run from the saved extract
    python3 scripts/backward_test.py --refresh FILE   # rebuild the extract from a full
                                                      # copy of epoch.ai/data/notable_ai_models.csv
"""

import argparse
import csv
import json
import math
from datetime import date, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
OUT = DATA / "backward-test"
EXTRACT = OUT / "epoch-notable-models-1990-2020.csv"
THRESHOLDS = ROOT / "docs" / "singularity-entry-thresholds.json"
EPOCH_URL = "https://epoch.ai/data/notable_ai_models.csv"
RETRIEVED = "2026-10-09"
FIRST_YEAR, LAST_YEAR = 1995, 2019


def parse_date(s):
    parts = [int(p) for p in s.split("-")] + [1, 1]
    return date(parts[0], parts[1], parts[2])


def year_frac(d):
    return d.year + (d.timetuple().tm_yday - 1) / 365.25


def refresh(full_path):
    """Keep the 1990 to 2020 rows of Epoch's file that carry a training compute figure."""
    with open(full_path, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    keep = [r for r in rows if r["Training compute (FLOP)"].strip()
            and "1990" <= r["Publication date"][:4] <= "2020"]
    keep.sort(key=lambda r: (r["Publication date"], r["Model"]))
    OUT.mkdir(parents=True, exist_ok=True)
    with EXTRACT.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["model", "organization", "publication_date", "training_compute_flop",
                    "confidence", "link", "source_url", "retrieved"])
        for r in keep:
            w.writerow([r["Model"], r["Organization"], r["Publication date"],
                        r["Training compute (FLOP)"], r["Confidence"], r["Link"],
                        EPOCH_URL, RETRIEVED])
    print(f"{EXTRACT.relative_to(ROOT)}: {len(keep)} rows")


# ----------------------------------------------------------------------------- leg A
def pre1990_best(full_path):
    """Largest training compute among Epoch's systems published before 1990 (a check only)."""
    with open(full_path, newline="", encoding="utf-8") as f:
        return max(float(r["Training compute (FLOP)"]) for r in csv.DictReader(f)
                   if r["Training compute (FLOP)"].strip() and r["Publication date"][:4] < "1990")


def leg_a_windows(seed=0.0):
    with EXTRACT.open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    pts = sorted((dict(model=r["model"], date=parse_date(r["publication_date"]),
                       flop=float(r["training_compute_flop"])) for r in rows),
                 key=lambda p: (p["date"], -p["flop"]))
    # Record-setting: more training compute than every earlier system in the saved
    # 1990 to 2020 rows (see the 2026-10-09 note in docs/backward-test-method.md).
    # seed > 0 also counts an earlier best, for the pre-1990 check.
    frontier, best = [], seed
    for p in pts:
        if p["flop"] > best:
            frontier.append(p)
            best = p["flop"]
    # Same computation as scripts/site.py leg_a: windows ending at each frontier point.
    series = []
    for p in frontier:
        win = [q for q in frontier if 0 <= (p["date"] - q["date"]).days <= 365]
        if len(win) < 3:
            continue
        xs = [year_frac(q["date"]) for q in win]
        ys = [math.log(q["flop"]) for q in win]
        mx, my = sum(xs) / len(xs), sum(ys) / len(ys)
        sxx = sum((x - mx) ** 2 for x in xs)
        slope = sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / sxx if sxx else 0
        if slope > 0:
            series.append(dict(date=p["date"], model=p["model"], days=math.log(2) / slope * 365.25,
                               n=len(win), models="; ".join(q["model"] for q in win)))
    return frontier, series


def leg_a_at(series, d, la):
    done = [s for s in series if s["date"] <= d]
    if not done:
        return dict(state="not measurable", gauge=None, days=None, falling=False,
                    looser="not measurable")
    cur = done[-1]
    falling = len(done) >= 3 and done[-1]["days"] < done[-2]["days"] < done[-3]["days"]
    t_star, t_ref = la["doubling_time_threshold_days"], la["reference_doubling_time_days"]
    g = max(0.0, min(1.0, (t_ref - cur["days"]) / (t_ref - t_star)))
    met = cur["days"] <= t_star and falling
    # Looser reading of "still falling over the last two windows": one drop, the latest
    # window quicker than the one before. Reported beside the live site's reading, not scored.
    one_drop = len(done) >= 2 and done[-1]["days"] < done[-2]["days"]
    return dict(state="met" if met else "not met", gauge=g, days=cur["days"], falling=falling,
                window_end=cur["date"],
                looser="met" if cur["days"] <= t_star and one_drop else "not met")


# ----------------------------------------------------------------------------- leg D
def leg_d_series(ld):
    with (DATA / "world_measures.csv").open(newline="", encoding="utf-8") as f:
        rows = [r for r in csv.DictReader(f) if r["unit"] == "percent_growth"]
    growth = {int(r["date"]): float(r["value"]) for r in rows}
    ref_years = [y for y in growth if 1961 <= y <= 2019]
    mean_g = sum(growth[y] for y in ref_years) / len(ref_years)
    t_ref = math.log(2) / math.log(1 + mean_g / 100)
    t_star = math.log(2) / math.log(1 + ld["growth_threshold_percent_per_year"] / 100)
    return growth, t_ref, t_star, mean_g


def quarter_ends(y):
    return [(q, date(y, 3 * q + 1, 1) - timedelta(days=1) if q < 4 else date(y, 12, 31))
            for q in (1, 2, 3, 4)]


def run():
    th = json.loads(THRESHOLDS.read_text())
    la, lc, ld = th["leg_a"], th["leg_c"], th["leg_d"]
    need = th["persistence_quarters"]
    frontier, series = leg_a_windows()
    growth, d_ref, d_star, mean_g = leg_d_series(ld)

    with (OUT / "leg-a-windows.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["window_end", "record_setting_system", "days_per_doubling", "systems_in_window",
                    "systems", "at_or_below_line"])
        for s in series:
            w.writerow([s["date"].isoformat(), s["model"], f"{s['days']:.1f}", s["n"], s["models"],
                        "yes" if s["days"] <= la["doubling_time_threshold_days"] else "no"])

    quarters = []
    # Four scenarios: as measured (unmeasurable legs cannot be met), and with the
    # unmeasurable legs B and C assumed met, to see whether the verdict rests on them.
    runs = {"as_measured": 0, "b_and_c_assumed_met": 0,
            "looser_pace_reading": 0, "looser_pace_reading_b_and_c_assumed_met": 0}
    for y in range(FIRST_YEAR, LAST_YEAR + 1):
        for q, d in quarter_ends(y):
            a = leg_a_at(series, d, la)
            g = growth.get(y)
            d_met = g is not None and g >= ld["growth_threshold_percent_per_year"]
            dbl = math.log(2) / math.log(1 + g / 100) if g and g > 0 else None
            g_d = max(0.0, min(1.0, (d_ref - dbl) / (d_ref - d_star))) if dbl else 0.0
            row = dict(year=y, quarter=q, quarter_end=d.isoformat(),
                       leg_a=a["state"], leg_a_days=a["days"], leg_a_gauge=a["gauge"],
                       leg_a_getting_quicker=a["falling"], leg_a_looser_reading=a["looser"],
                       leg_b="not measurable", leg_c="not measurable",
                       leg_d="met" if d_met else "not met", leg_d_growth=g, leg_d_gauge=g_d)
            for k in runs:
                a_met = (a["looser"] if k.startswith("looser") else a["state"]) == "met"
                assumed = k.endswith("b_and_c_assumed_met")
                legs = [a_met, assumed, assumed, d_met]
                runs[k] = runs[k] + 1 if all(legs) else 0
                row[k] = ("entered" if runs[k] >= need else
                          "mark crossed, under persistence test" if runs[k] else "not entered")
            quarters.append(row)

    def fmt(v, p=1):
        return "" if v is None else (f"{v:.{p}f}" if isinstance(v, float) else v)

    cols = ["year", "quarter", "quarter_end", "leg_a", "leg_a_days", "leg_a_gauge",
            "leg_a_getting_quicker", "leg_a_looser_reading", "leg_b", "leg_c", "leg_d", "leg_d_growth", "leg_d_gauge",
            "as_measured", "b_and_c_assumed_met", "looser_pace_reading",
            "looser_pace_reading_b_and_c_assumed_met"]
    with (OUT / "results-by-quarter.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(cols)
        for r in quarters:
            w.writerow([fmt(r[c], 2 if c.endswith("gauge") else 1) if not isinstance(r[c], bool)
                        else ("yes" if r[c] else "no") for c in cols])

    years = []
    for y in range(FIRST_YEAR, LAST_YEAR + 1):
        qs = [r for r in quarters if r["year"] == y]
        in_year = [s for s in series if s["date"].year == y]
        fastest = min((s["days"] for s in in_year), default=None)
        gauges = [r["leg_a_gauge"] for r in qs if r["leg_a_gauge"] is not None]
        years.append(dict(
            year=y,
            leg_a_met_any_quarter="yes" if any(r["leg_a"] == "met" for r in qs) else
                                  ("not measurable" if all(r["leg_a"] == "not measurable" for r in qs) else "no"),
            leg_a_met_looser_reading="yes" if any(r["leg_a_looser_reading"] == "met" for r in qs) else "no",
            leg_a_highest_gauge=fmt(max(gauges), 2) if gauges else "",
            windows_ending_in_year=len(in_year),
            fastest_window_days=fmt(fastest),
            any_window_at_or_below_line="yes" if fastest is not None and fastest <= la["doubling_time_threshold_days"] else "no",
            leg_d_growth_percent=fmt(growth.get(y), 2),
            leg_d_met="yes" if qs[0]["leg_d"] == "met" else "no",
            leg_d_gauge=fmt(qs[0]["leg_d_gauge"], 2),
            verdict_as_measured="entered" if any(r["as_measured"] == "entered" for r in qs) else "not entered",
            verdict_b_and_c_assumed_met="entered" if any(r["b_and_c_assumed_met"] == "entered" for r in qs) else "not entered",
            verdict_looser_pace_reading="entered" if any(r["looser_pace_reading"] == "entered" for r in qs) else "not entered",
            verdict_looser_pace_reading_b_and_c_assumed_met="entered" if any(
                r["looser_pace_reading_b_and_c_assumed_met"] == "entered" for r in qs) else "not entered",
        ))
    with (OUT / "results-by-year.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(years[0]))
        w.writeheader()
        w.writerows(years)

    print(f"record-setting systems: {len(frontier)}; twelve-month windows scored: {len(series)}")
    print(f"leg D reference: mean growth 1961-2019 {mean_g:.2f}% = {d_ref:.1f} years per doubling; "
          f"line {ld['growth_threshold_percent_per_year']}% = {d_star:.2f} years")
    print("year  legA(met?) A-gauge fastest-window  growth%  D-met  verdict / with B,C assumed met")
    for r in years:
        print(f"{r['year']}  {r['leg_a_met_any_quarter']:<14} {r['leg_a_highest_gauge']:>5} "
              f"{r['fastest_window_days']:>8} ({r['any_window_at_or_below_line']:>3})  "
              f"{r['leg_d_growth_percent']:>6}  {r['leg_d_met']:<4} {r['verdict_as_measured']} / "
              f"{r['verdict_b_and_c_assumed_met']}")
    looser = [f"{r['year']} Q{r['quarter']}" for r in quarters if r["leg_a_looser_reading"] == "met"]
    print("pace condition met on the looser one-drop reading:", ", ".join(looser) or "never")
    print("verdict on the looser reading:",
          "entered somewhere" if any(r["verdict_looser_pace_reading_b_and_c_assumed_met"] == "entered" or
                                     r["verdict_looser_pace_reading"] == "entered" for r in years)
          else "not entered in every year (also with B and C assumed met)")
    failed = [r["year"] for r in years if r["verdict_as_measured"] == "entered"]
    print("RESULT:", "FAIL in " + ", ".join(map(str, failed)) if failed else
          "PASS: not entered in every quarter 1995 to 2019")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--refresh", metavar="FILE", help="full copy of " + EPOCH_URL)
    ap.add_argument("--check-pre1990", metavar="FILE",
                    help="full copy of the Epoch file: list the record-setting systems and windows "
                         "when pre-1990 systems also count, and say whether any 1995-2019 window changes")
    args = ap.parse_args()
    if args.refresh:
        refresh(args.refresh)
    if args.check_pre1990:
        seed = pre1990_best(args.check_pre1990)
        base_f, base_s = leg_a_windows()
        f2, s2 = leg_a_windows(seed)
        key = lambda s: [(w["date"], round(w["days"], 6), w["n"]) for w in s
                         if FIRST_YEAR <= w["date"].year <= LAST_YEAR]
        dropped = [p["model"] for p in base_f if p not in f2]
        print(f"pre-1990 best: {seed:.3g} FLOP; record-setting systems {len(base_f)} -> {len(f2)}; "
              f"dropped: {', '.join(dropped) or 'none'}")
        print("1995-2019 windows unchanged:", key(base_s) == key(s2))
    else:
        run()
