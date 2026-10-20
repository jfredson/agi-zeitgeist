#!/usr/bin/env python3
"""Draw the charts for "The current zeitgeist" from data/*.csv into site/.

Four charts, one point each, in the order the section tells it:
  zeitgeist-experts.png      the doubters' dates have come decades closer; Kurzweil's has not moved
  zeitgeist-researchers.png  researchers' year for "every task" against "every job", survey by survey
  zeitgeist-search.png       searches for AGI were flat for fifteen years, then climbed
  zeitgeist-forum.png        almost no popular r/singularity post says AGI has arrived

    .venv/bin/python scripts/charts.py
"""

import sys
from pathlib import Path

from matplotlib.patches import Rectangle

sys.path.insert(0, str(Path(__file__).resolve().parent))
from chart_style import GRID, INK, INK_2, PALETTE, PANEL_TIERS, PEOPLE, SURFACE, figure, measured, read, save, titles  # noqa: E402
import chart_style as cs  # noqa: E402

# Each person's earliest and latest guess at when machines will match people at most thinking work
# (target_capability broad_competence), chosen by hand from the quotes so the choice can be checked.
# One rule for both points: the person's own words, not a reporter's or organiser's summary (that
# leaves out Altman's 2023 and August 2026 dates and Marcus's 2026 "at least a decade"). A floor
# ("no sooner than") or a ceiling ("within ten years") counts and is labelled as one.
EXPERT_POINTS = [
    ("kurzweil", "kurzweil-2006-02", "kurzweil-2026-01"),
    ("altman", "altman-2024-02", "altman-2026-02"),
    ("lecun", "lecun-2024-07", "lecun-2025-05"),
    ("hinton", "hinton-2015-01", "hinton-2025-03"),
    ("marcus", "marcus-2016-01", "marcus-2025-06"),
]
FLOORS = {"hinton-2015-01", "marcus-2016-01"}   # "no sooner than 2070"; "at least thirty or fifty years"
CEILINGS = {"altman-2024-02", "lecun-2025-05"}  # "by the end of this decade"; "within the next ten years"


def chart_experts():
    by_id = {s["statement_id"]: s for s in measured(read("statements.csv"))}  # tip_only rows never plotted

    def point(sid):
        s = by_id[sid]
        lo = int(s["timeline_year"])
        hi = int(s["timeline_year_high"] or lo)
        words = (f"at least {lo}" if sid in FLOORS else f"by {lo}" if sid in CEILINGS
                 else f"{lo}–{hi}" if hi != lo else f"{lo}")
        return s["date"][:4], lo, hi, (lo + hi) / 2, words

    fig, ax = figure(10, 5.8)
    fig.subplots_adjust(left=0.19, right=0.97, top=0.82, bottom=0.14)
    for i, (pid, first_id, last_id) in enumerate(EXPERT_POINTS):
        name, col = PEOPLE[pid]
        y = len(EXPERT_POINTS) - 1 - i
        fy, _, _, fmid, fwords = point(first_id)
        ly, llo, lhi, lmid, lwords = point(last_id)
        same = fwords == lwords
        ax.plot([fmid, lmid], [y, y], color=col, lw=1.5, alpha=0.5, zorder=2)
        if lhi != llo:
            ax.plot([llo, lhi], [y, y], color=col, lw=8, alpha=0.25, solid_capstyle="round", zorder=1)
        if not same:
            ax.plot(fmid, y, "o", ms=10, mfc=SURFACE, mec=col, mew=2, zorder=4)
            ax.text(fmid, y + 0.2, f"{fwords}, said in {fy}", ha="center", va="bottom", fontsize=8, color=INK_2)
        ax.plot(lmid, y, "o", ms=10, color=col, zorder=5)
        when = f"said in {fy} and still in {ly}" if same else f"said in {ly}"
        ax.text(lmid, y - 0.2, f"{lwords}, {when}", ha="center", va="top", fontsize=8.5, color=col,
                fontweight="bold")
        ax.text(2019.5, y, name, ha="right", va="center", fontsize=10, color=col, fontweight="bold")
    ax.set_xlim(2020, 2076)
    ax.set_ylim(-0.6, len(EXPERT_POINTS) - 0.4)
    ax.set_yticks([])
    ax.set_xticks(range(2025, 2076, 10))
    ax.grid(axis="x", color=GRID, lw=0.8)
    ax.set_axisbelow(True)
    ax.set_xlabel("The year they said machines would match people at most thinking work", fontsize=9, color=INK_2)
    titles(fig, "Hinton's and Marcus's dates have come closer; Kurzweil's has not moved",
           "Each person's earliest dated guess (open circle, label above) and their latest (filled, label below). "
           "A shaded bar is a range.",
           "Guesses in the person's own words only; earliest means the earliest collected so far. "
           "Source: agizeitgeist.com/data")
    return save(fig, "zeitgeist-experts.png")


def chart_researchers():
    rows = {r["aggregate_id"]: r for r in read("aggregates.csv")}
    year = lambda k: int(rows[k]["value"])  # noqa: E731
    TASK, JOB = PALETTE[0], PALETTE[1]
    BG = dict(facecolor=SURFACE, edgecolor="none", pad=1)

    fig, ax = figure(10, 4.6)
    fig.subplots_adjust(left=0.13, right=0.97, top=0.74, bottom=0.17)
    surveys = [("2016", "aiimpacts-2016"), ("2022", "aiimpacts-2022"), ("2023", "aiimpacts-2023")]
    for i, (label, key) in enumerate(surveys):
        y = len(surveys) - i
        t50, j50 = year(f"{key}-hlmi50"), year(f"{key}-faol50")
        ax.plot([t50, j50], [y, y], color=GRID, lw=2, zorder=1, solid_capstyle="round")
        ax.scatter([t50], [y], s=110, color=TASK, zorder=4)
        ax.scatter([j50], [y], s=110, color=JOB, zorder=4)
        ax.text(t50, y - 0.2, str(t50), ha="center", va="top", fontsize=10, fontweight="bold", color=TASK, bbox=BG)
        ax.text(j50, y - 0.2, str(j50), ha="center", va="top", fontsize=10, fontweight="bold", color=JOB, bbox=BG)
        ax.text(2019, y, f"{label} survey", ha="right", va="center", fontsize=10.5, fontweight="bold", color=INK)
    top = len(surveys)
    ax.text(year("aiimpacts-2016-hlmi50"), top + 0.25, "machines could do\nevery task", ha="center",
            va="bottom", fontsize=8.5, color=TASK)
    ax.text(year("aiimpacts-2016-faol50"), top + 0.25, "machines could do\nevery job", ha="center",
            va="bottom", fontsize=8.5, color=JOB)
    ax.axvline(2026, color=INK_2, lw=0.8, ls=(0, (2, 3)), zorder=0)
    ax.text(2026, 0.42, "today", ha="center", va="bottom", fontsize=8, color=INK_2)
    ax.set_xlim(2020, 2172)
    ax.set_ylim(0.4, top + 0.85)
    ax.set_yticks([])
    ax.set_xticks(range(2025, 2171, 25))
    ax.grid(axis="x", color=GRID, lw=0.6)
    ax.set_axisbelow(True)
    n_task, n_job = rows["aiimpacts-2023-hlmi50"]["n"], rows["aiimpacts-2023-faol50"]["n"]
    titles(fig, "AI researchers say 2047 for every task, but 2116 for every job",
           "The year by which researchers, taken together, give an even chance that machines could do it "
           "better and more cheaply than people.",
           f"Source: AI Impacts surveys of researchers who publish at major AI conferences; in 2023, "
           f"{int(n_task):,} answered the task question and {n_job} the job question. agizeitgeist.com/data")
    return save(fig, "zeitgeist-researchers.png")


# AI releases marked on the charts with a time axis, read from data/events.csv by id so the
# dates have one source. Only releases: with 31 events, marking them all would bury the charts.
RELEASES = [("alphago-lee-sedol-2016", "AlphaGo"), ("gpt-2-2019", "GPT-2"), ("gpt-3-2020", "GPT-3"),
            ("chatgpt-2022", "ChatGPT"), ("gpt-4-2023", "GPT-4"), ("deepseek-r1-2025", "DeepSeek-R1"),
            ("gpt-5-2025", "GPT-5")]


def releases(start=None, end=None):
    """[(fractional year, label, iso date)] for the marked releases, optionally within [start, end)."""
    rows = {e["event_id"]: e for e in read("events.csv")}
    out = []
    for eid, label in RELEASES:
        d = rows[eid]["date"]
        y, m = int(d[:4]), int(d[5:7]) if len(d) >= 7 else 7
        day = int(d[8:10]) if len(d) >= 10 else 15
        x = y + (m - 1 + (day - 1) / 31) / 12
        if (start is None or d >= start) and (end is None or d < end):
            out.append((x, label, d))
    return out


def chart_search():
    rows = read("aggregates.csv")

    def series(key):
        return sorted((int(a["date"]), float(a["value"])) for a in rows if key in a["measure"])

    fig, ax = figure(10, 4.8)
    fig.subplots_adjust(left=0.06, right=0.8, top=0.78, bottom=0.12)
    for key, col, label in [("topic 'Artificial general intelligence'", PALETTE[0], "Artificial general\nintelligence"),
                            ("topic 'Technological singularity'", "#8a8780", "The singularity")]:
        data = series(key)
        xs, ys = [d[0] for d in data], [d[1] for d in data]
        ax.plot(xs, ys, color=col, lw=2.5, marker="o", ms=4)
        ax.annotate(label, (xs[-1], ys[-1]), xytext=(10, 0), textcoords="offset points", va="center",
                    fontsize=10, color=col, fontweight="bold")
    marks = releases()
    for i, (x, label, _) in enumerate(marks):
        ax.axvline(x, color=INK_2, lw=0.8, ls=(0, (2, 3)), zorder=0)
        # When the next release is under half a year away, this label goes on the left of its line.
        left = i + 1 < len(marks) and marks[i + 1][0] - x < 0.5
        ax.text(x - 0.12 if left else x + 0.12, 58.5, label, rotation=90, ha="right" if left else "left",
                va="top", fontsize=7.5, color=INK_2)
    ax.set_xlim(2004.5, 2026.5)
    ax.set_ylim(0, 60)
    ax.set_xticks(range(2005, 2027, 3))
    ax.set_yticks([0, 20, 40, 60])
    ax.grid(axis="y", color=GRID, lw=0.8)
    titles(fig, "Around 2023, people started searching for AGI",
           "Worldwide Google searches, average for each year. Google gives no counts: 100 is the busiest\n"
           "single month for any of the related searches compared. 2026 is January to September. Dotted lines: AI releases.",
           "Source: Google Trends; agizeitgeist.com/data")
    return save(fig, "zeitgeist-search.png")


def chart_forum():
    """r/singularity's most popular posts as squares, one per post, counted exactly as
    vanguard_figure.py counts them (imported, not copied)."""
    import vanguard_figure as v

    posts = v.load_posts()
    quarters = sorted(v.apply_cutoff(posts))
    months = {"Q1": "Jan–Mar", "Q2": "Apr–Jun", "Q3": "Jul–Sep", "Q4": "Oct–Dec"}
    cats = [("What AI can do now", {"specific_capability"}, PALETTE[0]),
            ("AI companies and the law", {"industry_governance"}, PALETTE[6]),
            ("Jobs and society", {"consequence"}, PALETTE[1]),
            ("AGI or the singularity in general", {"agi", "pace_singularity", "self_improvement"}, PALETTE[3]),
            ("The three AI systems disagreed", {v.UNRESOLVED}, GRID)]
    cat_of = lambda p: next(i for i, (_, keys, _) in enumerate(cats) if p["claim_target"] in keys)  # noqa: E731

    def arrival(sample):
        xs = [p for p in posts.values() if p["sample"] == sample
              and all(p[f] != v.UNRESOLVED for f in v.HEADLINE_FIELDS)]
        return sum(map(v.headline, xs)), len(xs)

    top = {q: sorted(cat_of(p) for p in posts.values() if p["quarter"] == q and p["sample"] == "rewarded")
           for q in quarters}
    totals = [sum(1 for c in top.values() for x in c if x == i) for i in range(len(cats))]
    arr_top, dec_top = arrival("rewarded")
    arr_rand, dec_rand = arrival("prevalence")

    fig, ax = figure(10, 4.4)
    cols, size, gap, block_gap = 4, 1.0, 0.18, 1.6
    block_w = cols * size + (cols - 1) * gap
    edge = lambda c: "#b9b8b3" if c == len(cats) - 1 else cats[c][2]  # noqa: E731
    for b, q in enumerate(quarters):
        x0 = b * (block_w + block_gap)
        for k, c in enumerate(top[q]):
            ax.add_patch(Rectangle((x0 + (k % cols) * (size + gap), (k // cols) * (size + gap)), size, size,
                                   facecolor=cats[c][2], edgecolor=edge(c), lw=0.8))
        ax.text(x0 + block_w / 2, -0.45, f"{months[q[4:]]}\n{q[:4]}", ha="center", va="top", fontsize=9, color=INK_2)
    for _, label, d in releases(start=f"{quarters[0][:4]}-{int(quarters[0][5]) * 3 - 2:02d}"):
        q = f"{d[:4]}Q{(int(d[5:7]) - 1) // 3 + 1}"
        if q in quarters:
            b = quarters.index(q)
            ax.text(b * (block_w + block_gap) + block_w / 2, 6.45, f"{label} released", ha="center", va="bottom",
                    fontsize=8, color=INK, fontweight="bold")
            ax.annotate("", (b * (block_w + block_gap) + block_w / 2, 5.95), (b * (block_w + block_gap) + block_w / 2, 6.4),
                        arrowprops=dict(arrowstyle="-|>", color=INK_2, lw=1, mutation_scale=8))
    ax.set_xlim(-0.1, len(quarters) * (block_w + block_gap) - block_gap + 0.1)
    ax.set_ylim(-2.0, 7.0)
    ax.set_aspect("equal")
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_position([0.04, 0.27, 0.94, 0.45])
    handles = [Rectangle((0, 0), 1, 1, facecolor=c, edgecolor=edge(i)) for i, (_, _, c) in enumerate(cats)]
    fig.legend(handles, [f"{n} ({t})" for (n, _, _), t in zip(cats, totals)], loc="upper left",
               bbox_to_anchor=(0.03, 0.865), ncol=3, frameon=False, fontsize=8.5, labelcolor=INK,
               handlelength=1.1, handleheight=1.1, columnspacing=1.4)
    titles(fig, "Almost no post on r/singularity says AGI has already arrived",
           "Each square is one of the most popular posts, about 20 every three months, coloured by what it "
           "mainly says.",
           "Three AI systems from different companies sorted every post; a post counts only where two agreed. "
           "Source: agizeitgeist.com/data")
    fig.text(0.04, 0.17, f"Popular posts saying AGI or the singularity is already here: {arr_top} of {dec_top}. "
             f"Among {dec_rand} randomly picked posts: {arr_rand}.", fontsize=10, color=INK, fontweight="bold")
    return save(fig, "zeitgeist-forum.png")


BUILDER, OTHER = PALETTE[7], PALETTE[0]
TOP = 2100  # dates past this are drawn at the top edge with an arrow


def frontier_rows(statements=None, speakers=None):
    """The rows the frontier-voices chart reads: each statement that names a year for machines
    matching people at most thinking work (target broad_competence) and accepts, hedges or
    conditions it, with the speaker's frontier_lab tag as recorded in speakers.csv. A derived
    reading of coded rows (2026-10-17); nothing scored."""
    speakers = {r["speaker_id"]: r for r in (speakers or read("speakers.csv"))}
    out = []
    for r in measured(statements or read("statements.csv")):  # tip_only rows stay out of every figure (A29)
        if r["target_capability"] != "broad_competence" or not r.get("timeline_year"):
            continue
        if r["endorsement"] not in ("accepts", "uncertain", "conditional"):
            continue
        sp = speakers.get(r["speaker_id"])
        if not sp or sp["tier"] not in PANEL_TIERS:  # the ledger-only list never enters a figure (A30)
            continue
        lo = int(r["timeline_year"]); hi = int(r["timeline_year_high"] or lo)
        out.append(dict(id=r["statement_id"], speaker=r["speaker_id"], name=sp["name"], said=int(r["date"][:4]),
                        # A builder: the frontier-lab tag, or one of the fifteen industry leaders (John, 2026-10-19,
                        # amendment A31: Jensen Huang among them, the frozen tag itself left alone).
                        year=(lo + hi) / 2, builder=bool(sp["frontier_lab"]) or r["speaker_id"] in cs.LEADERS))
    return out


def frontier_reading(statements=None, speakers=None):
    """What the frontier-voices chart shows, in numbers: each group's median year among guesses made
    since 2023, and the people who study it in their earliest guesses. The chart's title and the home
    page's sentence both read this, so they cannot disagree."""
    import statistics
    rows = frontier_rows(statements, speakers)
    b = [r for r in rows if r["builder"]]
    o = [r for r in rows if not r["builder"]]
    rec = lambda rs: statistics.median([r["year"] for r in rs if r["said"] >= 2023]) if any(r["said"] >= 2023 for r in rs) else None
    first = sorted(o, key=lambda r: r["said"])[:max(3, len(o) // 4)]
    return dict(builders_now=rec(b), others_now=rec(o), others_then=statistics.median([r["year"] for r in first]) if first else None,
                enough=len(b) >= 10 and len(o) >= 10)


def chart_frontier(statements=None, speakers=None):
    """The panel's dated guesses, with the people who build frontier systems drawn apart from
    the people who study them, and each group's median by year."""
    rows = frontier_rows(statements, speakers)
    import statistics
    groups = {True: [r for r in rows if r["builder"]], False: [r for r in rows if not r["builder"]]}

    def medians(rs):
        by = {}
        for r in rs:
            by.setdefault(r["said"], []).append(r["year"])
        return {y: statistics.median(v) for y, v in by.items() if len(v) >= 2}

    fig, ax = figure(10, 6.2)
    fig.subplots_adjust(left=0.11, right=0.97, top=0.76, bottom=0.12)
    for builder, col, label in ((False, OTHER, "People who study it"), (True, BUILDER, "People who build it")):
        rs = groups[builder]
        xs = [r["said"] + (0.15 if builder else -0.15) for r in rs]
        ys = [min(r["year"], TOP) for r in rs]
        ax.plot(xs, ys, "o", ms=5.5, color=col, alpha=0.45, mec="none", zorder=3, label=f"{label} ({len(rs)} guesses)")
        for x, r in zip(xs, rs):
            if r["year"] > TOP:
                ax.annotate("", (x, TOP), (x, TOP - 4), arrowprops=dict(arrowstyle="-|>", color=col, lw=1, alpha=0.6), zorder=3)
        med = medians(rs)
        if med:
            ks = sorted(med)
            ax.plot(ks, [min(med[k], TOP) for k in ks], "-", color=col, lw=2.4, zorder=4)
            ax.plot(ks, [min(med[k], TOP) for k in ks], "o", ms=4, color=col, zorder=5)
    ax.plot([2020, 2027], [2020, 2027], color=GRID, lw=1, zorder=1)
    ax.text(2020.2, 2021.2, "a guess for the same year it was said", fontsize=7.5, color=INK_2, ha="left", va="bottom")
    ax.set_xlim(2004.5, 2027)
    ax.set_ylim(2020, TOP + 3)
    ax.set_xticks(range(2005, 2027, 3))
    ax.set_yticks(range(2030, TOP + 1, 10))
    ax.set_yticklabels([str(y) if y < TOP else f"{TOP} or later" for y in range(2030, TOP + 1, 10)])
    ax.grid(axis="y", color=GRID, lw=0.8)
    ax.set_axisbelow(True)
    ax.set_xlabel("When the guess was made", fontsize=9, color=INK_2)
    ax.set_ylabel("The year they said machines would match people at most thinking work", fontsize=9, color=INK_2)
    ax.legend(loc="lower left", bbox_to_anchor=(0, 1.0), ncol=2, frameon=False, fontsize=9)

    # The title states what the data shows, computed so it stays true as rows are added.
    def recent(rs, years):
        v = [r["year"] for r in rs if r["said"] >= years]
        return statistics.median(v) if v else None
    def early(rs):
        v = sorted(rs, key=lambda r: r["said"])
        v = [r["year"] for r in v[:max(3, len(v) // 4)]]
        return statistics.median(v) if v else None
    b_now, o_now, o_then = recent(groups[True], 2023), recent(groups[False], 2023), early(groups[False])
    enough = len(groups[True]) >= 10 and len(groups[False]) >= 10
    if enough and b_now and o_now and o_then:
        gap = o_now - b_now
        title = (f"The builders have said about {b_now:.0f} all along; the others have come down to meet them"
                 if abs(gap) <= 3 else
                 f"The builders say about {b_now:.0f}; the people who study it say about {o_now:.0f}")
    else:
        title = "Too few dated guesses on one side yet to compare the builders with the others"
    titles(fig, title,
           "Each dot is one dated guess by a panel member; the lines join each group's median for the years with two or more guesses.\n"
           "A builder is anyone on the panel who has worked at a company that builds frontier AI systems, or leads one.",
           "Guesses in the person's own words only, for machines matching people at most thinking work. Source: agizeitgeist.com/data")
    return save(fig, "zeitgeist-frontier.png")


def _x(when):
    """A claim's date as a decimal year (a month or a year alone is placed at its middle)."""
    p = str(when).split("-")
    return int(p[0]) + ((int(p[1]) - 1) / 12 if len(p) > 1 else 0.5) + ((int(p[2]) - 1) / 365 if len(p) > 2 else (1 / 24 if len(p) > 1 else 0))


def _mark(ax, c, y, colour, size=1.0):
    """One forecast on a timeline at height y: a bar for a range, a lighter bar from the day it was said for
    'by' a year, a dot for a single year, an arrow for 'not before'. A forecast known only from news reports
    is drawn hollow."""
    hollow = c["source_kind"] == "coverage_only"
    form, hi = c["form"], c["due"]
    if form == "not_before":
        ax.annotate("", (hi + 3, y), (hi, y), arrowprops=dict(arrowstyle="-|>", color=PALETTE[1], lw=2 * size))
        ax.plot([hi], [y], "|", ms=11 * size, mew=2.5 * size, color=PALETTE[1])
    elif form == "range" or (form == "by" and _x(c["when"]) < hi - 0.5):
        lo = c["due_early"] if form == "range" else max(_x(c["when"]), 2025.0)
        ax.plot([lo, hi], [y, y], "-", lw=6 * size, color=colour, solid_capstyle="round", alpha=0.85 if form == "range" else 0.4)
        if form == "by":
            ax.plot([hi], [y], "|", ms=10 * size, mew=2.5 * size, color=colour)
    else:
        ax.plot([hi], [y], "o", ms=9 * size, color=colour, mfc=SURFACE if hollow else colour, mew=2)


def chart_claims_now(claims=None, words=None, statements=None, speakers=None):
    """What the industry's leaders say now: each one's forecasts from the latest day they gave one, against
    the academics' band (amendment A31). Verdicts are never drawn here (John, 2026-10-19)."""
    now = cs.leaders_now(claims, words)
    band = cs.academics_band(statements, speakers)
    names = {r["speaker_id"]: r["name"] for r in read("speakers.csv")}
    rows = sorted((sp for sp in cs.LEADERS if now[sp]["latest"]),
                  key=lambda sp: (now[sp]["nearest"] is None, now[sp]["nearest"] or 0, sp))
    fig, ax = figure(11.5, 6.2)
    fig.subplots_adjust(left=0.27, right=0.97, top=0.78, bottom=0.14)
    if band:
        ax.axvspan(band["low"], band["high"], color=PALETTE[2], alpha=0.12, lw=0)
        ax.axvline(band["middle"], color=PALETTE[2], lw=1.5)
        ax.text(band["middle"] + 0.2, len(rows) - 0.35,
                f"academics and long-time thinkers on the panel: the middle half of\ntheir {band['n']} dated guesses since 2023 "
                f"({band['low']:.0f} to {band['high']:.0f}), middle about {band['middle']:.0f}", fontsize=7.5, color="#0b6b48", va="top")
    for i, sp in enumerate(rows):
        latest = now[sp]["latest"]
        for j, c in enumerate(sorted(latest, key=lambda c: c["due"])):
            off = (j - (len(latest) - 1) / 2) * 0.22
            _mark(ax, c, i + off, OTHER, 0.8 if len(latest) > 1 else 1.0)
    today = _x(cs_today())
    ax.axvline(today, color=INK_2, lw=0.8, ls=":")
    ax.text(today + 0.1, -0.85, "today", fontsize=7.5, color=INK_2)
    ax.set_ylim(len(rows) + 0.9, -0.6)
    ax.set_yticks(range(len(rows)))
    ax.set_yticklabels([f"{names[sp]}, said {now[sp]['day']}" for sp in rows], fontsize=8.5, color=INK)
    ax.set_xlim(2025, 2046)
    ax.set_xticks(range(2026, 2047, 4))
    ax.grid(axis="x", color=GRID, lw=0.8)
    ax.set_axisbelow(True)
    named = [sp for sp in rows if now[sp]["nearest"] is not None]
    if band:
        k = sum(1 for sp in named if now[sp]["nearest"] < band["middle"])
        title = f"{k} of {len(rows)} industry leaders now name a year before the academics' middle one, about {band['middle']:.0f}"
    else:
        title = "Too few dated guesses by the academics since 2023 to set the leaders against them"
    silent = [names[sp] for sp in cs.LEADERS if not now[sp]["latest"]]
    titles(fig, title,
           "Each leader's forecasts from the latest day they put a date on AGI, superintelligence or AI better than people at most things, in their own terms.\n"
           "A dark bar is a range they gave; a light bar runs to a year they said it would come by; a dot is a single year (hollow: known only from news reports);\nan orange arrow is a forecast that it will not come before that year.",
           f"{', '.join(silent)} have given no dated forecast of this kind; their latest words are on the claims page. Source: agizeitgeist.com/data")
    return save(fig, "claims-now.png")


def chart_claims_moved(claims=None):
    """How the industry's leaders' dates have moved since 2023: one small panel per leader with any such
    forecast, each mark placed at the day it was said and the year it named (amendment A31)."""
    claims = claims if claims is not None else cs.load_claims()
    names = {r["speaker_id"]: r["name"] for r in read("speakers.csv")}
    # One mark per day a forecast was said, its repeats included (a repeat is saying it again).
    d = [dict(c, when=s) for c in claims if cs.drawn(c) for s in cs.said_on(c) if int(s[:4]) >= 2023]
    people = [sp for sp in cs.LEADERS if any(c["speaker_id"] == sp for c in d)]
    people.sort(key=lambda sp: -sum(1 for c in d if c["speaker_id"] == sp))
    cols = 4
    nrows = (len(people) + cols - 1) // cols
    fig, axs = figure(11.5, 2.7 * nrows + 1.2, nrows=nrows, ncols=cols, sharex=True, sharey=True)
    fig.subplots_adjust(left=0.07, right=0.98, top=1 - 1.55 / (2.7 * nrows + 1.2), bottom=0.6 / (2.7 * nrows + 1.2), hspace=0.42, wspace=0.12)
    flat = list(axs.flat) if hasattr(axs, "flat") else [axs]
    for a, sp in zip(flat, people):
        a.plot([2023, 2041], [2023, 2041], color=GRID, lw=1)
        for c in [c for c in d if c["speaker_id"] == sp]:
            x = _x(c["when"])
            if c["form"] == "not_before":
                a.plot([x], [c["due"]], "^", ms=6, color=PALETTE[1])
                continue
            lo = c["due_early"] if c["form"] == "range" else None
            if lo:
                a.plot([x, x], [lo, c["due"]], "-", lw=3, color=OTHER, alpha=0.6)
            hollow = c["source_kind"] == "coverage_only"
            a.plot([x], [c["due"]], "v" if c["form"] == "by" else "o", ms=5, color=OTHER, mfc=SURFACE if hollow else OTHER, mew=1.5)
        a.set_title(names[sp], fontsize=9.5, color=INK, loc="left")
        a.grid(axis="y", color=GRID, lw=0.6)
        a.set_axisbelow(True)
    for a in flat[len(people):]:
        a.set_visible(False)
    flat[0].set_xlim(2022.7, 2027)
    flat[0].set_ylim(2024, 2046)
    flat[0].set_xticks([2023, 2025, 2027])
    flat[0].set_yticks([2025, 2030, 2035, 2040, 2045])
    m = cs.moved(claims)
    ways = {w: sum(1 for v in m.values() if v["way"] == w) for w in ("nearer", "held", "later")}
    parts = [f"{ways[w]} {t}" for w, t in (("nearer", "brought their dates nearer"), ("held", "held them"), ("later", "pushed them later")) if ways[w]]
    title = ("Since 2023: " + (", ".join(parts[:-1]) + ", " + parts[-1] if len(parts) > 1 else parts[0]).replace("brought their dates nearer", "leaders brought their dates nearer", 1)
             if m else "How the industry leaders' dates have moved since 2023")
    titles(fig, title,
           "Each mark is one forecast of AGI, superintelligence or AI better than people at most things, in their own terms, at a day it was said (repeats included) and the year it named.\n"
           "Dot: a year (hollow: known only from news reports). Bar: a range. Down-pointing triangle: a year it would come by. Orange: not before that year. Grey line: 'this year'.",
           "Nearer, held or later compares the nearest year named on the first and the latest day, a year or more counting as a move; the terms they use can change between days. Source: agizeitgeist.com/data")
    return save(fig, "claims-moved.png")


def cs_today():
    from datetime import datetime
    from zoneinfo import ZoneInfo
    return datetime.now(ZoneInfo("America/Los_Angeles")).date().isoformat()


def main():
    for chart in (chart_experts, chart_researchers, chart_search, chart_forum, chart_frontier, chart_claims_now, chart_claims_moved):
        print(chart())


if __name__ == "__main__":
    main()
