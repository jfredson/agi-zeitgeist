#!/usr/bin/env python3
"""Draw the r/singularity pilot samples for the vanguard sub-series (stream F design).

Per quarter, 2024Q4 to 2026Q3:
  rewarded    all posts ranked by recorded score (ties: earlier post first); the top
              RESERVE are kept so coders can screen down the list until 20 are eligible
  prevalence  a seeded random sample of RANDOM_N posts drawn without regard to score;
              inclusion probability RANDOM_N / posts in the quarter

Reads the archive listing saved by scripts/retrievability_check.py. Writes
data/vanguard/r-singularity-pilot-sample.csv (IDs, ranks, probabilities; no post text)
and, for coders, a work file with titles, bodies and links in the scratch folder, plus
the images of sampled image posts. Post text and images are not committed.

    python3 scripts/vanguard_pilot_samples.py
"""

import csv
import json
import random
import time
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

SEED = 20261003
RANDOM_N = 20
RESERVE = 60
START, END = "2024-10-01", "2026-10-01"
ROOT = Path(__file__).resolve().parent.parent
CACHE = Path("/Users/john/.claude/jobs/f819dd6c/tmp/retrievability_cache.json")
WORK = Path("/Users/john/.claude/jobs/f819dd6c/tmp/vanguard_pilot")
OUT = ROOT / "data" / "vanguard" / "r-singularity-pilot-sample.csv"

import sys
sys.path.insert(0, str(ROOT / "scripts"))
from retrievability_check import post_type, quarter  # noqa: E402


def ts(day):
    return int(datetime.fromisoformat(day).replace(tzinfo=timezone.utc).timestamp())


def main():
    posts = [p for p in json.loads(CACHE.read_text()) if ts(START) <= p["created_utc"] < ts(END)]
    by_q = {}
    for p in posts:
        by_q.setdefault(quarter(p["created_utc"]), []).append(p)
    rng = random.Random(SEED)
    rows, work = [], []
    for q in sorted(by_q):
        all_q = sorted(by_q[q], key=lambda p: p["id"])
        ranked = sorted(all_q, key=lambda p: (-(p.get("score") or 0), p["created_utc"]))
        for rank, p in enumerate(ranked[:RESERVE], 1):
            rows.append(("rewarded", rank, "", p, q, len(all_q)))
        for draw, p in enumerate(rng.sample(all_q, RANDOM_N), 1):
            rows.append(("prevalence", draw, f"{RANDOM_N / len(all_q):.6f}", p, q, len(all_q)))

    OUT.parent.mkdir(parents=True, exist_ok=True)
    WORK.mkdir(parents=True, exist_ok=True)
    media = WORK / "media"
    media.mkdir(exist_ok=True)
    with OUT.open("w", newline="") as f:
        w = csv.writer(f, lineterminator="\n")
        w.writerow(["quarter", "sample", "rank_or_draw", "post_id", "created_utc", "score",
                    "num_comments", "post_type", "inclusion_probability", "posts_in_quarter"])
        for sample, n, prob, p, q, size in rows:
            w.writerow([q, sample, n, p["id"], p["created_utc"], p.get("score"),
                        p.get("num_comments"), post_type(p), prob, size])

    fetched = 0
    for sample, n, prob, p, q, size in rows:
        kind = post_type(p)
        img = ""
        if kind == "image":
            url = p.get("url") or ""
            ext = Path(url.split("?")[0]).suffix or ".jpg"
            dest = media / f"{p['id']}{ext}"
            if not dest.exists():
                try:
                    req = urllib.request.Request(url, headers={"User-Agent": "agi-zeitgeist pilot"})
                    with urllib.request.urlopen(req, timeout=30) as r:
                        dest.write_bytes(r.read())
                    fetched += 1
                    time.sleep(0.5)
                except Exception as e:  # missing images are recorded, not replaced
                    dest = None
                    img = f"unavailable ({type(e).__name__})"
            if dest:
                img = str(dest)
        work.append({"quarter": q, "sample": sample, "rank_or_draw": n, "post_id": p["id"],
                     "post_type": kind, "title": p.get("title", ""), "selftext": p.get("selftext", ""),
                     "url": p.get("url", ""), "image_file": img,
                     "permalink": f"https://www.reddit.com/comments/{p['id']}"})
    (WORK / "posts.json").write_text(json.dumps(work, indent=1))
    print(f"{len(by_q)} quarters; {len(rows)} sample rows "
          f"({sum(r[0] == 'rewarded' for r in rows)} rewarded reserve, "
          f"{sum(r[0] == 'prevalence' for r in rows)} prevalence); images fetched: {fetched}; "
          f"images unavailable: {sum(1 for x in work if x['image_file'].startswith('unavailable'))}")
    for q in sorted(by_q):
        print(f"  {q}: {len(by_q[q])} posts; prevalence inclusion probability {RANDOM_N / len(by_q[q]):.5f}")


if __name__ == "__main__":
    main()
