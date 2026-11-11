"""Overlap pictures and numbers for the pace gauge's successor proposal (amendment A24, open).

Reads the METR time-horizon rows the gauge scores today (data/world_measures.csv) and dated copies of
three series published by Epoch AI (docs/leg-a-successor-2026-11-11/epoch-*.csv, retrieved 2026-11-11
from https://epoch.ai/data/benchmark_data.zip, CC BY 4.0), and writes into the same folder:

  overlap-eci-conversion.png      each system measured by both: METR's job length against Epoch's index
  overlap-eci.png                 the two series over time, and the days-to-double each one gives
  overlap-mirrorcode.png          MirrorCode against METR's job length, and MirrorCode over time
  overlap-remote-labor-index.png  the Remote Labor Index against METR's job length, and over time
  eci-overlap-models.csv, eci-doubling-time.csv, overlap-numbers.json   the numbers behind them

It changes nothing on the site and nothing that is scored: it does not touch site/, the thresholds
file or data/. Run: python3 scripts/leg_a_successor.py
"""

import csv
import json
import math
from datetime import date
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.dates as mdates
import matplotlib.pyplot as plt

import chart_style as cs

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "docs" / "leg-a-successor-2026-11-11"
THRESHOLDS = json.loads((ROOT / "docs" / "singularity-entry-thresholds.json").read_text())["leg_a"]
T_STAR, T_REF = THRESHOLDS["doubling_time_threshold_days"], THRESHOLDS["reference_doubling_time_days"]
RETRIEVED = "2026-11-11"
BLUE, ORANGE, GREEN, PURPLE = cs.PALETTE[0], cs.PALETTE[1], cs.PALETTE[2], cs.PALETTE[6]

# The gauge's METR rows (aggregate_id without the "metr-th11-" prefix) and the same system's name in
# each Epoch file. A system missing from a map is not in that Epoch file.
ECI_NAME = {
    "gpt-4": "GPT-4 (Mar 2023)", "gpt-4-1106": "GPT-4 Turbo (Nov 2023)", "claude-3-opus": "Claude 3 Opus",
    "gpt-4-turbo": "GPT-4 Turbo (Apr 2024)", "gpt-4o": "GPT-4o (May 2024)",
    "claude-3-5-sonnet-20240620": "Claude 3.5 Sonnet", "o1-preview": "o1-preview",
    "claude-3-5-sonnet-20241022": "Claude 3.5 Sonnet (October 2024)", "o1": "o1",
    "claude-3-7-sonnet": "Claude 3.7 Sonnet", "o3": "o3", "claude-4-opus": "Claude Opus 4",
    "claude-4-1-opus": "Claude Opus 4.1", "gpt-5-2025-08-07": "GPT-5", "gemini-3-pro": "Gemini 3 Pro",
    "claude-opus-4-5": "Claude Opus 4.5", "gpt-5-2": "GPT-5.2", "claude-opus-4-6": "Claude Opus 4.6",
    "gemini-3-1-pro": "Gemini 3.1 Pro", "gpt-5-4": "GPT-5.4",
}
VERSION_PREFIX = {  # the start of Epoch's "Model version" for the benchmark files
    "gpt-5-2025-08-07": "gpt-5-2025-08-07", "gemini-3-pro": "gemini-3-pro-preview",
    "claude-opus-4-5": "claude-opus-4-5", "gpt-5-2": "gpt-5.2-2025-12-11", "claude-opus-4-6": "claude-opus-4-6",
    "gemini-3-1-pro": "gemini-3.1-pro-preview", "gpt-5-4": "gpt-5.4-2026-03-05",
}


def parse_date(s):
    return date.fromisoformat(s[:10])


def year_frac(d):
    return d.year + (d.timetuple().tm_yday - 1) / 365.25


def fit(xs, ys):
    """Least-squares line: slope, intercept and the share of the variation it explains."""
    mx, my = sum(xs) / len(xs), sum(ys) / len(ys)
    sxx = sum((x - mx) ** 2 for x in xs)
    slope = sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / sxx if sxx else 0.0
    icpt = my - slope * mx
    ss_res = sum((y - (icpt + slope * x)) ** 2 for x, y in zip(xs, ys))
    ss_tot = sum((y - my) ** 2 for y in ys)
    return slope, icpt, (1 - ss_res / ss_tot) if ss_tot else 0.0


def metr_points():
    """The gauge's METR rows, read the way scripts/site.py reads them."""
    pts = []
    with (ROOT / "data" / "world_measures.csv").open(newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if r["speaker_id"] == "metr" and r["unit"] == "minutes":
                v = float(r["value"])
                pts.append(dict(key=r["aggregate_id"].removeprefix("metr-th11-"), date=parse_date(r["date"]), value=v,
                                frontier="not the frontier" not in r["notes"], over16=v > 960,
                                name=r["measure"].split(", ", 1)[1].split(" (METR")[0]))
    return sorted(pts, key=lambda p: p["date"])


def trailing(frontier, value, to_days):
    """For each frontier point, a line fitted over the year before it (three points or more).
    `value` gives the number fitted against time; `to_days` turns the slope per year into days per doubling."""
    out = []
    for p in frontier:
        win = [q for q in frontier if 0 <= (p["date"] - q["date"]).days <= 365]
        if len(win) < 3:
            continue
        slope, _, _ = fit([year_frac(q["date"]) for q in win], [value(q) for q in win])
        if slope > 0:
            out.append(dict(date=p["date"], days=to_days(slope), n=len(win), over16=any(q.get("over16") for q in win)))
    return out


def running_best(rows):
    """Rows that were the best so far on the day they came out (the frontier), oldest first."""
    out, best = [], -math.inf
    for r in sorted(rows, key=lambda r: r["date"]):
        if r["value"] > best:
            best = r["value"]
            out.append(r)
    return out


def epoch_benchmark(name, column):
    """One row per system from an Epoch benchmark file: its best score across settings, as a share of 1."""
    best = {}
    with (OUT / name).open(newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if not r[column] or not r["Release date"]:
                continue
            base = r["Model version"].rsplit("_", 1)[0] if "_" in r["Model version"] else r["Model version"]
            row = dict(version=base, date=parse_date(r["Release date"]), value=float(r[column]))
            if base not in best or row["value"] > best[base]["value"]:
                best[base] = row
    return sorted(best.values(), key=lambda r: r["date"])


def gauge(days):
    return max(0.0, min(1.0, (T_REF - days) / (T_REF - T_STAR)))


def quiet_dates(ax, months=(1, 7)):
    ax.xaxis.set_major_locator(mdates.MonthLocator(bymonth=list(months)))
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))
    ax.grid(axis="x", visible=False)
    ax.grid(axis="y", color=cs.GRID, lw=0.8)


def minutes_axis(ax, ticks=((1, "1 minute"), (10, "10 minutes"), (60, "1 hour"), (480, "8 hours"), (2400, "40 hours"))):
    ax.set_yscale("log")
    ax.set_yticks([t for t, _ in ticks])
    ax.set_yticklabels([s for _, s in ticks])
    ax.minorticks_off()


def main():
    numbers = {"retrieved": RETRIEVED, "threshold_days": T_STAR, "reference_days": T_REF}
    metr = metr_points()
    metr_frontier = [p for p in metr if p["frontier"]]
    metr_series = trailing(metr_frontier, lambda q: math.log(q["value"]), lambda s: math.log(2) / s * 365.25)
    # The site's own table is the check that this script reads the series as the gauge does.
    with (ROOT / "site" / "leg-a-doubling-time.csv").open(newline="") as f:
        site_rows = list(csv.DictReader(f))
    assert [f"{s['days']:.1f}" for s in metr_series] == [r["days_per_doubling"] for r in site_rows], "METR windows differ from the site's table"
    metr_clean = [s for s in metr_series if not s["over16"]]
    numbers["metr"] = dict(last_scorable_window=metr_clean[-1]["date"].isoformat(), days=round(metr_clean[-1]["days"], 1),
                           gauge=round(gauge(metr_clean[-1]["days"]), 3))

    # ------------------------------------------------------------------ Epoch Capabilities Index
    with (OUT / "epoch-eci-scores-2026-11-11.csv").open(newline="", encoding="utf-8") as f:
        eci = [dict(name=r["Model"], date=parse_date(r["date"]), value=float(r["eci"]),
                    lo=float(r["eci_ci_low"] or r["eci"]), hi=float(r["eci_ci_high"] or r["eci"]))
               for r in csv.DictReader(f) if r["eci"] and r["date"]]
    eci_by_name = {r["name"]: r for r in eci}
    both = [dict(p, eci=eci_by_name[ECI_NAME[p["key"]]]["value"]) for p in metr if p["key"] in ECI_NAME]
    usable = [b for b in both if not b["over16"]]
    slope, icpt, r2 = fit([b["eci"] for b in usable], [math.log2(b["value"]) for b in usable])
    points_per_doubling = 1 / slope
    numbers["eci_conversion"] = dict(systems_in_both=len(both), doublings_per_point=round(slope, 4),
                                     points_per_doubling=round(points_per_doubling, 2), r_squared=round(r2, 3),
                                     first=min(b["date"] for b in both).isoformat(), last=max(b["date"] for b in both).isoformat())
    to_minutes = lambda e: 2 ** (icpt + slope * e)

    eci_frontier = running_best(eci)
    eci_series = trailing(eci_frontier, lambda q: q["value"], lambda s: 365.25 * points_per_doubling / s)
    for s in eci_series:
        s["points_per_year"] = 365.25 * points_per_doubling / s["days"]
    # Windows that end inside the stretch where METR also has a scorable window: the overlap.
    first, last = metr_clean[0]["date"], metr_clean[-1]["date"]
    overlap = [s for s in eci_series if first <= s["date"] <= last]
    pairs = []  # each scorable METR window beside the index window that ended most recently on or before it
    for m in metr_clean:
        before = [s for s in eci_series if s["date"] <= m["date"]]
        if before:
            pairs.append((m, before[-1]))
    ratio = [e["days"] / m["days"] for m, e in pairs]
    numbers["eci"] = dict(
        frontier_systems=len(eci_frontier), windows=len(eci_series), overlap_windows=len(overlap),
        overlap_mean_days_metr=round(sum(m["days"] for m, _ in pairs) / len(pairs), 1),
        overlap_mean_days_eci=round(sum(e["days"] for _, e in pairs) / len(pairs), 1),
        overlap_ratio_low=round(min(ratio), 2), overlap_ratio_high=round(max(ratio), 2),
        at_metr_last_window=dict(metr_days=round(pairs[-1][0]["days"], 1), eci_days=round(pairs[-1][1]["days"], 1),
                                 eci_window_end=pairs[-1][1]["date"].isoformat(), eci_gauge=round(gauge(pairs[-1][1]["days"]), 3)),
        latest_window=dict(end=eci_series[-1]["date"].isoformat(), system=eci_frontier[-1]["name"], days=round(eci_series[-1]["days"], 1),
                           points_per_year=round(eci_series[-1]["points_per_year"], 1), systems=eci_series[-1]["n"],
                           gauge=round(gauge(eci_series[-1]["days"]), 3)),
        falling_last_three=bool(eci_series[-1]["days"] < eci_series[-2]["days"] < eci_series[-3]["days"]),
        whole_span_points_per_year=round(fit([year_frac(q["date"]) for q in eci_frontier if q["date"] >= date(2023, 3, 1)],
                                             [q["value"] for q in eci_frontier if q["date"] >= date(2023, 3, 1)])[0], 1))
    numbers["eci"]["whole_span_days"] = round(365.25 * points_per_doubling / numbers["eci"]["whole_span_points_per_year"], 1)

    with (OUT / "eci-overlap-models.csv").open("w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["system", "released", "metr_minutes", "epoch_index", "metr_reading_past_16_hours", "used_in_conversion"])
        for b in both:
            w.writerow([b["name"], b["date"].isoformat(), f"{b['value']:.2f}", f"{b['eci']:.2f}", "yes" if b["over16"] else "no", "no" if b["over16"] else "yes"])
    with (OUT / "eci-doubling-time.csv").open("w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["window_end", "index_points_per_year", "days_per_doubling_on_metr_scale", "frontier_systems_in_window", "share_of_the_way"])
        for s in eci_series:
            w.writerow([s["date"].isoformat(), f"{s['points_per_year']:.1f}", f"{s['days']:.1f}", s["n"], f"{gauge(s['days']):.2f}"])

    # Figure: the conversion.
    fig, ax = cs.figure(10, 6.2)
    fig.subplots_adjust(left=0.11, right=0.97, top=0.84, bottom=0.11)
    xs = [min(b["eci"] for b in both) - 1, max(b["eci"] for b in both) + 1]
    ax.plot(xs, [to_minutes(x) for x in xs], color=cs.INK_2, lw=1.2, linestyle="--")
    for b in both:
        ax.plot(b["eci"], b["value"], "o", ms=7, color=BLUE if not b["over16"] else cs.SURFACE, markeredgecolor=BLUE, markeredgewidth=1.5)
    for key, dx, dy, ha in (("gpt-4", 0, 9, "center"), ("claude-3-5-sonnet-20240620", 6, -10, "left"), ("o3", -7, 4, "right"),
                            ("gpt-5-2025-08-07", -7, 4, "right"), ("claude-opus-4-6", -7, 4, "right"), ("gpt-5-4", 7, -10, "left")):
        b = next(x for x in both if x["key"] == key)
        ax.annotate(b["name"], (b["eci"], b["value"]), textcoords="offset points", xytext=(dx, dy), ha=ha, fontsize=8, color=cs.INK)
    minutes_axis(ax, ((1, "1 minute"), (10, "10 minutes"), (60, "1 hour"), (480, "8 hours"), (960, "16 hours")))
    ax.grid(axis="x", visible=False)
    ax.grid(axis="y", color=cs.GRID, lw=0.8)
    ax.set_xlabel("Epoch Capabilities Index", fontsize=9, color=cs.INK_2)
    ax.set_ylabel("METR: longest job done right half the time", fontsize=9, color=cs.INK_2)
    cs.titles(fig, f"Every {points_per_doubling:.1f} points on Epoch's index went with a doubling of METR's job length",
              f"The {len(both)} systems measured by both, {both[0]['date'].year} to {both[-1]['date'].year}. Dashed: the straight line that fits them best "
              f"(it accounts for {100 * r2:.0f}% of the spread).",
              f"Sources: METR (benchmark_results_1_1.yaml) and Epoch AI (eci_scores.csv, retrieved {RETRIEVED}, CC BY). agizeitgeist.com/data")
    fig.savefig(OUT / "overlap-eci-conversion.png", facecolor=cs.SURFACE)
    plt.close(fig)

    # Figure: the two series over time, and the days to double each one gives.
    fig, (ax, ax2) = cs.figure(10, 8.6, nrows=2, gridspec_kw={"height_ratios": [3, 2.4], "hspace": 0.42})
    fig.subplots_adjust(left=0.11, right=0.97, top=0.88, bottom=0.07)
    shown = [q for q in eci_frontier if q["date"] >= date(2023, 3, 1)]
    ax.plot([q["date"] for q in shown], [to_minutes(q["value"]) for q in shown], color=ORANGE, lw=1.5, alpha=0.6)
    ax.plot([q["date"] for q in shown], [to_minutes(q["value"]) for q in shown], "o", ms=5, color=ORANGE, label="Epoch's index, best system at the time, put on METR's scale")
    for p in metr_frontier:
        if p["date"] >= date(2023, 3, 1):
            ax.plot(p["date"], p["value"], "o", ms=6.5, color=BLUE if not p["over16"] else cs.SURFACE, markeredgecolor=BLUE, markeredgewidth=1.5)
    ax.plot([], [], "o", color=BLUE, label="METR's job length, best system at the time (hollow: past 16 hours)")
    ax.axhline(960, color=cs.INK_2, linestyle=":", linewidth=1)
    ax.text(date(2023, 3, 10), 960 * 1.25, "16 hours: METR's tests cannot measure reliably beyond this", color=cs.INK_2, fontsize=8)
    ax.axvline(date(2026, 4, 7), color=cs.INK_2, lw=0.8)
    ax.text(date(2026, 4, 17), 100, "METR's last\nreading", fontsize=8, color=cs.INK_2, va="top")
    minutes_axis(ax, ((1, "1 minute"), (10, "10 minutes"), (60, "1 hour"), (480, "8 hours"), (2400, "40 hours"), (9600, "160 hours")))
    quiet_dates(ax)
    ax.legend(loc="lower right", frameon=False, fontsize=8.5, labelcolor=cs.INK)
    ax.set_title("The longest programming job the best system gets right half the time", loc="left", fontsize=10, color=cs.INK)

    for s in metr_series:
        ax2.plot(s["date"], s["days"], "o", ms=6.5, color=BLUE if not s["over16"] else cs.SURFACE, markeredgecolor=BLUE, markeredgewidth=1.5, zorder=3)
    ax2.plot([s["date"] for s in metr_series], [s["days"] for s in metr_series], color=BLUE, lw=1.5, alpha=0.6)
    ax2.plot([s["date"] for s in eci_series], [s["days"] for s in eci_series], color=ORANGE, lw=1.5, alpha=0.6)
    ax2.plot([s["date"] for s in eci_series], [s["days"] for s in eci_series], "o", ms=5, color=ORANGE, zorder=3)
    ax2.axhline(T_STAR, color=cs.INK, linestyle="--", linewidth=1.2)
    top = 260  # two index windows in early 2024 sit far above this and are named in words instead
    ax2.text(date(2023, 3, 10), T_STAR + 9, f"it would count here: doubling every {T_STAR:.0f} days, and still getting quicker", fontsize=8.5, color=cs.INK)
    ax2.axvspan(first, last, color=cs.GRID, alpha=0.45, zorder=0)
    ax2.text(first, top * 0.97, " the overlap: both give a scorable figure", fontsize=8, color=cs.INK_2, va="top")
    off = [s for s in eci_series if s["days"] > top]
    if off:
        ax2.annotate("off the chart: " + " and ".join(f"{s['days']:.0f}" for s in off) + " days\nin early 2024, before METR had\nenough systems to give a figure",
                     (date(2023, 3, 10), top * 0.97), ha="left", va="top", fontsize=8, color=cs.INK_2)
    ax2.set_ylim(0, top)
    ax2.set_xlim(ax.get_xlim())
    ax2.set_ylabel("days to double", fontsize=9, color=cs.INK_2)
    quiet_dates(ax2)
    ax2.set_title("How many days the job length took to double, over the year before each point", loc="left", fontsize=10, color=cs.INK)
    lw = numbers["eci"]["latest_window"]
    cs.titles(fig, "Epoch's index tells the same story as METR's series, and keeps going", None,
              f"Sources: METR and Epoch AI (retrieved {RETRIEVED}, CC BY). The index is turned into job length with the line in overlap-eci-conversion.png. agizeitgeist.com/data")
    fig.savefig(OUT / "overlap-eci.png", facecolor=cs.SURFACE)
    plt.close(fig)

    # ------------------------------------------------------------------ MirrorCode and the Remote Labor Index
    metr_by_key = {p["key"]: p for p in metr}
    for label, fname, column, colour, out_name, title, unit in (
            ("MirrorCode", "epoch-mirrorcode-2026-11-11.csv", "Best score (across scorers)", GREEN, "overlap-mirrorcode.png",
             "MirrorCode mostly agrees with METR, but its best score is already {top:.0f}%", "share of the programs rebuilt exactly"),
            ("Remote Labor Index", "epoch-remote-labor-index-2026-11-11.csv", "Score", PURPLE, "overlap-remote-labor-index.png",
             "The Remote Labor Index mostly agrees with METR and has room left: {top:.0f}%", "share of real paid freelance projects done in full")):
        rows = epoch_benchmark(fname, column)
        frontier = running_best(rows)
        shared = []
        for key, prefix in VERSION_PREFIX.items():
            hit = [r for r in rows if r["version"].startswith(prefix)]
            if hit:
                shared.append(dict(metr_by_key[key], score=max(h["value"] for h in hit)))
        shared.sort(key=lambda b: b["date"])
        # Does the score put the shared systems in the same order as METR's job length? (rank agreement)
        n = len(shared)
        agree = sum(1 for i in range(n) for j in range(i + 1, n)
                    if (shared[i]["value"] - shared[j]["value"]) * (shared[i]["score"] - shared[j]["score"]) > 0)
        series = trailing(frontier, lambda q: math.log(q["value"]), lambda s: math.log(2) / s * 365.25)
        key = "mirrorcode" if label == "MirrorCode" else "remote_labor_index"
        numbers[key] = dict(systems=len(rows), first=rows[0]["date"].isoformat(), last=rows[-1]["date"].isoformat(),
                            frontier_first=dict(system=frontier[0]["version"], date=frontier[0]["date"].isoformat(), share=round(frontier[0]["value"], 3)),
                            frontier_last=dict(system=frontier[-1]["version"], date=frontier[-1]["date"].isoformat(), share=round(frontier[-1]["value"], 3)),
                            shared_with_metr=[dict(system=b["name"], metr_minutes=round(b["value"], 1), share=round(b["score"], 3)) for b in shared],
                            pairs_in_same_order=f"{agree} of {n * (n - 1) // 2}",
                            share_doubling_days_latest_year=round(series[-1]["days"], 1) if series else None,
                            doublings_left_before_100_percent=round(math.log2(1 / frontier[-1]["value"]), 2))

        fig, (ax, ax2) = cs.figure(10, 5.6, ncols=2, gridspec_kw={"width_ratios": [1, 1.25], "wspace": 0.3})
        fig.subplots_adjust(left=0.1, right=0.97, top=0.78, bottom=0.12)
        for b in shared:
            ax.plot(b["value"], 100 * b["score"], "o", ms=7, color=colour)
            ax.annotate(b["name"], (b["value"], 100 * b["score"]), textcoords="offset points", xytext=(6, 4), fontsize=7.5, color=cs.INK)
        ax.set_xscale("log")
        ax.set_xticks([120, 240, 480, 960])
        ax.set_xticklabels(["2 hours", "4 hours", "8 hours", "16 hours"])
        ax.minorticks_off()
        ax.set_xlim(100, 1500)
        ax.set_ylim(0, max(100 * b["score"] for b in shared) * 1.35)
        ax.yaxis.set_major_formatter(lambda v, _: f"{v:.0f}%")
        ax.grid(axis="x", visible=False)
        ax.grid(axis="y", color=cs.GRID, lw=0.8)
        ax.set_xlabel("METR: longest job done right half the time", fontsize=9, color=cs.INK_2)
        ax.set_title(f"The {n} systems measured by both", loc="left", fontsize=10, color=cs.INK)
        ax2.plot([r["date"] for r in rows], [100 * r["value"] for r in rows], "o", ms=5, color=cs.SURFACE, markeredgecolor=colour, markeredgewidth=1.2)
        ax2.plot([r["date"] for r in frontier], [100 * r["value"] for r in frontier], color=colour, lw=1.5, alpha=0.6)
        ax2.plot([r["date"] for r in frontier], [100 * r["value"] for r in frontier], "o", ms=6, color=colour)
        ax2.axvline(date(2026, 4, 7), color=cs.INK_2, lw=0.8)
        ax2.text(date(2026, 4, 1), 97, "METR's last reading", fontsize=8, color=cs.INK_2, ha="right", va="top")
        ax2.set_ylim(0, 100)
        ax2.yaxis.set_major_formatter(lambda v, _: f"{v:.0f}%")
        quiet_dates(ax2, months=(1, 4, 7, 10))
        ax2.set_title("Every system, by the day it came out (filled: the best so far)", loc="left", fontsize=10, color=cs.INK)
        cs.titles(fig, title.format(top=100 * frontier[-1]["value"], low=100 * frontier[0]["value"]),
                  f"{label}: {unit}. Left, against METR's job length; right, over time.",
                  f"Sources: METR and Epoch AI's copy of {label} results (retrieved {RETRIEVED}, CC BY). agizeitgeist.com/data")
        fig.savefig(OUT / out_name, facecolor=cs.SURFACE)
        plt.close(fig)

    (OUT / "overlap-numbers.json").write_text(json.dumps(numbers, indent=2) + "\n")
    print(json.dumps(numbers, indent=2))


if __name__ == "__main__":
    main()
