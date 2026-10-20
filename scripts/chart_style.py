"""One look for every chart on the site: colours, figure setup, titles and saving.

A chart's title states what it found, in plain words; the line under it says what is drawn;
the bottom line names the source. Colour follows the thing (a person, a question), never its rank.
"""

import csv
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
