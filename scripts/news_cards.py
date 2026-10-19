#!/usr/bin/env python3
"""Draws the news posts' cards (tracker pattern, rule 4.15; John 2026-10-18): site/news/<slug>-card.png,
1200 by 630, what link previews show when a post is shared. Drawn in the Gazette skin's own tokens
(site/skin.css): the site's name as a letterspaced line in the red, the post's title in the serif on
newsprint, a kicker of News · the date · the kind, and the `before` and `after` lines from the
frontmatter as the numbers that moved. Run from anywhere after writing or retitling a post:

    .venv/bin/python scripts/news_cards.py            every post
    .venv/bin/python scripts/news_cards.py FILE ...   only those

Needs Pillow (installed with matplotlib in .venv) and this Mac's fonts; the cards are drawn here and
committed, never at deploy. scripts/check_news.py refuses a post with no card beside it.
"""
from __future__ import annotations

import re
import sys
from datetime import date
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
from check_news import frontmatter  # noqa: E402

W, H = 1200, 630
PAPER, INK, SOFT, MUTED, RED, SEPIA = "#f2f1ec", "#171614", "#363430", "#686661", "#b8322a", "#8a5a2b"
SERIF = "/System/Library/Fonts/Supplemental/Georgia.ttf"
SANS = "/System/Library/Fonts/HelveticaNeue.ttc"
MONO = "/System/Library/Fonts/Menlo.ttc"
KINDS = {"start-here": "start here", "rung-reached": "a line crossed", "estimate-revised": "a measure revised", "flagged-item-ruled": "a flagged item ruled",
         "claim": "a claim added or settled", "headline-moved": "the headline moved", "method-changed": "the method changed"}


def font(path, size, index=0):
    try:
        return ImageFont.truetype(path, size, index=index)
    except Exception:
        return ImageFont.truetype(path, size)


def wrap(d, text, f, maxw, maxlines):
    lines, cur = [], ""
    for w in text.split():
        t = (cur + " " + w).strip()
        if d.textlength(t, font=f) <= maxw:
            cur = t
        else:
            lines.append(cur); cur = w
    if cur:
        lines.append(cur)
    if len(lines) > maxlines:
        lines = lines[:maxlines]; lines[-1] = lines[-1].rstrip(",;") + " …"
    return lines


def card(path: Path, out: Path):
    fm, _ = frontmatter(path.read_text(encoding="utf-8"))
    im = Image.new("RGB", (W, H), PAPER); d = ImageDraw.Draw(im)
    for x in range(1, 6):  # the column rules, as the skin draws them
        d.line([x * W // 6, 0, x * W // 6, H], fill="#dedbd3", width=1)
    f_name = font(SANS, 26, 1); x = 72
    for ch in "AGI ZEITGEIST":
        d.text((x, 96), ch, font=f_name, fill=RED); x += d.textlength(ch, font=f_name) + 5
    f_mono = font(MONO, 24); d.text((W - 72 - d.textlength("agizeitgeist.com", font=f_mono), 96), "agizeitgeist.com", font=f_mono, fill=MUTED)
    for size in (56, 48, 42):
        f = font(SERIF, size); lines = wrap(d, fm.get("title", path.stem), f, W - 144, 9)
        if len(lines) <= 3:
            break
    lines = wrap(d, fm.get("title", path.stem), f, W - 144, 3)
    y = 176
    for ln in lines:
        d.text((72, y), ln, font=f, fill=INK); y += int(size * 1.2)
    when = date.fromisoformat(fm["date"])
    kicker = f"NEWS · {when.day} {when:%B %Y} · {KINDS.get(fm.get('kind'), fm.get('kind', ''))}".upper()
    d.text((72, H - 150), kicker, font=font(SANS, 20, 1), fill=SEPIA)
    numbers = f"{fm['before']} to {fm['after']}" if fm.get("before") and fm.get("after") else fm.get("after", "")
    f_num = font(SANS, 24); yy = H - 112
    for ln in wrap(d, numbers, f_num, W - 144, 2):
        d.text((72, yy), ln, font=f_num, fill=SOFT); yy += 32
    for yy in (40, 45):
        d.line([72, yy, W - 72, yy], fill="#c9c6bd", width=1)
    im.save(out)
    print("wrote", out)


def main(argv):
    posts = [Path(a) for a in argv] if argv else sorted((ROOT / "docs" / "news").glob("*.md"))
    (ROOT / "site" / "news").mkdir(parents=True, exist_ok=True)
    for p in posts:
        card(p, ROOT / "site" / "news" / f"{p.stem}-card.png")


if __name__ == "__main__":
    main(sys.argv[1:])
