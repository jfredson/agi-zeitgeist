#!/usr/bin/env python3
"""Draw the blind second-coder subset for the r/singularity pilot (run record: 30% of
screened posts per quarter and sample, rounded up, seed 20261004).

Reads data/vanguard/r-singularity-pilot-codes.csv (first pass). Writes:
  data/vanguard/second-coder-worksheet.csv   for human coders: post id, quarter, sample,
                                             link and post type, with empty code columns
  <scratch>/second_posts.json                for the blind model second pass: the same
                                             posts' content, without first-pass codes

    python3 scripts/vanguard_second_subset.py
"""

import csv
import json
import math
import random
from pathlib import Path

SEED = 20261004
FRACTION = 0.30
ROOT = Path(__file__).resolve().parent.parent
CODES = ROOT / "data" / "vanguard" / "r-singularity-pilot-codes.csv"
SHEET = ROOT / "data" / "vanguard" / "second-coder-worksheet.csv"
WORK = Path.home() / "Documents" / ".agi-zeitgeist" / "work" / "vanguard_pilot"
FIELDS = ["eligible", "exclusion_reason", "claim_target", "si_level", "temporal_status",
          "forecast_horizon", "stance", "epistemic_qualification", "rhetorical_mode",
          "development_preference", "attribution", "frame_tags", "title_only"]


def main():
    with CODES.open(newline="") as f:
        rows = list(csv.DictReader(f))
    posts = {}
    for r in rows:
        posts.setdefault((r["quarter"], r["sample"]), {})[r["post_id"]] = int(r["rank_or_draw"])
    rng = random.Random(SEED)
    chosen = []
    for key in sorted(posts):
        ids = sorted(posts[key], key=lambda i: posts[key][i])
        k = math.ceil(FRACTION * len(ids))
        chosen += [(key[0], key[1], i) for i in sorted(rng.sample(ids, k), key=lambda i: posts[key][i])]
    content = {p["post_id"]: p for p in json.loads((WORK / "posts.json").read_text())}
    SHEET.parent.mkdir(parents=True, exist_ok=True)
    with SHEET.open("w", newline="") as f:
        w = csv.writer(f, lineterminator="\n")
        w.writerow(["post_id", "quarter", "sample", "post_type", "permalink"] + FIELDS)
        for q, s, i in chosen:
            w.writerow([i, q, s, content[i]["post_type"], content[i]["permalink"]] + [""] * len(FIELDS))
    blind = [{k: content[i][k] for k in ("quarter", "sample", "post_id", "post_type", "title",
                                         "selftext", "url", "image_file", "permalink")} for q, s, i in chosen]
    (WORK / "second_posts.json").write_text(json.dumps(blind, indent=1))
    print(f"{len(chosen)} posts in the second-coder subset ({FRACTION:.0%} per quarter and sample, seed {SEED})")


if __name__ == "__main__":
    main()
