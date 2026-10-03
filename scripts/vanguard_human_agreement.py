#!/usr/bin/env python3
"""John's 40-post blind codes against each model (amendment section 9, revised 2026-10-03).

Reads data/vanguard/john-vanguard-worksheet.csv (John fills one row per post: eligibility
and the post's main claim) and compares it with the first pass (claude-opus-5-5) and the
cross-family pass (gemini-3.1-pro-preview), field by field: posts compared, agreement,
Cohen's kappa. Rows John hasn't filled are skipped.

    python3 scripts/vanguard_human_agreement.py
"""

import csv
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from vanguard_agreement import kappa, load  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
D = ROOT / "data" / "vanguard"
MODELS = {"claude-opus-5-5 (first pass)": D / "r-singularity-pilot-codes.csv",
          "gemini-3.1-pro-preview (cross-family pass)": D / "r-singularity-pilot-codes-crossfamily.csv"}
FIELDS = ["claim_target", "temporal_status", "stance", "epistemic_qualification",
          "rhetorical_mode", "development_preference", "attribution", "title_only",
          "extrapolates_to_horizon"]


def main():
    with (D / "john-vanguard-worksheet.csv").open(newline="") as f:
        john = {r["post_id"]: r for r in csv.DictReader(f) if r["eligible"].strip()}
    if not john:
        sys.exit("John's worksheet has no coded rows yet")
    for name, path in MODELS.items():
        model = load(path)
        ids = sorted(i for i in john if i in model)
        print(f"\nJohn vs {name}: {len(ids)} posts")
        print(f"{'field':40} {'n':>4} {'agree':>7} {'kappa':>7}")
        pairs = [(john[i]["eligible"].strip(), model[i][0]["eligible"]) for i in ids]
        rows = [("eligible", pairs)]
        both = [i for i in ids if john[i]["eligible"].strip() == "yes" == model[i][0]["eligible"]]
        for field in FIELDS:
            rows.append((f"main claim: {field}",
                         [(john[i][field].strip(),
                           next((c for c in model[i] if c["claim_n"] == "1"), model[i][0])[field].strip())
                          for i in both]))
        for label, p in rows:
            if not p:
                print(f"{label:40} {0:>4} {'-':>7} {'-':>7}")
                continue
            share = sum(a == b for a, b in p) / len(p)
            print(f"{label:40} {len(p):>4} {share:>7.0%} {kappa(p):>7.2f}")


if __name__ == "__main__":
    main()
