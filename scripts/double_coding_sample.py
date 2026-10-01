#!/usr/bin/env python3
"""Draw the blind double-coding sample (methodology-v2 sections 10 and 12; A14 ruling 13).

30 statements: 15 from Hinton and 15 from Marcus, stratified by era (2005-2015,
2016-2022, 2023 onward). Within each speaker, the 15 are split across the eras in
proportion to how many statements each era holds (largest remainder, at least one per
era that has any), then drawn at random within each era with a fixed seed.

Writes, in data/double-coding/:
  john-sample.csv   statement, source and quote, with the five codes left blank for John
  agent-codes.csv   the agent's codes for the same 30 statements, at the time of drawing

Rerunning with the same seed and the same statements.csv reproduces the same sample.

    python3 scripts/double_coding_sample.py
"""

import csv
import random
from pathlib import Path

SEED = 20261001
PER_SPEAKER = 15
SPEAKERS = ["hinton", "marcus"]
ERAS = [("2005-2015", 2005, 2015), ("2016-2022", 2016, 2022), ("2023-onward", 2023, 2100)]
FIELDS = ["target_capability", "frame_primary", "endorsement", "present_capability", "affect"]

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "data" / "double-coding"


def era_of(row):
    year = int(row["date"][:4])
    return next(name for name, lo, hi in ERAS if lo <= year <= hi)


def allocate(sizes, total):
    """Proportional allocation with largest remainder, at least one per non-empty stratum."""
    n = sum(sizes.values())
    quota = {k: total * v / n for k, v in sizes.items()}
    alloc = {k: (max(1, int(q)) if sizes[k] else 0) for k, q in quota.items()}
    alloc = {k: min(a, sizes[k]) for k, a in alloc.items()}
    while sum(alloc.values()) < total:
        k = max((k for k in sizes if alloc[k] < sizes[k]),
                key=lambda k: quota[k] - alloc[k])
        alloc[k] += 1
    while sum(alloc.values()) > total:
        k = max((k for k in sizes if alloc[k] > 1), key=lambda k: alloc[k] - quota[k])
        alloc[k] -= 1
    return alloc


def main():
    with (ROOT / "data" / "statements.csv").open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    rng = random.Random(SEED)
    chosen = []
    for sp in SPEAKERS:
        mine = sorted((r for r in rows if r["speaker_id"] == sp), key=lambda r: r["statement_id"])
        by_era = {name: [r for r in mine if era_of(r) == name] for name, _, _ in ERAS}
        alloc = allocate({k: len(v) for k, v in by_era.items()}, PER_SPEAKER)
        for name, _, _ in ERAS:
            picked = rng.sample(by_era[name], alloc[name])
            chosen += picked
            print(f"{sp} {name}: {len(by_era[name])} statements, drew {alloc[name]}")
    rng.shuffle(chosen)  # so the file is not grouped by speaker or era

    OUT.mkdir(parents=True, exist_ok=True)
    with (OUT / "john-sample.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, lineterminator="\n")
        w.writerow(["statement_id", "speaker", "date", "source_url", "quote"] + FIELDS)
        for r in chosen:
            w.writerow([r["statement_id"], r["speaker_id"], r["date"], r["source_url"],
                        r["quote"]] + [""] * len(FIELDS))
    with (OUT / "agent-codes.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, lineterminator="\n")
        w.writerow(["statement_id", "coder"] + FIELDS)
        for r in chosen:
            w.writerow([r["statement_id"], r["coder"]] + [r[k] for k in FIELDS])
    print(f"seed {SEED}: wrote {len(chosen)} statements to {OUT}")


if __name__ == "__main__":
    main()
