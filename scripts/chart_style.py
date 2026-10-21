"""One look for every chart on the site: colours, figure setup, titles and saving.

A chart's title states what it found, in plain words; the line under it says what is drawn;
the bottom line names the source. Colour follows the thing (a person, a question), never its rank.
"""

import csv
import statistics
import tomllib
from datetime import date
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
SITE = ROOT / "site"

SURFACE, INK, INK_2, GRID = "#fcfcfb", "#0b0b0b", "#52514e", "#e4e3df"
# Reference categorical palette from the dataviz skill, slots 1-8 in fixed order.
PALETTE = ["#2a78d6", "#eb6834", "#1baf7a", "#eda100", "#e87ba4", "#008300", "#4a3aa7", "#e34948"]
PEOPLE = {"kurzweil": ("Ray Kurzweil", PALETTE[0]), "hinton": ("Geoffrey Hinton", PALETTE[1]),
          "marcus": ("Gary Marcus", PALETTE[2]), "lecun": ("Yann LeCun", PALETTE[6]),
          "altman": ("Sam Altman", PALETTE[7])}
SOURCE = "Source: agizeitgeist.com/data"


def read(name):
    with (DATA / name).open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def note_tags(row):
    """The leading '; '-separated words of a row's notes, before any free text (codebook section 9)."""
    return {part.strip().split(":")[0].strip() for part in (row.get("notes") or "").split(";")}


def from_tip(row):
    """A statement that came in by tip (docs/tip-intake.md). Since amendment A32 (John, 2026-10-21) it is an
    ordinary row in every figure, shown publicly as added from a tip."""
    return "tip" in note_tags(row)


# The frozen panel's two tiers (amendment A18). The opinion record (figures, shares, the panel's counts)
# reads only these; the claims ledger's ledger-only list (tier claims_only, A30) never enters it.
PANEL_TIERS = ("core", "cohort_2020s")


def panel(speakers):
    """The speaker ids on the frozen panel, from the rows of speakers.csv."""
    return {r["speaker_id"] for r in speakers if r["tier"] in PANEL_TIERS}


def searched_through(speaker_ids, log=None, year=None):
    """The date through which every one of these people has been searched for this year's words: for each
    person, the latest date_searched of a search-log row for them and the current year; the earliest of
    those across the people (amendment A32, item 3). None if anyone has no such row."""
    year = str(year or date.today().year)
    latest = {}
    for r in (log if log is not None else read("search_log.csv")):
        if r["speaker_id"] in speaker_ids and r["year"] == year and r.get("date_searched"):
            latest[r["speaker_id"]] = max(latest.get(r["speaker_id"], ""), r["date_searched"])
    if not speaker_ids or set(speaker_ids) - set(latest):
        return None
    return min(latest.values())


def long_date(iso):
    d = date.fromisoformat(iso)
    return f"{d.day} {d:%B %Y}"


def freshness(speaker_ids, log=None):
    """The sentence every chart or headline that compares people carries (A32, item 3)."""
    d = searched_through(set(speaker_ids), log)
    return (f"Every person here searched for new words through {long_date(d)}." if d
            else "Not every person here has been searched for new words this year.")


def figure(w=10, h=6, **kw):
    """A figure on the site's surface with quiet axes: no frame, no tick marks."""
    fig, ax = plt.subplots(figsize=(w, h), dpi=160, **kw)
    fig.patch.set_facecolor(SURFACE)
    for a in (ax.flat if hasattr(ax, "flat") else [ax]):
        a.set_facecolor(SURFACE)
        a.tick_params(colors=INK_2, labelsize=9, length=0)
        for side in a.spines.values():
            side.set_visible(False)
    return fig, ax


def titles(fig, title, subtitle=None, source=SOURCE):
    fig.suptitle(title, x=0.04, y=0.975, ha="left", fontsize=14, fontweight="bold", color=INK)
    if subtitle:
        fig.text(0.04, 0.915, subtitle, fontsize=9, color=INK_2, ha="left", va="top")
    fig.text(0.04, 0.015, source, fontsize=7.5, color=INK_2)


def save(fig, name):
    out = SITE / name
    fig.savefig(out, facecolor=SURFACE)
    plt.close(fig)
    return out


# ----------------------------------------------------------------------------- the industry's voice
# The claims ledger (docs/claims-ledger-method.md, amendment A31): what the industry's leaders say now,
# set against the academics. Shared by charts.py (the two claims figures) and site.py (the claims page,
# the home-page sentence and the status file), so the page, the figures and the sentence agree.
LEADERS = ["altman", "musk", "amodei", "huang", "hassabis", "suleyman", "sutskever", "legg", "lecun",
           "liangwenfeng", "mensch", "zuckerberg", "pichai", "nadella", "kaifulee"]  # the fifteen (A30)
DRAWN = {"agi", "superintelligence", "beyond_people"}  # what a forecast must say arrives to be drawn
ARRIVES_WORDS = {"agi": "AGI or human-level AI", "superintelligence": "superintelligence",
                 "beyond_people": "AI better than people at most or all things"}


def load_claims():
    """Every claim file, oldest first."""
    out = [tomllib.loads(p.read_text(encoding="utf-8"))["claim"] for p in sorted((DATA / "claims").glob("*.toml"))]
    out.sort(key=lambda c: (str(c["when"]), c["id"]))
    return out


def load_words():
    """Every record of a leader's undated words on when (data/claims_undated/, A31), oldest first."""
    folder = DATA / "claims_undated"
    out = [tomllib.loads(p.read_text(encoding="utf-8"))["words"] for p in sorted(folder.glob("*.toml"))] if folder.exists() else []
    out.sort(key=lambda w: (str(w["when"]), w["id"]))
    return out


def drawn(c):
    """A dated forecast that goes on the claims figures: a timing claim about AGI or beyond, not the far
    tail of a stated chance (a 10% or 90% year marks the edge of a spread, not the forecast)."""
    return c["kind"] in ("timing", "capability") and c.get("arrives") in DRAWN and c.get("form") != "chance_tail"


def said_on(c):
    """Every day a claim was said: its own date and each day it was repeated unchanged (`repeated_on`)."""
    return [str(c["when"])] + [d.isoformat() for d in c.get("repeated_on") or []]


def near_end(c):
    """The nearer year a forecast names: the early end of a range, otherwise its year (a 'by' year is the
    latest it allows, so it stands as named). None for 'not before'."""
    if c.get("form") == "not_before":
        return None
    return c["due_early"] if c.get("form") == "range" else c["due"]


def nearest(cs):
    """The nearest year named among one day's forecasts (see near_end), ignoring 'not before'."""
    ys = [near_end(c) for c in cs if near_end(c) is not None]
    return min(ys) if ys else None


# Panel members not tagged as builders who nonetheless worked at a company that builds frontier AI, in any
# role. John ruled on 2026-10-20 ("(b)") that they stay among the long-time thinkers, and the page says plainly
# that they worked at OpenAI earlier in their careers (amendment A31). ACADEMICS_STRICT on would leave them out.
WORKED_AT_A_LAB = {"kokotajlo": "OpenAI, 2022 to 2024", "aschenbrenner": "OpenAI, 2023 to 2024"}
ACADEMICS_STRICT = False


def academics_band(statements=None, speakers=None, since=2023):
    """The academics and long-time thinkers, counted the way the leaders are: each person once, at their
    latest dated guess since `since`, by the nearer year it names. Panel members only, never a builder by the
    frozen tag, never one of the fifteen leaders, and (when ACADEMICS_STRICT) never anyone who worked at a
    frontier AI company in any role. Rows as the frontier-voices chart reads them (accepts, hedges or conditions
    a year for machines matching people at most thinking work; tip rows count like any other, A32)."""
    speakers = {r["speaker_id"]: r for r in (speakers or read("speakers.csv"))}
    latest = {}
    for r in sorted((statements or read("statements.csv")), key=lambda r: r["date"]):
        sp = speakers.get(r["speaker_id"])
        if (r["target_capability"] != "broad_competence" or not r.get("timeline_year")
                or r["endorsement"] not in ("accepts", "uncertain", "conditional") or int(r["date"][:4]) < since
                or not sp or sp["tier"] not in PANEL_TIERS or sp["frontier_lab"] or r["speaker_id"] in LEADERS
                or (ACADEMICS_STRICT and r["speaker_id"] in WORKED_AT_A_LAB)):
            continue
        latest[r["speaker_id"]] = dict(id=r["speaker_id"], name=sp["name"], said=r["date"], year=int(r["timeline_year"]))
    if len(latest) < 3:
        return None
    v = sorted(x["year"] for x in latest.values())
    return dict(n=len(v), people=sorted(latest.values(), key=lambda x: x["year"]), middle=statistics.median(v), low=v[0], high=v[-1])


def leaders_now(claims=None, words=None):
    """For each of the fifteen: the forecasts from the latest day they gave a drawn one, the nearest year
    among them, their latest dated prediction of any kind, and their latest undated words on when."""
    claims = claims if claims is not None else load_claims()
    words = words if words is not None else load_words()
    out = {}
    for sp in LEADERS:
        mine = [c for c in claims if c["speaker_id"] == sp]
        d = [c for c in mine if drawn(c)]
        day = max((s for c in d for s in said_on(c)), default=None)  # a repeat counts as saying it again
        latest = [c for c in d if day in said_on(c)]
        w = [x for x in words if x["speaker_id"] == sp]
        out[sp] = dict(day=day, latest=latest, nearest=nearest(latest) if latest else None,
                       any=max(mine, key=lambda c: (str(c["when"]), c["id"])) if mine else None,
                       words=w[-1] if w else None)
    return out


def moved(claims=None, since=2023):
    """Per leader with two or more days of drawn forecasts since `since`: the nearest year on the first
    such day and on the last, and whether it moved nearer, held or moved later (by a year or more)."""
    claims = claims if claims is not None else load_claims()
    out = {}
    for sp in LEADERS:
        days = {}
        for c in claims:
            if c["speaker_id"] == sp and drawn(c):
                for s in said_on(c):
                    if int(s[:4]) >= since:
                        days.setdefault(s, []).append(c)
        named = [(d, nearest(cs)) for d, cs in sorted(days.items()) if nearest(cs) is not None]
        if len(named) >= 2:
            first, last = named[0][1], named[-1][1]
            way = "nearer" if last <= first - 1 else "later" if last >= first + 1 else "held"
            # The same length of time said again from a later day ("within five years", fourteen weeks on) can cross
            # into the next year without the person moving: a restatement marked same_span counts as held.
            first_ids = {c["id"] for c in days[named[0][0]]}
            if any(c.get("same_span") and c.get("restates") in first_ids for c in days[named[-1][0]]):
                way = "held"
            out[sp] = dict(first=first, last=last, way=way)
    return out
