#!/usr/bin/env python3
"""Retrievability check for the vanguard sub-series (amendment 2026-10-02, section 5).

For one subreddit and the pilot window, tests whether a public reader can:
  1. reach the versioned source (the Arctic Shift archive API);
  2. list every post in the window (paging by post time);
  3. reproduce the ranking (stream F's top 20 posts by recorded score per quarter);
  4. retrieve the text needed to check the coding.

Writes, under docs/feasibility/:
  r-<sub>-pilot-index.csv      every listed post: id, created_utc, retrieved_on, score,
                               num_comments (no titles or text)
  r-<sub>-pilot-top-posts.csv  the top 50 per quarter with recoverability flags
and prints the summary used in vanguard-retrievability-2026-10.md.

No post text is stored. Pacing: about one request a second to the archive; one bulk
lookup per 100 posts to Reddit; one HEAD request per image link. Any refusal (HTTP 401,
403, 429) or archive timeout stops the run and keeps what it has (overnight rule).

    python3 scripts/retrievability_check.py singularity 2024-10-01 2026-10-01
"""

import csv
import json
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

ARCHIVE = "https://arctic-shift.photon-reddit.com/api/posts/search"
FIELDS = "id,created_utc,retrieved_on,score,num_comments,title,selftext,url,post_hint"
UA = "agi-zeitgeist retrievability check (public research dataset)"
TOP_N, ROBUST_N = 20, 50
ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "docs" / "feasibility"
CACHE = Path.home() / "Documents" / ".agi-zeitgeist" / "work" / "retrievability_cache.json"


class Stop(Exception):
    pass


LAST_HEADERS = {}
# Back-off waits (seconds) after the archive asks to slow down; the run stops after the last.
BACKOFF = [60, 120, 300, 600, 900]
PACE = 2.0  # seconds between archive requests


def fetch(url, method="GET"):
    req = urllib.request.Request(url, headers={"User-Agent": UA}, method=method)
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            LAST_HEADERS.clear()
            LAST_HEADERS.update({k.lower(): v for k, v in r.headers.items()})
            return r.status, r.read()
    except urllib.error.HTTPError as e:
        LAST_HEADERS.clear()
        LAST_HEADERS.update({k.lower(): v for k, v in (e.headers or {}).items()})
        return e.code, e.read()
    except (urllib.error.URLError, ConnectionError, TimeoutError, OSError) as e:
        raise Stop(f"connection problem with {urllib.parse.urlsplit(url).netloc}: {e}")


def quarter(ts):
    d = datetime.fromtimestamp(ts, timezone.utc)
    return f"{d.year}Q{(d.month - 1) // 3 + 1}"


def list_posts(sub, start, end):
    """All posts in [start, end), paging by created_utc. Resumable from the cache."""
    posts = json.loads(CACHE.read_text()) if CACHE.exists() else []
    after = (max(p["created_utc"] for p in posts)) if posts else start
    end_ts = int(datetime.fromisoformat(end).replace(tzinfo=timezone.utc).timestamp())
    seen = {p["id"] for p in posts}
    requests, tries = 0, 0
    while True:
        q = urllib.parse.urlencode({"subreddit": sub, "after": after, "before": end, "sort": "asc",
                                    "limit": 100, "fields": FIELDS})
        status, body = fetch(f"{ARCHIVE}?{q}")
        requests += 1
        try:
            data = json.loads(body or b"{}")
        except ValueError:
            data = {"error": "unreadable reply"}
        if status in (401, 403):
            CACHE.write_text(json.dumps(posts))
            raise Stop(f"archive refused access (HTTP {status}) after {requests} requests; "
                       f"{len(posts)} posts listed so far, cached for resume")
        if status != 200 or data.get("error"):
            # Throttle ("Maybe slow down a bit", HTTP 422) or rate limit (429): back off, then resume.
            CACHE.write_text(json.dumps(posts))
            if tries >= len(BACKOFF):
                raise Stop(f"archive still throttling after {tries} back-offs (HTTP {status}: "
                           f"{data.get('error')}); {len(posts)} posts listed so far, cached for resume")
            reset = LAST_HEADERS.get("x-ratelimit-reset", "")
            wait = max(BACKOFF[tries], int(reset) if reset.isdigit() else 0)
            print(f"  archive throttled (HTTP {status}: {data.get('error')}); waiting {wait}s "
                  f"(back-off {tries + 1} of {len(BACKOFF)})", flush=True)
            tries += 1
            time.sleep(wait)
            continue
        tries = 0
        batch = [p for p in (data.get("data") or []) if p["id"] not in seen]
        if not batch:
            break
        posts += batch
        seen.update(p["id"] for p in batch)
        after = max(p["created_utc"] for p in batch)
        if requests % 50 == 0:
            CACHE.write_text(json.dumps(posts))
            print(f"  {len(posts)} posts listed, up to "
                  f"{datetime.fromtimestamp(after, timezone.utc):%Y-%m-%d}", flush=True)
        if after >= end_ts:
            break
        time.sleep(PACE)
    CACHE.write_text(json.dumps(posts))
    return posts, requests


def post_type(p):
    url = (p.get("url") or "").lower()
    hint = p.get("post_hint") or ""
    if "/gallery/" in url:
        return "gallery"
    if "v.redd.it" in url or hint in ("hosted:video", "rich:video"):
        return "video"
    if hint == "image" or "i.redd.it" in url or "imgur.com" in url or url.endswith((".jpg", ".png", ".gif", ".jpeg", ".webp")):
        return "image"
    if (p.get("selftext") or "").strip() or f"/comments/{p['id']}" in url:
        return "text"
    return "link"


def archive_text_status(p, kind):
    title = (p.get("title") or "").strip()
    body = (p.get("selftext") or "").strip()
    if not title:
        return "no_title"
    if kind == "text":
        if body in ("[deleted]", "[removed]"):
            return f"body_{body.strip('[]')}_in_archive"
        return "title_and_body" if body else "title_only_text_post"
    return "title_and_link" if p.get("url") else "title_no_link"


def reddit_status(ids):
    """One bulk lookup per 100 ids on reddit.com. Returns {id: status} or raises Stop."""
    out = {}
    for i in range(0, len(ids), 100):
        chunk = ",".join("t3_" + x for x in ids[i:i + 100])
        status, body = fetch(f"https://www.reddit.com/by_id/{chunk}.json?raw_json=1")
        if status in (401, 403, 429):
            raise Stop(f"reddit.com refused the status lookup (HTTP {status})")
        if status != 200:
            raise Stop(f"reddit.com status lookup failed (HTTP {status})")
        for child in json.loads(body).get("data", {}).get("children", []):
            d = child.get("data", {})
            if d.get("removed_by_category"):
                s = f"removed ({d['removed_by_category']})"
            elif d.get("author") == "[deleted]" or (d.get("selftext") or "") == "[deleted]":
                s = "deleted by author"
            else:
                s = "live"
            out[d.get("id")] = s
        time.sleep(2.0)
    return out


def media_status(url):
    status, _ = fetch(url, method="HEAD")
    if status in (401, 403, 429) and "redd.it" in url:
        raise Stop(f"media host refused (HTTP {status})")
    return "loads" if status == 200 else f"HTTP {status}"


def main():
    sub, start, end = sys.argv[1], sys.argv[2], sys.argv[3]
    OUT.mkdir(parents=True, exist_ok=True)
    if "--cached" in sys.argv:
        # Analyse the posts already listed (after a stopped run) without new archive requests.
        posts, requests = json.loads(CACHE.read_text()), 0
    else:
        posts, requests = list_posts(sub, start, end)
    end_ts = int(datetime.fromisoformat(end).replace(tzinfo=timezone.utc).timestamp())
    start_ts = int(datetime.fromisoformat(start).replace(tzinfo=timezone.utc).timestamp())
    posts = [p for p in posts if start_ts <= p["created_utc"] < end_ts]
    # --tag NAME writes r-<sub>-pilot-index-NAME.csv etc., so a later window does not
    # overwrite an earlier one.
    tag = ("-" + sys.argv[sys.argv.index("--tag") + 1]) if "--tag" in sys.argv else ""
    with (OUT / f"r-{sub}-pilot-index{tag}.csv").open("w", newline="") as f:
        w = csv.writer(f, lineterminator="\n")
        w.writerow(["id", "created_utc", "retrieved_on", "score", "num_comments"])
        for p in sorted(posts, key=lambda p: p["created_utc"]):
            w.writerow([p["id"], p["created_utc"], p.get("retrieved_on"), p.get("score"), p.get("num_comments")])

    by_q = defaultdict(list)
    for p in posts:
        by_q[quarter(p["created_utc"])].append(p)
    top = []
    for q in sorted(by_q):
        ranked = sorted(by_q[q], key=lambda p: (-(p.get("score") or 0), p["created_utc"]))
        for rank, p in enumerate(ranked[:ROBUST_N], 1):
            top.append((q, rank, p))

    # Gaps in the listing (possible archive holes): any stretch over 24 hours with no posts.
    times = sorted(p["created_utc"] for p in posts)
    gaps = [(a, b) for a, b in zip(times, times[1:]) if b - a > 86400]

    ids = [p["id"] for _, rank, p in top]
    try:
        if "--no-reddit" in sys.argv:
            raise Stop("skipped (reddit.com refused this lookup on 2026-10-02)")
        live = reddit_status(ids)
        live_note = "checked"
    except Stop as e:
        live, live_note = {}, f"not checked: {e}"
    rows, media_note = [], "checked"
    for q, rank, p in top:
        kind = post_type(p)
        ms = ""
        if kind == "image" and rank <= TOP_N and media_note == "checked":
            try:
                ms = media_status(p["url"])
                time.sleep(0.5)
            except Stop as e:
                media_note = f"stopped: {e}"
        rows.append({"quarter": q, "rank": rank, "id": p["id"], "created_utc": p["created_utc"],
                     "score": p.get("score"), "num_comments": p.get("num_comments"),
                     "hours_to_archive_update": round(((p.get("retrieved_on") or 0) - p["created_utc"]) / 3600, 1)
                     if p.get("retrieved_on") else "",
                     "post_type": kind, "archive_text": archive_text_status(p, kind),
                     "reddit_status": live.get(p["id"], ""), "media": ms})
    with (OUT / f"r-{sub}-pilot-top-posts{tag}.csv").open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]), lineterminator="\n")
        w.writeheader()
        w.writerows(rows)

    def summary(n):
        sel = [r for r in rows if r["rank"] <= n]
        rec = [r for r in sel if r["archive_text"] in ("title_and_body", "title_and_link", "title_only_text_post")]
        lost = [r for r in sel if r["archive_text"].startswith("body_") or r["archive_text"] in ("no_title", "title_no_link")]
        live_ok = [r for r in sel if r["reddit_status"] == "live"]
        return sel, rec, lost, live_ok

    print(f"\nlisted {len(posts)} posts in {requests} archive requests; quarters: {len(by_q)}; "
          f"listing gaps over 24 h: {len(gaps)}")
    for q in sorted(by_q):
        print(f"  {q}: {len(by_q[q])} posts")
    for n in (TOP_N, ROBUST_N):
        sel, rec, lost, live_ok = summary(n)
        print(f"top {n} per quarter: {len(sel)} posts; text recoverable from archive {len(rec)} "
              f"({len(rec) / len(sel):.0%}); body lost in archive {len(lost)}; "
              f"live on reddit {len(live_ok)} ({len(live_ok) / len(sel):.0%}) [{live_note}]")
    types = defaultdict(int)
    for r in rows:
        if r["rank"] <= TOP_N:
            types[r["post_type"]] += 1
    print("top-20 post types:", dict(types))
    imgs = [r for r in rows if r["rank"] <= TOP_N and r["post_type"] == "image"]
    print(f"top-20 image links loading: {sum(r['media'] == 'loads' for r in imgs)} of {len(imgs)} [{media_note}]")
    hrs = sorted(r["hours_to_archive_update"] for r in rows if r["rank"] <= TOP_N and r["hours_to_archive_update"] != "")
    if hrs:
        print(f"hours from posting to archive capture (top 20): median {hrs[len(hrs) // 2]}, min {hrs[0]}, max {hrs[-1]}")
    for a, b in gaps[:10]:
        print(f"  gap: {datetime.fromtimestamp(a, timezone.utc):%Y-%m-%d %H:%M} to "
              f"{datetime.fromtimestamp(b, timezone.utc):%Y-%m-%d %H:%M}")


if __name__ == "__main__":
    try:
        main()
    except Stop as e:
        sys.exit(f"stopped: {e}")
