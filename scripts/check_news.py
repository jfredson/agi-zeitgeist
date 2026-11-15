#!/usr/bin/env python3
"""AGI Zeitgeist Tracker: refuse a news post that cannot be trusted (tracker pattern, rule 4.16).

Plain Python, standard library only. Run from anywhere:

    python3 scripts/check_news.py                 check docs/news/, print the count
    python3 scripts/check_news.py --posts DIR --amendments FILE --cards DIR --claims DIR   (for tests)

A post is one Markdown file, YYYY-MM-DD-slug.md, with a frontmatter block. The records on this
site are rows and amendments, not pages (tracker pattern, section 9), so a post names the
amendment it explains (A25) or one of the four parts of the test (A, B, C, D). The check refuses a
post that: has a file name not of that form, or a frontmatter date that differs from it; carries
a kind outside the eight (the eighth, "year-review", proposed 2026-11-15 for the year-end post and not yet ruled); names no record, or an amendment that is not in docs/amendments.md (the
opener, kind "start-here", is the one post that need not name a record); cites no source with an
https address; states a figure (any digit) in a paragraph that carries no link (a Markdown link
or a written-out https address) to a source or a record (a table is covered by the record links
the page draws under the post); names an amendment whose section carries no date within fourteen
days of the post's date; or has no card drawn beside it (site/news/<slug>-card.png, from
scripts/news_cards.py). The rules are John's of 2026-10-18.

It also refuses every post while any claim on the site carries an open check: a non-empty
`verify` line in a file of data/claims/ (the list of facts set down before their source was
opened). That is rule 3.3 part 4 of the tracker pattern, ruled by John on 2026-10-17: nothing
that sends readers to the site goes out while a fact waits to be checked, and the count across
the site must be none. Added 2026-11-09, on John's ruling of that day, after posts went out on
2026-10-19 and 2026-10-21 while ten checks were open. The rule is kept strict: while a check is
open the check fails, so the site is not rebuilt until the check is cleared or the fact removed.

Pictures (tracker pattern, rule 4.23, in force since 2026-11-14). A post may show real photographs
of its event. The check refuses a post whose picture: is not written as a <figure> with an <img> and
a <figcaption>; is loaded from another site and not from /news/ here; has no description (alt); has
no entry under `photos:` in the frontmatter giving its file, source page, credit, licence, licence
link and the day the licence was read; has a caption that does not link to that source page; or is
listed under `photos:` and not shown. It also refuses a listed picture whose file is not in the
folder the site serves at /news/. The check cannot tell whether a licence really allows the use:
that is read on the source page by whoever adds the picture, and the entry records that it was.
"""
from __future__ import annotations

import argparse
import re
import sys
import tomllib
from datetime import date, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
KINDS = {"start-here", "rung-reached", "estimate-revised", "flagged-item-ruled", "claim", "headline-moved", "method-changed", "year-review"}
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


def open_checks(claims_dir: Path) -> list[tuple[str, str]]:
    """Every claim whose `verify` line is not empty, as (file name, what waits to be checked).
    A file that cannot be read counts as open, because what it holds cannot be known."""
    out: list[tuple[str, str]] = []
    for path in sorted(claims_dir.glob("*.toml")) if claims_dir.exists() else []:
        try:
            claim = tomllib.loads(path.read_text(encoding="utf-8")).get("claim", {})
        except (tomllib.TOMLDecodeError, UnicodeDecodeError) as e:
            out.append((path.name, f"cannot be read: {e}")); continue
        v = claim.get("verify") if isinstance(claim, dict) else None
        if isinstance(v, str) and v.strip():
            out.append((path.name, v.strip()))
    return out


PHOTO_FIELDS = ("source", "credit", "licence", "licence_url", "read_on")
FIGURE_RE = re.compile(r"<figure\b.*?</figure>", re.S | re.I)
IMG_RE = re.compile(r"<img\b[^>]*>", re.I)


def _attr(tag: str, name: str) -> str | None:
    m = re.search(rf'\b{name}\s*=\s*"([^"]*)"', tag, re.I)
    return m.group(1) if m else None


def check_photos(name: str, fm: dict, body: str, pictures_dir: Path | None) -> list[str]:
    """The pictures in one post (tracker pattern, rule 4.23, in force since 2026-11-14). Every picture
    the post shows is written as a <figure> holding an <img> and a <figcaption>, is kept on this site,
    carries a description for readers who cannot see it, and has an entry under `photos:` in the
    frontmatter naming its file, its source page, its credit, its licence with a link, and the day the
    licence was read. The caption links to the source page. Every entry is a picture the post shows."""
    problems: list[str] = []
    listed: dict[str, dict] = {}
    for ph in fm.get("photos") or []:
        if not isinstance(ph, dict) or not ph.get("file"):
            problems.append(f"{name}: an entry under photos names no file"); continue
        f = ph["file"]
        listed[f] = ph
        for field in PHOTO_FIELDS:
            if not str(ph.get(field) or "").strip():
                problems.append(f"{name}: the picture {f} has no {field} under photos")
        for field in ("source", "licence_url"):
            v = str(ph.get(field) or "")
            if v and not v.startswith("https://"):
                problems.append(f"{name}: the picture {f} gives a {field} that is not an https address")
        if ph.get("read_on"):
            try:
                date.fromisoformat(str(ph["read_on"]))
            except ValueError:
                problems.append(f"{name}: the picture {f} gives a read_on that is not a date (YYYY-MM-DD)")
        if pictures_dir is not None and not (pictures_dir / f).is_file():
            problems.append(f"{name}: the picture file {f} is not in {pictures_dir.name}/; a picture is kept on this site")
    if re.search(r"!\[[^\]]*\]\(", body):
        problems.append(f"{name}: a picture is written as ![...](...); write it as a <figure> with a <figcaption>")
    outside = FIGURE_RE.sub("", body)
    if IMG_RE.search(outside):
        problems.append(f"{name}: a picture stands outside a <figure>; every picture needs a caption")
    shown: set[str] = set()
    for fig in FIGURE_RE.findall(body):
        caption = re.search(r"<figcaption\b.*?</figcaption>", fig, re.S | re.I)
        for tag in IMG_RE.findall(fig):
            src = _attr(tag, "src") or ""
            f = src.rsplit("/", 1)[-1]
            shown.add(f)
            if not src.startswith("/news/"):
                problems.append(f"{name}: the picture {src or '(no address)'} is not served from /news/ on this site")
            if not (_attr(tag, "alt") or "").strip():
                problems.append(f"{name}: the picture {f} has no description (alt) for readers who cannot see it")
            if not caption:
                problems.append(f"{name}: the picture {f} has no caption")
            if f not in listed:
                problems.append(f"{name}: the picture {f} has no entry under photos (file, source, credit, licence, licence_url, read_on)")
            elif caption and listed[f].get("source") and str(listed[f]["source"]) not in caption.group(0):
                problems.append(f"{name}: the caption of {f} does not link to its source page")
    for f in listed:
        if f not in shown:
            problems.append(f"{name}: photos lists {f}, which the post does not show")
    return problems


def check(posts_dir: Path, amend: dict[str, list[str]], cards_dir: Path | None,
          checks: list[tuple[str, str]] | None = None, pictures_dir: Path | None = None) -> tuple[list[str], int]:
    problems: list[str] = []
    files = sorted(posts_dir.glob("*.md")) if posts_dir.exists() else []
    if checks and files:
        problems.append(f"{len(checks)} claim(s) carry an open check, so no post may go out "
                        f"(tracker pattern, rule 3.3 part 4); clear each check at its source or remove the fact:")
        problems.extend(f"  {name}: {what}" for name, what in checks)
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
            problems.append(f"{name}: kind {kind!r} is not one of the listed kinds")
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
        problems.extend(check_photos(name, fm, body, pictures_dir))
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
    ap.add_argument("--claims", default=str(ROOT / "data" / "claims"))
    ap.add_argument("--no-cards", action="store_true")
    ap.add_argument("--pictures", default=str(ROOT / "site" / "news"), help="the folder the site serves at /news/, where a post's pictures are kept")
    a = ap.parse_args(argv)
    amend = amendments(Path(a.amendments).read_text(encoding="utf-8")) if Path(a.amendments).exists() else {}
    problems, n = check(Path(a.posts), amend, None if a.no_cards else Path(a.cards), open_checks(Path(a.claims)), pictures_dir=Path(a.pictures) if a.pictures else None)
    if problems:
        print("\n".join(problems), file=sys.stderr)
        print(f"{len(problems)} problem(s) in {n} post(s)", file=sys.stderr)
        return 1
    print(f"OK: {n} news post(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
