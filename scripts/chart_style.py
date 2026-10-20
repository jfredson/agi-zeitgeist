"""One look for every chart on the site: colours, figure setup, titles and saving.

A chart's title states what it found, in plain words; the line under it says what is drawn;
the bottom line names the source. Colour follows the thing (a person, a question), never its rank.
"""

import csv
import statistics
import tomllib
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


def tip_only(row):
    """A statement that came in by tip and that the fixed searches did not find (docs/tip-intake.md).
    It stays in the record and out of every figure and share (ruled by John 2026-10-18)."""
    return any(part.strip().split(":")[0].strip() == "tip_only" for part in (row.get("notes") or "").split(";"))


# The frozen panel's two tiers (amendment A18). The opinion record (figures, shares, the panel's counts)
# reads only these; the claims ledger's ledger-only list (tier claims_only, A30) never enters it.
PANEL_TIERS = ("core", "cohort_2020s")


def panel(speakers):
    """The speaker ids on the frozen panel, from the rows of speakers.csv."""
    return {r["speaker_id"] for r in speakers if r["tier"] in PANEL_TIERS}


def measured(rows):
    """The statements figures and shares are computed from: every row except tip_only rows."""
    return [r for r in rows if not tip_only(r)]


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
    return c["kind"] == "timing" and c.get("arrives") in DRAWN and c.get("form") != "chance_tail"


def nearest(cs):
    """The nearest year named among one day's forecasts: the late end of each, ignoring 'not before'."""
    ys = [c["due"] for c in cs if c.get("form") != "not_before"]
    return min(ys) if ys else None


def academics_band(statements=None, speakers=None):
    """The academics and long-time thinkers: panel members not tagged as builders, leaving out all fifteen
    leaders, and their dated guesses since 2023 from the frontier-voices rows. The middle half and the middle."""
    from charts import frontier_rows  # the same rows as the home page's frontier-voices chart
    v = sorted(r["year"] for r in frontier_rows(statements, speakers)
               if not r["builder"] and r["speaker"] not in LEADERS and r["said"] >= 2023)
    if len(v) < 8:
        return None
    return dict(n=len(v), low=v[len(v) // 4], middle=statistics.median(v), high=v[3 * len(v) // 4])


def leaders_now(claims=None, words=None):
    """For each of the fifteen: the forecasts from the latest day they gave a drawn one, the nearest year
    among them, their latest dated prediction of any kind, and their latest undated words on when."""
    claims = claims if claims is not None else load_claims()
    words = words if words is not None else load_words()
    out = {}
    for sp in LEADERS:
        mine = [c for c in claims if c["speaker_id"] == sp]
        d = [c for c in mine if drawn(c)]
        day = max((str(c["when"]) for c in d), default=None)
        latest = [c for c in d if str(c["when"]) == day]
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
            if c["speaker_id"] == sp and drawn(c) and int(str(c["when"])[:4]) >= since:
                days.setdefault(str(c["when"]), []).append(c)
        named = [(d, nearest(cs)) for d, cs in sorted(days.items()) if nearest(cs) is not None]
        if len(named) >= 2:
            first, last = named[0][1], named[-1][1]
            out[sp] = dict(first=first, last=last, way="nearer" if last <= first - 1 else "later" if last >= first + 1 else "held")
    return out
