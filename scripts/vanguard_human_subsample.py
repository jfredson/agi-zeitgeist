#!/usr/bin/env python3
"""Draw John's 40-post blind human subsample (amendment section 9, revised 2026-10-03).

Drawn from the 140-post second-pass subset (data/vanguard/second-coder-worksheet.csv),
restricted to posts the first pass still codes, so John's codes can be compared with both
models. Stratified by sample in proportion (24 top posts, 16 random posts), seed 20261005.

Writes data/vanguard/john-vanguard-worksheet.csv: post id, quarter, sample, post type and
link, with empty columns for the main claim. No model codes appear in it.

    python3 scripts/vanguard_human_subsample.py
"""

import csv
import random
from pathlib import Path

SEED = 20261005
TAKE = {"rewarded": 24, "prevalence": 16}
ROOT = Path(__file__).resolve().parent.parent
SUBSET = ROOT / "data" / "vanguard" / "second-coder-worksheet.csv"
FIRST = ROOT / "data" / "vanguard" / "r-singularity-pilot-codes.csv"
OUT = ROOT / "data" / "vanguard" / "john-vanguard-worksheet.csv"
FIELDS = ["eligible", "exclusion_reason", "claim_target", "si_level", "temporal_status",
          "stance", "epistemic_qualification", "rhetorical_mode", "development_preference",
          "attribution", "title_only", "extrapolates_to_horizon", "notes"]


def main():
    with SUBSET.open(newline="") as f:
        subset = list(csv.DictReader(f))
    with FIRST.open(newline="") as f:
        in_first = {r["post_id"] for r in csv.DictReader(f)}
    pool = [r for r in subset if r["post_id"] in in_first]
    rng = random.Random(SEED)
    chosen = []
    for sample, k in TAKE.items():
        group = sorted((r for r in pool if r["sample"] == sample), key=lambda r: r["post_id"])
        chosen += rng.sample(group, k)
    rng.shuffle(chosen)
    with OUT.open("w", newline="") as f:
        w = csv.writer(f, lineterminator="\n")
        w.writerow(["post_id", "quarter", "sample", "post_type", "permalink"] + FIELDS)
        for r in chosen:
            w.writerow([r["post_id"], r["quarter"], r["sample"], r["post_type"], r["permalink"]]
                       + [""] * len(FIELDS))
    print(f"{len(chosen)} posts drawn from {len(pool)} (seed {SEED}) into {OUT}")


if __name__ == "__main__":
    main()
