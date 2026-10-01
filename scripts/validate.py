#!/usr/bin/env python3
"""Check every row in data/*.csv against the codebook and methodology.

Exits 1 and lists every problem found, or exits 0 and prints row counts.
Standard library only, so anyone can run it: python3 scripts/validate.py
"""

import csv
import re
import sys
from datetime import date
from pathlib import Path

DATA = Path(__file__).resolve().parent.parent / "data"

HEADERS = {
    "speakers.csv": ["speaker_id", "name", "speaker_type", "role_summary",
                     "frontier_lab_tie", "panel_tier", "inclusion_note"],
    # Version 2 fields (docs/methodology-v2.md section 2).
    "statements.csv": ["statement_id", "speaker_id", "date", "date_precision",
                       "source_url", "source_type", "quote", "claim_summary",
                       "target_capability", "frame_primary", "frames_present",
                       "concern_tag", "endorsement", "present_capability",
                       "timeline_type", "timeline_year", "timeline_year_high",
                       "timeline_prob", "timeline_text", "consequence_type",
                       "consequence_valence", "affect", "agency", "elicitation",
                       "definition_note", "coding_confidence", "ambiguous", "coder",
                       "retrieved", "notes"],
    "aggregates.csv": ["aggregate_id", "speaker_id", "date", "measure", "value",
                       "unit", "n", "source_url", "notes"],
    "events.csv": ["event_id", "date", "date_precision", "event_type", "title",
                   "description", "source_url", "notes"],
    "search_log.csv": ["search_id", "speaker_id", "year", "query",
                       "where_searched", "what_found", "date_searched"],
}

SPEAKER_TYPES = {"individual", "survey", "prediction_market", "institution", "poll"}
PANEL_TIERS = {"core", "cohort_2020s"}
SOURCE_TYPES = {"interview", "talk", "paper", "blog", "podcast", "social_post",
                "book", "survey_response", "testimony"}
TARGETS = {"conversation", "narrow_task", "broad_competence", "superintelligence",
           "si_assist", "si_research", "si_modify", "si_sustained", "none"}
FRAMES = {"possibility", "timeline", "capability_now", "self_improvement",
          "definition", "consequences", "governance", "other_concern"}
CONCERN_TAGS = {"jobs", "reliability", "privacy", "bias", "misinformation", "military",
                "consciousness", "ownership", "other"}
ENDORSEMENT = {"accepts", "rejects", "uncertain", "conditional", "unexpressed"}
PRESENT = {"demonstrated", "claimed", "disputed", "hypothetical", "na"}
CONSEQUENCE_TYPES = {"existential", "economic", "social", "mixed", "unspecified"}
VALENCE = {"beneficial", "harmful", "mixed", "unspecified"}
AFFECT = {"enthusiasm", "fear", "resignation", "neutral", "mixed", "unexpressed"}
AGENCY = {"can_influence", "cannot_influence", "unexpressed"}
ELICITATION = {"unprompted", "interview", "survey", "quoted"}
TIMELINE_TYPES = {"point_year", "range", "prob_by_year", "qualitative", "none"}
CONFIDENCE = {"high", "medium", "low"}
CODERS = {"john", "claude-agent", "claude-agent-v2"}
# Single-valued coded fields and their allowed values.
CODED_FIELDS = {
    "target_capability": TARGETS, "frame_primary": FRAMES, "endorsement": ENDORSEMENT,
    "present_capability": PRESENT, "consequence_type": CONSEQUENCE_TYPES,
    "consequence_valence": VALENCE, "affect": AFFECT, "agency": AGENCY,
    "elicitation": ELICITATION, "coding_confidence": CONFIDENCE,
}
UNITS = {"year", "probability", "percent_of_respondents", "index"}
EVENT_TYPES = {"open_letter", "public_statement", "government_action", "report"}
PRECISION_PATTERNS = {
    "day": re.compile(r"^\d{4}-\d{2}-\d{2}$"),
    "month": re.compile(r"^\d{4}-\d{2}$"),
    "year": re.compile(r"^\d{4}$"),
}
NOTE_TAGS = {"secondhand", "incidental", "sampled", "lower_bound"}
# Books, papers and recorded talks may carry a full citation instead of a link.
CITATION_TYPES = {"book", "paper", "talk"}
SLUG = re.compile(r"^[a-z0-9][a-z0-9_-]*$")

errors = []
warnings = []


def err(file, row_num, msg):
    errors.append(f"{file} row {row_num}: {msg}")


def warn(file, row_num, msg):
    warnings.append(f"{file} row {row_num}: {msg}")


def read(name):
    path = DATA / name
    if not path.exists():
        errors.append(f"{name}: file missing")
        return []
    with path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        if reader.fieldnames != HEADERS[name]:
            errors.append(f"{name}: header is {reader.fieldnames}, expected {HEADERS[name]}")
            return []
        rows = list(reader)
    for i, row in enumerate(rows, start=2):
        if None in row or any(v is None for v in row.values()):
            err(name, i, "wrong number of columns")
    return rows


def valid_date(value, precision=None):
    """True if value is a real date in the form precision asks for (any form if None)."""
    forms = [precision] if precision else ["day", "month", "year"]
    for form in forms:
        pattern = PRECISION_PATTERNS.get(form)
        if pattern and pattern.match(value or ""):
            parts = [int(p) for p in value.split("-")] + [1, 1]
            try:
                d = date(parts[0], parts[1], parts[2])
            except ValueError:
                return False
            return date(1990, 1, 1) <= d <= date.today()
    return False


def valid_source(url, source_type=None):
    if re.match(r"^https?://\S+$", url or ""):
        return True
    return source_type in CITATION_TYPES and (url or "").startswith("cite: ") and len(url) > 20


def as_int(value):
    try:
        return int(value)
    except (TypeError, ValueError):
        return None


def note_tags(notes):
    """Tags are the leading '; '-separated words before any free text."""
    tags = set()
    for part in (notes or "").split(";"):
        word = part.strip().split(":")[0].strip()
        if word in NOTE_TAGS:
            tags.add(word)
    return tags


def unique(name, rows, key):
    seen = set()
    for i, row in enumerate(rows, start=2):
        value = row.get(key)
        if not value:
            err(name, i, f"{key} is blank")
        elif value in seen:
            err(name, i, f"duplicate {key} {value!r}")
        seen.add(value)


def check_speakers(rows):
    unique("speakers.csv", rows, "speaker_id")
    for i, r in enumerate(rows, start=2):
        f = "speakers.csv"
        if r["speaker_id"] and not SLUG.match(r["speaker_id"]):
            err(f, i, f"speaker_id {r['speaker_id']!r} is not a lowercase slug")
        if not r["name"]:
            err(f, i, "name is blank")
        if r["speaker_type"] not in SPEAKER_TYPES:
            err(f, i, f"invalid speaker_type {r['speaker_type']!r}")
        if r["frontier_lab_tie"] not in {"yes", "no"}:
            err(f, i, f"frontier_lab_tie must be yes or no, got {r['frontier_lab_tie']!r}")
        if r["speaker_type"] == "individual":
            if r["panel_tier"] not in PANEL_TIERS:
                err(f, i, f"individual needs panel_tier core or cohort_2020s, got {r['panel_tier']!r}")
            if not r["inclusion_note"]:
                err(f, i, "individual needs an inclusion_note")
        elif r["panel_tier"]:
            err(f, i, "panel_tier must be blank for non-individual sources")
        if not r["role_summary"]:
            err(f, i, "role_summary is blank")


def check_statements(rows, speakers):
    f = "statements.csv"
    unique(f, rows, "statement_id")
    for i, r in enumerate(rows, start=2):
        sid = r["statement_id"]
        if r["speaker_id"] not in speakers:
            err(f, i, f"speaker_id {r['speaker_id']!r} not in speakers.csv")
        if r["date_precision"] not in PRECISION_PATTERNS:
            err(f, i, f"invalid date_precision {r['date_precision']!r}")
        elif not valid_date(r["date"], r["date_precision"]):
            err(f, i, f"date {r['date']!r} is not a valid {r['date_precision']} date")
        m = re.match(r"^(.+)-(\d{4})-(\d{2})$", sid or "")
        if not m:
            err(f, i, f"statement_id {sid!r} is not <speaker>-<YYYY>-<NN>")
        else:
            if m.group(1) != r["speaker_id"]:
                err(f, i, f"statement_id {sid!r} does not start with speaker_id")
            if m.group(2) != (r["date"] or "")[:4]:
                err(f, i, f"statement_id {sid!r} year does not match date {r['date']!r}")
        if r["date"] and r["date"][:4] < "2005":
            err(f, i, "statement is before 2005, outside the dataset window")
        if r["source_type"] not in SOURCE_TYPES:
            err(f, i, f"invalid source_type {r['source_type']!r}")
        if not valid_source(r["source_url"], r["source_type"]):
            err(f, i, "missing or malformed source (needs an http(s) link, or 'cite: ...' for a book, paper or talk)")
        words = len((r["quote"] or "").split())
        if words == 0:
            err(f, i, "quote is blank")
        elif words > 60:
            err(f, i, f"quote is {words} words; limit is 60")
        if not r["claim_summary"]:
            err(f, i, "claim_summary is blank")
        check_codes(f, i, r)
        if r["coder"] not in CODERS:
            err(f, i, f"invalid coder {r['coder']!r}")
        if not valid_date(r["retrieved"], "day"):
            err(f, i, f"retrieved {r['retrieved']!r} is not a valid YYYY-MM-DD date")
        check_timeline(f, i, r)
        if "secondhand" in note_tags(r["notes"]) and r["coding_confidence"] != "low":
            err(f, i, "secondhand rows must have coding_confidence low")


def normalise(text):
    """Fold curly quotes, dashes and whitespace so a basis phrase matches its quote."""
    table = str.maketrans({"‘": "'", "’": "'", "“": '"', "”": '"',
                           "–": "-", "—": "-", "…": "..."})
    return " ".join((text or "").translate(table).lower().split())


def check_codes(f, i, r):
    """Version 2 coded fields (codebook sections 1 to 8)."""
    for field, allowed in CODED_FIELDS.items():
        if r[field] not in allowed:
            err(f, i, f"invalid {field} {r[field]!r}")
    if r["ambiguous"] not in {"yes", ""}:
        err(f, i, f"ambiguous must be 'yes' or blank, got {r['ambiguous']!r}")

    present = [p.strip() for p in (r["frames_present"] or "").split(";") if p.strip()]
    for p in present:
        if p not in FRAMES:
            err(f, i, f"invalid frame {p!r} in frames_present")
    if r["frame_primary"] and r["frame_primary"] not in present:
        err(f, i, "frames_present must include frame_primary")
    if "other_concern" in present:
        if r["concern_tag"] not in CONCERN_TAGS:
            err(f, i, f"other_concern needs a concern_tag, got {r['concern_tag']!r}")
    elif r["concern_tag"]:
        err(f, i, "concern_tag is only for units where other_concern is present")

    if (r["target_capability"] == "none") != (r["present_capability"] == "na"):
        err(f, i, "present_capability is 'na' exactly when target_capability is 'none'")

    # Endorsement is never inferred from silence: anything but 'unexpressed' must be
    # anchored to words the speaker actually said, recorded as basis: "..." in notes.
    if r["endorsement"] and r["endorsement"] != "unexpressed":
        if r["target_capability"] == "none":
            err(f, i, "no capability is claimed (target none), so endorsement must be unexpressed")
        m = re.search(r'basis:\s*"([^"]+)"', r["notes"] or "")
        if not m:
            err(f, i, f"endorsement {r['endorsement']!r} needs basis: \"<words from the quote>\" in notes")
        elif normalise(m.group(1)) not in normalise(r["quote"]):
            err(f, i, f"basis {m.group(1)!r} does not appear in the quote")

    if r["frame_primary"] == "self_improvement" and not r["target_capability"].startswith("si_"):
        warn(f, i, "self_improvement frame without an si_* target; notes should say why")


def check_timeline(f, i, r):
    tt = r["timeline_type"]
    if tt not in TIMELINE_TYPES:
        err(f, i, f"invalid timeline_type {tt!r}")
        return
    low, high = r["timeline_year"], r["timeline_year_high"]
    for label, v in (("timeline_year", low), ("timeline_year_high", high)):
        if v and not (as_int(v) and 2000 <= as_int(v) <= 2500):
            err(f, i, f"{label} {v!r} is not a year between 2000 and 2500")
    if r["timeline_prob"]:
        try:
            p = float(r["timeline_prob"])
            if not 0 <= p <= 1:
                raise ValueError
        except ValueError:
            err(f, i, f"timeline_prob {r['timeline_prob']!r} must be a number from 0 to 1")
    if tt == "none" and (low or high or r["timeline_prob"]):
        err(f, i, "timeline_type none but timeline fields are filled")
    if tt in {"point_year", "prob_by_year"} and not low:
        err(f, i, f"timeline_type {tt} needs timeline_year")
    if tt == "prob_by_year" and not r["timeline_prob"]:
        err(f, i, "timeline_type prob_by_year needs timeline_prob")
    if tt == "range":
        if not (low and high):
            err(f, i, "timeline_type range needs timeline_year and timeline_year_high")
        elif as_int(low) and as_int(high) and as_int(high) < as_int(low):
            err(f, i, "timeline_year_high is earlier than timeline_year")
    elif high:
        err(f, i, "timeline_year_high is only for timeline_type range")
    if tt == "qualitative" and not r["timeline_text"]:
        err(f, i, "timeline_type qualitative needs timeline_text")
    # "Won't happen by YYYY" is not an arrival date (amendments, agent entry 2026-09-30).
    if re.search(r"not_by:\s*\d{4}", r["notes"] or ""):
        if tt != "qualitative" or low:
            err(f, i, "not_by rows must be timeline_type qualitative with timeline_year blank")
    if "lower_bound" in note_tags(r["notes"]) and not low:
        err(f, i, "lower_bound rows need the bound in timeline_year")


def check_aggregates(rows, speakers):
    f = "aggregates.csv"
    unique(f, rows, "aggregate_id")
    for i, r in enumerate(rows, start=2):
        if r["speaker_id"] not in speakers:
            err(f, i, f"speaker_id {r['speaker_id']!r} not in speakers.csv")
        if not valid_date(r["date"]):
            err(f, i, f"date {r['date']!r} is not YYYY, YYYY-MM or YYYY-MM-DD")
        if not r["measure"]:
            err(f, i, "measure is blank")
        try:
            float(r["value"])
        except ValueError:
            err(f, i, f"value {r['value']!r} is not a number")
        if r["unit"] not in UNITS:
            err(f, i, f"invalid unit {r['unit']!r}")
        if r["n"] and as_int(r["n"]) is None:
            err(f, i, f"n {r['n']!r} is not a whole number")
        if not valid_source(r["source_url"]):
            err(f, i, "missing or malformed source_url")
        if not r["notes"]:
            err(f, i, "notes must give the definition and question wording")


def check_events(rows):
    f = "events.csv"
    unique(f, rows, "event_id")
    for i, r in enumerate(rows, start=2):
        if r["date_precision"] not in PRECISION_PATTERNS:
            err(f, i, f"invalid date_precision {r['date_precision']!r}")
        elif not valid_date(r["date"], r["date_precision"]):
            err(f, i, f"date {r['date']!r} is not a valid {r['date_precision']} date")
        if r["event_type"] not in EVENT_TYPES:
            err(f, i, f"invalid event_type {r['event_type']!r}")
        if not r["title"]:
            err(f, i, "title is blank")
        if not valid_source(r["source_url"]):
            err(f, i, "missing or malformed source_url")


def check_search_log(rows, speakers):
    f = "search_log.csv"
    unique(f, rows, "search_id")
    for i, r in enumerate(rows, start=2):
        # Searches for dated events (events.csv) have no speaker; they use "events".
        if r["speaker_id"] not in speakers and r["speaker_id"] != "events":
            err(f, i, f"speaker_id {r['speaker_id']!r} not in speakers.csv")
        if r["year"] and not (as_int(r["year"]) and 1990 <= as_int(r["year"]) <= 2100):
            err(f, i, f"year {r['year']!r} is not a year")
        if not r["query"]:
            err(f, i, "query is blank")
        if not r["where_searched"]:
            err(f, i, "where_searched is blank")
        if not valid_date(r["date_searched"], "day"):
            err(f, i, f"date_searched {r['date_searched']!r} is not a valid YYYY-MM-DD date")


def main():
    tables = {name: read(name) for name in HEADERS}
    speakers = {r["speaker_id"] for r in tables["speakers.csv"]}
    check_speakers(tables["speakers.csv"])
    check_statements(tables["statements.csv"], speakers)
    check_aggregates(tables["aggregates.csv"], speakers)
    check_events(tables["events.csv"])
    check_search_log(tables["search_log.csv"], speakers)

    # Every speaker with statements must have logged searches (sampling rule 1).
    searched = {r["speaker_id"] for r in tables["search_log.csv"]}
    for sp in sorted({r["speaker_id"] for r in tables["statements.csv"]} - searched):
        errors.append(f"statements.csv: speaker {sp!r} has statements but no searches in search_log.csv")

    for w in warnings:
        print("  warning: " + w)
    if errors:
        print(f"FAILED: {len(errors)} problem(s)")
        for e in errors:
            print("  " + e)
        sys.exit(1)
    counts = ", ".join(f"{name} {len(rows)}" for name, rows in tables.items())
    print(f"OK: {counts}")


if __name__ == "__main__":
    main()
