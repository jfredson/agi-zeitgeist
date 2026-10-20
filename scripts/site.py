#!/usr/bin/env python3
"""Build the static site (site/index.html, its figures, the rendered docs and the data copies) from data/*.csv.

The page has two halves that are deliberately kept apart:

- what people believe (the tracker proper: statements, surveys, markets, communities);
- what the world is doing (data/world_measures.csv), shown under the draft definition
  of "entering the singularity" in docs/singularity-entry-definition-draft-2026-10-07.md.

The definition was adopted on 2026-10-08 (amendment A19) with four legs, and its frozen
values live in docs/singularity-entry-thresholds.json. `score()` turns the readings into
the four gauges, the progress number (the smallest gauge) and the status. Leg B has no
ledger yet and is shown as not yet measurable.

Also renders every Markdown document under docs/ (plus the README) to site/docs/ with
pandoc, and copies the CSV data to site/data/, so the public page never links into the
private repository.

    .venv/bin/python scripts/site.py
"""

import csv
import html
import json
import math
import re
import shutil
import subprocess
import tomllib
from datetime import date, datetime

from zoneinfo import ZoneInfo


def pacific_today():
    """Today in Pacific time, John's clock. A cloud workspace keeps universal time, so an evening
    run would otherwise be stamped a day ahead (John's ruling, 2026-10-18)."""
    return datetime.now(ZoneInfo("America/Los_Angeles")).date()
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.dates as mdates
import matplotlib.pyplot as plt

import chart_style as cs

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
SITE = ROOT / "site"
DOCS = ROOT / "docs"
DRAFT = "docs/singularity-entry-definition-draft-2026-10-07.md"
DEFINITION = "docs/singularity-entry-definition.md"
SITE_URL = "https://agizeitgeist.com"
THRESHOLDS = DOCS / "singularity-entry-thresholds.json"
REPO = "https://github.com/jfredson/agi-zeitgeist"

# Same reference palette as charts.py (dataviz skill, categorical slots), fixed order.
BLUE, ORANGE, GREEN, YELLOW = "#2a78d6", "#eb6834", "#1baf7a", "#eda100"
INK, MUTED, GRID = "#1f2933", "#6b7785", "#e3e8ee"

plt.rcParams.update({
    "font.size": 10, "axes.edgecolor": GRID, "axes.labelcolor": INK, "xtick.color": MUTED,
    "ytick.color": MUTED, "axes.grid": True, "grid.color": GRID, "grid.linewidth": 0.8,
    "axes.spines.top": False, "axes.spines.right": False, "figure.dpi": 160,
})


def read(name):
    with (DATA / name).open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def parse_date(s):
    parts = [int(p) for p in s.split("-")] + [1, 1]
    return date(parts[0], parts[1], parts[2])


def year_frac(d):
    return d.year + (d.timetuple().tm_yday - 1) / 365.25


def git_commit():
    try:
        return subprocess.check_output(["git", "rev-parse", "--short", "HEAD"], cwd=ROOT, text=True).strip()
    except Exception:
        return "uncommitted"


# ----------------------------------------------------------------------------- leg A
def leg_a(world):
    """Time-horizon readings and the trailing twelve-month doubling time of the frontier."""
    rows = [r for r in world if r["speaker_id"] == "metr" and r["unit"] == "minutes"]
    pts = []
    for r in rows:
        lo, hi = [float(x) for x in r["notes"].split("95% interval ")[1].split(" minutes")[0].split(" to ")]
        pts.append(dict(id=r["aggregate_id"], date=parse_date(r["date"]), value=float(r["value"]), lo=lo, hi=hi,
                        frontier="not the frontier" not in r["notes"],
                        over16=float(r["value"]) > 960,
                        name=r["measure"].split(", ", 1)[1].split(" (METR")[0], url=r["source_url"]))
    pts.sort(key=lambda p: p["date"])
    frontier = [p for p in pts if p["frontier"]]

    # Trailing 12-month doubling time on the frontier (draft section 2, leg A), needing
    # at least three frontier points in the window. Days per doubling.
    series = []
    for p in frontier:
        win = [q for q in frontier if 0 <= (p["date"] - q["date"]).days <= 365]
        if len(win) < 3:
            continue
        xs = [year_frac(q["date"]) for q in win]
        ys = [math.log(q["value"]) for q in win]
        mx, my = sum(xs) / len(xs), sum(ys) / len(ys)
        sxx = sum((x - mx) ** 2 for x in xs)
        slope = sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / sxx if sxx else 0
        if slope > 0:
            series.append(dict(date=p["date"], days=math.log(2) / slope * 365.25, n=len(win),
                               over16=any(q["over16"] for q in win)))

    t_star = json.loads(THRESHOLDS.read_text())["leg_a"]["doubling_time_threshold_days"]
    fig, (ax, ax2) = cs.figure(10, 8.2, nrows=2, gridspec_kw={"height_ratios": [3, 2], "hspace": 0.45})
    fig.subplots_adjust(left=0.1, right=0.97, top=0.89, bottom=0.08)
    blue, orange = cs.PALETTE[0], cs.PALETTE[1]
    for p in pts:
        ax.plot([p["date"], p["date"]], [p["lo"], p["hi"]], color=blue, alpha=0.3, linewidth=1.5)
        ax.plot(p["date"], p["value"], "o", ms=6, color=blue if p["frontier"] else cs.SURFACE,
                markeredgecolor=blue, markeredgewidth=1.5)
    ax.axhline(960, color=cs.INK_2, linestyle=":", linewidth=1)
    ax.text(pts[0]["date"], 960 * 1.25, "16 hours: METR's tests cannot measure reliably beyond this", color=cs.INK_2, fontsize=8)
    ax.set_yscale("log")
    ax.set_yticks([0.1, 1, 10, 60, 480, 2400])
    ax.set_yticklabels(["6 seconds", "1 minute", "10 minutes", "1 hour", "8 hours", "40 hours"])
    ax.minorticks_off()
    ax.grid(axis="x", visible=False)
    ax.grid(axis="y", color=cs.GRID, lw=0.8)
    ax.set_title("The longest programming job each new AI system gets right half the time", loc="left", fontsize=10, color=cs.INK)
    ax.plot([], [], "o", color=blue, label="the best system at the time")
    ax.plot([], [], "o", color=cs.SURFACE, markeredgecolor=blue, label="not the best at the time")
    ax.legend(loc="lower right", frameon=False, fontsize=8.5, labelcolor=cs.INK)
    for p in frontier[-1:]:
        ax.annotate(p["name"], (p["date"], p["value"]), textcoords="offset points", xytext=(-8, 4), ha="right", fontsize=8, color=cs.INK)
    ax.xaxis.set_major_locator(mdates.YearLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))

    for s in series:
        ax2.plot(s["date"], s["days"], "o", ms=6, color=orange if not s["over16"] else cs.SURFACE,
                 markeredgecolor=orange, markeredgewidth=1.5, zorder=3)
    ax2.plot([s["date"] for s in series], [s["days"] for s in series], color=orange, linewidth=1.5, alpha=0.6)
    ax2.axhline(t_star, color=cs.INK, linestyle="--", linewidth=1.2)
    ax2.text(series[0]["date"], t_star + 6, f"it would count here: doubling every {t_star:.0f} days, and still getting quicker",
             fontsize=8.5, color=cs.INK)
    ax2.set_ylim(0, max(s["days"] for s in series) * 1.2)
    ax2.set_ylabel("days to double", fontsize=9, color=cs.INK_2)
    ax2.grid(axis="x", visible=False)
    ax2.grid(axis="y", color=cs.GRID, lw=0.8)
    ax2.set_title("How many days the job length took to double, over the year before each point", loc="left", fontsize=10, color=cs.INK)
    ax2.plot([], [], "o", color=cs.SURFACE, markeredgecolor=orange, label="includes a reading past 16 hours (not scored)")
    ax2.legend(loc="upper right", frameon=False, fontsize=8.5, labelcolor=cs.INK)
    ax2.xaxis.set_major_locator(mdates.MonthLocator(bymonth=[1, 7]))
    ax2.xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))
    cs.titles(fig, "AI's job length doubles about every four months, not yet every month", None,
              "Source: METR, a research group that tests AI systems; thin lines are its range of likely values. agizeitgeist.com/data")
    fig.savefig(SITE / "leg-a-time-horizon.png", facecolor=cs.SURFACE)
    plt.close(fig)
    with (SITE / "leg-a-doubling-time.csv").open("w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["window_end", "days_per_doubling", "frontier_points_in_window", "window_includes_reading_over_16h"])
        for s in series:
            w.writerow([s["date"].isoformat(), f"{s['days']:.1f}", s["n"], "yes" if s["over16"] else "no"])
    return pts, series


# ----------------------------------------------------------------------------- leg B
def leg_b(aggregates):
    """Stand-in for the forecast horizon: how fast the consensus arrival date is being pulled in."""
    ai = sorted([r for r in aggregates if r["aggregate_id"].startswith("aiimpacts-") and r["aggregate_id"].endswith("-hlmi50")],
                key=lambda r: r["date"])
    pts = []
    for r in ai:
        d = parse_date(r["date"])
        pts.append(dict(id=r["aggregate_id"], date=d, t=year_frac(d), m=float(r["value"]), url=r["source_url"],
                        n=(f"{int(r['n']):,} researchers asked" if r.get("n") else "")))
    for p in pts:
        p["remaining"] = p["m"] - p["t"]
    steps = []
    for a, b in zip(pts, pts[1:]):
        dt = b["t"] - a["t"]
        dd = b["remaining"] - a["remaining"]
        steps.append(dict(frm=a, to=b, years=dt, change=dd, pull_in=-dd / dt - 1))  # draft: v = -dD/dt - 1

    mb = [r for r in aggregates if r["aggregate_id"] == "mullerbostrom-2013-hlmi50"]
    mani = sorted([r for r in aggregates if r["aggregate_id"].startswith("manifold-agi2030-")], key=lambda r: r["date"])

    with (SITE / "leg-b-pull-in.csv").open("w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["from_survey", "to_survey", "calendar_years_between", "change_in_years_remaining", "excess_pull_in_per_year"])
        for s in steps:
            w.writerow([s["frm"]["id"], s["to"]["id"], f"{s['years']:.2f}", f"{s['change']:.1f}", f"{s['pull_in']:.1f}"])
    return pts, steps, mani


# ----------------------------------------------------------------------------- leg C
def leg_c(world):
    rows = sorted([r for r in world if r["unit"] == "percent"], key=lambda r: r["date"])
    pts = []
    for r in rows:
        bound = "upper bound" if "upper bound" in r["notes"] else "lower bound" if "lower bound" in r["notes"] else ""
        pts.append(dict(id=r["aggregate_id"], date=parse_date(r["date"]), value=float(r["value"]), measure=r["measure"],
                        url=r["source_url"], bound=bound, who=r["speaker_id"]))
    # Only the scored figure is drawn: Anthropic's share of its AI research its AI leads. Google's
    # code share and Anthropic's "collaborates" share measure other things and stay in the table.
    leads = [p for p in pts if p["id"].endswith("-rd-leads")]
    line = json.loads(THRESHOLDS.read_text())["leg_c"]["share_threshold"] * 100
    fig, ax = cs.figure(10, 3.8)
    fig.subplots_adjust(left=0.16, right=0.95, top=0.72, bottom=0.2)
    green = cs.PALETTE[2]
    for i, p in enumerate(leads):
        y = len(leads) - 1 - i
        ax.barh(y, p["value"], color=green, height=0.5)
        shown = "under 1%" if p["bound"] == "upper bound" else f"{int(p['value'])}%"
        ax.text(p["value"] + 1.2, y, shown, va="center", fontsize=11, fontweight="bold", color=green)
        ax.text(-2, y, p["date"].strftime("%B %Y"), ha="right", va="center", fontsize=10, color=cs.INK)
    ax.axvline(line, color=cs.INK, linestyle="--", linewidth=1.2)
    ax.text(line + 1, len(leads) - 0.45, f"it would count at {line:.0f}%", fontsize=9, color=cs.INK)
    ax.set_xlim(0, 100)
    ax.set_ylim(-0.6, len(leads) - 0.3)
    ax.set_yticks([])
    ax.set_xticks([0, 25, 50, 75, 100])
    ax.set_xticklabels(["0%", "25%", "50%", "75%", "100%"])
    ax.grid(axis="x", color=cs.GRID, lw=0.8)
    ax.set_axisbelow(True)
    cs.titles(fig, "Anthropic says its AI went from leading under 1% of its research to 26% in six months",
              "Share of Anthropic's AI research work led by its own AI, by the company's own count.",
              "Source: Anthropic's own statements, judged by its AI itself; nobody outside the company can check them. agizeitgeist.com/data")
    fig.savefig(SITE / "leg-c-self-reports.png", facecolor=cs.SURFACE)
    plt.close(fig)
    return pts


# ----------------------------------------------------------------------------- leg D
def leg_d(world):
    """World output growth and its doubling time, one reading a year (World Bank)."""
    rows = sorted([r for r in world if r["unit"] == "percent_growth"], key=lambda r: r["date"])
    pts = []
    for r in rows:
        g = float(r["value"])
        pts.append(dict(id=r["aggregate_id"], year=int(r["date"]), growth=g, url=r["source_url"],
                        doubling=(math.log(2) / math.log(1 + g / 100)) if g > 0 else None))
    fig, ax = cs.figure(10, 4.6)
    fig.subplots_adjust(left=0.07, right=0.97, top=0.8, bottom=0.12)
    ax.bar([p["year"] for p in pts], [p["growth"] for p in pts], color=cs.PALETTE[2], width=0.8)
    ax.axhline(30, color=cs.INK, linestyle="--", linewidth=1.2)
    ax.text(pts[0]["year"], 31, "it would count here: 30% in a year", fontsize=9, color=cs.INK)
    ax.axhline(0, color=cs.INK_2, linewidth=0.8)
    ax.set_ylim(-5, 35)
    ax.set_yticks([0, 10, 20, 30])
    ax.set_yticklabels(["0%", "10%", "20%", "30%"])
    ax.grid(axis="x", visible=False)
    ax.grid(axis="y", color=cs.GRID, lw=0.8)
    ax.set_axisbelow(True)
    cs.titles(fig, "The world's economy grows about 3% a year; it would count at 30%",
              f"Growth of everything the world produces, after prices, each year from {pts[0]['year']} to {pts[-1]['year']}.",
              "Source: the World Bank. agizeitgeist.com/data")
    fig.savefig(SITE / "leg-d-world-growth.png", facecolor=cs.SURFACE)
    plt.close(fig)
    with (SITE / "leg-d-world-growth.csv").open("w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["year", "growth_percent", "doubling_time_years"])
        for q in pts:
            w.writerow([q["year"], f"{q['growth']:.2f}", f"{q['doubling']:.1f}" if q["doubling"] else ""])
    return pts


# ----------------------------------------------------------------------------- scoring
def clip(x):
    return max(0.0, min(1.0, x))


def score(th, a_series, c_pts, d_pts):
    """The four gauges, the progress number and the status, from the frozen thresholds."""
    out = {"adopted": th["adopted"], "reference_year": th["reference_year"], "persistence": th["persistence_quarters"]}

    # Leg A: last trailing window without a reading past 16 hours; falling over the last two windows.
    la = th["leg_a"]
    clean = [s for s in a_series if not s["over16"]]
    if clean:
        cur = clean[-1]
        t_star, t_ref = la["doubling_time_threshold_days"], la["reference_doubling_time_days"]
        g = clip((t_ref - cur["days"]) / (t_ref - t_star))
        falling = len(clean) >= 3 and clean[-1]["days"] < clean[-2]["days"] < clean[-3]["days"]
        out["A"] = dict(gauge=g, reading=cur["days"], date=cur["date"], t_star=t_star, t_ref=t_ref,
                        at_threshold=(cur["days"] <= t_star and falling), falling=falling, measurable=True)
    else:
        out["A"] = dict(gauge=None, measurable=False)

    # Leg B: no ledger yet.
    out["B"] = dict(gauge=None, measurable=False, note=th["leg_b"]["status"], threshold=th["leg_b"]["horizon_threshold_years"])

    # Leg C: latest Anthropic "leads" share.
    leads = sorted([p for p in c_pts if p["id"].endswith("-rd-leads")], key=lambda p: p["date"])
    lc = th["leg_c"]
    if leads:
        f = leads[-1]["value"] / 100
        out["C"] = dict(gauge=clip(f / lc["share_threshold"]), reading=f, date=leads[-1]["date"], row=leads[-1],
                        threshold=lc["share_threshold"], at_threshold=f >= lc["share_threshold"], measurable=True)
    else:
        out["C"] = dict(gauge=None, measurable=False)

    # Leg D: latest annual world growth against the 30% line; reference is the 1961-to-2019 mean.
    ld = th["leg_d"]
    ref_years = [p for p in d_pts if p["year"] <= th["reference_year"]]
    g_ref = sum(p["growth"] for p in ref_years) / len(ref_years)
    t_ref = math.log(2) / math.log(1 + g_ref / 100)
    g_star = ld["growth_threshold_percent_per_year"]
    t_star = math.log(2) / math.log(1 + g_star / 100)
    cur = d_pts[-1]
    t_cur = cur["doubling"] if cur["doubling"] else float("inf")
    out["D"] = dict(gauge=clip((t_ref - t_cur) / (t_ref - t_star)), reading=cur["growth"], year=cur["year"],
                    doubling=cur["doubling"], g_ref=g_ref, t_ref=t_ref, g_star=g_star, t_star=t_star,
                    at_threshold=cur["growth"] >= g_star, measurable=True)

    measured = {k: v["gauge"] for k, v in out.items() if k in "ABCD" and v.get("measurable")}
    unmeasured = [k for k in "ABCD" if not out[k].get("measurable")]
    out["progress"] = min(measured.values())
    out["progress_is_upper_bound"] = bool(unmeasured)
    out["bottleneck"] = min(measured, key=measured.get)
    out["unmeasured"] = unmeasured
    # The headline (ruled 2026-10-17, docs/headline-proposal-2026-10-17.md): how many of the four
    # parts are past one half, with each part's share as the words. It reports the gauges; it
    # does not combine them, so section 4's P(t) above stays the one progress number.
    names = {"A": "pace", "B": "forecasts", "C": "AI doing the research", "D": "economy"}
    out["parts_past_half"] = sum(1 for g in measured.values() if g > 0.5)
    shares = ", ".join(f"{names[k]} {round(measured[k] * 100)}%" if k in measured else f"{names[k]} unmeasured" for k in "ABCD")
    out["shares_text"] = shares
    # Revised the same evening (amendment A25): the headline is the average share of the way
    # across the measured parts, with the slowest part named. It is a reading aid printed
    # beside P(t), never the status, and never the test's own progress number.
    out["average_share"] = sum(measured.values()) / len(measured)
    out["headline"] = f'{round(out["average_share"] * 100)}%'
    slow = out["bottleneck"]
    out["headline_label"] = (f'of the way, averaged over the {len(measured)} parts that can be measured'
                             f'{" (" + ", ".join(names[k] for k in unmeasured) + " unmeasured)" if unmeasured else ""}; '
                             f'all four must cross, and the slowest, the {names[slow]}, is at {round(measured[slow] * 100)}%')
    if unmeasured:
        out["status"] = "not entered"
    elif all(out[k]["at_threshold"] for k in "ABCD"):
        out["status"] = "mark crossed, under persistence test"
    elif all(out[k]["gauge"] > 0.5 for k in "ABCD"):
        out["status"] = "approaching"
    else:
        out["status"] = "not entered"
    return out


def years_to_line(a_series, c_pts, d_pts, sc):
    """Years to each leg's line if its recent trend continued (amendment A25): per-leg
    sentences with their range for the panels, and the crossing years for the headline's
    on-current-trends sentence. The method is written in docs/amendments.md under A25."""
    out = {}
    cross = {}  # leg -> (earliest year, latest year) or None when the trend does not reach the line
    clean = [w for w in a_series if not w["over16"]]
    if len(clean) >= 4:
        t_star = sc["A"]["t_star"]
        xs = [(w["date"] - clean[0]["date"]).days / 365.25 for w in clean]
        ys = [math.log(w["days"]) for w in clean]
        n = len(xs); mx = sum(xs) / n; my = sum(ys) / n
        b = sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / sum((x - mx) ** 2 for x in xs)
        cur = clean[-1]["days"]
        fast = math.log(cur / t_star, 2)  # years if the doubling time halved every year
        y0 = clean[-1]["date"].year + clean[-1]["date"].timetuple().tm_yday / 365.25
        if b < 0:
            slow = (math.log(t_star) - math.log(cur)) / b
            cross["A"] = (round(y0 + fast), round(y0 + slow))
            out["A"] = (f"Extending the trend gives a range, not a date: over all the twelve-month windows since {clean[0]['date'].year} the "
                        f"doubling time has fallen about {abs(100 * (math.exp(b) - 1)):.0f} percent a year, which would reach {t_star:.0f} days in "
                        f"about {slow:.0f} years; if it halved every year or two, as it did between 2024 and 2025, {fast:.0f} to {2 * fast:.0f} years; "
                        f"and over the latest year it has not fallen at all.")
        else:
            cross["A"] = (round(y0 + fast), None)
            out["A"] = (f"Extending the trend gives no date: the doubling time has not fallen over the windows since {clean[0]['date'].year}. "
                        f"If it halved every year or two, as it did between 2024 and 2025, the line would be {fast:.0f} to {2 * fast:.0f} years away.")
    leads = sorted([p for p in c_pts if p["id"].endswith("-rd-leads")], key=lambda p: p["date"])
    if len(leads) >= 2 and leads[-1]["value"] > leads[-2]["value"] > 0:
        f0, f1 = leads[-2]["value"] / 100, leads[-1]["value"] / 100
        dt = (leads[-1]["date"] - leads[-2]["date"]).days / 365.25
        thr = sc["C"]["threshold"]
        if f1 < thr:
            lin = (thr - f1) / ((f1 - f0) / dt)
            exp_ = math.log(thr / f1) / (math.log(f1 / f0) / dt)
            yc = leads[-1]["date"].year + leads[-1]["date"].timetuple().tm_yday / 365.25
            cross["C"] = (round(yc + max(exp_, 1 / 12)), round(yc + lin))
            out["C"] = (f"At the pace of its first {dt * 12:.0f} months ({leads[-2]['value']:.0f}% to {leads[-1]['value']:.0f}%), the share would reach half in "
                        f"about {lin * 12:.0f} months if it rose steadily, and in about {max(exp_ * 12, 1):.0f} {'month' if max(exp_ * 12, 1) < 1.5 else 'months'} if it kept multiplying; two readings are a thin "
                        f"basis for either.")
    recent = [q for q in d_pts if int(q["year"]) >= 2010]
    if len(recent) >= 5:
        xs = [int(q["year"]) for q in recent]; gs = [q["growth"] for q in recent]
        n = len(xs); mx = sum(xs) / n; mg = sum(gs) / n
        b = sum((x - mx) * (g - mg) for x, g in zip(xs, gs)) / sum((x - mx) ** 2 for x in xs)
        if b <= 0 or (sc["D"]["g_star"] - gs[-1]) / b > 100:
            cross["D"] = None
            out["D"] = (f"Extending the trend gives no date: since 2010 growth has been flat to falling ({b:+.2f} points a year), "
                        f"and the line is {sc['D']['g_star'] / max(q['growth'] for q in d_pts):.0f} times the best year on record.")
        else:
            cross["D"] = (int(xs[-1] + (sc["D"]["g_star"] - gs[-1]) / b),) * 2
            out["D"] = f"At the trend since 2010 ({b:+.2f} points a year) the line would be about {(sc['D']['g_star'] - gs[-1]) / b:.0f} years away."
    if sc["C"].get("measurable") and sc["C"]["at_threshold"]:
        cross["C"] = ("crossed", "crossed")
    out["_cross"] = cross
    out["_sentence"] = crossing_sentence(cross, sc)
    return out


def crossing_sentence(cross, sc):
    """One sentence: on current trends, when each part crosses its line, and whether the test is met."""
    names = {"A": "the pace", "B": "forecasts", "C": "the AI-research share", "D": "the economy"}
    def span(v):
        if v is None:
            return "does not cross its line"
        lo, hi = v
        if lo == "crossed":
            return "has crossed"
        if hi is None:
            return f"does not cross on the fitted trend, though it would by {lo} if its 2024-to-2025 halving resumed"
        return f"crosses in {lo}" if lo == hi else f"crosses between {lo} and {hi}"
    parts, misses = [], []
    for k in "ACD":
        if not sc[k].get("measurable") or k not in cross:
            continue
        v = cross[k]
        if v is None or (v[1] is None):
            misses.append(k)
    order = misses + [k for k in "ACD" if k in cross and k not in misses]
    parts = [f"{names[k]} {span(cross[k])}" for k in order]
    unmeasured = [names[k] for k in "ABCD" if not sc[k].get("measurable")]
    head = ("On current trends the test is not met: " if misses else "On current trends every measured part crosses: ")
    tail = "; ".join(parts)
    if misses:
        tail = tail.replace("; ", ", so the test is not met on current trends; ", 1) if len(parts) > 1 else tail
        head = "On current trends "
    if unmeasured:
        tail += f"; {' and '.join(unmeasured)} unmeasured"
    if not misses:
        latest = max(v[1] for k, v in cross.items() if v and v[1] not in (None, "crossed"))
        head = f"On current trends every measured part has crossed by {latest}: "
    return head + tail + "."


def load_thresholds():
    return json.loads(THRESHOLDS.read_text())


# ----------------------------------------------------------------------------- shell
# Writing rule (John, 2026-10-08; design standard section 1a): the public pages use none of the
# project's internal language and build every idea from scratch, assuming only what a five-year-old
# knows plus what the page has already said. The working documents are published as written, each
# with a preface saying what it is; the plain account lives on the home page.
# The page shell follows the Sentient Horizons design standard (sentient-horizons/design/README.md):
# the icon set (favicon.svg is the source; the PNGs, the .ico and site.webmanifest are rendered from it by the
# family's icons script, sentient-horizons/site/scripts/icons.mjs, pointed at site/), the skeleton site/shell.css
# (copied unchanged from the standard, version in its header) and this
# site's skin site/skin.css ("Gazette", ruled by John 2026-10-17: newsprint, ink, one red for the mark
# and for links, a blue-grey for the gauge bars; light by default), the top bar with two tiers and the
# theme toggle, the skin's backdrop (a broadsheet's column rules) on the home page only, and the five-line
# footer ending "A Sentient Horizons project." (linking to the family's Projects page, John 2026-10-17) with the attribution line "© year John Fredrickson. provenance. licence."
# (No "with Claude" in the line: John, 2026-10-08. Who did the sorting is said in the method section instead.)
SITE_NAME = "AGI Zeitgeist"
SITE_TITLE = "AGI Zeitgeist Tracker"
# The question the headline number answers (John, 2026-10-18); "Are we in the singularity?" sits
# directly above its own answer, the verdict.
HEADLINE_QUESTION = "How far along the way are we?"
TAGLINE = ("A dated record of what people expect from artificial general intelligence, with every quote linked to its source, "
           "and a test of whether the singularity has begun.")
# Labels ruled by John, 2026-10-08.
# Short handles (tracker pattern rule 4.7, ruled for this site by John on 2026-10-18): one word per page, so the
# bar holds one row on laptop and tablet widths; the full names stay as the sections' own headings.
NAV_PRIMARY = [("/#belief", "Zeitgeist"), ("/#singularity", "Singularity"), ("/claims/", "Claims"), ("/#method", "Method"), ("/news/", "News")]  # "Claims": amendment A27; News: tracker pattern rule 4.10, John 2026-10-18
# "Family" ends the lighter tier on every tracker and links to the family's Projects page (John, 2026-10-17; tracker pattern rule 4.9).
NAV_SECONDARY = [("/docs/singularity-entry-definition", "Definitions"), ("/docs/amendments", "Changelog"), ("https://sentient-horizons.com/projects/", "Family")]
FOOTER_LINKS = [("/data/", "Download the data"), ("/#method", "Method and data"), ("/disagree/", "Disagree with something"),
                ("/docs/singularity-entry-definition", "Definitions"), ("/docs/amendments", "Changelog")]

THEME_SCRIPT = """<script>
(function(){try{var s=localStorage.getItem('theme');var t=s==='light'||s==='dark'?s:(window.matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light');document.documentElement.dataset.theme=t;}catch(e){}})();
</script>"""

SHELL_SCRIPT = """<script>
(function(){var h=document.querySelector('.site-header');var b=h&&h.querySelector('.nav-toggle');var m=document.getElementById('site-nav');
if(b&&m){var so=function(o){h.classList.toggle('nav-open',o);b.setAttribute('aria-expanded',o?'true':'false');};
b.addEventListener('click',function(){so(!h.classList.contains('nav-open'));});m.addEventListener('click',function(e){if(e.target.closest('a'))so(false);});
window.addEventListener('resize',function(){if(window.innerWidth>820)so(false);});}
var t=document.querySelector('.theme-toggle');var meta=document.getElementById('theme-color-meta');var C={dark:'#111214',light:'#f2f1ec'};
function sync(x){document.documentElement.dataset.theme=x;if(meta)meta.setAttribute('content',C[x]||C.light);}
sync(document.documentElement.dataset.theme==='dark'?'dark':'light');
if(t)t.addEventListener('click',function(){var n=document.documentElement.dataset.theme==='light'?'dark':'light';try{localStorage.setItem('theme',n);}catch(e){}sync(n);});})();
</script>"""

ICON_MENU = ('<svg class="ico-open" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M3 6h18M3 12h18M3 18h18"></path></svg>'
             '<svg class="ico-close" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M6 6l12 12M18 6L6 18"></path></svg>')
ICON_THEME = ('<svg class="icon-sun" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="4"></circle><path d="M12 2v2M12 20v2M4.93 4.93l1.41 1.41M17.66 17.66l1.41 1.41M2 12h2M20 12h2M4.93 19.07l1.41-1.41M17.66 6.34l1.41-1.41"></path></svg>'
              '<svg class="icon-moon" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path></svg>')

# Styles of this site only, on top of the shared file. Tokens only; no new colours.
SITE_CSS = """
.brand { white-space: nowrap; }
.with-rail { display: grid; grid-template-columns: minmax(0, 1fr) 280px; gap: 40px; align-items: start; }
.rail { position: sticky; top: 86px; border: 1px solid var(--line); border-radius: var(--radius); padding: 16px 16px 14px; background: var(--panel); font-family: var(--sans); }
.rail h4 { margin: 0 0 8px; padding-bottom: 8px; border-bottom: 1px solid var(--line); font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: var(--muted); font-weight: 600; }
.rail h4 + h4, .rail .rail-sec { margin-top: 18px; }
.rail .rstatus { font-size: 13px; color: var(--text-soft); margin: 0 0 10px; line-height: 1.45; }
.rail .rstatus b { color: var(--text); }
.rail .mini { display: grid; grid-template-columns: 1.1em 1fr; gap: 6px 8px; align-items: center; font-size: 12px; color: var(--muted); }
.rail .mini .bar { margin: 0; height: 12px; }
.rail .mini .bar span { display: none; }
.rail .mini .bar.none { background: repeating-linear-gradient(90deg, var(--line) 0 6px, transparent 6px 10px); }
.rail .mini .k { color: var(--text-soft); font-weight: 600; }
.rail .mini .v { grid-column: 2; margin: -4px 0 4px; font-size: 11px; }
.rail .toc { display: flex; flex-direction: column; }
.rail .toc a { padding: 5px 0; line-height: 1.35; color: var(--text-soft); text-decoration: none; font-size: 13.5px; }
.rail .toc a:hover { color: var(--accent); }
.rail .toc a.d3 { font-size: 12.5px; color: var(--muted); padding-left: 12px; }
.rail .use { font-size: 12.5px; color: var(--muted); margin: 0; line-height: 1.5; }
.rail .use a { text-decoration: none; }
@media (max-width: 900px) { .with-rail { grid-template-columns: 1fr; } .rail { position: static; } }
.hero { padding: 56px 0 8px; max-width: 760px; }
/* the landing hero: the answer on the left, the four conditions beneath it, the experts' dates on the right.
   Type roles follow The Belt Equation's hero: sans for the answer and claims, mono with tabular figures for
   numbers, serif only for the explanatory line. */
.land { display: grid; grid-template-columns: minmax(0, 1fr) 400px; gap: 48px; align-items: start; padding: 48px 0 24px; }
.land .eyebrow { margin-bottom: 18px; }
.land .eyebrow-verdict { margin: 30px 0 10px; }
.land .answer { font-family: var(--sans); font-size: clamp(72px, 10.5vw, 128px); line-height: 0.92; font-weight: 600; letter-spacing: -0.04em; color: var(--text); margin: 0 0 22px; }
.land h1 { font-family: var(--sans); font-size: clamp(22px, 2.5vw, 31px); line-height: 1.2; font-weight: 500; letter-spacing: -0.015em; margin: 0 0 12px; max-width: 640px; }
.land .lede { font-style: normal; font-size: 17px; line-height: 1.5; color: var(--muted); margin: 0 0 24px; max-width: 600px; }
.land .kicker { margin: 0 0 12px; }
.land .shares { font-family: var(--sans); font-size: 17px; line-height: 1.5; color: var(--text); margin: 0 0 22px; }
.land h1 .verdict { font-weight: 700; }
.conds { display: grid; gap: 14px; margin: 0 0 22px; max-width: 640px; }
.cond { display: grid; grid-template-columns: 28px 1fr; gap: 2px 14px; align-items: center; font-family: var(--sans); }
.cond .k { font-family: var(--mono); font-size: 13px; font-weight: 500; color: var(--muted); grid-row: span 3; align-self: start; padding-top: 2px; }
.cond .n { font-size: 15px; font-weight: 600; letter-spacing: -0.01em; color: var(--text); }
.cond .bar { margin: 5px 0 0; height: 7px; border-radius: 3px; }
.cond .bar span { display: none; }
.cond .bar.none { background: repeating-linear-gradient(90deg, var(--line) 0 6px, transparent 6px 10px); }
.cond .d { grid-column: 2; font-size: 13px; color: var(--muted); line-height: 1.45; margin-top: 2px; }
.fresh { font-family: var(--sans); font-size: 12.5px; color: var(--muted); margin: 0 0 18px; line-height: 1.5; }
.card { background: var(--panel); border: 1px solid var(--line); border-radius: var(--radius); padding: 22px 24px; font-family: var(--sans); }
.card .ch-big { font-family: var(--sans); font-size: 30px; font-weight: 600; letter-spacing: -0.02em; line-height: 1; color: var(--text); margin: 0 0 6px; }
.card .ch { font-size: 11px; letter-spacing: 0.12em; text-transform: uppercase; color: var(--muted); margin: 0 0 16px; }
.card .big { font-family: var(--mono); font-variant-numeric: tabular-nums; font-size: 54px; font-weight: 500; line-height: 1; letter-spacing: -0.03em; color: var(--text); margin: 0 0 8px; }
.card .what { font-size: 13.5px; color: var(--muted); line-height: 1.5; margin: 0 0 16px; }
.card .what b { color: var(--text); font-weight: 600; }
.card .ladder { border-top: 1px solid var(--line); margin: 4px 0 14px; }
.card .ladder > div { display: grid; grid-template-columns: 60px 1fr; gap: 12px; padding: 12px 0; border-bottom: 1px solid var(--line); align-items: start; }
.card .ladder > div > b { font-family: var(--mono); font-variant-numeric: tabular-nums; font-size: 24px; font-weight: 500; letter-spacing: -0.02em; color: var(--text); line-height: 1.1; }
.card .ladder span { font-size: 12.5px; color: var(--muted); line-height: 1.45; }
.card .ladder span b { color: var(--text-soft); font-weight: 600; }
.card .foot { font-size: 12.5px; color: var(--muted); line-height: 1.5; margin: 0; }
.card .foot a { text-decoration: none; }
@media (max-width: 960px) { .land { grid-template-columns: 1fr; gap: 28px; } }
.hero h1 { margin-bottom: 10px; }
.hero .lede { font-style: normal; color: var(--text-soft); font-size: 18px; line-height: 1.5; margin: 0 0 14px; }
.intro { max-width: 760px; }
.prose { max-width: 760px; }
.prose p { max-width: 70ch; }
.section { padding: 10px 0 0; }
.section > h2 { font-size: 26px; font-weight: 600; line-height: 1.25; margin: 44px 0 10px; padding-top: 18px; border-top: 1px solid var(--line); }
.section h3 { font-size: 20px; margin: 30px 0 8px; }
.status { background: var(--callout-bg); border-left: 3px solid var(--accent); border-radius: 0 8px 8px 0; padding: 15px 17px; margin: 20px 0 6px; max-width: 760px; color: var(--text-soft); }
.status strong { display: block; color: var(--text); font-size: 18px; margin-bottom: 4px; }
.status b { color: var(--text); }
figure.fig { margin: 18px 0; background: var(--figure-bg); border: 1px solid var(--line); border-radius: var(--radius); padding: 8px; }
figure.fig img { width: 100%; height: auto; display: block; border-radius: 4px; }
figure.fig figcaption { font-family: var(--sans); font-size: 13px; line-height: 1.5; color: var(--muted); padding: 10px 6px 2px; }
table.data { font-size: 13px; }
table.data th, table.data td { white-space: nowrap; }
table.data td:nth-child(2) { white-space: normal; min-width: 14ch; }
details { margin: 8px 0 18px; font-family: var(--sans); font-size: 14px; }
summary { cursor: pointer; color: var(--accent); }
details p { color: var(--text-soft); }
.legs { display: grid; grid-template-columns: repeat(auto-fit, minmax(230px, 1fr)); gap: 12px; margin: 18px 0 8px; }
.leg { background: var(--panel); border: 1px solid var(--line); border-radius: var(--radius); padding: 14px 16px; }
.leg b { display: block; color: var(--text); margin-bottom: 4px; }
.leg .g { font-family: var(--sans); font-size: 13px; line-height: 1.45; color: var(--muted); }
.leg .num { font-size: 26px; font-weight: 600; line-height: 1.1; color: var(--text); margin: 6px 0 4px; }
.bar { position: relative; height: 20px; background: var(--line); border-radius: 4px; margin: 10px 0 2px; overflow: hidden; font-family: var(--sans); }
.bar i { position: absolute; left: 0; top: 0; bottom: 0; background: var(--accent-3); }
.bar span { position: absolute; left: 8px; top: 0; line-height: 20px; font-size: 12px; font-weight: 600; color: var(--text); }
.bar.none span { color: var(--muted); font-weight: 400; }
.cite { font-family: var(--sans); font-size: 13.5px; color: var(--muted); }
.document > h1 { display: none; }
.document h2 { margin-top: 2em; }
.document img { max-width: 100%; height: auto; background: var(--figure-bg); border-radius: 4px; }
.document pre { font-family: var(--mono); font-size: 13px; background: var(--chip-bg); border: 1px solid var(--line); border-radius: 6px; padding: 10px 12px; overflow-x: auto; }
.document pre code { border: 0; background: none; padding: 0; }
.footer-meta a { color: inherit; }
/* ---- the Gazette's register (ruled 2026-10-17; the tokens and the backdrop are in site/skin.css) ----
   The mark: each gauge's line is a red tick at the bar's right edge, grey where the part cannot be scored. */
.cond .bar { overflow: visible; }
.cond .bar::after { content: ""; position: absolute; right: 0; top: -4px; bottom: -4px; width: 2px; background: var(--accent); border-radius: 1px; }
.cond .bar.none::after { background: var(--muted); }
/* The serif leads the headline, the monospace the datelines. */
.land .answer, .land h1 { font-family: var(--serif); }
.land .answer { font-weight: 700; letter-spacing: -0.02em; }
.land h1 { font-weight: 400; }
.card .ch-big { font-family: var(--serif); }
.eyebrow, .kicker, .fresh, .card .ch { font-family: var(--mono); text-transform: none; letter-spacing: 0.02em; }
/* The When? box: a boxed item between double rules, no panel fill. */
.card { border-radius: 0; border-top: 3px double var(--line-strong); border-bottom: 3px double var(--line-strong); border-left: 0; border-right: 0; background: transparent; padding: 18px 4px 14px; }
figure.fig { border-radius: 0; }
.footer-follow { margin: 4px 0 0; font-size: 12.5px; } .footer-follow a { color: var(--muted); }
.news-follow { font-family: var(--sans); font-size: 13.5px; color: var(--muted); max-width: 760px; margin-top: 22px; border-top: 1px solid var(--line); padding-top: 10px; }
/* ---- news (tracker pattern, rules 4.10 to 4.13; John 2026-10-18) ---- */
.news-list { list-style: none; padding: 0; margin: 0; max-width: 760px; }
.news-item { border-top: 1px solid var(--line); padding: 18px 0; }
.news-item time { font-family: var(--mono); font-size: 12.5px; color: var(--muted); }
.news-item .kind { font-family: var(--sans); font-size: 11px; letter-spacing: 0.08em; text-transform: uppercase; color: var(--accent); margin-left: 10px; }
.news-item h3 { margin: 4px 0 6px; font-size: 21px; line-height: 1.25; }
.news-item h3 a { text-decoration: none; color: var(--text); }
.news-item p { margin: 0; color: var(--text-soft); font-size: 15.5px; }
.news-foot { font-family: var(--sans); font-size: 13.5px; color: var(--muted); max-width: 760px; border-top: 3px double var(--line-strong); padding-top: 12px; margin-top: 8px; }
.opener { max-width: 760px; border: 1px solid var(--line-strong); border-left: 4px solid var(--accent); border-radius: var(--radius); padding: 18px 22px 14px; margin: 0 0 26px; background: var(--panel); }
.opener .k { font-family: var(--sans); font-size: 11px; letter-spacing: 0.1em; text-transform: uppercase; color: var(--accent); display: block; margin-bottom: 6px; }
.opener h3 { margin: 0 0 8px; font-size: 22px; line-height: 1.25; }
.opener h3 a { text-decoration: none; color: var(--text); }
.opener p { margin: 0; color: var(--text-soft); font-size: 15.5px; }
.opener .meta { margin-top: 8px; font-family: var(--mono); font-size: 12.5px; color: var(--muted); }
.post { max-width: 760px; }
.post h2 { font-size: 20px; margin: 30px 0 8px; }
.post p { font-size: 17px; line-height: 1.6; }
.post table { width: 100%; border-collapse: collapse; font-family: var(--sans); font-size: 14.5px; border-top: 3px double var(--line-strong); border-bottom: 3px double var(--line-strong); margin: 18px 0 22px; }
.post td, .post th { text-align: left; padding: 8px 10px 8px 0; vertical-align: top; border-bottom: 1px solid var(--line); }
.post th { font-size: 11px; letter-spacing: 0.08em; text-transform: uppercase; color: var(--muted); font-weight: 600; }
.post .stand-in { border: 1px dashed var(--line-strong); padding: 8px 12px; font-family: var(--sans); font-size: 13px; color: var(--muted); margin: 0 0 18px; }
.post-record { margin-top: 28px; border-top: 1px solid var(--line); padding-top: 12px; }
.post-record .rec { font-family: var(--sans); font-size: 14px; color: var(--text-soft); margin: 0 0 8px; }
.post-record .sources { font-family: var(--sans); font-size: 13.5px; color: var(--muted); margin: 0; }
.section.news { padding-top: 0; }
.in-the-news { border-left: 3px solid var(--accent); padding: 10px 14px; margin: 18px 0; background: var(--callout-bg); font-family: var(--sans); font-size: 14px; max-width: 760px; }
.in-the-news .k { font-size: 11px; letter-spacing: 0.08em; text-transform: uppercase; color: var(--muted); display: block; margin-bottom: 4px; }

"""


# ----------------------------------------------------------------------------- news
# The news section (tracker pattern, rules 4.10 to 4.16; ruled by John 2026-10-18, the pattern built
# first on Outrunning Ageing): one post per event of note in docs/news/YYYY-MM-DD-slug.md, rendered
# through the same shell as the documents to site/news/<slug>/, with the list at site/news/ (the
# opening post pinned at the top) and an RSS feed at site/news/feed.xml. A post's card,
# site/news/<slug>-card.png, is drawn by scripts/news_cards.py when the post is written and
# committed; scripts/check_news.py refuses a post that cannot be trusted. The records here are rows
# and amendments, not pages, so a post names the amendment it explains and the page links the changelog.
NEWS_KINDS = {"start-here": "start here", "rung-reached": "a line crossed", "estimate-revised": "a measure revised",
              "flagged-item-ruled": "a flagged item ruled", "claim": "a claim added or settled",
              "headline-moved": "the headline moved", "method-changed": "the method changed"}


def news_frontmatter(text):
    """The post's frontmatter: scalars, [a, b] lists, and lists of label/url tables."""
    if not text.startswith("---\n"):
        return {}, text
    end = text.find("\n---", 4)
    head, body = text[4:end], text[end + 4:]
    data, key = {}, None
    for raw in head.split("\n"):
        if not raw.strip():
            continue
        if raw.lstrip().startswith("- ") and key is not None:
            item = raw.lstrip()[2:].strip()
            k, v = item.split(":", 1)
            data.setdefault(key, []).append({k.strip(): v.strip().strip('"')})
            continue
        if raw.startswith("  ") and ":" in raw and key is not None and isinstance(data.get(key), list) and data[key] and isinstance(data[key][-1], dict):
            k, v = raw.strip().split(":", 1)
            data[key][-1][k.strip()] = v.strip().strip('"')
            continue
        m = re.match(r"^([A-Za-z_]+):\s*(.*)$", raw)
        if not m:
            continue
        key, val = m.group(1), m.group(2).strip()
        if val == "":
            data[key] = []
        elif val.startswith("[") and val.endswith("]"):
            data[key] = [x.strip().strip('"') for x in val[1:-1].split(",") if x.strip()]
        else:
            data[key] = val.strip('"')
    return data, body.lstrip("\n")


def render_news(built, commit):
    out_root = SITE / "news"
    out_root.mkdir(exist_ok=True)
    posts = []
    for src in sorted((DOCS / "news").glob("*.md")):
        fm, body = news_frontmatter(src.read_text(encoding="utf-8"))
        html = subprocess.run(["pandoc", "-f", "gfm", "-t", "html5"], input=body, capture_output=True, text=True, check=True).stdout  # the body only
        slug = src.stem
        posts.append({"slug": slug, "fm": fm, "html": html, "words": len(body.split())})
    posts.sort(key=lambda p: (p["fm"].get("date", ""), p["slug"]), reverse=True)
    opener = next((p for p in posts if p["fm"].get("kind") == "start-here"), None)
    dated = [p for p in posts if p["fm"].get("kind") != "start-here"]
    for p in posts:
        fm = p["fm"]
        kind = NEWS_KINDS.get(fm.get("kind"), fm.get("kind", ""))
        records = fm.get("records") or []
        record_line = ""
        if fm.get("kind") != "start-here":
            parts = [f'<a href="/docs/amendments">amendment {esc(r)}</a>' if re.match(r"^A\d+$", r) else esc(r) for r in records]
            srcs = fm.get("sources") or []
            srcs = fm.get("sources") or []
            src_html = " · ".join('<a href="%s" rel="noopener">%s</a>' % (esc(x.get("url", "")), esc(x.get("label", ""))) for x in srcs)
            record_line = ('<section class="post-record">' +
                           ('<p class="rec">The record: %s · <a href="/docs/amendments">the changelog</a>.</p>' % " · ".join(parts) if parts else "") +
                           ('<p class="sources">Sources: %s.</p>' % src_html if srcs else "") +
                           "</section>")
        card = f"/news/{p['slug']}-card.png" if (out_root / f"{p['slug']}-card.png").exists() else None
        follow = '<p class="news-follow">Follow the news: <a href="/news/feed.xml">the feed</a> · <a href="https://x.com/SentHorizons" rel="noopener">@SentHorizons on X</a>.</p>'
        body_html = f'<article class="post prose narrow">{p["html"]}{record_line}{follow}</article>'
        page = shell(f"{fm.get('title', p['slug'])} | {SITE_TITLE}", fm.get("summary", ""), body_html, built, commit,
                     canonical_path=f"/news/{p['slug']}/", eyebrow=f"News · {long_date(fm['date'])} · {kind}", h1=fm.get("title", p["slug"]),
                     lede=(None if fm.get("kind") == "start-here" else esc(fm.get("summary", ""))), active="/news/", image=card)
        (out_root / p["slug"]).mkdir(exist_ok=True)
        (out_root / p["slug"] / "index.html").write_text(page, encoding="utf-8")
    items = ""
    if opener:
        fm = opener["fm"]
        items += (f'<div class="opener"><span class="k">Start here</span><h3><a href="/news/{opener["slug"]}/">{esc(fm["title"])}</a></h3>'
                  f'<p>{esc(fm.get("summary", ""))}</p><p class="meta">{long_date(fm["date"])} · about {round(opener["words"] / 100) * 100:,} words · <a href="/news/{opener["slug"]}/">read it</a></p></div>')
    if dated:
        items += '<ul class="news-list">' + "".join(
            f'<li class="news-item"><time datetime="{p["fm"]["date"]}">{p["fm"]["date"]}</time><span class="kind">{esc(NEWS_KINDS.get(p["fm"].get("kind"), ""))}</span>'
            f'<h3><a href="/news/{p["slug"]}/">{esc(p["fm"]["title"])}</a></h3><p>{esc(p["fm"].get("summary", ""))}</p></li>' for p in dated) + "</ul>"
    else:
        items += '<p class="empty">No post yet. The first is written the day something of note moves.</p>'
    foot = ('<p class="news-foot">Every change to the method and the record, including the ones no post explains, is in <a href="/docs/amendments">the changelog</a>. '
            'The weekly readings are in <a href="https://github.com/jfredson/agi-zeitgeist/tree/main/data/readings" rel="noopener">the public record</a>. </p>' + '<p class="news-follow">Follow the news: <a href="/news/feed.xml">the feed</a> · <a href="https://x.com/SentHorizons" rel="noopener">@SentHorizons on X</a>.</p>')
    lede = ("A post is written only when a weekly reading or a ruling changes something a reader would want explained: a new measurement on one of the four parts, "
            "the headline moving, a claim added to the ledger or settled, the method changed. Each post says what happened, where the record is, what it changes on this site, and what it does not mean.")
    page = shell(f"News | {SITE_TITLE}", "What moved the test, and why: one post for each change a reader would want explained.",
                 f'<section class="section news">{items}{foot}</section>', built, commit, canonical_path="/news/", eyebrow="News", h1="What moved the test, and why", lede=lede, active="/news/")
    (out_root / "index.html").write_text(page, encoding="utf-8")
    # the feed: RSS, full text, the card as the picture
    from email.utils import format_datetime
    from datetime import datetime, timezone
    rss_items = ""
    for p in posts:
        fm = p["fm"]
        d = datetime.fromisoformat(fm["date"]).replace(hour=12, tzinfo=timezone.utc)
        card = out_root / f"{p['slug']}-card.png"
        enclosure = f'<enclosure url="{SITE_URL}/news/{p["slug"]}-card.png" length="{card.stat().st_size}" type="image/png"/>' if card.exists() else ""
        rss_items += (f"<item><title>{esc(fm['title'])}</title><link>{SITE_URL}/news/{p['slug']}/</link><guid>{SITE_URL}/news/{p['slug']}/</guid>"
                      f"<pubDate>{format_datetime(d)}</pubDate><description>{esc(fm.get('summary', ''))}</description>"
                      f"<content:encoded><![CDATA[{p['html']}]]></content:encoded>{enclosure}</item>")
    feed = (f'<?xml version="1.0" encoding="UTF-8"?><rss version="2.0" xmlns:content="http://purl.org/rss/1.0/modules/content/" xmlns:atom="http://www.w3.org/2005/Atom">'
            f'<channel><title>{SITE_TITLE} · News</title><link>{SITE_URL}/news/</link><description>What moved the test, and why: one post for each change a reader would want explained.</description>'
            f'<language>en-gb</language><atom:link href="{SITE_URL}/news/feed.xml" rel="self" type="application/rss+xml"/>{rss_items}</channel></rss>')
    (out_root / "feed.xml").write_text(feed, encoding="utf-8")
    return len(posts)


def long_date(iso):
    d = date.fromisoformat(iso)
    return f"{d.day} {d:%B %Y}"


def provenance(built, commit):
    """The plain-language provenance clause of the attribution line (design standard, section 8)."""
    n_statements = len(cs.measured(read("statements.csv")))  # tip_only rows are noted, not counted
    n_world = len(read("world_measures.csv"))
    posts = DATA / "vanguard" / "full-run-posts.csv"
    n_posts = (sum(1 for _ in posts.open(encoding="utf-8")) - 1) if posts.exists() else 0
    return (f"Last built {long_date(built)} (version {esc(commit)}) from {n_statements} expert statements, "
            f"{n_world} measurements of AI and the economy and {n_posts} community posts.")


def shell(title, description, body, built, commit, *, canonical_path="/", backdrop=False, eyebrow=None, h1=None, lede=None, active=None, image=None):
    nav1 = "".join(f'<a href="{esc(h)}" class="nav-primary{" active" if h == active else ""}">{esc(t)}</a>' for h, t in NAV_PRIMARY)
    nav2 = "".join(f'<a href="{esc(h)}" class="nav-secondary{" active" if h == active else ""}"{" rel=\"noopener\"" if h.startswith("http") else ""}>{esc(t)}</a>' for h, t in NAV_SECONDARY)
    links = "".join(f'<a href="{esc(h)}"{" rel=\"noopener\"" if h.startswith("http") else ""}>{esc(t)}</a>' for h, t in FOOTER_LINKS)
    hero = ""
    if h1:
        hero = (f'<section class="hero">{f"<p class=eyebrow>{esc(eyebrow)}</p>" if eyebrow else ""}<h1>{esc(h1)}</h1>'
                f'{f"<p class=lede>{lede}</p>" if lede else ""}</section>')
    bg = '<div class="space-bg" aria-hidden="true"></div>' if backdrop else ""
    year = built[:4]
    # The preview picture: a news post passes its own card; every other page carries the site's picture
    # (site/social-preview.png, made by scripts/social-image.mjs). One set of image tags per page.
    preview = image or "/social-preview.png"
    preview_alt = esc(title) if image else "AGI Zeitgeist Tracker: Are we in the singularity?"
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
{THEME_SCRIPT}
<meta id="theme-color-meta" name="theme-color" content="#f2f1ec">
<title>{esc(title)}</title>
<meta name="description" content="{esc(description)}">
<meta name="author" content="John Fredrickson">
<link rel="canonical" href="{SITE_URL}{esc(canonical_path)}">
<link rel="license" href="https://creativecommons.org/licenses/by/4.0/">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{SITE_TITLE}">
<meta property="og:url" content="{SITE_URL}{esc(canonical_path)}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(description)}">
<meta property="og:image" content="{SITE_URL}{esc(preview)}">
<meta property="og:image:type" content="image/png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{preview_alt}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="{SITE_URL}{esc(preview)}">
<link rel="alternate" type="application/rss+xml" title="AGI Zeitgeist Tracker · News" href="/news/feed.xml">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="icon" type="image/png" sizes="32x32" href="/favicon-32.png">
<link rel="icon" type="image/png" sizes="16x16" href="/favicon-16.png">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
<link rel="stylesheet" href="/shell.css">
<link rel="stylesheet" href="/skin.css">
<style>{SITE_CSS}</style>
</head>
<body>
{bg}
<header class="site-header"><div class="container nav">
<a class="brand" href="/">{SITE_NAME}</a>
<button type="button" class="nav-toggle" aria-label="Menu" aria-expanded="false" aria-controls="site-nav">{ICON_MENU}</button>
<nav class="navlinks" id="site-nav">{nav1}<span class="nav-divider" aria-hidden="true"></span>{nav2}<button type="button" class="theme-toggle" aria-label="Toggle light and dark theme" title="Toggle theme">{ICON_THEME}</button></nav>
</div></header>
<main class="container">
{hero}
{body}
</main>
<footer class="site-footer"><div class="container footer-grid"><div>
<span class="footer-brand">{SITE_TITLE}</span>
<p class="footer-tag">{TAGLINE}</p>
<p class="footer-links">{links}</p>
<p class="footer-meta">© {year} John Fredrickson. {provenance(built, commit)} Free to reuse with credit (<a href="https://creativecommons.org/licenses/by/4.0/" rel="license">CC BY 4.0</a>); code under the MIT licence.</p>
<p class="footer-parent"><a href="https://sentient-horizons.com/projects/" rel="noopener">A Sentient Horizons project.</a></p><p class="footer-follow"><a href="https://x.com/SentHorizons" rel="noopener">Follow on X</a></p>
</div></div></footer>
{SHELL_SCRIPT}
</body>
</html>
"""


# ----------------------------------------------------------------------------- docs and data
# One plain line saying what each document the site links to is, shown in its preface.
DOC_PURPOSE = {
    "singularity-entry-definition": "The rules that decide whether the singularity has started, and the record of how they were fixed.",
    "singularity-entry-definition-draft-2026-10-07": "The first draft of the rules for the singularity test, kept unchanged; the adopted rules are in a separate document.",
    "amendments": "Every change to how the record is kept, with its date and the reason for it.",
    "methodology-v2": "How the record is kept: who is tracked, what is collected, and how it is sorted.",
    "methodology": "The first version of how the record is kept, replaced by version 2 and kept as the record of where the project started.",
    "codebook": "The rules for sorting each statement by what it says, with examples.",
    "README": "An overview of the project and of every file in it, written for people working on it.",
    "2026-09-30-kickoff": "The plan the project started from.",
    "claims-ledger-method": "The rules of the claims ledger: which of a person's predictions get in, the five status words, what counts as a hit, how the due year is set, and how the record is kept honest.",
    "claims-ledger-proposal-2026-10-17": "The proposal the claims ledger was adopted from, with the decisions behind it and the rulings made on it.",
    "claims-ledger-seed-2026-10-17": "The list of 79 dated claims found for the proposal, each with its source and a proposed verdict; a working list, not the record.",
}


def noted_outside_record():
    """The changelog's list of tip_only statements: in the record, left out of every figure and share
    (docs/tip-intake.md, open decision 1, ruled by John 2026-10-18). Written from statements.csv at build."""
    rows = [r for r in read("statements.csv") if cs.tip_only(r)]
    names = {r["speaker_id"]: r["name"] for r in read("speakers.csv")}
    head = ('<h2 id="noted-outside-the-measured-record">Noted, outside the measured record</h2>'
            '<p>Statements that came in by tip (<a href="tip-intake.html">tip intake</a>) and that the fixed searches '
            'did not find. They are kept in <a href="../data/statements.csv">the statements table</a> and left out of '
            'every figure and share until the searches find their source.</p>')
    if not rows:
        return head + "<p>None at present.</p>"
    items = "".join(f'<li><code>{esc(r["statement_id"])}</code>, {esc(names.get(r["speaker_id"], r["speaker_id"]))}, '
                    f'{esc(r["date"])}: {esc(r["claim_summary"])} <a href="{esc(r["source_url"])}">Source</a>.</li>'
                    for r in sorted(rows, key=lambda r: (r["date"], r["statement_id"])))
    return head + f"<ul>{items}</ul>"


def render_docs(built, commit):
    """Render every Markdown document to site/docs/ with pandoc, in the shared shell, rewriting links between them."""
    out_root = SITE / "docs"
    if out_root.exists():
        shutil.rmtree(out_root)
    out_root.mkdir()
    # Session handoff notes are instructions from one working session to the next, not part of
    # the record, so they stay in the repository and off the public site (John, 2026-10-08).
    sources = sorted(p for p in DOCS.rglob("*.md") if not p.name.startswith("handoff-") and "news" not in p.relative_to(DOCS).parts) + [ROOT / "README.md"]
    n = 0
    for src in sources:
        rel = src.relative_to(ROOT) if src.name != "README.md" else Path("docs/README.md")
        rel = Path(*rel.parts[1:])  # drop the leading docs/
        dst = out_root / rel.with_suffix(".html")
        dst.parent.mkdir(parents=True, exist_ok=True)
        depth = len(rel.parts) - 1
        up = "../" * depth
        body = subprocess.check_output(["pandoc", "-f", "gfm", "-t", "html5", str(src)], text=True)
        body = re.sub(r'href="([^"#]*?)\.md(#[^"]*)?"', lambda m: f'href="{m.group(1)}.html{m.group(2) or ""}"', body)
        body = re.sub(r'href="(?:\.\./)*docs/', f'href="{up}', body)
        body = re.sub(r'href="(?:\.\./)*data/', f'href="{up}../data/', body)
        body = re.sub(r'href="(?:\.\./)*site/', f'href="{up}../', body)
        body = re.sub(r'src="(?:\.\./)*site/', f'src="{up}../', body)
        body = re.sub(r'href="(?:\.\./)*scripts/([^"]+)"', lambda m: f'href="{REPO}/blob/main/scripts/{m.group(1)}"', body)
        body = re.sub(r'href="LICENSE(-DATA)?"', lambda m: f'href="{up}../data/LICENSE{m.group(1) or ""}.txt"', body)
        title = re.search(r"<h1[^>]*>(.*?)</h1>", body, re.S)
        title = re.sub("<[^>]+>", "", title.group(1)) if title else rel.stem
        folder = {"vanguard": "Online communities pilot", "reviews": "Outside review", "amendments": "Amendment",
                  "panel-evidence-2026-10": "Panel evidence", "feasibility": "Feasibility check"}.get(rel.parts[0] if depth else "", "Document")
        note = f'<p class="cite">Rendered from <code>{esc(str(src.relative_to(ROOT)))}</code> at version {esc(commit)}.</p>'
        if rel.as_posix() == "amendments.md":
            body += noted_outside_record()
        what = DOC_PURPOSE.get(rel.with_suffix("").as_posix(), "")
        preface = ('<div class="status"><strong>A working document.</strong> ' + (what + ' ' if what else '') +
                   'It is one of the documents the site is built from, published as it is written for anyone checking the work, '
                   'and it uses the project\'s own shorthand. The plain account of the same material is on the <a href="/">home page</a>.</div>')
        page = shell(f"{title} | {SITE_TITLE}", f"{title}: a document of the {SITE_TITLE}.", f'{preface}<div class="prose narrow document">{body}{note}</div>',
                     built, commit, canonical_path=f"/docs/{rel.with_suffix('').as_posix()}", eyebrow=folder, h1=title)
        dst.write_text(page, encoding="utf-8")
        n += 1
    for src in DOCS.rglob("*.csv"):  # evidence tables the documents link to
        dst = out_root / src.relative_to(DOCS)
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)
    return n


def issue_url(template, title):
    from urllib.parse import urlencode
    return f"{REPO}/issues/new?{urlencode({'template': template, 'title': title})}"


def disagree_page(built, commit):
    """A short disagree page with a repository link (tracker pattern decision 12; lessons review
    2026-10-17, lesson 24). Three kinds of disagreement, each opening a prefilled issue."""
    kinds = [
        ("A statement is miscoded, misdated or misquoted",
         "A row in the statements table that says something its source does not, carries the wrong date, or is coded wrongly: who it endorses AGI for, the year it names, which question it raises. Give the row's id or the person and the date, what is wrong, and the source where the words are.",
         issue_url("statement-miscoded.md", "Statement: "), "Report a statement"),
        ("A measure, a line or a reading should be different",
         "One of the four parts of the singularity test rests on a measure and a line fixed in advance, and on readings of that measure. If the measure is the wrong one, the line is in the wrong place, or a reading is wrong, say what you would change it to and point at the published source that supports it; a line moves on a source and a dated reason, never on a feeling.",
         issue_url("argue-a-measure.md", "Measure: "), "Argue a measure"),
        ("An error on a page",
         "A number, a date, a name or a claim on any page that is wrong. Say which page, what it says, and what it should say, with a source where there is one.",
         issue_url("error-on-a-page.md", "Error on a page: "), "Point out an error"),
    ]
    cards = "".join(f'<h3>{esc(h)}</h3><p>{esc(t)}</p><p><a class="btn ghost" href="{esc(u)}" rel="noopener">{esc(b)}</a></p>' for h, t, u, b in kinds)
    body = f"""<section class="section prose">
<p>The point of publishing every row with its source is that you can argue with one. Three kinds of disagreement move this record: a statement that is wrongly recorded, a measure or a line in the singularity test that should be different, and an error on a page. Each is welcome, and each leaves a trace that the change can cite.</p>
<h2>The three forms</h2>
{cards}
<p>Each form opens an issue in the public repository with the right questions already in it. Issues are used because they are durable and quotable, and folding one into the record is a change that can cite it. Or write a plain issue: the page or the row, what you would change, and why is exactly enough.</p>
<h2>What happens to it</h2>
<p>John Fredrickson rules on it. Some disagreements change the record; some are answered and left as they are. Either way the issue records the ruling and the reason.</p>
<p>A corrected statement gets a dated note in its row that cites the issue; the search that found it stays in the search log. A changed measure, line or rule is a dated amendment with its reason, never a quiet edit, because the test's lines were fixed before the numbers were looked at. A new reading is a row added with its source. The expert panel is fixed, so that it cannot drift toward the story; adding or removing a person is an amendment too.</p>
<p>The repository is at <a href="{REPO}" rel="noopener">github.com/jfredson/agi-zeitgeist</a>. The data is free to reuse with credit (CC BY 4.0) and the scripts are under the MIT licence; <a href="/data/">how to cite</a> is on the data page.</p>
</section>"""
    out = SITE / "disagree"
    out.mkdir(exist_ok=True)
    (out / "index.html").write_text(shell(f"Disagree with something | {SITE_TITLE}", "How to report a wrongly recorded statement, argue a measure or a line with a source, or point out an error, and what happens to each.",
                                          body, built, commit, canonical_path="/disagree/", eyebrow="Disagree", h1="Disagree with something"), encoding="utf-8")


def copy_data():
    """Publish the CSV data beside the page so the dataset is downloadable under CC BY 4.0."""
    out = SITE / "data"
    if out.exists():
        shutil.rmtree(out)
    files = sorted(DATA.rglob("*.csv"))
    for src in files:
        dst = out / src.relative_to(DATA)
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)
    for lic in ("LICENSE-DATA", "LICENSE"):
        shutil.copy2(ROOT / lic, out / (lic + ".txt"))
    # an index page, since the asset host does not list folders: the main tables first, each said
    # in a line, then the working files from the forum trial runs and the double-checking.
    main = {"statements.csv": "every statement by the experts traced so far, with its date, its words and a link to where it was said",
            "speakers.csv": "who each person is, and why they are on the list",
            "aggregates.csv": "the surveys of researchers, the opinion polls, the betting odds and the Google search figures",
            "world_measures.csv": "how good AI actually got, what the AI companies reported about themselves, and how the world's economy grew",
            "events.csv": "dated events such as open letters and government actions",
            "search_log.csv": "every search that was run to find a statement, so that someone else can run it again",
            "claims.csv": "the claims ledger as one table: each dated prediction by a person on the list, in their words, with its test and its verdict",
            "wide_list_candidates.csv": "the wider list of well-known people the experts were chosen from, and where each name came from"}
    size = lambda f: f"{f.stat().st_size // 1024 + 1} KB"  # noqa: E731
    li = lambda f, what="": (f'<li><a href="{esc(f.relative_to(DATA).as_posix())}">{esc(f.relative_to(DATA).as_posix())}</a> ({size(f)})'  # noqa: E731
                             + (f': {esc(what)}' if what else "") + "</li>")
    first = [f for f in files if f.relative_to(DATA).as_posix() in main]
    first.sort(key=lambda f: list(main).index(f.relative_to(DATA).as_posix()))
    rest = [f for f in files if f not in first]
    body = (f'<div class="prose narrow"><p>Every table behind the site, as it stood when the site was last built. Each row carries a link to where its number came from. '
            f'Free to reuse with credit (<a href="LICENSE-DATA.txt">the licence</a>); how to cite is on the <a href="/#method">home page</a>.</p>'
            f'<h2>The main tables</h2><ul>{"".join(li(f, main[f.relative_to(DATA).as_posix()]) for f in first)}</ul>'
            f'<h2>Working files</h2><p>The rest are working files: the forum posts and how each of three AI systems sorted them in each trial run, '
            f'and the samples used to double-check the sorting of statements. They are kept so that every step can be checked; the plain account is on the <a href="/">home page</a>.</p>'
            f'<ul>{"".join(li(f) for f in rest)}</ul></div>')
    (out / "index.html").write_text(shell(f"Download the data | {SITE_TITLE}", "Every CSV table behind the AGI Zeitgeist Tracker, under CC BY 4.0.", body,
                                          pacific_today().isoformat(), git_commit(), canonical_path="/data/", eyebrow="Data", h1="Download the data"), encoding="utf-8")
    return len(files)


# ----------------------------------------------------------------------------- claims ledger
# One file per dated claim by one of the industry's figureheads, on the panel or on the ledger-only
# list (data/claims/*.toml; docs/claims-ledger-method.md; amendments A27 and A30). The page shows the claims per person with their verdicts; it scores nothing
# the home page scores and feeds nothing into the headline.
CLAIM_FIELDS = ["id", "speaker_id", "when", "when_note", "occasion", "source_kind", "source_url", "source_locator",
                "checked_how", "quote", "reported_as", "statement_id", "prediction", "kind", "bar", "due", "due_early",
                "due_date", "due_basis", "is_goal", "has_probability", "restates", "repeated_on", "status", "verdict_on",
                "verdict_why", "verdict_source", "evidence_by", "direction", "search_ids", "notes", "verify"]
# The order John ruled: Altman and Musk (2026-10-17), then the thirteen he added on 2026-10-19 (A30),
# Kai-Fu Lee last.
LEDGER_ORDER = ["altman", "musk", "amodei", "huang", "hassabis", "suleyman", "sutskever", "legg", "lecun",
                "liangwenfeng", "mensch", "zuckerberg", "pichai", "nadella", "kaifulee"]
STATUS_WORDS = {"not_yet_due": "not yet due", "hit": "came true", "missed": "did not", "withdrawn": "took it back",
                "unfalsifiable": "cannot be tested"}
STATUS_CHIP = {"hit": "chip ok", "missed": "chip no", "withdrawn": "chip no", "not_yet_due": "chip", "unfalsifiable": "chip"}
DIRECTION_WORDS = {"later": "came later than said", "not_come": "has not come", "sooner": "came sooner than said", "on_time": "came on time"}
# One plain line on who each person is, for the page, as written HTML with the companies linked at their
# first mention (the link-what-you-name rule); anyone not named here gets the first clause of their speaker row.
WHO = {"altman": 'Head of <a href="https://openai.com/">OpenAI</a> since 2019; its co-chair from 2015.',
       "musk": 'Head of <a href="https://www.tesla.com/">Tesla</a> and <a href="https://www.spacex.com/">SpaceX</a>; co-founded OpenAI in 2015 and left its board in 2018; founded <a href="https://x.ai/">xAI</a> in 2023.',
       "amodei": 'Head of <a href="https://www.anthropic.com/">Anthropic</a>, which he co-founded in 2021.',
       "huang": 'Head of <a href="https://www.nvidia.com/">Nvidia</a>, which he co-founded in 1993 and which makes the chips the AI companies train on.',
       "hassabis": 'Head of <a href="https://deepmind.google/">Google DeepMind</a>, which he co-founded as DeepMind in 2010.',
       "suleyman": 'Co-founder of DeepMind in 2010; co-founder and head of <a href="https://inflection.ai/">Inflection AI</a> from 2022; head of <a href="https://microsoft.ai/">Microsoft AI</a> since 2024. His words from 2019 to early 2022, when he held none of these roles, are not counted.',
       "sutskever": 'Co-founder and chief scientist of OpenAI from 2015 to 2024; co-founder of <a href="https://ssi.inc/">Safe Superintelligence</a> in 2024 and its head since 2025.',
       "legg": 'Co-founder and chief scientist of DeepMind from 2010, now Chief AGI Scientist of Google DeepMind. His words from before DeepMind was founded are not counted.',
       "lecun": 'Chief AI scientist of <a href="https://about.meta.com/">Meta</a> from 2018 to 2025; since then executive chairman of the start-up <a href="https://techcrunch.com/2025/12/19/yann-lecun-confirms-his-new-world-model-startup-reportedly-seeks-5b-valuation/">AMI Labs</a>. His words as head of Facebook\'s AI research lab, 2013 to 2018, are not counted.',
       "liangwenfeng": 'Founder and head of <a href="https://www.deepseek.com/">DeepSeek</a> since 2023.',
       "mensch": 'Co-founder and head of <a href="https://mistral.ai/">Mistral AI</a> since 2023.',
       "zuckerberg": 'Founder and head of Facebook, now Meta. Not on the site\'s fixed list of experts: he is on this page only (the ledger-only list).',
       "pichai": 'Head of <a href="https://about.google/">Google</a> since 2015 and of its parent <a href="https://abc.xyz/">Alphabet</a> since 2019. Not on the site\'s fixed list of experts: he is on this page only (the ledger-only list).',
       "kaifulee": 'Founder and head of <a href="https://www.01.ai/">01.AI</a> since 2023; earlier a venture investor and head of Google China. His words from before 01.AI are not counted.',
       "nadella": 'Head of <a href="https://www.microsoft.com/">Microsoft</a> since 2014 and its chair since 2021. Not on the site\'s fixed list of experts: he is on this page only (the ledger-only list).'}
# Each person's name links, at its first mention on the page (the counts table), to their Wikipedia article.
WHO_LINK = {sp: f"https://en.wikipedia.org/wiki/{slug}" for sp, slug in {
    "altman": "Sam_Altman", "musk": "Elon_Musk", "amodei": "Dario_Amodei", "huang": "Jensen_Huang",
    "hassabis": "Demis_Hassabis", "suleyman": "Mustafa_Suleyman", "sutskever": "Ilya_Sutskever", "legg": "Shane_Legg",
    "lecun": "Yann_LeCun", "liangwenfeng": "Liang_Wenfeng", "mensch": "Arthur_Mensch", "zuckerberg": "Mark_Zuckerberg",
    "pichai": "Sundar_Pichai", "nadella": "Satya_Nadella", "kaifulee": "Kai-Fu_Lee"}.items()}


def load_claims():
    folder = DATA / "claims"
    if not folder.exists():
        return []
    out = []
    for path in sorted(folder.glob("*.toml")):
        out.append(tomllib.loads(path.read_text(encoding="utf-8"))["claim"])
    out.sort(key=lambda c: (str(c["when"]), c["id"]))
    return out


def claims_csv(claims):
    """The flat table of the ledger, one row per claim, for download beside the other tables."""
    out = SITE / "data" / "claims.csv"
    out.parent.mkdir(exist_ok=True)
    with out.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(CLAIM_FIELDS)
        for c in claims:
            w.writerow(["; ".join(str(x) for x in c[k]) if isinstance(c.get(k), list) else ("" if k not in c else str(c[k]).lower() if isinstance(c[k], bool) else str(c[k])) for k in CLAIM_FIELDS])


def claims_counts(claims, search_ids, statements):
    """Per person: the counts the method asks for, the rate only where its guards allow, and the
    direction of the misses. Withdrawn counts as missed everywhere; a numeric chance is kept out
    of the plain count; no percentage before a trace or under five due claims."""
    people = {}
    for c in claims:
        p = people.setdefault(c["speaker_id"], dict(hit=0, missed=0, not_yet_due=0, unfalsifiable=0, withdrawn=0,
                                                   plain_hit=0, plain_missed=0, later=0, not_come=0, sooner=0, chance=0, goal=0, coverage=0, n=0, unf_due=0))
        p["n"] += 1
        p[c["status"]] += 1
        # A claim is due once its date has passed (31 December of the due year, or due_date); every settled
        # claim has, and a "cannot be tested" claim counts as due only from its own date, not from entry.
        end = c["due_date"] if isinstance(c.get("due_date"), date) else date(c["due"], 12, 31)
        p["unf_due"] += c["status"] == "unfalsifiable" and end < pacific_today()
        if c.get("has_probability"):
            p["chance"] += 1
        elif c["status"] == "hit":
            p["plain_hit"] += 1
        elif c["status"] in ("missed", "withdrawn"):
            p["plain_missed"] += 1
        if c["status"] in ("missed", "withdrawn") and c.get("direction") in ("later", "not_come"):
            p[c["direction"]] += 1
        if c["status"] == "hit" and c.get("direction") == "sooner":
            p["sooner"] += 1
        p["goal"] += bool(c.get("is_goal"))
        p["coverage"] += c["source_kind"] == "coverage_only"
    for sp, p in people.items():
        p["due"] = p["hit"] + p["missed"] + p["withdrawn"] + p["unf_due"]
        p["plain_due"] = p["plain_hit"] + p["plain_missed"]
        p["traced"] = f"{sp}-claims-traced" in search_ids
        p["rate"] = None
        if p["traced"] and p["plain_due"] >= 5:
            p["rate"] = p["plain_hit"] / p["plain_due"]
        p["rate_label"] = (f"{round(p['rate'] * 100)}% ({p['plain_hit']} of {p['plain_due']} due)" if p["rate"] is not None
                           else "too few to rate" if p["traced"] else "seed only: not a rate")
        # The coded statements that look ahead, and how many carry a year (the undated-claim rule).
        ahead = [r for r in statements if r["speaker_id"] == sp and ({"timeline", "possibility"} & set(x.strip() for x in r["frames_present"].split(";")))]
        p["statements_ahead"] = len(ahead)
        p["statements_dated"] = sum(1 for r in ahead if r["timeline_year"])
    return people


def claims_page(sc, claims, built, commit):
    speakers = {r["speaker_id"]: r for r in read("speakers.csv")}
    statements = read("statements.csv")
    search_ids = {r["search_id"] for r in read("search_log.csv")}
    people = claims_counts(claims, search_ids, statements)
    order = [sp for sp in LEDGER_ORDER if sp in people] + sorted((sp for sp in people if sp not in LEDGER_ORDER),
                                                                  key=lambda sp: (not speakers[sp]["frontier_lab"], speakers[sp]["name"]))
    # The four gauges' shares, drawn from the same figures as the home page: display only, linked to no claim (rule 6.4).
    share_names = {"A": "Pace", "B": "Forecasts", "C": "AI doing the research", "D": "Economy"}
    strip = "".join(f'<span class="chip">{esc(share_names[k])} {f"{round(sc[k]['gauge'] * 100)}% of the way" if sc[k].get("measurable") else "unmeasured"}</span>' for k in "ABCD")

    rows = []
    for sp in order:
        p = people[sp]
        misses = []
        if p["later"]:
            misses.append(f"{p['later']} came later than said")
        if p["not_come"]:
            misses.append(f"{p['not_come']} {'has' if p['not_come'] == 1 else 'have'} not come")
        name = esc(speakers[sp]["name"])
        rows.append([f'<a href="{WHO_LINK[sp]}">{name}</a>' if sp in WHO_LINK else name, p["n"], p["due"], p["hit"], p["missed"] + p["withdrawn"], p["not_yet_due"], p["unfalsifiable"],
                     esc(p["rate_label"]), esc("; ".join(misses) or ""),
                     "none recorded: not on the list of experts" if speakers[sp]["tier"] == "claims_only"
                     else f'{p["statements_ahead"]} ({p["statements_dated"]} with a year)'])
    counts_table = table(["who", "claims", "due", "came true", "did not", "not yet due", "cannot be tested", "rate", "which way the misses went", "coded statements that look ahead"], rows)

    n_all = len(claims)
    n_due = sum(p["due"] for p in people.values())
    n_hit = sum(p["hit"] for p in people.values())
    n_missed = sum(p["missed"] + p["withdrawn"] for p in people.values())
    n_unf = sum(p["unfalsifiable"] for p in people.values())
    n_unf_due = sum(p["unf_due"] for p in people.values())

    sections = []
    for sp in order:
        p = people[sp]
        items = []
        for c in [c for c in claims if c["speaker_id"] == sp]:
            when = str(c["when"])
            chip = f'<span class="{STATUS_CHIP[c["status"]]}">{esc(STATUS_WORDS[c["status"]])}</span>'
            marks = []
            if c.get("is_goal"):
                marks.append('<span class="chip">a stated goal</span>')
            if c.get("has_probability"):
                marks.append('<span class="chip">a stated chance, not counted</span>')
            if c["source_kind"] == "coverage_only":
                marks.append('<span class="chip">reported, not their own words</span>')
            if c.get("evidence_by") == "maker":
                marks.append('<span class="chip accent">on the company\'s own word</span>')
            if c.get("restates"):
                marks.append(f'<a class="chip" href="#{esc(c["restates"])}">restates an earlier claim</a>')
            words = (f'&ldquo;{esc(c["quote"])}&rdquo;' if c.get("quote") else f'<span class="dim">{esc(c["reported_as"])}</span>')
            due = f'due {c["due"]}' + (f' (by {c["due_date"].strftime("%-d %B %Y")})' if c.get("due_date") else "") + (f', or {c["due_early"]} at the early end' if c.get("due_early") else "")
            verdict = ""
            if c["status"] in ("hit", "missed", "withdrawn"):
                verdict = (f'<br><span class="dim"><b>{esc(STATUS_WORDS[c["status"]].capitalize())}</b> ({c["verdict_on"].strftime("%-d %B %Y")}'
                           f'{", " + esc(DIRECTION_WORDS[c["direction"]]) if c.get("direction") else ""}): {esc(c["verdict_why"])} '
                           f'(<a href="{esc(c["verdict_source"])}">where this is shown</a>)</span>')
            elif c["status"] == "unfalsifiable":
                verdict = f'<br><span class="dim"><b>Cannot be tested:</b> {esc(c["verdict_why"])}</span>'
            items.append(f'<li id="{esc(c["id"])}"><span class="mono">{esc(when)}</span> {chip} {" ".join(marks)}<br>'
                         f'{words} (<a href="{esc(c["source_url"])}">the source</a>; {esc(c["occasion"])}) &middot; {esc(due)}<br>'
                         f'<span class="dim"><b>What it commits to:</b> {esc(c["prediction"])} <b>The test:</b> {esc(c["bar"])}</span>{verdict}</li>')
        who = speakers[sp]
        sections.append(f'<h2 id="{esc(sp)}">{esc(who["name"])}</h2>'
                        f'<p class="dim">{WHO.get(sp) or esc(who["role_summary"].split(";")[0] + ".")} {p["n"]} dated claims: {p["hit"]} came true, {p["missed"] + p["withdrawn"]} did not'
                        f'{f" (of which {p['withdrawn']} taken back)" if p["withdrawn"] else ""}, {p["not_yet_due"]} not yet due, {p["unfalsifiable"]} cannot be tested. {esc(p["rate_label"].capitalize())}.</p>'
                        f'<ul>{"".join(items)}</ul>')

    body = f"""<section class="section prose">
<p class="kicker">Where the world is, on the same day</p>
<div class="chips">{strip}</div>
<p class="dim">The four parts of the singularity test on the <a href="/">home page</a>, each as its share of the way to its line. They are shown here so that what these people said can be read against what has actually happened; nothing on this page changes them.</p>

<h2>What this page is</h2>
<p>The people who run the AI companies both sell the story and see further than anyone else. This page keeps a plain account of their predictions: each one that carried a date, in the person's own words, with where it was said, the test it will be judged by, and, once the date has passed, whether it came true. It answers one narrow question, how often each person's dated predictions have come true so far, and which way the misses went. It does not say whether anyone is right about the future, whether they are sincere, or whether the technology is good or bad. A person with a poor record may be right next time; one with a good record may have been lucky.</p>
<p>The people on this page are the industry's figureheads: the head, founder-leader or chair of a company that builds the most advanced AI models or the chips they are trained on, or that company's named chief scientist. A prediction counts only if it was made while the person held that role. Twelve of them are on the site's fixed list of experts; three, Mark Zuckerberg, Sundar Pichai and Satya Nadella, are not, and they appear on this page only, never in the record of what experts expect.</p>
<p>A prediction gets in only if the person is one of these figureheads at the time, the words look forward, the words carry a date or a length of time, and there is a record of them being said. Whether it came true is never looked at when deciding what gets in. A prediction with no date ("AGI is coming", "we are close") is not scored; the table says how many of each person's recorded statements look ahead and how many of those carry a year, so vagueness stays visible. The full rules are in <a href="/docs/claims-ledger-method">the method</a>.</p>
<p>So far: {n_all} dated predictions by {len(people)} people. {n_due} are due, their dates passed: {n_hit} came true, {n_missed} did not and {n_unf_due} cannot be tested. Of those still ahead, {n_unf - n_unf_due} cannot be tested either, so will never be scored. The people here were traced for their best-known, checkable predictions first, so these counts measure which predictions were easy to find; no one gets a percentage until they have been traced year by year with every search written down, and never from fewer than five due predictions.</p>
{counts_table}
<p class="dim">"Did not" includes predictions the person later took back. "Cannot be tested" means the words carry a date but no test anyone outside could run, or the only judge is the speaker; such predictions are shown and counted apart, never scored. A stated chance ("a 50% chance") is kept and marked but left out of the rate.</p>
{"".join(sections)}
<h2>How to read a verdict</h2>
<p>A prediction counts as having come true only if every condition in its test was met by its date, shown by a dated public record: the maker's own release, an official result, a regulator's notice. Where the only evidence is the company's own word, the entry says so. A prediction that was only partly met, or met late, did not come true, and the entry says which part failed and whether the thing came later or has not come. The test is written when the prediction is entered and never changed afterwards. Every search that found a prediction or settled a verdict is in <a href="/data/search_log.csv">the search log</a>, and the whole ledger can be downloaded as <a href="/data/claims.csv">a table</a>. To argue with a verdict, use <a href="/disagree/">the disagree page</a>.</p>
</section>"""
    out = SITE / "claims"
    out.mkdir(exist_ok=True)
    (out / "index.html").write_text(shell(f"Claims | {SITE_TITLE}", "The dated predictions of the people who run the AI companies, in their own words, scored against what happened.",
                                          body, built, commit, canonical_path="/claims/", eyebrow="Claims", active="/claims/",
                                          h1="What the people who run the AI companies predicted, and what happened",
                                          lede="Every prediction that carried a date, in their own words, with its source and its verdict."), encoding="utf-8")
    claims_csv(claims)
    return dict(people={sp: {k: people[sp][k] for k in ("n", "due", "hit", "missed", "withdrawn", "not_yet_due", "unfalsifiable", "later", "not_come", "traced", "rate")} for sp in order},
                claims=n_all, due=n_due, hit=n_hit, missed=n_missed, unfalsifiable=n_unf, page=f"{SITE_URL}/claims/", table=f"{SITE_URL}/data/claims.csv")


# ----------------------------------------------------------------------------- html
def esc(s):
    return html.escape(str(s), quote=True)


def table(headers, rows):
    out = ['<table class="data"><thead><tr>' + "".join(f"<th>{esc(h)}</th>" for h in headers) + "</tr></thead><tbody>"]
    for r in rows:
        out.append("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>")
    out.append("</tbody></table>")
    return "\n".join(out)


def link(url, row_id):
    """A source link in a table: the word "source", with the data row's id kept in the hover text."""
    return f'<a href="{esc(url)}" title="row {esc(row_id)}">source</a>'


def gauge_bar(g):
    if g is None:
        return '<div class="bar none"><span>not yet measurable</span></div>'
    return f'<div class="bar"><i style="width:{g*100:.0f}%"></i><span>{g*100:.0f}% of the way to its line</span></div>'


MARKET_PAGES = {"hh2bXhwKDTioZ7KtGKfC": "https://manifold.markets/RemNi/will-we-get-agi-before-2030"}


def market_page(api_url):
    """The reader-facing page for a betting market whose number was read from its API."""
    for cid, page in MARKET_PAGES.items():
        if cid in api_url:
            return page
    return api_url


def expert_dates():
    """Each traced expert's latest dated statement giving a year for AGI (a machine matching people at
    thinking work: target broad_competence), where the statement accepts, hedges or conditions it.
    Returns (median year, low, high, [(name, year, date, url)])."""
    speakers = {r["speaker_id"]: r["name"] for r in read("speakers.csv")}
    panel = cs.panel(read("speakers.csv"))  # the experts' dates come from the panel only, never the ledger-only list (A30)
    latest = {}
    for r in cs.measured(read("statements.csv")):  # tip_only rows stay out of every figure
        if r["speaker_id"] not in panel:
            continue
        if r["target_capability"] != "broad_competence" or not r.get("timeline_year"):
            continue
        if r["endorsement"] not in ("accepts", "uncertain", "conditional"):
            continue
        if r["speaker_id"] not in latest or r["date"] > latest[r["speaker_id"]]["date"]:
            latest[r["speaker_id"]] = r
    rows = sorted(((speakers.get(k, k), int(v["timeline_year"]), v["date"], v["source_url"]) for k, v in latest.items()), key=lambda x: x[1])
    years = [y for _, y, _, _ in rows]
    med = (years[len(years) // 2] if len(years) % 2 else round((years[len(years) // 2 - 1] + years[len(years) // 2]) / 2))
    return med, years[0], years[-1], rows


def landing(sc, b_pts, mani, aggregates, built, commit, ytl):
    """The first screen: the answer, the four conditions, the experts' date."""
    A, C, D = sc["A"], sc["C"], sc["D"]
    answer = {"not entered": "Not yet.", "approaching": "Getting close.",
              "mark crossed, under persistence test": "Crossing now.", "entered": "Yes."}[sc["status"]]
    conds = [
        ("A", "AI is getting better faster and faster", A.get("gauge"),
         f"How long a job the best AI can do by itself has been doubling every {A['reading']:.0f} days. It would count at {A['t_star']:.0f} days and still speeding up."),
        ("B", "Nobody can predict AI progress any more", None,
         "Cannot be scored yet: that needs a record of old predictions set against what actually happened, and it has not been built."),
        ("C", "AI now does most of the work of improving AI", C.get("gauge"),
         f"Anthropic, an AI company, says its own AI leads {C['reading']*100:.0f}% of its AI research. It would count at half. Only the company can check that."),
        ("D", "The world's economy grows ten times faster than it ever has", D.get("gauge"),
         f"The world's economy grew {D['reading']:.1f}% in {D['year']}. It would count at {D['g_star']:.0f}% in a year."),
    ]
    rows = "".join(f'<div class="cond"><span class="k">{k}</span><span class="n">{esc(n)}</span>{gauge_bar(g)}<span class="d">{esc(d)}</span></div>' for k, n, g, d in conds)
    share_names = {"A": "Pace", "B": "Forecasts", "C": "AI doing the research", "D": "Economy"}
    share_rows = [(share_names[k], f"{round(sc[k]['gauge'] * 100)}%" if sc[k].get("measurable") else "unmeasured") for k in "ABCD"]
    latest = b_pts[-1]
    med, lo, hi, ex_rows = expert_dates()
    hlmi10 = next((int(float(r["value"])) for r in aggregates if r["aggregate_id"] == f"aiimpacts-{latest['date'].year}-hlmi10"), "")
    faol = next((int(float(r["value"])) for r in aggregates if r["aggregate_id"] == f"aiimpacts-{latest['date'].year}-faol50"), "")
    m = mani[-1] if mani else None
    market = (f' People betting on Manifold put the odds of AGI before 2030 at <a href="{esc(market_page(m["source_url"]))}">{float(m["value"])*100:.0f}%</a>.' if m else "")
    return f"""<section class="land">
<div>
<p class="eyebrow">{esc(HEADLINE_QUESTION)}</p>
<p class="answer">{esc(sc["headline"])}</p>
<p class="kicker">{esc(sc["headline_label"])}</p>
<p class="shares">{" · ".join(f"{esc(n)} {v}" for n, v in share_rows)}</p>
<p class="shares">{esc(ytl["_sentence"])}</p>
<p class="eyebrow eyebrow-verdict">Are we in the singularity?</p>
<h1><span class="verdict">{answer}</span> Four things would all have to be true, and stay true for a year. Today none of them is.</h1>
<p class="lede">The singularity is the idea that machines will one day get smarter so fast that the world changes faster than anyone can keep up with. The step before it is artificial general intelligence, or AGI: a machine that can do most of the thinking work a person can. This site checks whether the singularity has started, and records when people expect AGI.</p>
<p class="kicker">The four pillars of the singularity</p>
<div class="conds">{rows}</div>
<p class="fresh">Each bar shows how far that measure has come since {sc['reference_year']} toward the line where it would count.</p>
<p class="fresh">Scored {long_date(built)} from public numbers. <a href="/docs/amendments">Track the changes here.</a></p>
</div>
<aside class="card">
<p class="ch-big">When?</p>
<p class="ch">It depends what you mean by AGI</p>
<p class="big">about {med}</p>
<p class="what"><b>Machines match people at thinking and digital work.</b> The middle of the latest dates from the {len(ex_rows)} experts traced so far ({lo} to {hi}).{market}</p>
<div class="ladder">
<div><b>{int(latest['m'])}</b><span><b>Every task, better and cheaper than a human worker.</b> Even odds, from {latest['n'] or 'AI researchers'} in the <a href="{esc(latest['url'])}">largest survey</a> ({latest['date'].year}); one-in-ten odds by {hlmi10}. {int(b_pts[0]['m']) - int(latest['m'])} years closer than the {b_pts[0]['date'].year} survey said.</span></div>
<div><b>{faol}</b><span><b>All human work could be automated.</b> Even odds, same survey. Factories and hospitals move far more slowly than software.</span></div>
</div>
<p class="foot"><a href="#belief">The full record is below.</a></p>
</aside>
</section>"""


def rail(sc, built, commit):
    names = {"A": "Pace", "B": "Forecasts", "C": "AI doing research", "D": "Economy"}
    rows = []
    for k in "ABCD":
        g = sc[k].get("gauge") if sc[k].get("measurable") else None
        bar = gauge_bar(g)
        val = "not yet measurable" if g is None else f"{g:.2f} of 1"
        rows.append(f'<span class="k">{k}</span>{bar}<span class="v">{esc(names[k])}: {val}</span>')
    progress = ("at most " if sc["progress_is_upper_bound"] else "") + f"{sc['progress']:.2f}"
    toc = [("#belief", "The current zeitgeist", ""), ("#singularity", "Are we in the singularity?", ""),
           ("#leg-a", "A. The pace", "d3"), ("#leg-b", "B. Forecasts", "d3"), ("#leg-c", "C. AI doing research", "d3"), ("#leg-d", "D. The economy", "d3"),
           ("#owed", "Not finished yet", "d3"), ("#method", "Method and data", "")]
    toc_html = "".join(f'<a href="{h}" class="{c}">{esc(t)}</a>' for h, t, c in toc)
    return f"""<aside class="rail">
<h4>On this page</h4>
<nav class="toc">{toc_html}</nav>
<h4 class="rail-sec">Use the data</h4>
<p class="use"><a href="/data/">Download every table</a> (free to reuse with credit) · <a href="#method">How to cite</a> · <a href="/data/">What each file holds</a> · version {esc(commit)}</p>
</aside>"""


def build_html(a_pts, a_series, b_pts, b_steps, mani, c_pts, d_pts, sc, built, commit):
    frontier = [p for p in a_pts if p["frontier"]]
    latest = frontier[-1]
    last_step = b_steps[-1]
    A, B, C, D = sc["A"], sc["B"], sc["C"], sc["D"]
    lead = C["row"]

    a_rows = [[p["date"].isoformat(), esc(p["name"]),
               f"{p['value']/60:.1f} h" if p["value"] >= 60 else f"{p['value']:.1f} min",
               f"{p['lo']/60:.1f} to {p['hi']/60:.1f} h" if p["hi"] >= 60 else f"{p['lo']:.1f} to {p['hi']:.1f} min",
               "yes" if p["frontier"] else "", "past 16 h" if p["over16"] else "",
               link(p["url"], p["id"])] for p in a_pts]
    dt_rows = [[s["date"].isoformat(), f"{s['days']:.0f}", s["n"], "yes" if s["over16"] else ""] for s in a_series]
    b_rows = [[p["date"].isoformat(), int(p["m"]), f"{p['remaining']:.1f}", link(p["url"], p["id"])] for p in b_pts]
    step_rows = [[f"{s['frm']['date'].year} to {s['to']['date'].isoformat()}", f"{s['years']:.1f}", f"{s['change']:+.1f}", f"{s['pull_in']:+.1f}"] for s in b_steps]
    mani_rows = [[r["date"], f"{float(r['value'])*100:.0f}%", link(market_page(r["source_url"]), r["aggregate_id"])] for r in mani]
    c_rows = [[p["date"].isoformat(), esc(p["measure"]), f"{int(p['value'])}%" + (f" ({p['bound']})" if p["bound"] else ""), link(p["url"], p["id"])] for p in c_pts]
    d_rows = [[q["year"], f"{q['growth']:.2f}%", f"{q['doubling']:.1f}" if q["doubling"] else "none (output fell)", link(q["url"], q["id"])] for q in reversed(d_pts)]

    progress_word = "at most " if sc["progress_is_upper_bound"] else ""
    status_line = {
        "not entered": "Not entered.",
        "approaching": "Approaching: every gauge is above one half.",
        "mark crossed, under persistence test": "Mark crossed; the four-quarter persistence count is running.",
    }[sc["status"]]

    ytl = years_to_line(a_series, c_pts, d_pts, sc)
    _panel = cs.panel(read("speakers.csv"))  # the ledger-only list (A30) is never counted as the panel
    _stmts = [r for r in read("statements.csv") if r["speaker_id"] in _panel]
    n_panel, n_statements = len({r["speaker_id"] for r in _stmts}), len(_stmts)
    cl = _CLAIMS
    claims_line = (f'Of the {cl["claims"]} predictions with a date recorded so far from {len(cl["people"])} of the people who run the AI companies, {cl["due"]} are now due, and {cl["hit"]} came true. '
                   f'Each is on <a href="/claims/">the claims page</a> in their own words, with its source and its verdict.') if cl["claims"] else ""
    body = f"""{landing(sc, b_pts, mani, _AGG, built, commit, ytl)}
<div class="with-rail"><div>
<section class="section prose" id="belief">
<h2>The current zeitgeist</h2>
<p>"Zeitgeist" is a German word for the mood of a time: what people are saying and what they expect. This part of the site records what well-known experts, surveys of researchers, opinion polls, betting markets and online forums have said since 2005 about AGI. Every quote carries its date and a link to where it was said.</p>
<p>Has the argument moved: from <em>whether</em> such a machine can be built, to <em>when</em> it will arrive, to <em>whether today's machines are nearly there</em>? Four things stand out so far.</p>
<p>First, the doubters have moved. Geoffrey Hinton, a computer scientist whose work underlies today's AI, said "no sooner than 2070" in 2015 and "between five and 20 years" in 2025. Gary Marcus, a psychologist and the best-known critic of today's AI, said "at least thirty or fifty years" in 2016 and "10-25 years" in 2025. Ray Kurzweil has said 2029 the whole time. This is where the "about 2030" at the top of the page comes from.</p>

<figure class="fig"><a href="zeitgeist-experts.png" title="Open the chart full size"><img src="zeitgeist-experts.png" alt="Each of five experts' earliest and latest guess at when machines will match people at most thinking work"></a>
<figcaption>Only guesses in the person's own words are shown, not a reporter's summary of them. Every guess, with its quote and a link to where it was said, is in <a href="/data/statements.csv">a table</a>.</figcaption></figure>

<p>Fifth, and this is a reading of the same rows rather than a new measure: the people building these systems have named about the same year all along, and the people studying them have come down to meet it. The chart below takes every dated guess by a panel member for machines matching people at most thinking work and draws apart the people tagged as having worked at a company that builds frontier systems from the rest: the academics, the critics and the philosophers. A builder has a front-row seat and a product to sell; a critic has neither. The chart shows whether the two groups differ and whether the gap moves; it does not say which group is right.</p>

<figure class="fig"><a href="zeitgeist-frontier.png" title="Open the chart full size"><img src="zeitgeist-frontier.png" alt="Every dated guess by a panel member for when machines will match people at most thinking work, from 2005 to 2026, with the people who build frontier AI systems drawn apart from the people who study them, and each group's median by year"></a>
<figcaption>One dot per dated guess; the lines join each group's median for years with two or more guesses. Who counts as a builder is the frontier-lab tag in <a href="/data/speakers.csv">the speakers table</a>, with the dates that justify it. The numbers are in <a href="/data/statements.csv">a table</a>.</figcaption></figure>

<p>Second, AI researchers have moved too, more slowly, and how far depends on the question. In the largest repeated survey of researchers, the year they give an even chance that machines could do every task better and more cheaply than people came 14 years closer between 2016 and 2023, to 2047. Asked when machines could do every job that way, they say 2116.</p>

<figure class="fig"><a href="zeitgeist-researchers.png" title="Open the chart full size"><img src="zeitgeist-researchers.png" alt="AI researchers' even-chance year for machines doing every task and every job, in surveys from 2016, 2022 and 2023"></a>
<figcaption>Two different groups of researchers answered the two questions in each survey. The numbers are in <a href="/data/aggregates.csv">a table</a>.</figcaption></figure>

<p>Third, ordinary people have started paying attention. Google searches for artificial general intelligence were flat for fifteen years and have climbed steeply since 2023, and in polls since 2023 about half of American adults say they are more concerned than excited about the growing use of AI in daily life.</p>

<figure class="fig"><a href="zeitgeist-search.png" title="Open the chart full size"><img src="zeitgeist-search.png" alt="Worldwide Google searches for artificial general intelligence and for the singularity, each year from 2005 to 2026"></a>
<figcaption>Google reports searches on its own scale rather than as counts. The numbers, and the polls, are in <a href="/data/aggregates.csv">a table</a>.</figcaption></figure>

<p>Fourth, almost no one says the machine has arrived, not even on r/singularity, a forum on the website Reddit for people who expect it.</p>

<figure class="fig"><a href="zeitgeist-forum.png" title="Open the chart full size"><img src="zeitgeist-forum.png" alt="The most popular posts on the r/singularity forum every three months from late 2024 to 2026, by what each mainly says"></a>
<figcaption>One forum, not the public. The numbers are in <a href="vanguard-pilot-r-singularity.csv">a table</a>.</figcaption></figure>

<p>This rests on the {n_panel} people on the expert panel, each traced year by year from their first public statement on AGI ({n_statements} statements in all, every search written down), {len(b_pts)} waves of the largest survey of AI researchers, opinion polls, betting markets and one online forum. A weekly reading adds what is new.</p>
<p>{claims_line}</p>
<p>Expecting it soon is not the same as it happening. Whether the singularity has actually begun is the test below.</p>
</section>

<section class="section prose" id="singularity">
<h2>Are we in the singularity?</h2>
<p>The number at the top of the page is the average, across the parts that can be measured, of how far each is from its starting point toward its line, and the words beneath it give each part's share and when each would cross on its current trend; the test's own single progress number is stricter, the weakest part's share, today {"at most " if sc["progress_is_upper_bound"] else ""}{round(sc["progress"] * 100)}% (the {({"A": "pace", "B": "forecasts", "C": "AI-research share", "D": "economy"})[sc["bottleneck"]]}). The answer itself comes from a test with four parts. The singularity has been described in three classic ways: machines getting better faster and faster, machines doing the work of making machines better, and change so fast that nobody can predict what comes next. Each alone gives false alarms. A fast decade in any industry looks like the first; a company's claim that its AI does its own research cannot be checked from outside; and every new technology makes old forecasts look foolish, the internet included. So the test asks for all three at once, plus a fourth that people outside the AI world measure: whether the world's economy has changed gear. Each part has a line where it would count, fixed before anyone looked at the numbers. The full rules are in <a href="/docs/singularity-entry-definition">a working document</a>.</p>

<h3 id="leg-a">A. Is AI getting better faster and faster?</h3>
<p><em>The idea, from the inventor Ray Kurzweil: AI gets better faster and faster, so the time it takes to double is itself shrinking.</em></p>
<p>The measure is how long a job the best AI can finish on its own. METR, a research group that tests AI systems, gives each new system computer-programming jobs of known length, from seconds to days of a skilled person's time, and finds the longest it gets right half the time. Most tests of AI are maxed out within a year or two; this one keeps rising, which is why it was chosen. That length has been doubling every few months. Steady doubling is fast, but it is not a singularity: for this part to count, the doubling itself has to keep getting quicker, down to {A['t_star']:.0f} days. Over the year to {A['date'].strftime('%B %Y')} it took {A['reading']:.0f} days; in {sc['reference_year']} it took {A['t_ref']:.0f}. The rules also ask for it to have got quicker two readings in a row, which today it {"has" if A['falling'] else "has not"}. {esc(ytl.get("A", ""))} Since September 2026 METR has stopped updating this series, and its tests cannot measure past 16 hours, which the best system has already passed; the rules say a replacement measure must be named with an overlap before the series stops, and that question is open (<a href="/docs/amendments">amendment A24</a>).</p>
<figure class="fig"><a href="leg-a-time-horizon.png" title="Open the chart full size"><img src="leg-a-time-horizon.png" alt="The longest programming job each AI system gets right half the time, from 2019 to 2026, and how many days that length took to double"></a>
<figcaption>Filled dots were the best system on the day they came out; hollow dots were not. METR says its tests cannot measure reliably beyond 16 hours, so a year that includes such a reading is drawn hollow in the lower chart and not scored. The latest best system is {esc(latest['name'])}, at {latest['value']/60:.0f} hours, {latest['date'].strftime('%B %Y')}. The numbers are in <a href="leg-a-doubling-time.csv">a table</a>.</figcaption></figure>
<details><summary>Every system measured ({len(a_pts)}) and every twelve-month window</summary>
{table(["came out", "system", "longest job it gets right half the time", "likely range", "best at the time", "", "source"], a_rows)}
{table(["window ends", "days to double", "systems in the window", "includes a reading past 16 hours"], dt_rows)}
</details>

<h3 id="leg-b">B. Has AI become impossible to predict?</h3>
<p><em>The idea, from the writer Vernor Vinge: past some point nobody can predict what comes next, and it can only be confirmed after the fact. A post on an online forum put it this way: "Any prediction made now about the next five years will look stupid in retrospect."</em></p>
<p>This part cannot be scored yet. Scoring it needs old predictions of the measure in part A set against what then happened, to see how far ahead forecasts still beat the simplest guess, that the trend carries on. Nobody has collected that record, and it can only be scored once the predicted dates have passed. The nearest evidence is the surveys of AI researchers in the section above. If their forecasts had been right, the year they expect would have stood still while time passed. Instead it jumped closer: between {last_step['frm']['date'].year} and {last_step['to']['date'].year}, about {abs(last_step['change']):.0f} years of expected waiting disappeared in {last_step['years']:.1f} years. Forecasts that keep being wrong in the same direction, too slow, are what this part looks for, but surveys about a distant year are only a hint, not the score.</p>
<details><summary>The surveys, the steps between them, and the betting odds for comparison</summary>
{table(["survey", "even-odds year", "years away at the time", "source"], b_rows)}
{table(["step", "years of real time", "change in years away", "years closer per year, beyond the passage of time"], step_rows)}
<p>Betting odds on Manifold for "AGI created and publicly announced before 2030", for comparison only (a price people bet at, not a survey):</p>
{table(["date", "odds", "source"], mani_rows)}
</details>

<h3 id="leg-c">C. Is AI doing the work of improving AI?</h3>
<p><em>The idea, from the mathematician I. J. Good: once machines do the work of making machines better, progress feeds on itself.</em></p>
<p>Nobody outside the AI companies can measure how much of the work of improving AI is now done by AI, so what exists is what the companies say about themselves. Anthropic, which makes the Claude AI systems, reports what share of its AI research work its own AI leads, as judged by that AI. That is the figure scored, and it would count at half. Google says about three-quarters of its new computer code is written by AI, but that covers all its code, not its research, so it is not scored. Anthropic also says its AI takes part in more than 90% of its research work, a lower bar than leading it. {esc(ytl.get("C", ""))}</p>
<figure class="fig"><a href="leg-c-self-reports.png" title="Open the chart full size"><img src="leg-c-self-reports.png" alt="The share of Anthropic's AI research work led by its own AI: under 1% in February 2026 and 26% in August 2026, against a line at one half"></a>
<figcaption>Anthropic gave its February figure as "under 1%". Every statement, including Google's, is in the table below.</figcaption></figure>
<details><summary>What the companies said</summary>
{table(["date", "what was measured", "figure", "source"], c_rows)}
</details>

<h3 id="leg-d">D. Has the economy changed gear?</h3>
<p><em>The idea, from the economist Robin Hanson: each new era of history has made the world's economy double about a hundred times faster than the one before.</em></p>
<p>The economist Robin Hanson looked at the whole history of the world's economy and found three eras: hunting, farming and industry. In each, the amount the world produces doubled about a hundred times faster than in the era before: every 230,000 years, then every 860 years, then every 15 years. A fourth era would double it in a few years or less. This part asks whether that has started, using the World Bank's yearly count of everything the world produces. In {D['year']} it grew {D['reading']:.1f} percent, a pace that doubles it every {D['doubling']:.0f} years; since 1961 it has averaged {D['g_ref']:.1f} percent. The line, 30 percent in a year, would double it every {D['t_star']:.1f} years. It comes from a 2021 report by Tom Davidson for the research funder Open Philanthropy, not from this project, and it is far above the best year since 1961, {max(q['growth'] for q in d_pts):.1f} percent. This is the one part measured by people outside the AI world, which is why it is in the test; the cost is that the economy reacts years after the technology, so it will usually be the furthest behind. {esc(ytl.get("D", ""))}</p>
<figure class="fig"><a href="leg-d-world-growth.png" title="Open the chart full size"><img src="leg-d-world-growth.png" alt="Growth of the world's economy each year since 1961, between about minus 3 and 7 percent, with the line at 30 percent far above"></a>
<figcaption>One bar per year. Countries revise their figures for years afterwards; if a revision pulls a year back below the line, the clock on this part starts again. How many years each rate takes to double the economy is in <a href="leg-d-world-growth.csv">a table</a>.</figcaption></figure>
<details><summary>Every year ({len(d_pts)} readings)</summary>
{table(["year", "growth", "years to double at that rate", "source"], d_rows)}
</details>

<h3 id="owed">Not finished yet</h3>
<p>Three pieces the test needs before it is complete.</p>
<ol>
<li><b>A trial run on the past.</b> Run on the years 1995 to 2019, the test must say "not yet". The internet boom should trip only part B, and the years when today's AI methods took off should trip only part A. The measures do not reach back that far yet, so this has not been done. The test was adopted without it. If the trial later trips on those years, the lines are wrong and will be changed, with the change written down.</li>
<li><b>The record of old predictions, for part B.</b> Predictions of the measure in part A, starting with the dates researchers gave in a 2016 survey, set against what then happened. Until it exists, part B cannot be scored.</li>
<li><b>A second source for part C</b> that is not a company talking about itself.</li>
</ol>
</section>

<section class="section prose" id="method">
<h2>Method and data</h2>
<p>Everything on this page is worked out from tables anyone can <a href="/data/">download</a>, and every row in those tables links to where it came from. What people said and expected is kept in <a href="/data/statements.csv">one set of tables</a>, and what the world actually did (how good AI got, what the companies reported, how the economy grew) in <a href="/data/world_measures.csv">another</a>; the two are never mixed. Every search that was run to find a quote is <a href="/data/search_log.csv">written down</a>, so that someone else can run it again. The working documents behind the site are published as they are written, in the project's own terms, for anyone checking the work: <a href="/docs/methodology-v2">the method</a>, <a href="/docs/codebook">the rules for sorting statements</a>, <a href="/docs/singularity-entry-definition">the rules of the test</a>, and <a href="/docs/amendments">every change, with its date and reason</a>. This page is the plain account of the same material.</p>
<p>The searching and the sorting of statements were done by Claude, an AI model made by Anthropic, following those written rules; every rule, and every line of the test, was decided by John Fredrickson. The forum posts were sorted by three AI systems from three companies with no person checking them, and systems from different companies can still share blind spots.</p>
<p class="cite">Cite as: Fredrickson, J. (2026). <em>AGI Zeitgeist Tracker</em> [dataset]. Version of {built} ({esc(commit)}). {SITE_URL}. Data under <a href="/data/LICENSE-DATA.txt">CC BY 4.0</a>; scripts under MIT. The charts are pictures; the table linked beside each one holds the numbers drawn. The test's lines were fixed on {long_date(sc['adopted'])}; <a href="/docs/singularity-entry-definition#record-of-the-rulings-2026-10-08">the record of that decision</a>.</p>
</section>
</div>
{rail(sc, built, commit)}
</div>
"""
    return shell(SITE_TITLE, TAGLINE, body, built, commit, backdrop=True)


def main():
    SITE.mkdir(exist_ok=True)
    world = read("world_measures.csv")
    aggregates = read("aggregates.csv")
    a_pts, a_series = leg_a(world)
    b_pts, b_steps, mani = leg_b(aggregates)
    c_pts = leg_c(world)
    d_pts = leg_d(world)
    sc = score(load_thresholds(), a_series, c_pts, d_pts)
    ytl = years_to_line(a_series, c_pts, d_pts, sc)
    globals()["_AGG"] = aggregates
    built = pacific_today().isoformat()
    claims = load_claims()
    globals()["_CLAIMS"] = claims_page(sc, claims, built, git_commit())
    (SITE / "index.html").write_text(build_html(a_pts, a_series, b_pts, b_steps, mani, c_pts, d_pts, sc, built, git_commit()), encoding="utf-8")
    last_reading = max((p.stem for p in (ROOT / "data" / "readings").glob("*.json")), default=None)
    newest_measurement = max((r["date"] for r in world if r["speaker_id"] in ("metr", "anthropic_institute", "world_bank") and r["aggregate_id"] != "metr-th11-doubling-all"), default=None)
    headline = {"headline_question": HEADLINE_QUESTION, "headline": sc["headline"], "headline_label": sc["headline_label"], "crossing_sentence": ytl["_sentence"],
                "verdict": "Not yet." if sc["status"] == "not entered" else sc["status"], "status": sc["status"],
                "average_share": round(sc["average_share"], 3), "progress": round(sc["progress"], 3), "bottleneck": sc["bottleneck"],
                "gauges": {k: (round(sc[k]["gauge"], 3) if sc[k].get("measurable") else None) for k in "ABCD"},
                "computed_on": built, "last_reading": last_reading, "newest_measurement": newest_measurement, "version": git_commit(),
                "definition": f"{SITE_URL}/docs/singularity-entry-definition", "status_file": f"{SITE_URL}/status.json"}
    (SITE / "status.json").write_text(json.dumps({
        "built": built, "version": git_commit(), "last_reading": last_reading, "newest_measurement": newest_measurement,
        "status": sc["status"], "progress": round(sc["progress"], 3),
        "progress_is_upper_bound": sc["progress_is_upper_bound"], "bottleneck": sc["bottleneck"],
        "gauges": {k: (round(sc[k]["gauge"], 3) if sc[k].get("measurable") else None) for k in "ABCD"},
        "unmeasured": sc["unmeasured"],
        "headline_question": HEADLINE_QUESTION, "headline": sc["headline"], "headline_label": sc["headline_label"],
        "average_share": round(sc["average_share"], 3), "parts_past_half": sc["parts_past_half"],
        "crossing_sentence": ytl["_sentence"],
        "crossings": {k: (list(v) if v else None) for k, v in ytl["_cross"].items()},
        "definition": f"{SITE_URL}/docs/singularity-entry-definition.html",
        # The claims ledger's own block (amendment A27): counts only, never a field the headline could be mistaken for.
        "claims_ledger": _CLAIMS}, indent=2), encoding="utf-8")
    n_docs = render_docs(built, git_commit())
    n_news = render_news(built, git_commit())
    n_data = copy_data()
    claims_csv(claims)
    (SITE / "data" / "headline.json").write_text(json.dumps(headline, indent=2), encoding="utf-8")
    disagree_page(built, git_commit())
    print(f"site/index.html built: {len(a_pts)} time-horizon readings, {len(a_series)} doubling-time windows, "
          f"{len(b_pts)} survey points, {len(c_pts)} self-reports, {len(d_pts)} years of world growth; "
          f"status {sc['status']!r}, progress {'<= ' if sc['progress_is_upper_bound'] else ''}{sc['progress']:.2f} "
          f"(A {sc['A']['gauge']:.2f}, B none, C {sc['C']['gauge']:.2f}, D {sc['D']['gauge']:.2f}); {n_docs} docs rendered, {n_news} news posts, {n_data} data files copied; "
          f"claims page: {len(claims)} claims by {len(_CLAIMS['people'])} people")


if __name__ == "__main__":
    main()
