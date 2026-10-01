#!/usr/bin/env python3
"""Compare John's blind codes with the agent's codes for the double-coding sample.

Reads data/double-coding/john-sample.csv (John fills the five code columns) and
data/double-coding/agent-codes.csv, and reports for each field: how many statements
both coded, the share where the codes match, and Cohen's kappa (agreement corrected for
chance). Lists every disagreement. Blank cells in John's file are left out of the counts.

The pass check (methodology-v2 section 12) asks for at least 80% agreement on
frame_primary, endorsement and target_capability.

    python3 scripts/agreement.py
"""

import csv
import sys
from collections import Counter
from pathlib import Path

DIR = Path(__file__).resolve().parent.parent / "data" / "double-coding"
FIELDS = ["target_capability", "frame_primary", "endorsement", "present_capability", "affect"]
PASS_FIELDS = {"target_capability", "frame_primary", "endorsement"}
THRESHOLD = 0.80


def load(name):
    with (DIR / name).open(newline="", encoding="utf-8") as f:
        return {r["statement_id"]: r for r in csv.DictReader(f)}


def kappa(pairs):
    """Cohen's kappa for a list of (code_a, code_b) pairs."""
    n = len(pairs)
    if n == 0:
        return None
    observed = sum(a == b for a, b in pairs) / n
    ca, cb = Counter(a for a, _ in pairs), Counter(b for _, b in pairs)
    expected = sum(ca[k] * cb[k] for k in set(ca) | set(cb)) / (n * n)
    return 1.0 if expected == 1 else (observed - expected) / (1 - expected)


def main():
    john, agent = load("john-sample.csv"), load("agent-codes.csv")
    missing = sorted(set(john) ^ set(agent))
    if missing:
        sys.exit(f"the two files list different statements: {missing}")
    print(f"{len(john)} statements in the sample\n")
    print(f"{'field':20} {'coded':>5} {'agree':>7} {'kappa':>7}  pass check")
    disagreements, ok = [], True
    for field in FIELDS:
        pairs = [(john[s][field].strip(), agent[s][field].strip())
                 for s in john if john[s][field].strip()]
        if not pairs:
            print(f"{field:20} {0:>5} {'-':>7} {'-':>7}  not yet coded")
            ok = False if field in PASS_FIELDS else ok
            continue
        share = sum(a == b for a, b in pairs) / len(pairs)
        k = kappa(pairs)
        verdict = ""
        if field in PASS_FIELDS:
            verdict = "meets 80%" if share >= THRESHOLD else "BELOW 80%"
            ok = ok and share >= THRESHOLD
        print(f"{field:20} {len(pairs):>5} {share:>7.0%} {k:>7.2f}  {verdict}")
        disagreements += [(s, field, john[s][field], agent[s][field])
                          for s in john if john[s][field].strip()
                          and john[s][field].strip() != agent[s][field].strip()]
    if disagreements:
        print("\nDisagreements (statement, field, John, agent):")
        for d in disagreements:
            print("  " + " | ".join(d))
    print("\nPass check:", "met" if ok else "not met (or not yet fully coded)")


if __name__ == "__main__":
    main()
