#!/usr/bin/env python3
"""AGI Zeitgeist Tracker: refuse a news post that cannot be trusted (tracker pattern, rule 4.16).

Plain Python, standard library only. Run from anywhere:

    python3 scripts/check_news.py                 check docs/news/, print the count
    python3 scripts/check_news.py --posts DIR --amendments FILE --cards DIR   (for tests)

A post is one Markdown file, YYYY-MM-DD-slug.md, with a frontmatter block. The records on this
site are rows and amendments, not pages (tracker pattern, section 9), so a post names the
amendment it explains (A25) or one of the four parts of the test (A, B, C, D). The check refuses a
post that: has a file name not of that form, or a frontmatter date that differs from it; carries
a kind outside the seven; names no record, or an amendment that is not in docs/amendments.md (the
opener, kind "start-here", is the one post that need not name a record); cites no source with an
https address; states a figure (any digit) in a paragraph that carries no link (a Markdown link
or a written-out https address) to a source or a record (a table is covered by the record links
the page draws under the post); names an amendment whose section carries no date within fourteen
days of the post's date; or has no card drawn beside it (site/news/<slug>-card.png, from
scripts/news_cards.py). The rules are John's of 2026-10-18.
"""
from __future__ import annotations

import argparse
import re
import sys
from datetime import date, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
KINDS = {"start-here", "rung-reached", "estimate-revised", "flagged-item-ruled", "claim", "headline-moved", "method-changed"}
LEGS = {"A", "B", "C", "D"}
WINDOW_DAYS = 14
NAME_RE = re.compile(r"^(\d{4}-\d{2}-\d{2})-([a-z0-9]+(?:-[a-z0-9]+)*)\.md$")


def frontmatter(text: str) -> tuple[dict, str]:
    if not text.startswith("---\n"):
        return {}, text
    end = text.find("\n---", 4)
    if end == -1:
        return {}, text
    head, body = text[4:end], text[end + 4:]
    data: dict = {}
    key = None
    for raw in head.split("\n"):
        if not raw.strip():
            continue
        if raw.lstrip().startswith("- ") and key is not None:
            item = raw.lstrip()[2:].strip()
            if ":" in item and not item.startswith(("http:", "https:")):
                k, v = item.split(":", 1)
                data.setdefault(key, []).append({k.strip(): v.strip().strip('"')})
            else:
                data.setdefault(key, []).append(item.strip('"'))
            continue
        if raw.startswith("  ") and ":" in raw and key is not None and isinstance(data.get(key), list) and data[key] and isinstance(data[key][-1], dict):
            k, v = raw.strip().split(":", 1)
            data[key][-1][k.strip()] = v.strip().strip('"')
            continue
        m = re.match(r"^([A-Za-z_]+):\s*(.*)$", raw)
        if not m:
            continue
        key, val = m.group(1), m.group(2).strip()
        if val == "":
            data[key] = []
        elif val.startswith("[") and val.endswith("]"):
            data[key] = [x.strip().strip('"') for x in val[1:-1].split(",") if x.strip()]
        else:
            data[key] = val.strip('"')
    return data, body


def paragraphs(body: str) -> list[str]:
    out, cur = [], []
    for line in body.split("\n"):
        s = line.strip()
        if not s or s.startswith("#") or s.startswith("|"):
            if cur:
                out.append(" ".join(cur)); cur = []
            continue
        cur.append(s)
    if cur:
        out.append(" ".join(cur))
    return out


def amendments(text: str) -> dict[str, list[str]]:
    """Each amendment's id (A25) with the dates its section mentions."""
    out: dict[str, list[str]] = {}
    cur = None
    for line in text.split("\n"):
        m = re.match(r"^###\s+(A\d+)\.", line)
        if m:
            cur = m.group(1); out[cur] = []; continue
        if cur:
            out[cur].extend(re.findall(r"\b(\d{4}-\d{2}-\d{2})\b", line))
    return out


def check(posts_dir: Path, amend: dict[str, list[str]], cards_dir: Path | None) -> tuple[list[str], int]:
    problems: list[str] = []
    files = sorted(posts_dir.glob("*.md")) if posts_dir.exists() else []
    openers = 0
    for path in files:
        name = path.name
        m = NAME_RE.match(name)
        if not m:
            problems.append(f"{name}: the file name must be YYYY-MM-DD-slug.md"); continue
        fm, body = frontmatter(path.read_text(encoding="utf-8"))
        if not fm:
            problems.append(f"{name}: no frontmatter"); continue
        for field in ("title", "date", "kind", "summary"):
            if not fm.get(field):
                problems.append(f"{name}: frontmatter has no {field}")
        if fm.get("date") and fm["date"] != m.group(1):
            problems.append(f"{name}: the frontmatter date {fm['date']} differs from the file name's {m.group(1)}")
        kind = fm.get("kind")
        if kind not in KINDS:
            problems.append(f"{name}: kind {kind!r} is not one of the seven")
        if kind == "start-here":
            openers += 1
        recs = fm.get("records") or []
        if kind != "start-here" and not recs:
            problems.append(f"{name}: names no record (records: [...])")
        try:
            when = date.fromisoformat(fm.get("date") or m.group(1))
        except ValueError:
            when = None
        for rid in recs:
            if rid in LEGS:
                continue
            if rid not in amend:
                problems.append(f"{name}: names an amendment that is not in docs/amendments.md: {rid}"); continue
            if when and kind != "start-here":
                lo, hi = when - timedelta(days=WINDOW_DAYS), when + timedelta(days=WINDOW_DAYS)
                if not any(lo <= date.fromisoformat(d) <= hi for d in amend[rid]):
                    problems.append(f"{name}: {rid} carries no date within {WINDOW_DAYS} days of {when}; a post cannot announce what the record does not show")
        sources = fm.get("sources") or []
        if not any(isinstance(s, dict) and str(s.get("url", "")).startswith("https://") for s in sources):
            problems.append(f"{name}: cites no source with an https address")
        for i, para in enumerate(paragraphs(body), 1):
            if re.search(r"\d", para) and "](" not in para and "https://" not in para:
                problems.append(f"{name}: paragraph {i} states a figure with no link to a source or a record: {para[:70]!r}")
        if cards_dir is not None and not (cards_dir / f"{path.stem}-card.png").exists():
            problems.append(f"{name}: no card beside it; run python3 scripts/news_cards.py")
    if openers > 1:
        problems.append(f"{posts_dir}: {openers} posts of kind start-here; there is one per site")
    return problems, len(files)


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--posts", default=str(ROOT / "docs" / "news"))
    ap.add_argument("--amendments", default=str(ROOT / "docs" / "amendments.md"))
    ap.add_argument("--cards", default=str(ROOT / "site" / "news"))
    ap.add_argument("--no-cards", action="store_true")
    a = ap.parse_args(argv)
    amend = amendments(Path(a.amendments).read_text(encoding="utf-8")) if Path(a.amendments).exists() else {}
    problems, n = check(Path(a.posts), amend, None if a.no_cards else Path(a.cards))
    if problems:
        print("\n".join(problems), file=sys.stderr)
        print(f"{len(problems)} problem(s) in {n} post(s)", file=sys.stderr)
        return 1
    print(f"OK: {n} news post(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
