#!/usr/bin/env python3
"""Pilot figure for the vanguard sub-series (amendment 2026-10-02, sections 8 and 10, with
John's rulings of 2026-10-03).

Primary measures, by quarter, for the top-post (rewarded) and random-post (prevalence)
samples, each with and without title-only rows:
  capability claims          share of eligible posts with a specific_capability claim
  consequence claims         share of eligible posts with a consequence claim
  industry and governance    share of eligible posts with an industry_governance claim
  extrapolation              share of posts with a capability claim that infer a timeline
                             or consequence from it (extrapolates_to_horizon = yes)
  headline claims            share of eligible posts affirming any of the four headline
                             claims (AGI achieved; AGI by a stated horizon; self-improvement
                             under way; singularity framing), reported as near-absent

A measure is drawn only if every field it depends on passed the three-model reliability
test (data/vanguard/three-model-reliability.csv, amendment section 9); the others are listed
under the figure as excluded. Shares come from the first pass over the whole sample
(claude-opus-5-5), because the three-model majority code exists only for the 140-post set.

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
LABEL = "model-coded"
RELIABILITY = ROOT / "data" / "vanguard" / "three-model-reliability.csv"


def has(target):
    return lambda v: any(c["claim_target"] == target for c in v)


def headline(v):
    for c in v:
        if c["stance"] != "affirms":
            continue
        t, s = c["claim_target"], c["temporal_status"]
        if (t == "agi" and s == "achieved") or (t == "agi" and s == "forecast" and c["forecast_horizon"].strip()) \
                or (t == "self_improvement" and s in ("under_way", "achieved")) \
                or "singularity" in c["frame_tags"].lower():
            return True
    return False


# (label, filter for the denominator posts, test for the numerator, fields it depends on)
ALL_MEASURES = [
    ("Capability claims", lambda v: True, has("specific_capability"), ["claim_target"]),
    ("Consequence claims", lambda v: True, has("consequence"), ["claim_target"]),
    ("Industry and\ngovernance claims", lambda v: True, has("industry_governance"), ["claim_target"]),
    ("Capability posts that\nextrapolate to a\ntimeline or consequence", has("specific_capability"),
     lambda v: v[0]["extrapolates_to_horizon"] == "yes", ["claim_target", "extrapolates_to_horizon"]),
    ("Headline claims\n(any of the four)", lambda v: True, headline, ["claim_target", "temporal_status", "stance"]),
]


def reliability():
    with RELIABILITY.open(newline="") as f:
        return {r["field"]: r["verdict"] for r in csv.DictReader(f)}


VERDICT = reliability()
UNRELIABLE = sorted(f for f, v in VERDICT.items() if v != "reliable")
MEASURES = [m[:3] for m in ALL_MEASURES if all(VERDICT.get(f) == "reliable" for f in m[3] + ["eligible"])]
EXCLUDED = [m[0].replace("\n", " ") for m in ALL_MEASURES if m[:3] not in MEASURES]
SHOW_TITLE_ONLY_LINE = VERDICT.get("title_only") == "reliable"
PLAIN = {"eligible": "eligibility", "claim_target": "what the claim is about", "temporal_status": "forecast or achieved",
         "stance": "whether the poster agrees", "epistemic_qualification": "hedging", "rhetorical_mode": "irony",
         "development_preference": "speed up or slow down", "attribution": "whose claim",
         "title_only": "title-only coding", "extrapolates_to_horizon": "extrapolation"}
SAMPLES = {"rewarded": "Top posts (stream F rewarded series)", "prevalence": "Random posts (stream F prevalence sample)"}
BLUE, ORANGE = "#2a78d6", "#eb6834"  # dataviz reference palette, slots 1 and 2
SURFACE, INK, INK_2, GRID = "#fcfcfb", "#0b0b0b", "#52514e", "#e4e3df"


def main():
    with CODES.open(newline="") as f:
        rows = list(csv.DictReader(f))
    posts = defaultdict(list)
    for r in rows:
        posts[(r["quarter"], r["sample"], r["post_id"])].append(r)
    quarters = sorted({k[0] for k in posts})
    table, data = [], {}
    for s in SAMPLES:
        for label, base, test, _ in ALL_MEASURES:
            for q in quarters:
                elig = [v for k, v in posts.items() if k[0] == q and k[1] == s and v[0]["eligible"] == "yes"]
                den_all = [v for v in elig if base(v)]
                den_full = [v for v in den_all if not any(c["title_only"] == "yes" for c in v)]
                k_all, k_full = sum(map(test, den_all)), sum(map(test, den_full))
                data[(s, label, q)] = (k_all / len(den_all) if den_all else None,
                                       k_full / len(den_full) if den_full else None)
                table.append([q, s, label.replace("\n", " "), len(den_all), k_all, len(den_full), k_full,
                              "yes" if (label, base, test) in MEASURES else "no: depends on an unreliable field"])
    with TABLE.open("w", newline="") as f:
        w = csv.writer(f, lineterminator="\n")
        w.writerow(["quarter", "sample", "measure", "denominator_posts", "posts_meeting_measure",
                    "denominator_posts_excl_title_only", "posts_meeting_measure_excl_title_only", "shown_in_figure"])
        w.writerows(table)

    if not MEASURES:
        raise SystemExit("no measure passed the reliability test; no figure drawn")
    fig, axes = plt.subplots(len(MEASURES), len(SAMPLES), figsize=(10, 2.3 * len(MEASURES) + 2), dpi=160,
                             sharex=True, sharey=True, squeeze=False)
    fig.patch.set_facecolor(SURFACE)
    x = list(range(len(quarters)))
    for col, s in enumerate(SAMPLES):
        for row, (label, _, _) in enumerate(MEASURES):
            ax = axes[row][col]
            ax.set_facecolor(SURFACE)
            a = [data[(s, label, q)][0] for q in quarters]
            b = [data[(s, label, q)][1] for q in quarters]
            ax.plot(x, [v * 100 if v is not None else float("nan") for v in a], color=BLUE, lw=2,
                    marker="o", ms=4, label="All eligible posts")
            if SHOW_TITLE_ONLY_LINE:
                ax.plot(x, [v * 100 if v is not None else float("nan") for v in b], color=ORANGE, lw=2,
                        ls=(0, (4, 2)), marker="s", ms=4, label="Excluding title-only rows")
            ax.set_ylim(0, 100)
            ax.set_yticks([0, 50, 100])
            ax.set_yticklabels(["0%", "50%", "100%"])
            ax.grid(axis="y", color=GRID, lw=0.8)
            ax.tick_params(colors=INK_2, labelsize=8, length=0)
            for side in ax.spines.values():
                side.set_visible(False)
            if row == 0:
                ax.set_title(SAMPLES[s], fontsize=10, color=INK, loc="left")
            if col == 0:
                ax.set_ylabel(label, fontsize=8.5, color=INK)
            ax.set_xticks(x)
            ax.set_xticklabels([q.replace("20", "", 1) for q in quarters], fontsize=7)
    handles, labels = axes[0][0].get_legend_handles_labels()
    fig.legend(handles, labels, loc="upper left", bbox_to_anchor=(0.04, 0.94), frameon=False,
               fontsize=9, ncol=2, labelcolor=INK)
    fig.suptitle(f"Vanguard sub-series (stream F), r/singularity pilot, 2024Q4 to 2026Q3 ({LABEL})",
                 x=0.04, y=0.995, ha="left", fontsize=12, fontweight="bold", color=INK)
    fig.text(0.04, 0.962, CAPTION, fontsize=9, color=INK_2, ha="left")
    fig.text(0.04, 0.946, "Share of eligible posts per quarter (extrapolation: share of posts with a capability "
             "claim). Unit: one post. Counts in site/vanguard-pilot-r-singularity.csv.",
             fontsize=7.5, color=INK_2, ha="left")
    excluded = "; ".join(EXCLUDED) if EXCLUDED else "none"
    fig.text(0.04, 0.008, "Model-coded, no human coder. Shares from the first pass (claude-opus-5-5); fields checked by "
             "blind passes from gemini-3.1-pro-preview and gpt-6-astra.\nUnreliable fields (left out): "
             f"{', '.join(PLAIN.get(f, f) for f in UNRELIABLE) or 'none'}. Measures left out: {excluded}. "
             "Random-post shares rest on few eligible posts per quarter.", fontsize=7, color=INK_2)
    fig.tight_layout(rect=(0, 0.03, 1, 0.925))
    fig.subplots_adjust(hspace=0.3)
    fig.savefig(PNG, facecolor=SURFACE)
    print(PNG)


if __name__ == "__main__":
    main()
