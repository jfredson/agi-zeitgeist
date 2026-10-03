#!/usr/bin/env python3
"""Blind double-coding worksheet.

  python3 scripts/worksheet.py make   writes data/double-coding/john-worksheet.md from john-sample.csv
  python3 scripts/worksheet.py fill   copies the answers in the worksheet back into john-sample.csv

The worksheet lets John code in Obsidian without editing a CSV by hand. Each statement
has five answer lines; he types one code after each colon. Blank answers stay blank.
"""
import csv, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SAMPLE = ROOT / "data/double-coding/john-sample.csv"
SHEET = ROOT / "data/double-coding/john-worksheet.md"
FIELDS = ["target_capability", "frame_primary", "endorsement", "present_capability", "affect"]

CHEAT = """# Blind coding worksheet (30 statements)

Type one code after each colon. Leave blank if you want to skip. Don't open agent-codes.csv
until you've run `python3 scripts/worksheet.py fill` and then `python3 scripts/agreement.py`.
Full rules: docs/codebook.md. Short version:

**target_capability** (what capability is the claim about?)
conversation | narrow_task | broad_competence (AGI, human-level) | superintelligence |
si_assist (AI helps humans build AI) | si_research (AI does parts of AI research) |
si_modify (edits its own code or weights) | si_sustained (each generation builds the next) | none
Loose "takeoff" or "improve itself" with no one named as the improver: si_assist.

**frame_primary** (the question the statement leads with)
possibility | timeline | capability_now | self_improvement | definition | consequences | governance | other_concern

**endorsement** (will the capability exist, ever or by the horizon the speaker names?)
accepts (will, expect, I think, a firm first-person date, 50%+ probability, a bet, "decades away")
rejects (won't happen, ever or by the horizon given; "not here yet" is NOT a rejection)
uncertain (don't know, below 50%, or a date hedged with may/might/could)
conditional (only if a stated condition holds) | unexpressed (discusses it, takes no position)

**present_capability** (does it exist now, in the speaker's view?)
demonstrated (exists, points to it) | claimed (exists, no evidence given) | disputed (current systems don't have it) |
hypothetical (future or possible) | na (only when target is none)

**affect** (only from explicit emotional cues)
enthusiasm | fear | resignation | neutral (signals detachment) | mixed | unexpressed (a plain forecast)

---
"""

def make():
    rows = list(csv.DictReader(SAMPLE.open(newline="")))
    out = [CHEAT]
    for i, r in enumerate(rows, 1):
        out.append(f"## {i}. {r['speaker']} — {r['date']}  <!-- {r['statement_id']} -->\n")
        out.append(f"Source: {r['source_url']}\n")
        out.append(f"> {r['quote'].strip()}\n")
        for f in FIELDS:
            out.append(f"- {f}: {r.get(f, '')}")
        out.append("")
    SHEET.write_text("\n".join(out))
    print(f"wrote {SHEET} ({len(rows)} statements)")

def fill():
    text = SHEET.read_text()
    blocks = re.split(r"^## \d+\. ", text, flags=re.M)[1:]
    answers = {}
    for b in blocks:
        sid = re.search(r"<!-- (\S+) -->", b).group(1)
        answers[sid] = {f: (re.search(rf"^- {f}:\s*(\S*)", b, flags=re.M).group(1).strip()) for f in FIELDS}
    rows = list(csv.DictReader(SAMPLE.open(newline="")))
    fieldnames = list(rows[0].keys())
    filled = 0
    for r in rows:
        a = answers.get(r["statement_id"], {})
        for f in FIELDS:
            r[f] = a.get(f, "")
        filled += all(a.get(f) for f in FIELDS)
    with SAMPLE.open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=fieldnames)
        w.writeheader(); w.writerows(rows)
    print(f"filled {SAMPLE}: {filled} of {len(rows)} statements fully coded")

if __name__ == "__main__":
    {"make": make, "fill": fill}[sys.argv[1]]()
