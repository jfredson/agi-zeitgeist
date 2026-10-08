#!/usr/bin/env python3
"""Build the static site (site/index.html and its figures) from data/*.csv.

The page has two halves that are deliberately kept apart:

- what people believe (the tracker proper: statements, surveys, markets, communities);
- what the world is doing (data/world_measures.csv), shown under the draft definition
  of "entering the singularity" in docs/singularity-entry-definition-draft-2026-10-07.md.

The draft is not adopted and its thresholds are not frozen, so the page publishes the
readings and the derived series (doubling time, pull-in of the consensus date) but no
gauge and no status. The gauge code exists (`leg_status`) and returns "not scored" until
docs/singularity-entry-thresholds.json exists; see the draft's section 5.

    .venv/bin/python scripts/site.py
"""

import csv
import html
import json
import math
import subprocess
from datetime import date, datetime
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.dates as mdates
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
SITE = ROOT / "site"
DOCS = ROOT / "docs"
DRAFT = "docs/singularity-entry-definition-draft-2026-10-07.md"
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

    fig, (ax, ax2) = plt.subplots(2, 1, figsize=(8, 7), sharex=True, gridspec_kw={"height_ratios": [3, 2]})
    for p in pts:
        ax.plot([p["date"], p["date"]], [p["lo"], p["hi"]], color=BLUE, alpha=0.35, linewidth=1.5)
        ax.plot(p["date"], p["value"], "o", ms=6, color=BLUE if p["frontier"] else "white",
                markeredgecolor=BLUE, markeredgewidth=1.5)
    ax.axhline(960, color=MUTED, linestyle=":", linewidth=1)
    ax.text(pts[0]["date"], 960 * 1.15, "16 hours: METR's reliable range ends here", color=MUTED, fontsize=8)
    ax.set_yscale("log")
    ax.set_yticks([0.1, 1, 10, 60, 480, 2400])
    ax.set_yticklabels(["6 s", "1 min", "10 min", "1 h", "8 h", "40 h"])
    ax.set_ylabel("task length finished at 50% success")
    ax.set_title("Leg A. How long a task the best AI can finish, by model release", loc="left", color=INK)
    ax.plot([], [], "o", color=BLUE, label="frontier at release")
    ax.plot([], [], "o", color="white", markeredgecolor=BLUE, label="not the frontier")
    ax.legend(loc="lower right", frameon=False, fontsize=8)
    for p in frontier[-1:]:
        ax.annotate(p["name"], (p["date"], p["value"]), textcoords="offset points", xytext=(-6, 6), ha="right", fontsize=8, color=INK)

    for s in series:
        ax2.plot(s["date"], s["days"], "o", ms=6, color=ORANGE if not s["over16"] else "white", markeredgecolor=ORANGE, markeredgewidth=1.5)
    ax2.plot([s["date"] for s in series], [s["days"] for s in series], color=ORANGE, linewidth=1.5, alpha=0.6)
    ax2.set_ylabel("days per doubling")
    ax2.set_ylim(0, max([s["days"] for s in series] + [300]) * 1.1)
    ax2.set_title("Doubling time of the frontier, trailing twelve months (shorter is faster)", loc="left", color=INK, fontsize=10)
    ax2.plot([], [], "o", color="white", markeredgecolor=ORANGE, label="window includes a reading past 16 h")
    ax2.legend(loc="upper right", frameon=False, fontsize=8)
    ax2.xaxis.set_major_locator(mdates.YearLocator())
    ax2.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
    fig.text(0.01, 0.005, "Source: METR Time Horizon 1.1 results file (data/world_measures.csv, metr-th11-* rows). Bars are METR's 95% ranges.", fontsize=7, color=MUTED)
    fig.tight_layout(rect=(0, 0.02, 1, 1))
    fig.savefig(SITE / "leg-a-time-horizon.png")
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
        pts.append(dict(id=r["aggregate_id"], date=d, t=year_frac(d), m=float(r["value"]), url=r["source_url"]))
    for p in pts:
        p["remaining"] = p["m"] - p["t"]
    steps = []
    for a, b in zip(pts, pts[1:]):
        dt = b["t"] - a["t"]
        dd = b["remaining"] - a["remaining"]
        steps.append(dict(frm=a, to=b, years=dt, change=dd, pull_in=-dd / dt - 1))  # draft: v = -dD/dt - 1

    mb = [r for r in aggregates if r["aggregate_id"] == "mullerbostrom-2013-hlmi50"]
    mani = sorted([r for r in aggregates if r["aggregate_id"].startswith("manifold-agi2030-")], key=lambda r: r["date"])

    fig, ax = plt.subplots(figsize=(8, 4.2))
    xs = [p["t"] for p in pts]
    ax.plot(xs, [p["remaining"] for p in pts], "-o", color=BLUE, ms=7, linewidth=2, label="AI Impacts surveys: years until a 50% chance of human-level AI")
    # Reference: if the forecast date stood still, remaining years fall one per year.
    ax.plot([xs[0], xs[-1] + 1], [pts[0]["remaining"], pts[0]["remaining"] - (xs[-1] + 1 - xs[0])], "--", color=MUTED, linewidth=1,
            label="if the forecast date stood still (one year per year)")
    for p in pts:
        ax.annotate(f"{int(p['m'])}", (p["t"], p["remaining"]), textcoords="offset points", xytext=(0, 8), ha="center", fontsize=8, color=INK)
    if mb:
        r = mb[0]
        t = year_frac(parse_date(r["date"]))
        ax.plot(t, float(r["value"]) - t, "s", color="white", markeredgecolor=GREEN, markeredgewidth=1.5, ms=7,
                label="Müller and Bostrom 2013 (different aggregation, shown for context)")
    ax.set_ylim(0, 55)
    ax.set_ylabel("years remaining at the time of the survey")
    ax.set_title("Leg B stand-in. The consensus arrival date is being pulled in", loc="left", color=INK)
    ax.legend(loc="lower left", frameon=False, fontsize=8)
    fig.text(0.01, 0.005, "Labels are the forecast year. Source: data/aggregates.csv (aiimpacts-*-hlmi50, mullerbostrom-2013-hlmi50).", fontsize=7, color=MUTED)
    fig.tight_layout(rect=(0, 0.03, 1, 1))
    fig.savefig(SITE / "leg-b-pull-in.png")
    plt.close(fig)
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
    fig, ax = plt.subplots(figsize=(8, 4))
    labels = {"google-2026-04-code-share": "Google, Apr 2026:\nnew code AI-generated and approved\n(all code, not research work)",
              "anthropic_institute-2026-02-rd-leads": "Anthropic, Feb 2026:\nAI research work Claude leads\n(reported as under 1%)",
              "anthropic_institute-2026-08-rd-leads": "Anthropic, Aug 2026:\nAI research work Claude leads",
              "anthropic_institute-2026-08-rd-collaborates": "Anthropic, Aug 2026:\nAI research work at or above\n'collaborates' (reported as above 90%)"}
    order = [p for p in pts]
    for i, p in enumerate(order):
        color = GREEN if p["who"] == "anthropic_institute" else YELLOW
        ax.barh(i, p["value"], color=color, height=0.55)
        ax.text(p["value"] + 1, i, f"{int(p['value'])}%" + (f" ({p['bound']})" if p["bound"] else ""), va="center", fontsize=8, color=INK)
    ax.set_yticks(range(len(order)))
    ax.set_yticklabels([labels.get(p["id"], p["id"]) for p in order], fontsize=8)
    ax.set_xlim(0, 122)
    ax.set_xticks([0, 25, 50, 75, 100])
    ax.set_xlabel("percent of the company's own work (self-reports; the measures differ)")
    ax.axvline(50, color=MUTED, linestyle=":", linewidth=1)
    ax.text(51, -0.75, "one half: the draft's placeholder threshold", fontsize=7, color=MUTED, va="center")
    ax.set_ylim(len(order) - 0.5, -1)
    ax.set_title("Leg C. What the companies say AI does of their own work", loc="left", color=INK)
    ax.grid(axis="y", visible=False)
    fig.text(0.01, 0.005, "Source: data/world_measures.csv (google-*, anthropic_institute-* rows). Self-reported; the Anthropic figure is judged by Claude itself.", fontsize=7, color=MUTED)
    fig.tight_layout(rect=(0, 0.04, 1, 1))
    fig.savefig(SITE / "leg-c-self-reports.png")
    plt.close(fig)
    return pts


# ----------------------------------------------------------------------------- status
def leg_status():
    """Gauges per the draft. Returns 'not scored' until thresholds are frozen in a file."""
    if not THRESHOLDS.exists():
        return None
    return json.loads(THRESHOLDS.read_text())


# ----------------------------------------------------------------------------- html
def esc(s):
    return html.escape(str(s), quote=True)


def table(headers, rows):
    out = ["<table><thead><tr>" + "".join(f"<th>{esc(h)}</th>" for h in headers) + "</tr></thead><tbody>"]
    for r in rows:
        out.append("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>")
    out.append("</tbody></table>")
    return "\n".join(out)


def link(url, text):
    return f'<a href="{esc(url)}">{esc(text)}</a>'


def build_html(a_pts, a_series, b_pts, b_steps, mani, c_pts, built, commit):
    frontier = [p for p in a_pts if p["frontier"]]
    latest = frontier[-1]
    last_dt = [s for s in a_series if not s["over16"]][-1] if any(not s["over16"] for s in a_series) else None
    last_any = a_series[-1] if a_series else None
    last_step = b_steps[-1]
    lead = [p for p in c_pts if p["id"] == "anthropic_institute-2026-08-rd-leads"][0]

    a_rows = [[p["date"].isoformat(), esc(p["name"]),
               f"{p['value']/60:.1f} h" if p["value"] >= 60 else f"{p['value']:.1f} min",
               f"{p['lo']/60:.1f} to {p['hi']/60:.1f} h" if p["hi"] >= 60 else f"{p['lo']:.1f} to {p['hi']:.1f} min",
               "yes" if p["frontier"] else "", "past 16 h" if p["over16"] else "",
               link(p["url"], p["id"])] for p in a_pts]
    dt_rows = [[s["date"].isoformat(), f"{s['days']:.0f}", s["n"], "yes" if s["over16"] else ""] for s in a_series]
    b_rows = [[p["date"].isoformat(), int(p["m"]), f"{p['remaining']:.1f}", link(p["url"], p["id"])] for p in b_pts]
    step_rows = [[f"{s['frm']['date'].year} to {s['to']['date'].isoformat()}", f"{s['years']:.1f}", f"{s['change']:+.1f}", f"{s['pull_in']:+.1f}"] for s in b_steps]
    mani_rows = [[r["date"], f"{float(r['value'])*100:.0f}%", link(r["source_url"], r["aggregate_id"])] for r in mani]
    c_rows = [[p["date"].isoformat(), esc(p["measure"]), f"{int(p['value'])}%" + (f" ({p['bound']})" if p["bound"] else ""), link(p["url"], p["id"])] for p in c_pts]

    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>AGI Zeitgeist Tracker</title>
<meta name="description" content="A dated, sourced record of how opinion about artificial general intelligence has moved since 2005, and a draft measurable definition of entering the singularity.">
<style>
:root {{
  --bg: #fbfbfa; --card: #ffffff; --ink: #1f2933; --muted: #6b7785; --line: #e3e8ee; --accent: #2a78d6;
  --warn-bg: #fff6e0; --warn-ink: #6b4b00; --warn-line: #eda100;
}}
@media (prefers-color-scheme: dark) {{
  :root:not([data-theme="light"]) {{
    --bg: #14181d; --card: #1b2026; --ink: #e6e9ed; --muted: #98a2ae; --line: #2b323a; --accent: #6fa8ea;
    --warn-bg: #2a2410; --warn-ink: #f0d58a; --warn-line: #c98a00;
  }}
}}
:root[data-theme="dark"] {{
  --bg: #14181d; --card: #1b2026; --ink: #e6e9ed; --muted: #98a2ae; --line: #2b323a; --accent: #6fa8ea;
  --warn-bg: #2a2410; --warn-ink: #f0d58a; --warn-line: #c98a00;
}}
* {{ box-sizing: border-box; }}
body {{ margin: 0; background: var(--bg); color: var(--ink); font: 16px/1.55 -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; }}
main {{ max-width: 860px; margin: 0 auto; padding: 24px 16px 64px; }}
h1 {{ font-size: 1.9rem; line-height: 1.2; margin: 0 0 4px; }}
h2 {{ font-size: 1.35rem; margin: 48px 0 8px; padding-top: 16px; border-top: 1px solid var(--line); }}
h3 {{ font-size: 1.05rem; margin: 28px 0 6px; }}
p, li {{ max-width: 70ch; }}
a {{ color: var(--accent); }}
.sub {{ color: var(--muted); margin: 0 0 16px; }}
.status {{ background: var(--warn-bg); color: var(--warn-ink); border-left: 4px solid var(--warn-line); padding: 12px 14px; border-radius: 6px; margin: 20px 0; }}
.status strong {{ display: block; margin-bottom: 2px; }}
figure {{ margin: 16px 0; background: var(--card); border: 1px solid var(--line); border-radius: 8px; padding: 8px; }}
figure img {{ width: 100%; height: auto; display: block; border-radius: 4px; background: #fff; }}
figcaption {{ color: var(--muted); font-size: 0.85rem; padding: 8px 6px 2px; }}
table {{ border-collapse: collapse; width: 100%; font-size: 0.85rem; margin: 10px 0 4px; display: block; overflow-x: auto; }}
th, td {{ text-align: left; padding: 6px 8px; border-bottom: 1px solid var(--line); vertical-align: top; white-space: nowrap; }}
td:nth-child(2) {{ white-space: normal; min-width: 14ch; }}
th {{ color: var(--muted); font-weight: 600; }}
details {{ margin: 8px 0 18px; }}
summary {{ cursor: pointer; color: var(--accent); }}
.legs {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(230px, 1fr)); gap: 12px; margin: 16px 0; }}
.leg {{ background: var(--card); border: 1px solid var(--line); border-radius: 8px; padding: 12px 14px; }}
.leg b {{ display: block; margin-bottom: 4px; }}
.leg .g {{ color: var(--muted); font-size: 0.85rem; }}
.num {{ font-size: 1.6rem; font-weight: 600; line-height: 1.1; margin: 4px 0; }}
footer {{ color: var(--muted); font-size: 0.85rem; margin-top: 48px; border-top: 1px solid var(--line); padding-top: 12px; }}
code {{ font-size: 0.9em; background: var(--card); border: 1px solid var(--line); padding: 0 4px; border-radius: 3px; }}
</style>
</head>
<body>
<main>
<h1>AGI Zeitgeist Tracker</h1>
<p class="sub">A dated, sourced record of how expert and public opinion about artificial general intelligence has moved since 2005. Every number on this page links to the row it came from.</p>

<p>AGI here means AI that can do most intellectual work a person can. The working question: did the main public argument move from <em>whether</em> it is possible, to <em>when</em> it arrives, to <em>whether today's systems are already close or improving themselves</em>? The method is built so the data can say no. The seed phase is complete; the full panel and the public streams have not started.</p>

<div class="status"><strong>Singularity entry status: not scored.</strong>
The three-leg definition below is a draft under review. Its thresholds are not frozen, so this page shows the readings and nothing derived from a threshold. No gauge and no status will be published until the definition is adopted, by the draft's own rule.</div>

<h2 id="belief">What people believe</h2>
<p>The tracker proper. One row per public statement, survey result, market reading or poll, coded under <a href="{REPO}/blob/main/docs/methodology-v2.md">methodology version 2</a>.</p>

<figure><img src="chart-1-frames.png" alt="Share of coded statements by primary frame, by year, seed panel of five people">
<figcaption>Seed phase: what each statement was mainly about, by year, for five traced people (Kurzweil, Hinton, LeCun, Marcus, Altman). Counts in <a href="chart-1-frames.csv">chart-1-frames.csv</a>. Five people are not a panel; this chart exists to test the pipeline.</figcaption></figure>

<figure><img src="vanguard-pilot-r-singularity.png" alt="Framing in sampled high-score posts from r/singularity, 2024Q4 to 2026Q3, model-coded">
<figcaption>Pilot, model-coded: framing in sampled high-score posts from r/singularity, 2024Q4 to 2026Q3. Not representative of participants or the public. Three models from different companies coded a 140-post subset blind and the majority vote is the final code; <a href="{REPO}/blob/main/docs/vanguard/pilot-report-r-singularity-2026-10.md">pilot report</a>.</figcaption></figure>

<h2 id="singularity">Entering the singularity: a definition under review</h2>
<p>"Any prediction made now about the next five years will look stupid in retrospect" is one of three standard definitions of the singularity, and each one alone has a known false alarm. The <a href="{REPO}/blob/main/{DRAFT}">draft definition</a> requires all three to be true at once, for four consecutive quarters:</p>

<div class="legs">
<div class="leg"><b>A. The pace is accelerating</b>
<div class="g">Kurzweil's school. The doubling time of a frozen capability measure is itself shrinking.</div>
<div class="num">{(last_dt['days'] if last_dt else last_any['days']):.0f} days</div>
<div class="g">per doubling, trailing twelve months to {(last_dt or last_any)['date'].isoformat()}{" (last window without a reading past 16 h)" if last_dt and last_dt is not last_any else ""}. Gauge: not scored.</div></div>
<div class="leg"><b>B. Forecasts have stopped working</b>
<div class="g">Vinge's school. The horizon over which forecasts beat the trend is collapsing. Confirmed only in arrears; the live stand-in is how fast the consensus date is being pulled in.</div>
<div class="num">{last_step['pull_in']:+.1f} yr/yr</div>
<div class="g">excess pull-in of the expert consensus date, {last_step['frm']['date'].year} to {last_step['to']['date'].isoformat()}. Zero means the date stood still. Gauge: not scored.</div></div>
<div class="leg"><b>C. AI is doing the improving</b>
<div class="g">Good's school. The share of the work that produces frontier progress that is supplied by AI.</div>
<div class="num">{int(lead['value'])}%</div>
<div class="g">of Anthropic's AI research work "led" by its own model, {lead['date'].strftime('%B %Y')}, by its own measurement. Gauge: not scored.</div></div>
</div>

<h3>Leg A. How long a task the best AI can finish</h3>
<p>The anchor measure is METR's time horizon: the length of software task, in minutes an expert needs for it, that a model finishes half the time. It is chosen because it has not yet saturated the way benchmarks do. The lower panel is the draft's quantity: the doubling time of the frontier over a trailing twelve months. A flat line would mean steady exponential growth, which is Kurzweil's world but not yet a singularity; a falling line is the signature the draft looks for.</p>
<figure><img src="leg-a-time-horizon.png" alt="METR 50% time horizon by model release date on a log scale, with the trailing twelve-month doubling time of the frontier below">
<figcaption>Hollow points were not the frontier at release. METR treats estimates past 16 hours as beyond its task suite's reliable range, and its own doubling-time fit excludes them; windows that include such a reading are hollow in the lower panel. The latest frontier reading is {esc(latest['name'])} at {latest['value']/60:.0f} hours on {latest['date'].isoformat()}. Doubling-time series in <a href="leg-a-doubling-time.csv">leg-a-doubling-time.csv</a>.</figcaption></figure>
<details><summary>Every reading ({len(a_pts)} models) and every doubling-time window</summary>
{table(["release", "model", "50% horizon", "95% range", "frontier", "", "row"], a_rows)}
{table(["window end", "days per doubling", "frontier points", "includes a reading past 16 h"], dt_rows)}
</details>

<h3>Leg B. Are forecasts holding up?</h3>
<p>The real test scores old forecasts of the measure above against simple trend extrapolation and asks how far ahead they still win. That ledger does not exist yet and can only be scored once the forecast period has passed. The stand-in, available now, is the expert consensus date for human-level AI. If forecasters had the trend right, the date would stand still and the years remaining would fall by one each year, the dashed line. Instead the three AI Impacts surveys show the remaining distance collapsing: the step from 2022 to 2023 removed about {abs(last_step['change']):.0f} years of distance in {last_step['years']:.1f} calendar years. That is forecasts failing in the slow direction, which is the direction the draft records.</p>
<figure><img src="leg-b-pull-in.png" alt="Years remaining until the surveyed 50% date for human-level AI, by survey year, against a one-year-per-year reference line">
<figcaption>Surveys use different definitions and aggregation, so the 2013 survey is shown but not joined to the series. Steps in <a href="leg-b-pull-in.csv">leg-b-pull-in.csv</a>.</figcaption></figure>
<details><summary>The survey readings, the steps between them, and the market reading for context</summary>
{table(["survey", "50% year", "years remaining", "row"], b_rows)}
{table(["step", "calendar years", "change in years remaining", "excess pull-in per year"], step_rows)}
<p>Manifold market, "AGI created and publicly announced before 2030", for context only (a market price, not a survey):</p>
{table(["date", "probability", "row"], mani_rows)}
</details>

<h3>Leg C. Is AI doing the improving?</h3>
<p>The draft wants the share of inputs to frontier AI progress supplied by AI. Nobody outside the labs can measure that, so what exists is self-report. Two kinds are recorded: a company's share of all new code written by AI, which is a proxy at best, and Anthropic's self-measured share of its own AI research work that its model "leads", which is closer to the draft's measure but is judged by the model itself. The figures do not measure the same thing and should not be compared with each other.</p>
<figure><img src="leg-c-self-reports.png" alt="Bar chart of company self-reported shares of AI-done work, with the draft's one-half placeholder marked">
<figcaption>Every bar is a company statement about itself. Anthropic's row for February 2026 is "under 1%", recorded as 1. Its "above 90%" row is recorded as 90.</figcaption></figure>
<details><summary>The self-reports</summary>
{table(["date", "measure", "value", "row"], c_rows)}
</details>

<h3>What has to happen before a gauge appears</h3>
<ol>
<li>John adopts the definition and freezes the anchor measure, the reference year, the thresholds and the persistence window, with a one-line reason for each. Until then the page shows readings only.</li>
<li>The backward test: run on 1995 to 2019 the definition must return "not entered", with the internet years firing only leg B and the deep-learning years firing only leg A. The leg A series starts in 2019 and leg C in 2026, so this test cannot run yet and needs older series to be built.</li>
<li>The leg B forecast-versus-outcome ledger, starting from the 2016 expert survey's milestone dates and what actually happened.</li>
</ol>

<h2 id="method">Method and sources</h2>
<p>Belief measures and world measures live in separate files and are never combined. <code>data/statements.csv</code>, <code>data/aggregates.csv</code> and the community samples hold what people said and believed. <code>data/world_measures.csv</code> holds capability readings and company self-reports, with the same columns and the same rule that every row carries its source and the question wording. Every search that produced a row is in <code>data/search_log.csv</code>. The scripts <code>scripts/validate.py</code>, <code>scripts/charts.py</code> and <code>scripts/site.py</code> rebuild everything on this page from those files.</p>
<p>Cite as: Fredrickson, J. (2026). <em>AGI Zeitgeist Tracker</em> [dataset]. Version of {built}, commit {esc(commit)}. {REPO}. Data under CC BY 4.0; scripts under MIT.</p>

<footer>Built {built} from commit {esc(commit)}. Figures are static images; the CSV beside each one holds the plotted numbers.</footer>
</main>
</body>
</html>
"""


def main():
    SITE.mkdir(exist_ok=True)
    world = read("world_measures.csv")
    aggregates = read("aggregates.csv")
    a_pts, a_series = leg_a(world)
    b_pts, b_steps, mani = leg_b(aggregates)
    c_pts = leg_c(world)
    built = date.today().isoformat()
    (SITE / "index.html").write_text(build_html(a_pts, a_series, b_pts, b_steps, mani, c_pts, built, git_commit()), encoding="utf-8")
    print(f"site/index.html built: {len(a_pts)} time-horizon readings, {len(a_series)} doubling-time windows, "
          f"{len(b_pts)} survey points, {len(c_pts)} self-reports")


if __name__ == "__main__":
    main()
