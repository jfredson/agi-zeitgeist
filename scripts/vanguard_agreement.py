#!/usr/bin/env python3
"""Agreement between two codings of the r/singularity pilot subset.

Compares, post by post: eligibility; for posts both coders found eligible, the main
claim's fields (claim_n 1); and the four post-level claims the pilot figure reports.
Prints, per field, how many posts both coded, percentage agreement, and Cohen's kappa
(agreement corrected for chance).

    python3 scripts/vanguard_agreement.py data/vanguard/r-singularity-pilot-codes.csv \
        data/vanguard/r-singularity-pilot-codes-second.csv
"""

import csv
import sys
from collections import Counter

MAIN_FIELDS = ["claim_target", "temporal_status", "stance", "epistemic_qualification",
               "rhetorical_mode", "development_preference", "attribution", "title_only",
               "extrapolates_to_horizon"]


def load(path):
    posts = {}
    with open(path, newline="") as f:
        for r in csv.DictReader(f):
            posts.setdefault(r["post_id"], []).append(r)
    return posts


def kappa(pairs):
    n = len(pairs)
    if not n:
        return None
    po = sum(a == b for a, b in pairs) / n
    ca, cb = Counter(a for a, _ in pairs), Counter(b for _, b in pairs)
    pe = sum(ca[k] * cb[k] for k in set(ca) | set(cb)) / (n * n)
    return 1.0 if pe == 1 else (po - pe) / (1 - pe)


def indicators(claims):
    def any_(f):
        return "yes" if any(f(c) for c in claims) else "no"
    return {
        "AGI already achieved": any_(lambda c: c["claim_target"] == "agi" and c["temporal_status"] == "achieved" and c["stance"] == "affirms"),
        "AGI within a stated horizon": any_(lambda c: c["claim_target"] == "agi" and c["temporal_status"] == "forecast" and c["stance"] == "affirms" and c["forecast_horizon"].strip()),
        "self-improvement under way": any_(lambda c: c["claim_target"] == "self_improvement" and c["temporal_status"] in ("under_way", "achieved") and c["stance"] == "affirms"),
        "singularity framing": any_(lambda c: "singularity" in c["frame_tags"].lower() and c["stance"] == "affirms"),
    }


def main():
    first, second = load(sys.argv[1]), load(sys.argv[2])
    ids = sorted(set(first) & set(second))
    results = []
    elig = [(first[i][0]["eligible"], second[i][0]["eligible"]) for i in ids]
    results.append(("eligible", elig))
    both = [i for i in ids if first[i][0]["eligible"] == "yes" == second[i][0]["eligible"]]
    for field in MAIN_FIELDS:
        pairs = []
        for i in both:
            a = next((c for c in first[i] if c["claim_n"] == "1"), first[i][0])
            b = next((c for c in second[i] if c["claim_n"] == "1"), second[i][0])
            pairs.append((a.get(field, "").strip(), b.get(field, "").strip()))
        results.append((f"main claim: {field}", pairs))
    ind_a = {i: indicators(first[i]) for i in both}
    ind_b = {i: indicators(second[i]) for i in both}
    for name in ["AGI already achieved", "AGI within a stated horizon", "self-improvement under way", "singularity framing"]:
        results.append((f"post-level: {name}", [(ind_a[i][name], ind_b[i][name]) for i in both]))
    print(f"posts in both codings: {len(ids)}; eligible in both: {len(both)}\n")
    print(f"{'field':48} {'n':>4} {'agree':>7} {'kappa':>7}")
    for name, pairs in results:
        if not pairs:
            print(f"{name:48} {0:>4} {'-':>7} {'-':>7}")
            continue
        share = sum(a == b for a, b in pairs) / len(pairs)
        k = kappa(pairs)
        print(f"{name:48} {len(pairs):>4} {share:>7.0%} {k:>7.2f}")


if __name__ == "__main__":
    main()
