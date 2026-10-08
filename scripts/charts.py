#!/usr/bin/env python3
"""Build the charts from data/*.csv into site/.

Only chart 1 exists so far (seed phase): the share of statements by frame_primary
(version 2 codes), by year. The final chart set is decided after the seed (methodology-v2 section 11).

    .venv/bin/python scripts/charts.py
"""

import csv
from collections import Counter
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
SITE = ROOT / "site"

# Version 2 frame_primary codes, bottom to top in the order of the story being
# tested (whether, when, now), then the wider questions version 2 lets win.
FRAMES = ["possibility", "definition", "timeline", "capability_now",
          "self_improvement", "consequences", "governance", "other_concern"]
FRAME_LABELS = {
    "possibility": "Can it be built?",
    "definition": "What counts as AGI?",
    "timeline": "When will it arrive?",
    "capability_now": "Is today's machine close?",
    "self_improvement": "Can it make itself smarter?",
    "consequences": "What happens if it does?",
    "governance": "What should be done?",
    "other_concern": "Another AI concern",
}
# Reference palette from the dataviz skill, categorical slots 1-8 in fixed order
# (validated for adjacent pairs in light mode). Colour follows the frame, never rank.
COLORS = dict(zip(FRAMES, ["#2a78d6", "#eb6834", "#1baf7a", "#eda100",
                           "#e87ba4", "#008300", "#4a3aa7", "#e34948"]))
SURFACE = "#fcfcfb"
INK = "#0b0b0b"
INK_2 = "#52514e"
GRID = "#e4e3df"
FIRST_YEAR, LAST_YEAR = 2005, 2026
WINDOW = 3  # years pooled per point in chart 1
THIN_UNTIL = 2013  # years before this rest on five or fewer statements each
# Reports are context, not turning points; only these event types are marked on the axis.
MARKED_EVENTS = {"open_letter", "public_statement", "government_action"}


def read(name):
    with (DATA / name).open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def frame_counts(statements):
    counts = {y: Counter() for y in range(FIRST_YEAR, LAST_YEAR + 1)}
    for s in statements:
        year = int(s["date"][:4])
        if year in counts:
            counts[year][s["frame_primary"]] += 1
    return counts


def chart_frames(statements, events, window=WINDOW):
    counts = frame_counts(statements)
    years = list(counts)

    # Table view alongside the image (relief for the low-contrast colours): raw yearly counts.
    with (SITE / "chart-1-frames.csv").open("w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["year", "statements"] + FRAMES)
        for y in years:
            w.writerow([y, sum(counts[y].values())] + [counts[y][f] for f in FRAMES])

    # Most years hold only a handful of statements, so each point pools the year with
    # its neighbours (a centred moving window) before shares are taken.
    half = window // 2
    pooled = {y: sum((counts[z] for z in range(y - half, y + half + 1) if z in counts),
                     Counter()) for y in years}
    totals = [sum(pooled[y].values()) for y in years]
    shares = {f: [(pooled[y][f] / t * 100) if t else 0 for y, t in zip(years, totals)]
              for f in FRAMES}

    fig, ax = plt.subplots(figsize=(10, 6.2), dpi=160)
    fig.patch.set_facecolor(SURFACE)
    ax.set_facecolor(SURFACE)

    stacks = ax.stackplot(years, [shares[f] for f in FRAMES],
                          colors=[COLORS[f] for f in FRAMES],
                          edgecolor=SURFACE, linewidth=2)
    for poly, f in zip(stacks, FRAMES):
        poly.set_label(FRAME_LABELS[f])

    # Direct labels inside bands wide enough to hold them (identity is never colour alone).
    bottoms = [0] * len(years)
    for f in FRAMES:
        vals = shares[f]
        # Inner years only, so a label never spills past the plot edge or over the axis.
        best = max(range(2, len(years) - 2),
                   key=lambda i: vals[i] if totals[i] >= 8 else -1)
        if vals[best] >= 14 and totals[best] >= 8:
            ax.text(years[best], bottoms[best] + vals[best] / 2, FRAME_LABELS[f],
                    ha="center", va="center", fontsize=8, color=INK, zorder=5,
                    bbox=dict(boxstyle="round,pad=0.2", fc=SURFACE, ec="none", alpha=0.85))
        bottoms = [b + v for b, v in zip(bottoms, vals)]

    # Statement counts per year, so thin years are visibly thin.
    for y, t in zip(years, totals):
        ax.text(y, 101.5, str(t), ha="center", va="bottom", fontsize=7, color=INK_2)

    # Years resting on too few statements are veiled so they do not read as a finding.
    ax.axvspan(FIRST_YEAR, THIN_UNTIL, color=SURFACE, alpha=0.72, zorder=3, linewidth=0)
    ax.text((FIRST_YEAR + THIN_UNTIL) / 2, 50, "Too few statements\nto read much into",
            ha="center", va="center", fontsize=9, color=INK_2, zorder=4)

    ax.set_xlim(FIRST_YEAR, LAST_YEAR)
    ax.set_ylim(0, 100)
    ax.set_xticks(range(FIRST_YEAR, LAST_YEAR + 1, 3))
    ax.set_yticks([0, 25, 50, 75, 100])
    ax.set_yticklabels(["0%", "25%", "50%", "75%", "100%"])
    ax.tick_params(colors=INK_2, labelsize=9, length=0)
    ax.grid(axis="y", color=GRID, linewidth=0.8)
    for side in ax.spines.values():
        side.set_visible(False)

    fig.suptitle("What five experts mainly talked about, 2005 to 2026", x=0.06, y=0.975, ha="left",
                 fontsize=14, color=INK, fontweight="bold")
    ax.set_title(f"Share of each year's public statements, by the question each one mainly answers. "
                 f"Kurzweil, Hinton, LeCun, Marcus and Altman, {len(statements)} statements.\n"
                 f"Each year is blended with the years either side. The small numbers along the top are how many statements each point rests on.",
                 loc="left", fontsize=9, color=INK_2, pad=18)
    ax.legend(loc="upper left", bbox_to_anchor=(1.01, 1), frameon=False, fontsize=9,
              labelcolor=INK, reverse=True)
    fig.text(0.06, 0.015, "Source: agizeitgeist.com/data", fontsize=7.5, color=INK_2)
    fig.tight_layout(rect=(0, 0.03, 1, 0.97))
    out = SITE / "chart-1-frames.png"
    fig.savefig(out, facecolor=SURFACE)
    plt.close(fig)
    return out


def main():
    SITE.mkdir(exist_ok=True)
    statements = read("statements.csv")
    events = read("events.csv")
    print(chart_frames(statements, events))


if __name__ == "__main__":
    main()
