#!/usr/bin/env python3
"""Build the static site (site/index.html, its figures, the rendered docs and the data copies) from data/*.csv.

The page has two halves that are deliberately kept apart:

- what people believe (the tracker proper: statements, surveys, markets, communities);
- what the world is doing (data/world_measures.csv), shown under the draft definition
  of "entering the singularity" in docs/singularity-entry-definition-draft-2026-10-07.md.

The definition was adopted on 2026-10-08 (amendment A17) with four legs, and its frozen
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


# ----------------------------------------------------------------------------- docs and data
DOC_CSS = """
body { margin: 0; background: #fbfbfa; color: #1f2933; font: 16px/1.55 -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; }
@media (prefers-color-scheme: dark) { body { background: #14181d; color: #e6e9ed; } a { color: #6fa8ea; } th, td { border-color: #2b323a; } code, pre { background: #1b2026; border-color: #2b323a; } }
main { max-width: 820px; margin: 0 auto; padding: 24px 16px 64px; }
a { color: #2a78d6; } p, li { max-width: 75ch; }
table { border-collapse: collapse; font-size: 0.9rem; display: block; overflow-x: auto; }
th, td { text-align: left; padding: 5px 8px; border-bottom: 1px solid #e3e8ee; vertical-align: top; }
code, pre { background: #fff; border: 1px solid #e3e8ee; border-radius: 3px; font-size: 0.9em; }
pre { padding: 8px; overflow-x: auto; } code { padding: 0 3px; } pre code { border: 0; padding: 0; }
nav.top { font-size: 0.9rem; margin-bottom: 20px; } nav.top a { margin-right: 14px; }
h1 { line-height: 1.2; }
"""


def render_docs():
    """Render every Markdown document to site/docs/ with pandoc, rewriting links between them."""
    out_root = SITE / "docs"
    if out_root.exists():
        shutil.rmtree(out_root)
    out_root.mkdir()
    (out_root / "doc.css").write_text(DOC_CSS, encoding="utf-8")
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
        # links between documents: .md -> .html; repo-root paths -> site paths
        body = re.sub(r'href="([^"#]*?)\.md(#[^"]*)?"', lambda m: f'href="{m.group(1)}.html{m.group(2) or ""}"', body)
        body = re.sub(r'href="(?:\.\./)*docs/', f'href="{up}', body)
        body = re.sub(r'href="(?:\.\./)*data/', f'href="{up}../data/', body)
        body = re.sub(r'href="(?:\.\./)*site/', f'href="{up}../', body)
        body = re.sub(r'src="(?:\.\./)*site/', f'src="{up}../', body)
        body = re.sub(r'href="(?:\.\./)*scripts/([^"]+)"', lambda m: f'href="{REPO}/blob/main/scripts/{m.group(1)}"', body)
        body = re.sub(r'href="LICENSE(-DATA)?"', lambda m: f'href="{up}../data/LICENSE{m.group(1) or ""}.txt"', body)
        title = re.search(r"<h1[^>]*>(.*?)</h1>", body, re.S)
        title = re.sub("<[^>]+>", "", title.group(1)) if title else rel.stem
        page = f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)} | AGI Zeitgeist Tracker</title><link rel="stylesheet" href="{up}doc.css"></head><body><main>
<nav class="top"><a href="{up}../">AGI Zeitgeist Tracker</a> <a href="{up}README.html">About the data</a> <a href="{up}methodology-v2.html">Method</a> <a href="{up}singularity-entry-definition.html">Singularity definition</a> <a href="{up}amendments.html">Changes</a></nav>
{body}
<p style="color:#6b7785;font-size:0.85rem;margin-top:40px">Rendered from <code>{esc(str(src.relative_to(ROOT)))}</code>. Data CC BY 4.0, scripts MIT.</p>
</main></body></html>"""
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
    n = 0
    for src in sorted(DATA.rglob("*.csv")):
        dst = out / src.relative_to(DATA)
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)
        n += 1
    for lic in ("LICENSE-DATA", "LICENSE"):
        shutil.copy2(ROOT / lic, out / (lic + ".txt"))
    return n


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


def gauge_bar(g):
    if g is None:
        return '<div class="bar none"><span>not yet measurable</span></div>'
    return f'<div class="bar"><i style="width:{g*100:.0f}%"></i><span>{g:.2f}</span></div>'


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

    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>AGI Zeitgeist Tracker</title>
<meta name="description" content="A dated, sourced record of how opinion about artificial general intelligence has moved since 2005, and a preregistered four-part test for whether the world has entered the singularity, scored from public data.">
<link rel="canonical" href="{SITE_URL}/">
<style>
:root {{
  --bg: #fbfbfa; --card: #ffffff; --ink: #1f2933; --muted: #6b7785; --line: #e3e8ee; --accent: #2a78d6; --fill: #2a78d6;
  --warn-bg: #fff6e0; --warn-ink: #6b4b00; --warn-line: #eda100;
}}
@media (prefers-color-scheme: dark) {{
  :root:not([data-theme="light"]) {{
    --bg: #14181d; --card: #1b2026; --ink: #e6e9ed; --muted: #98a2ae; --line: #2b323a; --accent: #6fa8ea; --fill: #6fa8ea;
    --warn-bg: #2a2410; --warn-ink: #f0d58a; --warn-line: #c98a00;
  }}
}}
:root[data-theme="dark"] {{
  --bg: #14181d; --card: #1b2026; --ink: #e6e9ed; --muted: #98a2ae; --line: #2b323a; --accent: #6fa8ea; --fill: #6fa8ea;
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
nav.top {{ font-size: 0.9rem; color: var(--muted); margin: 0 0 18px; }} nav.top a {{ margin-right: 14px; }}
.sub {{ color: var(--muted); margin: 0 0 16px; }}
.status {{ background: var(--warn-bg); color: var(--warn-ink); border-left: 4px solid var(--warn-line); padding: 12px 14px; border-radius: 6px; margin: 20px 0; }}
.status strong {{ display: block; margin-bottom: 2px; font-size: 1.1rem; }}
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
.bar {{ position: relative; height: 22px; background: var(--line); border-radius: 4px; margin: 8px 0 4px; overflow: hidden; }}
.bar i {{ position: absolute; left: 0; top: 0; bottom: 0; background: var(--fill); }}
.bar span {{ position: absolute; left: 8px; top: 0; line-height: 22px; font-size: 0.8rem; font-weight: 600; color: var(--ink); mix-blend-mode: difference; filter: invert(1) grayscale(1) contrast(9); }}
.bar.none span {{ mix-blend-mode: normal; filter: none; color: var(--muted); font-weight: 400; }}
footer {{ color: var(--muted); font-size: 0.85rem; margin-top: 48px; border-top: 1px solid var(--line); padding-top: 12px; }}
code {{ font-size: 0.9em; background: var(--card); border: 1px solid var(--line); padding: 0 4px; border-radius: 3px; }}
</style>
</head>
<body>
<main>
<nav class="top"><a href="#belief">What people believe</a> <a href="#singularity">Singularity status</a> <a href="#method">Method and data</a> <a href="docs/README.html">About the data</a> <a href="docs/amendments.html">Changes</a></nav>
<h1>AGI Zeitgeist Tracker</h1>
<p class="sub">The spirit of the age about artificial general intelligence, as a dated and sourced record since 2005, beside a preregistered test of whether the world has entered the singularity. Every number on this page links to the row it came from.</p>

<p>AGI here means AI that can do most intellectual work a person can. The working question: did the main public argument move from <em>whether</em> it is possible, to <em>when</em> it arrives, to <em>whether today's systems are already close or improving themselves</em>? The method is built so the data can say no. The seed phase is complete and the expert panel is frozen; the full panel traces and the public streams have not started.</p>

<div class="status"><strong>Singularity entry status: {status_line}</strong>
Scored on {built} under the definition adopted {sc['adopted']}, with its thresholds frozen before any gauge was published. Progress toward the mark is <b>{progress_word}{sc['progress']:.2f}</b> on a scale of 0 to 1, set by the weakest leg ({sc['bottleneck']}). Leg B cannot be scored until its forecast ledger exists, so the number is an upper bound. Entry requires all four gauges at 1 for {sc['persistence']} consecutive quarters.</div>

<h2 id="belief">What people believe</h2>
<p>The tracker proper. One row per public statement, survey result, market reading or poll, coded under <a href="docs/methodology-v2.html">methodology version 2</a>.</p>

<figure><img src="chart-1-frames.png" alt="Share of coded statements by primary frame, by year, seed panel of five people">
<figcaption>Seed phase: what each statement was mainly about, by year, for five traced people (Kurzweil, Hinton, LeCun, Marcus, Altman). Counts in <a href="chart-1-frames.csv">chart-1-frames.csv</a>. Five people are not a panel; this chart exists to test the pipeline.</figcaption></figure>

<figure><img src="vanguard-pilot-r-singularity.png" alt="Framing in sampled high-score posts from r/singularity, 2024Q4 to 2026Q3, model-coded">
<figcaption>Pilot, model-coded: framing in sampled high-score posts from r/singularity, 2024Q4 to 2026Q3. Not representative of participants or the public. Three models from different companies (Claude, Gemini and GPT) each coded all 390 sampled posts blind under the final codebook, and the majority vote is the final code; where no two agree, the post is left out of the affected measure. Counts in <a href="vanguard-pilot-r-singularity.csv">vanguard-pilot-r-singularity.csv</a>; <a href="docs/vanguard/pilot-report-r-singularity-2026-10.html">pilot report</a>.</figcaption></figure>

<h2 id="singularity">Entering the singularity: the test and the score</h2>
<p>"Any prediction made now about the next five years will look stupid in retrospect" is one of the standard definitions of the singularity, and each definition alone has a known false alarm. The <a href="docs/singularity-entry-definition.html">adopted definition</a> requires four things to be true at once, for four consecutive quarters. Each gauge runs from 0 (the {sc['reference_year']} reference) to 1 (the frozen threshold); the smallest gauge is the honest distance remaining.</p>

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

<h3>Leg A. How long a task the best AI can finish</h3>
<p>The anchor measure is METR's time horizon: the length of software task, in minutes an expert needs for it, that a model finishes half the time. It is chosen because it has not yet saturated the way benchmarks do. The lower panel is the definition's quantity: the doubling time of the frontier over a trailing twelve months. A flat line would mean steady exponential growth, which is Kurzweil's world but not yet a singularity; a falling line is the signature the definition looks for. The gauge is scored on the last window with no reading past 16 hours, and the threshold also requires the doubling time to have fallen over the last two windows ({"met" if A['falling'] else "not met"} today).</p>
<figure><img src="leg-a-time-horizon.png" alt="METR 50% time horizon by model release date on a log scale, with the trailing twelve-month doubling time of the frontier below">
<figcaption>Hollow points were not the frontier at release. METR treats estimates past 16 hours as beyond its task suite's reliable range, and its own doubling-time fit excludes them; windows that include such a reading are hollow in the lower panel and are not scored. The latest frontier reading is {esc(latest['name'])} at {latest['value']/60:.0f} hours on {latest['date'].isoformat()}. Doubling-time series in <a href="leg-a-doubling-time.csv">leg-a-doubling-time.csv</a>.</figcaption></figure>
<details><summary>Every reading ({len(a_pts)} models) and every doubling-time window</summary>
{table(["release", "model", "50% horizon", "95% range", "frontier", "", "row"], a_rows)}
{table(["window end", "days per doubling", "frontier points", "includes a reading past 16 h"], dt_rows)}
</details>

<h3>Leg B. Are forecasts holding up?</h3>
<p>The real test scores old forecasts of the measure above against simple trend extrapolation and asks how far ahead they still win. That ledger does not exist yet and can only be scored once the forecast period has passed, so leg B is shown as not yet measurable and the progress number above is an upper bound. The stand-in, available now, is the expert consensus date for human-level AI. If forecasters had the trend right, the date would stand still and the years remaining would fall by one each year, the dashed line. Instead the three AI Impacts surveys show the remaining distance collapsing: the step from 2022 to 2023 removed about {abs(last_step['change']):.0f} years of distance in {last_step['years']:.1f} calendar years. That is forecasts failing in the slow direction, which is the direction the definition records.</p>
<figure><img src="leg-b-pull-in.png" alt="Years remaining until the surveyed 50% date for human-level AI, by survey year, against a one-year-per-year reference line">
<figcaption>Surveys use different definitions and aggregation, so the 2013 survey is shown but not joined to the series. Steps in <a href="leg-b-pull-in.csv">leg-b-pull-in.csv</a>.</figcaption></figure>
<details><summary>The survey readings, the steps between them, and the market reading for context</summary>
{table(["survey", "50% year", "years remaining", "row"], b_rows)}
{table(["step", "calendar years", "change in years remaining", "excess pull-in per year"], step_rows)}
<p>Manifold market, "AGI created and publicly announced before 2030", for context only (a market price, not a survey):</p>
{table(["date", "probability", "row"], mani_rows)}
</details>

<h3>Leg C. Is AI doing the improving?</h3>
<p>The definition wants the share of inputs to frontier AI progress supplied by AI. Nobody outside the labs can measure that, so what exists is self-report. Two kinds are recorded: a company's share of all new code written by AI, which is a proxy at best and is shown but not scored, and Anthropic's self-measured share of its own AI research work that its model "leads", which is closer to the definition's measure but is judged by the model itself and is the figure scored. The figures do not measure the same thing and should not be compared with each other.</p>
<figure><img src="leg-c-self-reports.png" alt="Bar chart of company self-reported shares of AI-done work, with the one-half threshold marked">
<figcaption>Every bar is a company statement about itself. Anthropic's row for February 2026 is "under 1%", recorded as 1. Its "above 90%" row is recorded as 90.</figcaption></figure>
<details><summary>The self-reports</summary>
{table(["date", "measure", "value", "row"], c_rows)}
</details>

<h3>Leg D. Has the economy changed mode?</h3>
<p>Robin Hanson's reading of the long record is that the world economy has had three growth modes, hunting, farming and industry, each doubling output about a hundred times faster than the one before: roughly 230,000 years, 860 years and 15 years per doubling. A new mode would double output in years or less. Leg D asks whether that has started, using world real output growth from the World Bank. The threshold, 30 percent a year, is Tom Davidson's published line for "explosive growth" (Open Philanthropy, 2021), chosen so the number is not this project's own invention: far above anything in the modern record, well short of Hanson's "days, not years". This leg is measured by people outside the AI field, which is why it is in the definition; the cost is that output lags capability by years, so it will usually be the weakest leg.</p>
<figure><img src="leg-d-world-growth.png" alt="World output growth by year since 1961, with the 30 percent threshold line far above the series">
<figcaption>Annual readings; the series is revised as countries revise their accounts, and a revision that pulls a year back below the line resets the persistence count. Doubling times in <a href="leg-d-world-growth.csv">leg-d-world-growth.csv</a>.</figcaption></figure>
<details><summary>Every year ({len(d_pts)} readings)</summary>
{table(["year", "growth", "doubling time (years)", "row"], d_rows)}
</details>

<h3>What the definition still owes</h3>
<ol>
<li><b>The backward test.</b> Run on 1995 to 2019 the definition must return "not entered", with the internet years firing only leg B and the deep-learning years firing only leg A. The leg A series starts in 2019 and leg C in 2026, so the test cannot run yet. The definition was adopted without it, with this gap stated here; if the test later fires on those years, the thresholds are amended in the open.</li>
<li><b>The leg B ledger.</b> Old forecasts of the anchor measure (starting from the 2016 expert survey's milestone dates) scored against what happened, by lead time. Until it exists, leg B is unmeasured.</li>
<li><b>A second source for leg C</b> that is not a company's report on itself.</li>
</ol>

<h2 id="method">Method and data</h2>
<p>Belief measures and world measures live in separate files and are never combined. <a href="data/statements.csv">statements.csv</a>, <a href="data/aggregates.csv">aggregates.csv</a> and the <a href="data/vanguard/">community samples</a> hold what people said and believed. <a href="data/world_measures.csv">world_measures.csv</a> holds capability readings, company self-reports and world output, with the same columns and the same rule that every row carries its source and the question wording. Every search that produced a row is in <a href="data/search_log.csv">search_log.csv</a>. The <a href="docs/methodology-v2.html">method</a>, the <a href="docs/codebook.html">codebook</a>, the <a href="docs/singularity-entry-definition.html">definition</a> and every <a href="docs/amendments.html">dated change</a> are published here; the scripts that rebuild this page from the data are in the source repository.</p>
<p>Cite as: Fredrickson, J. (2026). <em>AGI Zeitgeist Tracker</em> [dataset]. Version of {built}, commit {esc(commit)}. {SITE_URL}. Data under <a href="data/LICENSE-DATA.txt">CC BY 4.0</a>; scripts under MIT.</p>

<footer>Built {built} from commit {esc(commit)}. Figures are static images; the CSV beside each one holds the plotted numbers. Thresholds frozen {sc['adopted']} in <a href="docs/singularity-entry-definition.html#record-of-the-rulings-2026-10-08">amendment A17</a>.</footer>
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
    d_pts = leg_d(world)
    sc = score(load_thresholds(), a_series, c_pts, d_pts)
    built = date.today().isoformat()
    (SITE / "index.html").write_text(build_html(a_pts, a_series, b_pts, b_steps, mani, c_pts, d_pts, sc, built, git_commit()), encoding="utf-8")
    (SITE / "status.json").write_text(json.dumps({
        "built": built, "status": sc["status"], "progress": round(sc["progress"], 3),
        "progress_is_upper_bound": sc["progress_is_upper_bound"], "bottleneck": sc["bottleneck"],
        "gauges": {k: (round(sc[k]["gauge"], 3) if sc[k].get("measurable") else None) for k in "ABCD"},
        "unmeasured": sc["unmeasured"], "definition": f"{SITE_URL}/docs/singularity-entry-definition.html"}, indent=2), encoding="utf-8")
    n_docs = render_docs()
    n_data = copy_data()
    print(f"site/index.html built: {len(a_pts)} time-horizon readings, {len(a_series)} doubling-time windows, "
          f"{len(b_pts)} survey points, {len(c_pts)} self-reports, {len(d_pts)} years of world growth; "
          f"status {sc['status']!r}, progress {'<= ' if sc['progress_is_upper_bound'] else ''}{sc['progress']:.2f} "
          f"(A {sc['A']['gauge']:.2f}, B none, C {sc['C']['gauge']:.2f}, D {sc['D']['gauge']:.2f}); {n_docs} docs rendered, {n_data} data files copied")


if __name__ == "__main__":
    main()
