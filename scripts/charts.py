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
from chart_style import GRID, INK, INK_2, PALETTE, PEOPLE, SURFACE, figure, read, save, titles  # noqa: E402

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
    by_id = {s["statement_id"]: s for s in read("statements.csv")}

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


def main():
    for chart in (chart_experts, chart_researchers, chart_search, chart_forum):
        print(chart())


if __name__ == "__main__":
    main()
