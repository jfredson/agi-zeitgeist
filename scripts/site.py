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
    ax.text(51, -0.75, "one half: the frozen threshold (scored on the 'leads' rows)", fontsize=7, color=MUTED, va="center")
    ax.set_ylim(len(order) - 0.5, -1)
    ax.set_title("Leg C. What the companies say AI does of their own work", loc="left", color=INK)
    ax.grid(axis="y", visible=False)
    fig.text(0.01, 0.005, "Source: data/world_measures.csv (google-*, anthropic_institute-* rows). Self-reported; the Anthropic figure is judged by Claude itself.", fontsize=7, color=MUTED)
    fig.tight_layout(rect=(0, 0.04, 1, 1))
    fig.savefig(SITE / "leg-c-self-reports.png")
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
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.bar([p["year"] for p in pts], [p["growth"] for p in pts], color=GREEN, width=0.8)
    ax.axhline(30, color=ORANGE, linestyle="--", linewidth=1.2)
    ax.text(pts[0]["year"], 30.8, "30% a year: the frozen threshold (Davidson's 'explosive growth' line)", fontsize=8, color=ORANGE)
    ax.axhline(0, color=MUTED, linewidth=0.8)
    ax.set_ylim(-5, 34)
    ax.set_ylabel("world output growth, % over the previous year")
    ax.set_title("Leg D. World output growth, 1961 to " + str(pts[-1]["year"]), loc="left", color=INK)
    ax.grid(axis="x", visible=False)
    fig.text(0.01, 0.005, "Source: World Bank World Development Indicators, world GDP growth at constant 2015 US$ (data/world_measures.csv, worldbank-gdp-growth-* rows).", fontsize=7, color=MUTED)
    fig.tight_layout(rect=(0, 0.04, 1, 1))
    fig.savefig(SITE / "leg-d-world-growth.png")
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
    if unmeasured:
        out["status"] = "not entered"
    elif all(out[k]["at_threshold"] for k in "ABCD"):
        out["status"] = "mark crossed, under persistence test"
    elif all(out[k]["gauge"] > 0.5 for k in "ABCD"):
        out["status"] = "approaching"
    else:
        out["status"] = "not entered"
    return out


def load_thresholds():
    return json.loads(THRESHOLDS.read_text())


# ----------------------------------------------------------------------------- shell
# The page shell follows the Sentient Horizons design standard (sentient-horizons/design/README.md):
# shared stylesheet site/deep-field.css (copied unchanged, version in its header), the top bar with
# two tiers and the theme toggle, the cosmic backdrop on the home page only, and the five-line
# footer ending "A Sentient Horizons project." with the attribution line "© year John Fredrickson, with Claude. provenance. licence."
SITE_NAME = "AGI Zeitgeist"
SITE_TITLE = "AGI Zeitgeist Tracker"
TAGLINE = ("A dated, sourced record of how opinion about artificial general intelligence has moved since 2005, "
           "beside a test, with its rules fixed in advance, of whether the world has entered the singularity.")
WITH_CLAUDE = "https://sentient-horizons.com/with-claude/"
# Labels ruled by John, 2026-10-08.
NAV_PRIMARY = [("/#belief", "Current Zeitgeist"), ("/#singularity", "Are We in the Singularity?"), ("/#method", "Method and Data")]
NAV_SECONDARY = [("/docs/singularity-entry-definition", "Definitions"), ("/docs/amendments", "Changelog")]
FOOTER_LINKS = [("/data/", "Download the data"), ("/#method", "Method and data"),
                ("/docs/singularity-entry-definition", "Definitions"), ("/docs/amendments", "Changelog")]

THEME_SCRIPT = """<script>
(function(){try{var s=localStorage.getItem('theme');var t=s==='light'||s==='dark'?s:(window.matchMedia('(prefers-color-scheme: light)').matches?'light':'dark');document.documentElement.dataset.theme=t;}catch(e){}})();
</script>"""

SHELL_SCRIPT = """<script>
(function(){var h=document.querySelector('.site-header');var b=h&&h.querySelector('.nav-toggle');var m=document.getElementById('site-nav');
if(b&&m){var so=function(o){h.classList.toggle('nav-open',o);b.setAttribute('aria-expanded',o?'true':'false');};
b.addEventListener('click',function(){so(!h.classList.contains('nav-open'));});m.addEventListener('click',function(e){if(e.target.closest('a'))so(false);});
window.addEventListener('resize',function(){if(window.innerWidth>820)so(false);});}
var t=document.querySelector('.theme-toggle');var meta=document.getElementById('theme-color-meta');var C={dark:'#08070f',light:'#faf9f7'};
function sync(x){document.documentElement.dataset.theme=x;if(meta)meta.setAttribute('content',C[x]||C.dark);}
sync(document.documentElement.dataset.theme==='light'?'light':'dark');
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
/* the landing hero: the answer on the left, the four conditions beneath it, the experts' date on the right */
.land { display: grid; grid-template-columns: minmax(0, 1fr) 400px; gap: 48px; align-items: start; padding: 48px 0 24px; }
.land .eyebrow { margin-bottom: 18px; }
.land .answer { font-size: clamp(64px, 10vw, 112px); line-height: 0.95; font-weight: 600; letter-spacing: -0.02em; color: var(--text); margin: 0 0 22px; }
.land h1 { font-size: clamp(20px, 2.3vw, 27px); line-height: 1.3; font-weight: 600; margin: 0 0 12px; }
.land .lede { font-style: normal; font-size: 18px; line-height: 1.5; color: var(--text-soft); margin: 0 0 22px; max-width: 640px; }
.conds { display: grid; gap: 10px; margin: 0 0 22px; max-width: 640px; }
.cond { display: grid; grid-template-columns: 2.2em 1fr; gap: 2px 12px; align-items: center; font-family: var(--sans); }
.cond .k { font-size: 22px; font-weight: 600; color: var(--text); grid-row: span 2; align-self: center; }
.cond .n { font-size: 14px; color: var(--text); }
.cond .bar { margin: 4px 0 0; height: 10px; }
.cond .bar span { display: none; }
.cond .bar.none { background: repeating-linear-gradient(90deg, var(--line) 0 6px, transparent 6px 10px); }
.cond .d { grid-column: 2; font-size: 12.5px; color: var(--muted); line-height: 1.4; }
.fresh { font-family: var(--sans); font-size: 13px; color: var(--muted); margin: 0 0 18px; line-height: 1.5; }
.land .ctas { margin-bottom: 8px; }
.card { background: var(--panel); border: 1px solid var(--line); border-radius: var(--radius); padding: 22px 24px; font-family: var(--sans); }
.card .ch { font-size: 12px; letter-spacing: 0.1em; text-transform: uppercase; color: var(--muted); margin: 0 0 14px; }
.card .big { font-family: var(--serif); font-size: 64px; font-weight: 600; line-height: 1; color: var(--text); margin: 0 0 6px; }
.card .what { font-size: 14px; color: var(--text-soft); line-height: 1.5; margin: 0 0 16px; }
.card .trend { display: flex; gap: 18px; padding: 14px 0; border-top: 1px solid var(--line); border-bottom: 1px solid var(--line); margin: 0 0 14px; }
.card .trend div { flex: 1; }
.card .trend b { display: block; font-family: var(--serif); font-size: 24px; font-weight: 600; color: var(--text); }
.card .trend span { font-size: 11.5px; color: var(--muted); }
.card .foot { font-size: 13px; color: var(--muted); line-height: 1.5; margin: 0; }
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
figure.fig { margin: 18px 0; background: #fff; border: 1px solid var(--line); border-radius: var(--radius); padding: 8px; }
figure.fig img { width: 100%; height: auto; display: block; border-radius: 4px; }
figure.fig figcaption { font-family: var(--sans); font-size: 13px; line-height: 1.5; color: var(--muted); padding: 10px 6px 2px; }
:root[data-theme='light'] figure.fig { background: #fff; }
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
.document img { max-width: 100%; height: auto; background: #fff; border-radius: 4px; }
.document pre { font-family: var(--mono); font-size: 13px; background: var(--chip-bg); border: 1px solid var(--line); border-radius: 6px; padding: 10px 12px; overflow-x: auto; }
.document pre code { border: 0; background: none; padding: 0; }
.footer-meta a { color: inherit; }
"""


def starfield(seed=20261008, count=150):
    rng = __import__("random").Random(seed)
    out = []
    for _ in range(count):
        x, y = rng.random() * 100, rng.random() * 100
        size = 1 if rng.random() < 0.85 else 2
        op = 0.1 + rng.random() * 0.7
        tw = rng.random() < 0.38
        anim = f"animation:twk {2.5 + rng.random() * 4.5:.2f}s ease-in-out {rng.random() * 6:.2f}s infinite" if tw else ""
        out.append(f'<span style="left:{x:.2f}%;top:{y:.2f}%;width:{size}px;height:{size}px;opacity:{op:.2f};{anim}"></span>')
    return '<div class="starfield" aria-hidden="true">' + "".join(out) + "</div>"


def long_date(iso):
    d = date.fromisoformat(iso)
    return f"{d.day} {d:%B %Y}"


def provenance(built, commit):
    """The plain-language provenance clause of the attribution line (design standard, section 8)."""
    n_statements = len(read("statements.csv"))
    n_world = len(read("world_measures.csv"))
    posts = DATA / "vanguard" / "full-run-posts.csv"
    n_posts = (sum(1 for _ in posts.open(encoding="utf-8")) - 1) if posts.exists() else 0
    return (f"Last built {long_date(built)} (version {esc(commit)}) from {n_statements} expert statements, "
            f"{n_world} readings of the world and {n_posts} community posts.")


def shell(title, description, body, built, commit, *, canonical_path="/", backdrop=False, eyebrow=None, h1=None, lede=None, active=None):
    nav1 = "".join(f'<a href="{esc(h)}" class="nav-primary{" active" if h == active else ""}">{esc(t)}</a>' for h, t in NAV_PRIMARY)
    nav2 = "".join(f'<a href="{esc(h)}" class="nav-secondary{" active" if h == active else ""}">{esc(t)}</a>' for h, t in NAV_SECONDARY)
    links = "".join(f'<a href="{esc(h)}"{" rel=\"noopener\"" if h.startswith("http") else ""}>{esc(t)}</a>' for h, t in FOOTER_LINKS)
    hero = ""
    if h1:
        hero = (f'<section class="hero">{f"<p class=eyebrow>{esc(eyebrow)}</p>" if eyebrow else ""}<h1>{esc(h1)}</h1>'
                f'{f"<p class=lede>{lede}</p>" if lede else ""}</section>')
    bg = f'<div class="space-bg" aria-hidden="true"><div class="galaxy"></div><div class="core"></div>{starfield()}</div>' if backdrop else ""
    year = built[:4]
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
{THEME_SCRIPT}
<meta id="theme-color-meta" name="theme-color" content="#08070f">
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
<meta name="twitter:card" content="summary">
<link rel="stylesheet" href="/deep-field.css">
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
<p class="footer-meta">© {year} John Fredrickson, <a class="with-claude" href="{WITH_CLAUDE}">with Claude</a>. {provenance(built, commit)} Free to reuse with credit (<a href="https://creativecommons.org/licenses/by/4.0/" rel="license">CC BY 4.0</a>); code under the MIT licence.</p>
<p class="footer-parent"><a href="https://sentient-horizons.com" rel="noopener">A Sentient Horizons project.</a></p>
</div></div></footer>
{SHELL_SCRIPT}
</body>
</html>
"""


# ----------------------------------------------------------------------------- docs and data
def render_docs(built, commit):
    """Render every Markdown document to site/docs/ with pandoc, in the shared shell, rewriting links between them."""
    out_root = SITE / "docs"
    if out_root.exists():
        shutil.rmtree(out_root)
    out_root.mkdir()
    sources = sorted(DOCS.rglob("*.md")) + [ROOT / "README.md"]
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
        note = f'<p class="cite">Rendered from <code>{esc(str(src.relative_to(ROOT)))}</code> at commit {esc(commit)}.</p>'
        page = shell(f"{title} | {SITE_TITLE}", f"{title}: a document of the {SITE_TITLE}.", f'<div class="prose narrow document">{body}{note}</div>',
                     built, commit, canonical_path=f"/docs/{rel.with_suffix('').as_posix()}", eyebrow=folder, h1=title)
        dst.write_text(page, encoding="utf-8")
        n += 1
    for src in DOCS.rglob("*.csv"):  # evidence tables the documents link to
        dst = out_root / src.relative_to(DOCS)
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)
    return n


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
    # an index page, since the asset host does not list folders
    items = "".join(f'<li><a href="{esc(f.relative_to(DATA).as_posix())}">{esc(f.relative_to(DATA).as_posix())}</a> ({f.stat().st_size // 1024 + 1} KB)</li>' for f in files)
    body = (f'<div class="prose narrow"><p>Every table behind the site, as it stands at this build. Each row carries its source. '
            f'Licensed <a href="LICENSE-DATA.txt">CC BY 4.0</a>; cite as on the <a href="/#method">home page</a>. How each file is laid out: <a href="/docs/README">about the data</a>.</p><ul>{items}</ul></div>')
    (out / "index.html").write_text(shell(f"Download the data | {SITE_TITLE}", "Every CSV table behind the AGI Zeitgeist Tracker, under CC BY 4.0.", body,
                                          date.today().isoformat(), git_commit(), canonical_path="/data/", eyebrow="Data", h1="Download the data"), encoding="utf-8")
    return len(files)


# ----------------------------------------------------------------------------- html
def esc(s):
    return html.escape(str(s), quote=True)


def table(headers, rows):
    out = ['<table class="data"><thead><tr>' + "".join(f"<th>{esc(h)}</th>" for h in headers) + "</tr></thead><tbody>"]
    for r in rows:
        out.append("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>")
    out.append("</tbody></table>")
    return "\n".join(out)


def link(url, text):
    return f'<a href="{esc(url)}">{esc(text)}</a>'


def gauge_bar(g):
    if g is None:
        return '<div class="bar none"><span>not yet measurable</span></div>'
    return f'<div class="bar"><i style="width:{g*100:.0f}%"></i><span>{g:.2f}</span></div>'


def landing(sc, b_pts, mani, built, commit):
    """The first screen: the answer, the four conditions, the experts' date."""
    A, C, D = sc["A"], sc["C"], sc["D"]
    answer = {"not entered": "Not yet.", "approaching": "Getting close.",
              "mark crossed, under persistence test": "Crossing now.", "entered": "Yes."}[sc["status"]]
    conds = [
        ("A", "AI capability is doubling faster and faster", A.get("gauge"),
         f"The best AI's task horizon doubles every {A['reading']:.0f} days; the line is {A['t_star']:.0f} days, and it also has to be falling."),
        ("B", "Forecasts of AI progress have stopped working", None,
         "Not measurable yet: the record of past forecasts against what happened has not been built."),
        ("C", "AI does most of the research that improves AI", C.get("gauge"),
         f"Anthropic says its model leads {C['reading']*100:.0f}% of its AI research work, by its own count; the line is half."),
        ("D", "The world economy grows ten times faster than ever", D.get("gauge"),
         f"World output grew {D['reading']:.1f}% in {D['year']}; the line is {D['g_star']:.0f}% a year."),
    ]
    rows = "".join(f'<div class="cond"><span class="k">{k}</span><span class="n">{esc(n)}</span>{gauge_bar(g)}<span class="d">{esc(d)}</span></div>' for k, n, g, d in conds)
    latest = b_pts[-1]
    trend = "".join(f'<div><b>{int(p["m"])}</b><span>{p["date"].year} survey</span></div>' for p in b_pts)
    m = mani[-1] if mani else None
    market = (f' The betting market Manifold puts <a href="{esc(m["source_url"])}">{float(m["value"])*100:.0f}%</a> on AGI being announced before 2030 (as of {esc(m["date"])}).' if m else "")
    return f"""<section class="land">
<div>
<p class="eyebrow">Are we in the singularity?</p>
<p class="answer">{answer}</p>
<h1>Four things would all have to hold for a year. Today none of them does.</h1>
<p class="lede">The lines were fixed before any score was published, and the furthest from its line is the economy. Each bar shows how far a condition has come from where it stood in {sc['reference_year']} toward its line.</p>
<div class="conds">{rows}</div>
<p class="fresh">Scored {long_date(built)} from public data. The rules were fixed on {long_date(sc['adopted'])}; <a href="/docs/amendments">any change to them is logged</a>.</p>
<div class="ctas"><a class="btn" href="#singularity">What would it take?</a><a class="btn ghost" href="#belief">What do people believe?</a></div>
</div>
<aside class="card">
<p class="ch">What the experts expect</p>
<p class="big">{int(latest['m'])}</p>
<p class="what">The year AI researchers give even odds of machines doing every task better and cheaper than people, in the <a href="{esc(latest['url'])}">latest large survey of them</a> ({latest['date'].year}{(", " + latest['n']) if latest['n'] else ""}).</p>
<div class="trend">{trend}</div>
<p class="foot">The date has come {int(b_pts[0]['m']) - int(latest['m'])} years closer since {b_pts[0]['date'].year}.{market} <a href="#belief">The full record is below.</a></p>
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
           ("#owed", "What the test still owes", "d3"), ("#method", "Method and data", "")]
    toc_html = "".join(f'<a href="{h}" class="{c}">{esc(t)}</a>' for h, t, c in toc)
    return f"""<aside class="rail">
<h4>On this page</h4>
<nav class="toc">{toc_html}</nav>
<h4 class="rail-sec">Use the data</h4>
<p class="use"><a href="/data/">Download every table</a> (CC BY 4.0) · <a href="#method">How to cite</a> · <a href="/docs/README">What each file holds</a> · version {esc(commit)}</p>
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
    mani_rows = [[r["date"], f"{float(r['value'])*100:.0f}%", link(r["source_url"], r["aggregate_id"])] for r in mani]
    c_rows = [[p["date"].isoformat(), esc(p["measure"]), f"{int(p['value'])}%" + (f" ({p['bound']})" if p["bound"] else ""), link(p["url"], p["id"])] for p in c_pts]
    d_rows = [[q["year"], f"{q['growth']:.2f}%", f"{q['doubling']:.1f}" if q["doubling"] else "none (output fell)", link(q["url"], q["id"])] for q in reversed(d_pts)]

    progress_word = "at most " if sc["progress_is_upper_bound"] else ""
    status_line = {
        "not entered": "Not entered.",
        "approaching": "Approaching: every gauge is above one half.",
        "mark crossed, under persistence test": "Mark crossed; the four-quarter persistence count is running.",
    }[sc["status"]]

    body = f"""{landing(sc, b_pts, mani, built, commit)}
<div class="with-rail"><div>
<section class="section prose" id="belief">
<h2>The current zeitgeist</h2>
<p>AGI here means AI that can do most intellectual work a person can. The record asks one question of twenty years of public argument: did it move from <em>whether</em> AGI is possible, to <em>when</em> it arrives, to <em>whether today's systems are already close or improving themselves</em>? The method is built so the data can say no. So far the record covers five people in depth, three expert surveys, the polls and markets, and a sample of one online community; the full panel of 37 named experts, the newspapers and the other communities are still to come. One row per public statement, survey result, market reading or poll, labelled under <a href="/docs/methodology-v2">a written method</a>.</p>

<figure class="fig"><img src="chart-1-frames.png" alt="Share of coded statements by primary frame, by year, seed panel of five people">
<figcaption>Seed phase: what each statement was mainly about, by year, for five traced people (Kurzweil, Hinton, LeCun, Marcus, Altman). Counts in <a href="chart-1-frames.csv">chart-1-frames.csv</a>. Five people are not a panel; this chart exists to test the pipeline.</figcaption></figure>

<figure class="fig"><img src="vanguard-pilot-r-singularity.png" alt="Framing in sampled high-score posts from r/singularity, 2024Q4 to 2026Q3, model-coded">
<figcaption>Pilot, model-coded: framing in sampled high-score posts from r/singularity, 2024Q4 to 2026Q3. Not representative of participants or the public. Three models from different companies (Claude, Gemini and GPT) each coded all 390 sampled posts blind under the final codebook, and the majority vote is the final code; where no two agree, the post is left out of the affected measure. Counts in <a href="vanguard-pilot-r-singularity.csv">vanguard-pilot-r-singularity.csv</a>; <a href="/docs/vanguard/pilot-report-r-singularity-2026-10">pilot report</a>.</figcaption></figure>
</section>

<section class="section prose" id="singularity">
<h2>Are we in the singularity?</h2>
<p>"Any prediction made now about the next five years will look stupid in retrospect" is one of the standard definitions of the singularity, and each definition alone has a known false alarm. The <a href="/docs/singularity-entry-definition">adopted definition</a> requires four things to be true at once, for four consecutive quarters. Each gauge runs from 0 (the {sc['reference_year']} reference) to 1 (the frozen threshold); the smallest gauge is the honest distance remaining.</p>

<div class="legs">
<div class="leg"><b>A. The pace is accelerating</b>
<div class="g">Kurzweil's school. The doubling time of a frozen capability measure is itself shrinking.</div>
<div class="num">{A['reading']:.0f} days</div>
<div class="g">per doubling, trailing twelve months to {A['date'].isoformat()}. Threshold: {A['t_star']:.0f} days and still falling. Reference: {A['t_ref']:.0f} days.</div>
{gauge_bar(A['gauge'])}</div>
<div class="leg"><b>B. Forecasts have stopped working</b>
<div class="g">Vinge's school. The horizon over which forecasts beat the trend is collapsing. Confirmed only in arrears.</div>
<div class="num">{last_step['pull_in']:+.1f} yr/yr</div>
<div class="g">stand-in only: excess pull-in of the expert consensus date, {last_step['frm']['date'].year} to {last_step['to']['date'].isoformat()}. The gauge needs a forecast ledger that is not built yet. Threshold: a one-year horizon.</div>
{gauge_bar(None)}</div>
<div class="leg"><b>C. AI is doing the improving</b>
<div class="g">Good's school. The share of the work that produces frontier progress that is supplied by AI.</div>
<div class="num">{int(lead['value'])}%</div>
<div class="g">of Anthropic's AI research work "led" by its own model, {lead['date'].strftime('%B %Y')}, by its own measurement. Threshold: one half. One company, self-reported.</div>
{gauge_bar(C['gauge'])}</div>
<div class="leg"><b>D. The economy has changed mode</b>
<div class="g">Hanson's school. A new growth mode doubles world output a hundred times faster than the last.</div>
<div class="num">{D['reading']:.1f}% a year</div>
<div class="g">world output growth in {D['year']}, doubling every {D['doubling']:.0f} years. Threshold: {D['g_star']:.0f}% a year ({D['t_star']:.1f}-year doubling). Reference: {D['g_ref']:.1f}% ({D['t_ref']:.0f}-year doubling).</div>
{gauge_bar(D['gauge'])}</div>
</div>

<h3 id="leg-a">Leg A. How long a task the best AI can finish</h3>
<p>The anchor measure is METR's time horizon: the length of software task, in minutes an expert needs for it, that a model finishes half the time. It is chosen because it has not yet saturated the way benchmarks do. The lower panel is the definition's quantity: the doubling time of the frontier over a trailing twelve months. A flat line would mean steady exponential growth, which is Kurzweil's world but not yet a singularity; a falling line is the signature the definition looks for. The gauge is scored on the last window with no reading past 16 hours, and the threshold also requires the doubling time to have fallen over the last two windows ({"met" if A['falling'] else "not met"} today).</p>
<figure class="fig"><img src="leg-a-time-horizon.png" alt="METR 50% time horizon by model release date on a log scale, with the trailing twelve-month doubling time of the frontier below">
<figcaption>Hollow points were not the frontier at release. METR treats estimates past 16 hours as beyond its task suite's reliable range, and its own doubling-time fit excludes them; windows that include such a reading are hollow in the lower panel and are not scored. The latest frontier reading is {esc(latest['name'])} at {latest['value']/60:.0f} hours on {latest['date'].isoformat()}. Doubling-time series in <a href="leg-a-doubling-time.csv">leg-a-doubling-time.csv</a>.</figcaption></figure>
<details><summary>Every reading ({len(a_pts)} models) and every doubling-time window</summary>
{table(["release", "model", "50% horizon", "95% range", "frontier", "", "row"], a_rows)}
{table(["window end", "days per doubling", "frontier points", "includes a reading past 16 h"], dt_rows)}
</details>

<h3 id="leg-b">Leg B. Are forecasts holding up?</h3>
<p>The real test scores old forecasts of the measure above against simple trend extrapolation and asks how far ahead they still win. That ledger does not exist yet and can only be scored once the forecast period has passed, so leg B is shown as not yet measurable and the progress number above is an upper bound. The stand-in, available now, is the expert consensus date for human-level AI. If forecasters had the trend right, the date would stand still and the years remaining would fall by one each year, the dashed line. Instead the three AI Impacts surveys show the remaining distance collapsing: the step from 2022 to 2023 removed about {abs(last_step['change']):.0f} years of distance in {last_step['years']:.1f} calendar years. That is forecasts failing in the slow direction, which is the direction the definition records.</p>
<figure class="fig"><img src="leg-b-pull-in.png" alt="Years remaining until the surveyed 50% date for human-level AI, by survey year, against a one-year-per-year reference line">
<figcaption>Surveys use different definitions and aggregation, so the 2013 survey is shown but not joined to the series. Steps in <a href="leg-b-pull-in.csv">leg-b-pull-in.csv</a>.</figcaption></figure>
<details><summary>The survey readings, the steps between them, and the market reading for context</summary>
{table(["survey", "50% year", "years remaining", "row"], b_rows)}
{table(["step", "calendar years", "change in years remaining", "excess pull-in per year"], step_rows)}
<p>Manifold market, "AGI created and publicly announced before 2030", for context only (a market price, not a survey):</p>
{table(["date", "probability", "row"], mani_rows)}
</details>

<h3 id="leg-c">Leg C. Is AI doing the improving?</h3>
<p>The definition wants the share of inputs to frontier AI progress supplied by AI. Nobody outside the labs can measure that, so what exists is self-report. Two kinds are recorded: a company's share of all new code written by AI, which is a proxy at best and is shown but not scored, and Anthropic's self-measured share of its own AI research work that its model "leads", which is closer to the definition's measure but is judged by the model itself and is the figure scored. The figures do not measure the same thing and should not be compared with each other.</p>
<figure class="fig"><img src="leg-c-self-reports.png" alt="Bar chart of company self-reported shares of AI-done work, with the one-half threshold marked">
<figcaption>Every bar is a company statement about itself. Anthropic's row for February 2026 is "under 1%", recorded as 1. Its "above 90%" row is recorded as 90.</figcaption></figure>
<details><summary>The self-reports</summary>
{table(["date", "measure", "value", "row"], c_rows)}
</details>

<h3 id="leg-d">Leg D. Has the economy changed mode?</h3>
<p>Robin Hanson's reading of the long record is that the world economy has had three growth modes, hunting, farming and industry, each doubling output about a hundred times faster than the one before: roughly 230,000 years, 860 years and 15 years per doubling. A new mode would double output in years or less. Leg D asks whether that has started, using world real output growth from the World Bank. The threshold, 30 percent a year, is Tom Davidson's published line for "explosive growth" (Open Philanthropy, 2021), chosen so the number is not this project's own invention: far above anything in the modern record, well short of Hanson's "days, not years". This leg is measured by people outside the AI field, which is why it is in the definition; the cost is that output lags capability by years, so it will usually be the weakest leg.</p>
<figure class="fig"><img src="leg-d-world-growth.png" alt="World output growth by year since 1961, with the 30 percent threshold line far above the series">
<figcaption>Annual readings; the series is revised as countries revise their accounts, and a revision that pulls a year back below the line resets the persistence count. Doubling times in <a href="leg-d-world-growth.csv">leg-d-world-growth.csv</a>.</figcaption></figure>
<details><summary>Every year ({len(d_pts)} readings)</summary>
{table(["year", "growth", "doubling time (years)", "row"], d_rows)}
</details>

<h3 id="owed">What the definition still owes</h3>
<ol>
<li><b>The backward test.</b> Run on 1995 to 2019 the definition must return "not entered", with the internet years firing only leg B and the deep-learning years firing only leg A. The leg A series starts in 2019 and leg C in 2026, so the test cannot run yet. The definition was adopted without it, with this gap stated here; if the test later fires on those years, the thresholds are amended in the open.</li>
<li><b>The leg B ledger.</b> Old forecasts of the anchor measure (starting from the 2016 expert survey's milestone dates) scored against what happened, by lead time. Until it exists, leg B is unmeasured.</li>
<li><b>A second source for leg C</b> that is not a company's report on itself.</li>
</ol>
</section>

<section class="section prose" id="method">
<h2>Method and data</h2>
<p>Belief measures and world measures live in separate files and are never combined. <a href="/data/statements.csv">statements.csv</a>, <a href="/data/aggregates.csv">aggregates.csv</a> and the <a href="/data/">community samples</a> hold what people said and believed. <a href="/data/world_measures.csv">world_measures.csv</a> holds capability readings, company self-reports and world output, with the same columns and the same rule that every row carries its source and the question wording. Every search that produced a row is in <a href="/data/search_log.csv">search_log.csv</a>. The <a href="/docs/methodology-v2">method</a>, the <a href="/docs/codebook">codebook</a>, the <a href="/docs/singularity-entry-definition">definition</a> and every <a href="/docs/amendments">dated change</a> are published here; the scripts that rebuild this page from the data are in the source repository.</p>
<p class="cite">Cite as: Fredrickson, J. (2026). <em>AGI Zeitgeist Tracker</em> [dataset]. Version of {built}, commit {esc(commit)}. {SITE_URL}. Data under <a href="/data/LICENSE-DATA.txt">CC BY 4.0</a>; scripts under MIT. Figures are static images; the CSV beside each one holds the plotted numbers. Thresholds frozen {sc['adopted']} in <a href="/docs/singularity-entry-definition#record-of-the-rulings-2026-10-08">amendment A19</a>.</p>
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
    built = date.today().isoformat()
    (SITE / "index.html").write_text(build_html(a_pts, a_series, b_pts, b_steps, mani, c_pts, d_pts, sc, built, git_commit()), encoding="utf-8")
    (SITE / "status.json").write_text(json.dumps({
        "built": built, "status": sc["status"], "progress": round(sc["progress"], 3),
        "progress_is_upper_bound": sc["progress_is_upper_bound"], "bottleneck": sc["bottleneck"],
        "gauges": {k: (round(sc[k]["gauge"], 3) if sc[k].get("measurable") else None) for k in "ABCD"},
        "unmeasured": sc["unmeasured"], "definition": f"{SITE_URL}/docs/singularity-entry-definition.html"}, indent=2), encoding="utf-8")
    n_docs = render_docs(built, git_commit())
    n_data = copy_data()
    print(f"site/index.html built: {len(a_pts)} time-horizon readings, {len(a_series)} doubling-time windows, "
          f"{len(b_pts)} survey points, {len(c_pts)} self-reports, {len(d_pts)} years of world growth; "
          f"status {sc['status']!r}, progress {'<= ' if sc['progress_is_upper_bound'] else ''}{sc['progress']:.2f} "
          f"(A {sc['A']['gauge']:.2f}, B none, C {sc['C']['gauge']:.2f}, D {sc['D']['gauge']:.2f}); {n_docs} docs rendered, {n_data} data files copied")


if __name__ == "__main__":
    main()
