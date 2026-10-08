#!/usr/bin/env python3
"""Pilot figure for the vanguard sub-series (amendment 2026-10-02, sections 8 and 10, with
John's rulings of 2026-10-03 and 2026-10-04).

Shares come from the majority codes of the full-sample run: three models from different
companies (claude-opus-5-5; gemini-3.1-pro-preview, version 3.1-pro-preview-01-2026;
gpt-6-astra, pinned by its listed creation time 1787853604, reasoning effort medium) each
coded all 390 posts blind under the final codebook, and the final code for each field is the
value at least two of them gave (data/vanguard/r-singularity-pilot-codes-majority-full-final.csv,
written by scripts/vanguard_three_way.py --full). Where no two models agree the file says
"unresolved".

Primary measures, by quarter, for the top-post (rewarded) and random-post (prevalence)
samples, each with and without title-only rows:
  capability claims          share of eligible posts whose main claim is a specific_capability
  consequence claims         share of eligible posts whose main claim is a consequence
  industry and governance    share of eligible posts whose main claim is industry_governance
  extrapolation              share of posts with a capability main claim that infer a timeline
                             or consequence from it (extrapolates_to_horizon = yes)
  headline claims            share of eligible posts affirming any of the four headline claims
                             (AGI achieved; AGI by a stated horizon; self-improvement under way;
                             singularity framing), reported as near-absent

How the majority file is read, and the choices made here (agent decisions, 2026-10-08):
  * The majority file holds one row per post: the main claim (claim_n 1 in the model files)
    and the post-level fields. Secondary claims were never compared across models, so the
    three claim-kind measures count the main claim only. A post whose main claim is a
    capability but which also makes a consequence claim counts as capability, not consequence.
  * A post with "unresolved" in any field a measure uses is left out of that measure's
    denominator (it cannot be placed on either side). The count per quarter, sample and
    measure is in the counts table (posts_left_out_unresolved: eligible posts left out before
    the measure's own filter is applied, so for extrapolation it includes posts whose main
    claim could not be placed).
  * Two things the headline measure needs are not in the majority file: whether a forecast
    states a horizon (forecast_horizon) and whether "singularity" is among the words used
    (frame_tags). They are voted here the same way: each model's main-claim row gives yes or
    no, the answer needs two models, otherwise unresolved.
  * Irony. The codebook (section 3, rhetorical_mode; rule R1a) says to record irony in
    rhetorical_mode but does not say whether an ironic post can affirm a headline claim. So a
    post coded ironic by majority does not count as affirming a headline claim; posts coded
    mixed or unclear still can. This is the agent's reading, not a ruling, and the run record
    says how many posts it affects.
  * Top-post cut-off. The rewarded sample keeps, per quarter, the ranked posts down to the
    rank at which 20 are eligible by majority; eligible posts below that rank are left out of
    every denominator. Where the models have not coded deep enough for 20 (the majority finds
    fewer than 20 eligible among the screened ranks), every screened post counts and the
    shortfall is printed. The random sample has no cut-off.

A measure is drawn only if every field it depends on passed the three-model reliability test
(data/vanguard/three-model-reliability-full-final.csv, amendment section 9); the others are
listed under the figure as excluded.

Writes site/vanguard-pilot-r-singularity.png and a table of every count beside it, and
prints the per-quarter cut-off ranks.

    .venv/bin/python scripts/vanguard_figure.py
"""

import csv
from collections import Counter, defaultdict
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent.parent
D = ROOT / "data" / "vanguard"
CODES = D / "r-singularity-pilot-codes-majority-full-final.csv"
MODEL_FILES = [D / "r-singularity-pilot-codes-claude-full-final.csv",
               D / "r-singularity-pilot-codes-crossfamily-full-final.csv",
               D / "r-singularity-pilot-codes-gpt-full-final.csv"]
SAMPLE = D / "r-singularity-pilot-sample.csv"
RELIABILITY = D / "three-model-reliability-full-final.csv"
PNG = ROOT / "site" / "vanguard-pilot-r-singularity.png"
TABLE = ROOT / "site" / "vanguard-pilot-r-singularity.csv"
CAPTION = ("Framing in sampled high-score posts from selected AI enthusiast venues; "
           "not representative of participants or the public.")
LABEL = "model-coded"
TARGET_ELIGIBLE = 20  # rewarded sample: eligible posts per quarter (run record, "Samples")
UNRESOLVED = "unresolved"


def has(target):
    return lambda p: p["claim_target"] == target


def headline(p):
    """Poster affirms a headline claim, in a post not coded ironic (see the docstring)."""
    if p["stance"] != "affirms" or p["rhetorical_mode"] == "ironic":
        return False
    t, s = p["claim_target"], p["temporal_status"]
    return ((t == "agi" and s == "achieved") or (t == "agi" and s == "forecast" and p["horizon_stated"] == "yes")
            or (t == "self_improvement" and s in ("under_way", "achieved")) or p["singularity_tag"] == "yes")


# (label, filter for the denominator posts, test for the numerator, fields it depends on)
HEADLINE_FIELDS = ["claim_target", "temporal_status", "stance", "rhetorical_mode", "horizon_stated", "singularity_tag"]
ALL_MEASURES = [
    ("Capability claims\n(main claim)", lambda p: True, has("specific_capability"), ["claim_target"]),
    ("Consequence claims\n(main claim)", lambda p: True, has("consequence"), ["claim_target"]),
    ("Industry and\ngovernance claims\n(main claim)", lambda p: True, has("industry_governance"), ["claim_target"]),
    ("Capability posts that\nextrapolate to a\ntimeline or consequence", has("specific_capability"),
     lambda p: p["extrapolates_to_horizon"] == "yes", ["claim_target", "extrapolates_to_horizon"]),
    ("Headline claims\n(any of the four;\nironic posts left out)", lambda p: True, headline, HEADLINE_FIELDS),
]
# The two voted-here fields are built from forecast_horizon and frame_tags, which the
# reliability table does not cover; the test is applied to the table's fields.
TESTED = lambda fields: [f for f in fields if f not in ("horizon_stated", "singularity_tag")]  # noqa: E731


def reliability():
    with RELIABILITY.open(newline="") as f:
        return {r["field"]: r["verdict"] for r in csv.DictReader(f)}


VERDICT = reliability()
UNRELIABLE = sorted(f for f, v in VERDICT.items() if v != "reliable")
MEASURES = [m[:3] for m in ALL_MEASURES if all(VERDICT.get(f) == "reliable" for f in TESTED(m[3]) + ["eligible"])]
EXCLUDED = [m[0].replace("\n", " ") for m in ALL_MEASURES if m[:3] not in MEASURES]
SHOW_TITLE_ONLY_LINE = VERDICT.get("title_only") == "reliable"
PLAIN = {"eligible": "eligibility", "claim_target": "what the claim is about", "temporal_status": "forecast or achieved",
         "stance": "whether the poster agrees", "epistemic_qualification": "hedging", "rhetorical_mode": "irony",
         "development_preference": "speed up or slow down", "attribution": "whose claim",
         "title_only": "title-only coding", "extrapolates_to_horizon": "extrapolation"}
SAMPLES = {"rewarded": "Top posts (stream F rewarded series)", "prevalence": "Random posts (stream F prevalence sample)"}
BLUE, ORANGE = "#2a78d6", "#eb6834"  # dataviz reference palette, slots 1 and 2
SURFACE, INK, INK_2, GRID = "#fcfcfb", "#0b0b0b", "#52514e", "#e4e3df"


def vote(values):
    top = Counter(values).most_common(1)
    return top[0][0] if top and top[0][1] >= 2 else UNRESOLVED


def derived_votes():
    """Post id -> {horizon_stated, singularity_tag}: majority of the models' main-claim rows."""
    votes = defaultdict(lambda: {"horizon_stated": [], "singularity_tag": []})
    for path in MODEL_FILES:
        with path.open(newline="") as f:
            for r in csv.DictReader(f):
                if r["claim_n"] != "1":  # the main claim; claim_n 0 is an ineligible post
                    continue
                tags = {t.strip().lower() for t in r["frame_tags"].split(";")}
                votes[r["post_id"]]["horizon_stated"].append("yes" if r["forecast_horizon"].strip() else "no")
                votes[r["post_id"]]["singularity_tag"].append("yes" if "singularity" in tags else "no")
    return {i: {k: vote(v) for k, v in d.items()} for i, d in votes.items()}


def load_posts():
    """Eligible posts by majority, with the two voted-here fields added."""
    extra = derived_votes()
    posts = {}
    with CODES.open(newline="") as f:
        for r in csv.DictReader(f):
            if r["eligible"] != "yes":
                continue
            r.update(extra.get(r["post_id"], {"horizon_stated": UNRESOLVED, "singularity_tag": UNRESOLVED}))
            posts[r["post_id"]] = r
    return posts


def apply_cutoff(posts):
    """Drop eligible top posts below each quarter's cut-off rank; return {quarter: (cut-off rank,
    eligible kept, deepest rank the models coded, eligible found there)}."""
    with SAMPLE.open(newline="") as f:
        rank = {r["post_id"]: int(r["rank_or_draw"]) for r in csv.DictReader(f) if r["sample"] == "rewarded"}
    cutoffs = {}
    for q in sorted({p["quarter"] for p in posts.values()}):
        ranked = sorted((rank[i] for i, p in posts.items() if p["quarter"] == q and p["sample"] == "rewarded"))
        cut = ranked[TARGET_ELIGIBLE - 1] if len(ranked) >= TARGET_ELIGIBLE else None
        for i in [i for i, p in posts.items() if p["quarter"] == q and p["sample"] == "rewarded" and cut and rank[i] > cut]:
            del posts[i]
        cutoffs[q] = (cut, min(len(ranked), TARGET_ELIGIBLE), ranked[-1], len(ranked))
    return cutoffs


def main():
    posts = load_posts()
    cutoffs = apply_cutoff(posts)
    print("Top-post cut-off per quarter (rank at which 20 are eligible by majority):")
    for q, (cut, kept, deepest, found) in cutoffs.items():
        if cut:
            print(f"  {q}: rank {cut}, {kept} eligible kept, {found - kept} eligible below the cut-off left out")
        else:
            print(f"  {q}: no cut-off reached: {found} eligible among the ranks coded (deepest rank {deepest}); all kept")

    quarters = sorted(cutoffs)
    table, data = [], {}
    for s in SAMPLES:
        for label, base, test, fields in ALL_MEASURES:
            for q in quarters:
                elig = [p for p in posts.values() if p["quarter"] == q and p["sample"] == s]
                decided = [p for p in elig if all(p[f] != UNRESOLVED for f in fields)]
                den_all = [p for p in decided if base(p)]
                den_full = [p for p in den_all if p["title_only"] != "yes" and p["title_only"] != UNRESOLVED]
                k_all, k_full = sum(map(test, den_all)), sum(map(test, den_full))
                data[(s, label, q)] = (k_all / len(den_all) if den_all else None,
                                       k_full / len(den_full) if den_full else None)
                table.append([q, s, label.replace("\n", " "), len(den_all), k_all, len(den_full), k_full,
                              len(elig) - len(decided),
                              "yes" if (label, base, test) in MEASURES else "no: depends on an unreliable field"])
    with TABLE.open("w", newline="") as f:
        w = csv.writer(f, lineterminator="\n")
        w.writerow(["quarter", "sample", "measure", "denominator_posts", "posts_meeting_measure",
                    "denominator_posts_excl_title_only", "posts_meeting_measure_excl_title_only",
                    "posts_left_out_unresolved", "shown_in_figure"])
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
    fig.text(0.04, 0.946, "Share of eligible posts per quarter, by the post's main claim (extrapolation: share of "
             "posts with a capability main claim). Unit: one post.", fontsize=7.5, color=INK_2, ha="left")
    excluded = "; ".join(EXCLUDED) if EXCLUDED else "none"
    fig.text(0.04, 0.008, "Model-coded, no human coder. Shares are majority codes from three model families, each coding "
             "all 390 posts blind under the final codebook:\nclaude-opus-5-5 (Anthropic); gemini-3.1-pro-preview, "
             "version 3.1-pro-preview-01-2026 (Google); gpt-6-astra (OpenAI; pinned by its listed creation time "
             "1787853604,\nreasoning effort medium). A post where no two models agree on a field is left out of the "
             "measures using that field. Counts in site/vanguard-pilot-r-singularity.csv.\nUnreliable fields (left out): "
             f"{', '.join(PLAIN.get(f, f) for f in UNRELIABLE) or 'none'}. Measures left out: {excluded}. "
             "Random-post shares rest on few eligible posts per quarter.", fontsize=7, color=INK_2)
    fig.tight_layout(rect=(0, 0.05, 1, 0.925))
    fig.subplots_adjust(hspace=0.3)
    fig.savefig(PNG, facecolor=SURFACE)
    print(PNG)


if __name__ == "__main__":
    main()
