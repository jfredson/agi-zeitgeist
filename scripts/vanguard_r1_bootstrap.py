#!/usr/bin/env python3
"""How much the R1a and R1b trial results could move by chance.

The split trials compare kappas on about 65 eligible posts per pair, so a difference of
0.1 may be noise. This resamples the 112 trial posts with replacement (2,000 times, fixed
seed) and, for each pair of models, reports the kappa with the rule, without it, and the
change, each with a 90% range (the 5th to 95th percentile of the resamples). "Without" is
the other split's run: same codebook and date, only the rule under test missing. The same
resampled posts are used for both runs, so the range of the change reflects the pairing.

    python3 scripts/vanguard_r1_bootstrap.py
"""

import csv
import random
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from vanguard_agreement import kappa  # noqa: E402
from vanguard_three_way import PAIRS, R1_POSTS, SPLIT, load, value  # noqa: E402

SEED, DRAWS = 20261004, 2000
TESTS = (("R1a", "stance", "r1a-trial", "r1b-trial"), ("R1b", "attribution", "r1b-trial", "r1a-trial"))


def pairs_for(codes, a, b, field, ids):
    out = []
    for i in ids:
        x, y = codes[a].get(i), codes[b].get(i)
        if x and y and value(x, "eligible") == "yes" == value(y, "eligible"):
            out.append((value(x, field), value(y, field)))
    return out


def pct(xs, p):
    xs = sorted(xs)
    return xs[min(len(xs) - 1, int(p * len(xs)))]


def main():
    with R1_POSTS.open(newline="") as f:
        ids = [r["post_id"] for r in csv.DictReader(f)]
    runs = {tag: {m: load(p, set(ids)) for m, p in SPLIT[tag].items()} for tag in SPLIT}
    rng = random.Random(SEED)
    samples = [[rng.choice(ids) for _ in ids] for _ in range(DRAWS)]
    for rule, field, with_tag, without_tag in TESTS:
        print(f"\n{rule} on {field}: kappa with / without the rule, and the change (90% range)")
        for a, b in PAIRS:
            w = kappa(pairs_for(runs[with_tag], a, b, field, ids))
            wo = kappa(pairs_for(runs[without_tag], a, b, field, ids))
            bw, bwo, bd = [], [], []
            for s in samples:
                kw = kappa(pairs_for(runs[with_tag], a, b, field, s))
                kwo = kappa(pairs_for(runs[without_tag], a, b, field, s))
                bw.append(kw)
                bwo.append(kwo)
                bd.append(kw - kwo)
            share_up = sum(d > 0 for d in bd) / DRAWS
            print(f"  {a}-{b}: with {w:.2f} ({pct(bw, .05):.2f} to {pct(bw, .95):.2f}); "
                  f"without {wo:.2f} ({pct(bwo, .05):.2f} to {pct(bwo, .95):.2f}); "
                  f"change {w - wo:+.2f} ({pct(bd, .05):+.2f} to {pct(bd, .95):+.2f}); "
                  f"rule higher in {share_up:.0%} of resamples")


if __name__ == "__main__":
    main()
