#!/usr/bin/env python3
"""Pilot figure for the vanguard sub-series (amendment 2026-10-02, sections 8 and 10).

Shares of eligible posts by quarter making each of four claims, for the rewarded (top
posts) and prevalence (random) samples separately, each with and without title-only rows.
Writes site/vanguard-pilot-r-singularity.png and a table of every count beside it.

    .venv/bin/python scripts/vanguard_figure.py
"""

import csv
from collections import defaultdict
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent.parent
CODES = ROOT / "data" / "vanguard" / "r-singularity-pilot-codes.csv"
PNG = ROOT / "site" / "vanguard-pilot-r-singularity.png"
TABLE = ROOT / "site" / "vanguard-pilot-r-singularity.csv"
CAPTION = ("Framing in sampled high-score posts from selected AI enthusiast venues; "
           "not representative of participants or the public.")
MEASURES = {
    "AGI already achieved": lambda c: c["claim_target"] == "agi" and c["temporal_status"] == "achieved",
    "AGI within a stated horizon": lambda c: c["claim_target"] == "agi" and c["temporal_status"] == "forecast" and c["forecast_horizon"].strip(),
    "Self-improvement under way": lambda c: c["claim_target"] == "self_improvement" and c["temporal_status"] in ("under_way", "achieved"),
    "Singularity framing": lambda c: "singularity" in c["frame_tags"].lower(),
}
SAMPLES = {"rewarded": "Top posts (stream F rewarded series)", "prevalence": "Random posts (stream F prevalence sample)"}
# Dataviz reference palette, categorical slots 1 and 2 (validated adjacent pair).
BLUE, ORANGE = "#2a78d6", "#eb6834"
SURFACE, INK, INK_2, GRID = "#fcfcfb", "#0b0b0b", "#52514e", "#e4e3df"


def main():
    with CODES.open(newline="") as f:
        rows = list(csv.DictReader(f))
    posts = defaultdict(list)
    for r in rows:
        posts[(r["quarter"], r["sample"], r["post_id"])].append(r)
    quarters = sorted({k[0] for k in posts})
    table = []
    data = {}
    for s in SAMPLES:
        for m, test in MEASURES.items():
            for q in quarters:
                elig = [v for k, v in posts.items() if k[0] == q and k[1] == s and v[0]["eligible"] == "yes"]
                full = [v for v in elig if not any(c["title_only"] == "yes" for c in v)]
                aff = lambda v: any(test(c) and c["stance"] == "affirms" for c in v)
                den = lambda v: any(test(c) and c["stance"] == "denies" for c in v)
                k_all, k_full = sum(map(aff, elig)), sum(map(aff, full))
                d_all = sum(map(den, elig))
                data[(s, m, q)] = (k_all / len(elig) if elig else None, k_full / len(full) if full else None)
                table.append([q, s, m, len(elig), k_all, d_all, len(full), k_full])
    with TABLE.open("w", newline="") as f:
        w = csv.writer(f, lineterminator="\n")
        w.writerow(["quarter", "sample", "claim", "eligible_posts", "affirming", "disputing",
                    "eligible_posts_excl_title_only", "affirming_excl_title_only"])
        w.writerows(table)

    fig, axes = plt.subplots(len(MEASURES), len(SAMPLES), figsize=(10, 9.5), dpi=160, sharex=True, sharey=True)
    fig.patch.set_facecolor(SURFACE)
    x = range(len(quarters))
    for col, s in enumerate(SAMPLES):
        for row, m in enumerate(MEASURES):
            ax = axes[row][col]
            ax.set_facecolor(SURFACE)
            a = [data[(s, m, q)][0] for q in quarters]
            b = [data[(s, m, q)][1] for q in quarters]
            ax.plot(x, [v * 100 if v is not None else float("nan") for v in a], color=BLUE, lw=2,
                    marker="o", ms=4, label="All eligible posts")
            ax.plot(x, [v * 100 if v is not None else float("nan") for v in b], color=ORANGE, lw=2,
                    ls=(0, (4, 2)), marker="s", ms=4, label="Excluding title-only rows")
            ax.set_ylim(0, 40)  # no share exceeds 25% in the pilot; the axis says so
            ax.set_yticks([0, 20, 40])
            ax.set_yticklabels(["0%", "20%", "40%"])
            ax.grid(axis="y", color=GRID, lw=0.8)
            ax.tick_params(colors=INK_2, labelsize=8, length=0)
            for side in ax.spines.values():
                side.set_visible(False)
            if row == 0:
                ax.set_title(SAMPLES[s], fontsize=10, color=INK, loc="left")
            if col == 0:
                ax.set_ylabel(m, fontsize=9, color=INK)
            ax.set_xticks(list(x))
            ax.set_xticklabels([q.replace("20", "", 1) for q in quarters], fontsize=7, rotation=0)
    handles, labels = axes[0][0].get_legend_handles_labels()
    fig.legend(handles, labels, loc="upper left", bbox_to_anchor=(0.04, 0.93), frameon=False,
               fontsize=9, ncol=2, labelcolor=INK)
    fig.suptitle("Vanguard sub-series (stream F), r/singularity pilot, 2024Q4 to 2026Q3",
                 x=0.04, y=0.995, ha="left", fontsize=13, fontweight="bold", color=INK)
    fig.text(0.04, 0.955, CAPTION, fontsize=9, color=INK_2, ha="left")
    fig.text(0.04, 0.937, "Share of eligible posts per quarter making each claim (poster affirms it). "
             "Unit: one post. Scale 0 to 40%. Counts in site/vanguard-pilot-r-singularity.csv.",
             fontsize=8, color=INK_2, ha="left")
    fig.text(0.04, 0.01, "Pilot: first-pass codes by model claude-opus-5-5. Small samples; random-post "
             "shares rest on few eligible posts per quarter.", fontsize=7.5, color=INK_2)
    fig.tight_layout(rect=(0, 0.025, 1, 0.885))
    fig.subplots_adjust(hspace=0.35)
    fig.savefig(PNG, facecolor=SURFACE)
    print(PNG)


if __name__ == "__main__":
    main()
