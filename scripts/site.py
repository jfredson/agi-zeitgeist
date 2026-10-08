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
# Writing rule (John, 2026-10-08; design standard section 1a): the public pages use none of the
# project's internal language and build every idea from scratch, assuming only what a five-year-old
# knows plus what the page has already said. The working documents are published as written, each
# with a preface saying what it is; the plain account lives on the home page.
# The page shell follows the Sentient Horizons design standard (sentient-horizons/design/README.md):
# shared stylesheet site/deep-field.css (copied unchanged, version in its header), the top bar with
# two tiers and the theme toggle, the cosmic backdrop on the home page only, and the five-line
# footer ending "A Sentient Horizons project." with the attribution line "© year John Fredrickson. provenance. licence."
# (No "with Claude" in the line: John, 2026-10-08. Who did the sorting is said in the method section instead.)
SITE_NAME = "AGI Zeitgeist"
SITE_TITLE = "AGI Zeitgeist Tracker"
TAGLINE = ("A dated record of what people expect from artificial general intelligence, with every quote linked to its source, "
           "and a test of whether the singularity has begun.")
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
/* the landing hero: the answer on the left, the four conditions beneath it, the experts' dates on the right.
   Type roles follow The Belt Equation's hero: sans for the answer and claims, mono with tabular figures for
   numbers, serif only for the explanatory line. */
.land { display: grid; grid-template-columns: minmax(0, 1fr) 400px; gap: 48px; align-items: start; padding: 48px 0 24px; }
.land .eyebrow { margin-bottom: 18px; }
.land .answer { font-family: var(--sans); font-size: clamp(72px, 10.5vw, 128px); line-height: 0.92; font-weight: 600; letter-spacing: -0.04em; color: var(--text); margin: 0 0 22px; }
.land h1 { font-family: var(--sans); font-size: clamp(22px, 2.5vw, 31px); line-height: 1.2; font-weight: 500; letter-spacing: -0.015em; margin: 0 0 12px; max-width: 640px; }
.land .lede { font-style: normal; font-size: 17px; line-height: 1.5; color: var(--muted); margin: 0 0 24px; max-width: 600px; }
.land .kicker { margin: 0 0 12px; }
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
<p class="footer-meta">© {year} John Fredrickson. {provenance(built, commit)} Free to reuse with credit (<a href="https://creativecommons.org/licenses/by/4.0/" rel="license">CC BY 4.0</a>); code under the MIT licence.</p>
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
        preface = ('<div class="status"><strong>A working document.</strong> This is one of the documents the site is built from, published as it is written, in the project\'s own terms, '
                   'for anyone checking the work. It assumes the reader knows the method. The plain account of the same material is on the <a href="/">home page</a>.</div>')
        page = shell(f"{title} | {SITE_TITLE}", f"{title}: a document of the {SITE_TITLE}.", f'{preface}<div class="prose narrow document">{body}{note}</div>',
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
    body = (f'<div class="prose narrow"><p>Every table behind the site, as it stood when the site was last built. Each row carries a link to where its number came from. '
            f'Free to reuse with credit (<a href="LICENSE-DATA.txt">the licence</a>); how to cite is on the <a href="/#method">home page</a>. What each file holds is explained in <a href="/docs/README">a working document</a>.</p><ul>{items}</ul></div>')
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
    latest = {}
    for r in read("statements.csv"):
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


def landing(sc, b_pts, mani, aggregates, built, commit):
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
    latest = b_pts[-1]
    med, lo, hi, ex_rows = expert_dates()
    hlmi10 = next((int(float(r["value"])) for r in aggregates if r["aggregate_id"] == f"aiimpacts-{latest['date'].year}-hlmi10"), "")
    faol = next((int(float(r["value"])) for r in aggregates if r["aggregate_id"] == f"aiimpacts-{latest['date'].year}-faol50"), "")
    m = mani[-1] if mani else None
    market = (f' People betting on Manifold put the odds of AGI before 2030 at <a href="{esc(market_page(m["source_url"]))}">{float(m["value"])*100:.0f}%</a>.' if m else "")
    return f"""<section class="land">
<div>
<p class="eyebrow">Are we in the singularity?</p>
<p class="answer">{answer}</p>
<h1>Four things would all have to be true, and stay true for a year. Today none of them is.</h1>
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
<p class="use"><a href="/data/">Download every table</a> (free to reuse with credit) · <a href="#method">How to cite</a> · <a href="/docs/README">What each file holds</a> · version {esc(commit)}</p>
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

    body = f"""{landing(sc, b_pts, mani, _AGG, built, commit)}
<div class="with-rail"><div>
<section class="section prose" id="belief">
<h2>The current zeitgeist</h2>
<p>"Zeitgeist" is a German word for the mood of a time: what people are saying and what they expect. This part of the site records what well-known experts, surveys of researchers, opinion polls, betting markets and online forums have said since 2005 about AGI. Every quote carries its date and a link to where it was said.</p>
<p>Has the argument moved: from <em>whether</em> such a machine can be built, to <em>when</em> it will arrive, to <em>whether today's machines are nearly there</em>? Four things stand out so far.</p>
<p>First, the doubters have moved. Geoffrey Hinton, a computer scientist whose work underlies today's AI, said "no sooner than 2070" in 2015 and "between five and 20 years" in 2025. Gary Marcus, a psychologist and the best-known critic of today's AI, said "at least thirty or fifty years" in 2016 and "10-25 years" in 2025. Ray Kurzweil has said 2029 the whole time. This is where the "about 2030" at the top of the page comes from.</p>

<figure class="fig"><img src="zeitgeist-experts.png" alt="Each of five experts' earliest and latest guess at when machines will match people at most thinking work">
<figcaption>Only guesses in the person's own words are shown, not a reporter's summary of them. Every guess, with its quote and a link to where it was said, is in <a href="/data/statements.csv">a table</a>.</figcaption></figure>

<p>Second, AI researchers have moved too, more slowly, and how far depends on the question. In the largest repeated survey of researchers, the year they give an even chance that machines could do every task better and more cheaply than people came 14 years closer between 2016 and 2023, to 2047. Asked when machines could do every job that way, they say 2116.</p>

<figure class="fig"><img src="zeitgeist-researchers.png" alt="AI researchers' even-chance year for machines doing every task and every job, in surveys from 2016, 2022 and 2023">
<figcaption>Two different groups of researchers answered the two questions in each survey. The numbers are in <a href="/data/aggregates.csv">a table</a>.</figcaption></figure>

<p>Third, ordinary people have started paying attention. Google searches for artificial general intelligence were flat for fifteen years and have climbed steeply since 2023, and in polls since 2023 about half of American adults say they are more concerned than excited about the growing use of AI in daily life.</p>

<figure class="fig"><img src="zeitgeist-search.png" alt="Worldwide Google searches for artificial general intelligence and for the singularity, each year from 2005 to 2026">
<figcaption>Google reports searches on its own scale rather than as counts. The numbers, and the polls, are in <a href="/data/aggregates.csv">a table</a>.</figcaption></figure>

<p>Fourth, almost no one says the machine has arrived, not even on r/singularity, a forum on the website Reddit for people who expect it.</p>

<figure class="fig"><img src="zeitgeist-forum.png" alt="The most popular posts on the r/singularity forum every three months from late 2024 to 2026, by what each mainly says">
<figcaption>One forum, not the public. The numbers are in <a href="vanguard-pilot-r-singularity.csv">a table</a>.</figcaption></figure>

<p>So far this rests on five well-known people (Ray Kurzweil, Geoffrey Hinton, Yann LeCun, Gary Marcus and Sam Altman), three surveys of AI researchers, opinion polls, betting markets and one online forum. More people and sources are being added.</p>
<p>Expecting it soon is not the same as it happening. Whether the singularity has actually begun is the test below.</p>
</section>

<section class="section prose" id="singularity">
<h2>Are we in the singularity?</h2>
<p>The answer at the top of the page comes from a test with four parts. The singularity has been described in three classic ways: machines getting better faster and faster, machines doing the work of making machines better, and change so fast that nobody can predict what comes next. Each alone gives false alarms. A fast decade in any industry looks like the first; a company's claim that its AI does its own research cannot be checked from outside; and every new technology makes old forecasts look foolish, the internet included. So the test asks for all three at once, plus a fourth that people outside the AI world measure: whether the world's economy has changed gear. Each part has a line where it would count, fixed before anyone looked at the numbers. The full rules are in <a href="/docs/singularity-entry-definition">a working document</a>.</p>

<h3 id="leg-a">A. Is AI getting better faster and faster?</h3>
<p><em>The idea, from the inventor Ray Kurzweil: AI gets better faster and faster, so the time it takes to double is itself shrinking.</em></p>
<p>The measure is how long a job the best AI can finish on its own. METR, a research group that tests AI systems, gives each new system computer-programming jobs of known length, from seconds to days of a skilled person's time, and finds the longest it gets right half the time. Most tests of AI are maxed out within a year or two; this one keeps rising, which is why it was chosen. That length has been doubling every few months. Steady doubling is fast, but it is not a singularity: for this part to count, the doubling itself has to keep getting quicker, down to {A['t_star']:.0f} days. Over the year to {A['date'].strftime('%B %Y')} it took {A['reading']:.0f} days; in {sc['reference_year']} it took {A['t_ref']:.0f}. The rules also ask for it to have got quicker two readings in a row, which today it {"has" if A['falling'] else "has not"}.</p>
<figure class="fig"><img src="leg-a-time-horizon.png" alt="The longest programming job each AI system gets right half the time, from 2019 to 2026, and how many days that length took to double">
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
<p>Nobody outside the AI companies can measure how much of the work of improving AI is now done by AI, so what exists is what the companies say about themselves. Anthropic, which makes the Claude AI systems, reports what share of its AI research work its own AI leads, as judged by that AI. That is the figure scored, and it would count at half. Google says about three-quarters of its new computer code is written by AI, but that covers all its code, not its research, so it is not scored. Anthropic also says its AI takes part in more than 90% of its research work, a lower bar than leading it.</p>
<figure class="fig"><img src="leg-c-self-reports.png" alt="The share of Anthropic's AI research work led by its own AI: under 1% in February 2026 and 26% in August 2026, against a line at one half">
<figcaption>Anthropic gave its February figure as "under 1%". Every statement, including Google's, is in the table below.</figcaption></figure>
<details><summary>What the companies said</summary>
{table(["date", "what was measured", "figure", "source"], c_rows)}
</details>

<h3 id="leg-d">D. Has the economy changed gear?</h3>
<p><em>The idea, from the economist Robin Hanson: each new era of history has made the world's economy double about a hundred times faster than the one before.</em></p>
<p>The economist Robin Hanson looked at the whole history of the world's economy and found three eras: hunting, farming and industry. In each, the amount the world produces doubled about a hundred times faster than in the era before: every 230,000 years, then every 860 years, then every 15 years. A fourth era would double it in a few years or less. This part asks whether that has started, using the World Bank's yearly count of everything the world produces. In {D['year']} it grew {D['reading']:.1f} percent, a pace that doubles it every {D['doubling']:.0f} years; since 1961 it has averaged {D['g_ref']:.1f} percent. The line, 30 percent in a year, would double it every {D['t_star']:.1f} years. It comes from a 2021 report by Tom Davidson for the research funder Open Philanthropy, not from this project, and it is far above the best year since 1961, {max(q['growth'] for q in d_pts):.1f} percent. This is the one part measured by people outside the AI world, which is why it is in the test; the cost is that the economy reacts years after the technology, so it will usually be the furthest behind.</p>
<figure class="fig"><img src="leg-d-world-growth.png" alt="Growth of the world's economy each year since 1961, between about minus 3 and 7 percent, with the line at 30 percent far above">
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
<p>The searching and the sorting of statements were done by Claude, an AI model made by Anthropic, following those written rules; every rule, and every finishing line of the test, was decided by John Fredrickson. The forum posts were sorted by three AI systems from three companies with no person checking them, and systems from different companies can still share blind spots.</p>
<p class="cite">Cite as: Fredrickson, J. (2026). <em>AGI Zeitgeist Tracker</em> [dataset]. Version of {built}, commit {esc(commit)}. {SITE_URL}. Data under <a href="/data/LICENSE-DATA.txt">CC BY 4.0</a>; scripts under MIT. The charts are pictures; the table linked beside each one holds the numbers drawn. The test's finishing lines were fixed on {long_date(sc['adopted'])}; <a href="/docs/singularity-entry-definition#record-of-the-rulings-2026-10-08">the record of that decision</a>.</p>
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
    globals()["_AGG"] = aggregates
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
