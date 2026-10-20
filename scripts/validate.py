#!/usr/bin/env python3
"""Check every row in data/*.csv, every reading record and every claim file against the codebook, the methodology and the claims ledger method.

Exits 1 and lists every problem found, or exits 0 and prints row counts.
Standard library only, so anyone can run it: python3 scripts/validate.py
"""

import csv
import json
import re
import sys
import tomllib
from datetime import date, datetime

from zoneinfo import ZoneInfo


def pacific_today():
    """Today in Pacific time, John's clock. A cloud workspace keeps universal time, so an evening
    run would otherwise be stamped a day ahead (John's ruling, 2026-10-18)."""
    return datetime.now(ZoneInfo("America/Los_Angeles")).date()
from pathlib import Path

DATA = Path(__file__).resolve().parent.parent / "data"
# One file per run of the weekly reading (docs/weekly-reading.md), never edited.
READINGS = DATA / "readings"
# One file per dated claim by a panel member (docs/claims-ledger-method.md, amendment A27).
CLAIMS = DATA / "claims"

HEADERS = {
    # Tier and quota tags from amendment A13 (methodology-v2 section 3).
    "speakers.csv": ["speaker_id", "name", "speaker_type", "role_summary", "tier",
                     "skeptic", "non_us_uk", "philosopher", "frontier_lab",
                     "inclusion_note"],
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
    # World measures (capability readings, self-reported automation shares) for the
    # singularity-entry draft: same columns as aggregates.csv, kept in a separate file
    # so belief measures and world measures are never mixed.
    "world_measures.csv": ["aggregate_id", "speaker_id", "date", "measure", "value",
                           "unit", "n", "source_url", "notes"],
    "events.csv": ["event_id", "date", "date_precision", "event_type", "title",
                   "description", "source_url", "notes"],
    "search_log.csv": ["search_id", "speaker_id", "year", "query",
                       "where_searched", "what_found", "date_searched"],
}

SPEAKER_TYPES = {"individual", "survey", "prediction_market", "institution", "poll"}
PANEL_TIERS = {"core", "cohort_2020s", "wide"}
# The claims ledger's ledger-only list (amendment A30): people who may have claim files but are never
# panel members, never in statements.csv, the opinion charts or the panel's counts.
CLAIMS_ONLY_TIER = "claims_only"
# Who may have claim files: the frozen panel's two tiers and the ledger-only list (A27, A30).
CLAIMS_TIERS = {"core", "cohort_2020s", CLAIMS_ONLY_TIER}
QUOTA_TAGS = ["skeptic", "non_us_uk", "philosopher", "frontier_lab"]
# A quota tag is blank or "<justification> (<date>, <url>)": it needs a dated source.
TAG_EVIDENCE = re.compile(r"\d{4}(-\d{2}){0,2}.*https?://\S+")
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
CODERS = {"john", "claude-agent", "claude-agent-v2", "claude-agent-v2.1",
          # the frontier-lab traces of 2026-10-17 (Musk, Amodei, Hassabis, Sutskever; pull request 13)
          "claude-session-frontier-traces-2026-10-17"}
# Single-valued coded fields and their allowed values.
CODED_FIELDS = {
    "target_capability": TARGETS, "frame_primary": FRAMES, "endorsement": ENDORSEMENT,
    "present_capability": PRESENT, "consequence_type": CONSEQUENCE_TYPES,
    "consequence_valence": VALENCE, "affect": AFFECT, "agency": AGENCY,
    "elicitation": ELICITATION, "coding_confidence": CONFIDENCE,
}
UNITS = {"year", "probability", "percent_of_respondents", "index",
         # world_measures.csv only
         "minutes", "days", "percent", "percent_growth"}
EVENT_TYPES = {"open_letter", "public_statement", "government_action", "report", "ai_release"}  # ai_release: amendment A21
PRECISION_PATTERNS = {
    "day": re.compile(r"^\d{4}-\d{2}-\d{2}$"),
    "month": re.compile(r"^\d{4}-\d{2}$"),
    "year": re.compile(r"^\d{4}$"),
}
NOTE_TAGS = {"secondhand", "incidental", "sampled", "lower_bound",
             "tip", "tip_only", "asr_unverified"}  # tip intake (docs/tip-intake.md), ruled by John 2026-10-18
# Books, papers and recorded talks may carry a full citation instead of a link.
CITATION_TYPES = {"book", "paper", "talk"}
SLUG = re.compile(r"^[a-z0-9][a-z0-9_-]*$")

# The weekly reading (docs/weekly-reading.md, "The reading record").
READING_NAME = re.compile(r"^(\d{4}-\d{2}-\d{2})(-\d+)?$")
READING_FIELDS = ["date", "ran_at", "window_start", "window_end", "scope", "commit_before",
                  "by", "items_read", "searches", "new_rows", "flagged"]
READING_SCOPES = {"weekly", "monthly"}
READING_BY = {"hand", "scheduled"}
READING_PARTS = {"gauges", "institutions", "events"}
VERDICTS = ["quiet", "noted", "new-row", "flagged"]
# Searches that belong to no one speaker: "events" for data/events.csv (the existing rule),
# "reading" for the weekly reading's searches about a leg rather than a speaker.
SEARCH_SPEAKERS_RESERVED = {"events", "reading"}
# A reading's search ids carry its date: reading-YYYY-MM-DD-NN.
READING_SEARCH_ID = re.compile(r"^reading-(\d{4}-\d{2}-\d{2})-\d{2,}$")
URL = re.compile(r"^https?://\S+$")

# The claims ledger (docs/claims-ledger-method.md): the fields of a claim file, each with the
# kind of value it holds. "date" is YYYY-MM-DD; "when" allows YYYY-MM and YYYY too.
CLAIM_FIELDS = {
    "id": str, "speaker_id": str, "when": "when", "when_note": str, "occasion": str,
    "source_kind": str, "source_url": str, "source_locator": str, "checked_how": str,
    "quote": str, "reported_as": str, "statement_id": str, "prediction": str, "kind": str,
    "bar": str, "due": int, "due_basis": str, "due_date": "anydate", "due_early": int,
    "is_goal": bool, "has_probability": bool, "restates": str, "repeated_on": "dates",
    "status": str, "verdict_on": "date", "verdict_why": str, "verdict_source": str,
    "evidence_by": str, "direction": str, "search_ids": "strings", "notes": str, "verify": str,
    "arrives": str, "arrives_term": str, "form": str, "not_before_year": int,
}
CLAIM_REQUIRED = ["id", "speaker_id", "when", "occasion", "source_kind", "source_url",
                  "source_locator", "checked_how", "prediction", "kind", "bar", "due",
                  "due_basis", "status", "search_ids"]
CLAIM_SOURCE_KINDS = {"own_words", "transcript", "printed_qa", "coverage_only"}
CLAIM_KINDS = {"capability", "timing", "deployment"}
CLAIM_STATUSES = {"not_yet_due", "hit", "missed", "withdrawn", "unfalsifiable"}
CLAIM_SETTLED = {"hit", "missed", "withdrawn"}
CLAIM_EVIDENCE = {"outside", "maker"}
CLAIM_DIRECTIONS = {"later", "not_come", "sooner", "on_time"}
CLAIM_ID = re.compile(r"^(\d{4}-\d{2}-\d{2}|\d{4}-\d{2}|\d{4})-([a-z0-9_]+)-[a-z0-9-]+$")
CLAIM_QUOTE_WORDS = 25
# What a timing claim says arrives, and the shape of its date (amendment A31): entered by hand on
# every timing claim, never on another kind.
CLAIM_ARRIVES = {"agi", "superintelligence", "beyond_people", "other"}
CLAIM_FORMS = {"year", "range", "by", "not_before", "chance_tail"}
# A leader's undated words on when (data/claims_undated/, amendment A31): words only, never charted.
UNDATED = DATA / "claims_undated"
WORDS_FIELDS = {"id": str, "speaker_id": str, "when": "when", "when_note": str, "occasion": str, "source_kind": str,
                "source_url": str, "source_locator": str, "checked_how": str, "quote": str, "translation": str,
                "statement_id": str, "arrives": str, "about": str, "search_ids": "strings", "notes": str}
WORDS_REQUIRED = ["id", "speaker_id", "when", "occasion", "source_kind", "source_url", "source_locator",
                  "checked_how", "quote", "arrives", "about", "search_ids"]

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


def valid_date(value, precision=None, floor=date(1990, 1, 1)):
    """True if value is a real date in the form precision asks for (any form if None).
    Belief records start in 2005, so 1990 is a safe floor; world measures (the economic
    series back to 1961) pass their own floor."""
    forms = [precision] if precision else ["day", "month", "year"]
    for form in forms:
        pattern = PRECISION_PATTERNS.get(form)
        if pattern and pattern.match(value or ""):
            parts = [int(p) for p in value.split("-")] + [1, 1]
            try:
                d = date(parts[0], parts[1], parts[2])
            except ValueError:
                return False
            return floor <= d <= pacific_today()
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
        # Every row carries a tier: panel tiers for people, not_panel for other sources.
        if r["speaker_type"] == "individual":
            if r["tier"] not in PANEL_TIERS | {CLAIMS_ONLY_TIER}:
                err(f, i, f"individual needs tier core, cohort_2020s, wide or claims_only, got {r['tier']!r}")
            if r["tier"] == CLAIMS_ONLY_TIER and any(r[tag] for tag in QUOTA_TAGS):
                err(f, i, "a claims_only row is not on the panel, so it carries no panel quota tag")
            if not r["inclusion_note"]:
                err(f, i, "individual needs an inclusion_note")
        elif r["tier"] != "not_panel":
            err(f, i, f"non-individual sources need tier not_panel, got {r['tier']!r}")
        for tag in QUOTA_TAGS:
            if r[tag] and not TAG_EVIDENCE.search(r[tag]):
                err(f, i, f"quota tag {tag} needs a justification with a date and a link")
            if r[tag] and r["speaker_type"] != "individual":
                err(f, i, f"quota tag {tag} is only for individuals")
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
        # A one-letter suffix marks one row per capability of a split statement (A15).
        m = re.match(r"^(.+)-(\d{4})-(\d{2})([a-z]?)$", sid or "")
        if not m:
            err(f, i, f"statement_id {sid!r} is not <speaker>-<YYYY>-<NN>[a-z]")
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
        tags = note_tags(r["notes"])
        if "tip_only" in tags and "tip" not in tags:
            err(f, i, "tip_only is only for rows that came in by tip; the notes must also carry tip")
        if "asr_unverified" in tags and r["coding_confidence"] == "high":
            err(f, i, "asr_unverified rows must have coding_confidence medium or low")


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
        # An open-ended minimum ("at least a decade") leaves the high bound blank (A15).
        open_ended = "lower_bound" in note_tags(r["notes"])
        if not low or not (high or open_ended):
            err(f, i, "timeline_type range needs timeline_year and timeline_year_high "
                      "(or the lower_bound tag for an open-ended minimum)")
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


def check_aggregates(rows, speakers, f="aggregates.csv"):
    unique(f, rows, "aggregate_id")
    floor = date(1960, 1, 1) if f == "world_measures.csv" else date(1990, 1, 1)
    for i, r in enumerate(rows, start=2):
        if r["speaker_id"] not in speakers:
            err(f, i, f"speaker_id {r['speaker_id']!r} not in speakers.csv")
        if not valid_date(r["date"], floor=floor):
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
        # Searches for dated events (events.csv) have no speaker; they use "events". The
        # weekly reading's searches about a leg rather than a speaker use "reading".
        if r["speaker_id"] not in speakers and r["speaker_id"] not in SEARCH_SPEAKERS_RESERVED:
            err(f, i, f"speaker_id {r['speaker_id']!r} not in speakers.csv")
        if r["year"] and not (as_int(r["year"]) and 1990 <= as_int(r["year"]) <= 2100):
            err(f, i, f"year {r['year']!r} is not a year")
        if not r["query"]:
            err(f, i, "query is blank")
        if not r["where_searched"]:
            err(f, i, "where_searched is blank")
        if not valid_date(r["date_searched"], "day"):
            err(f, i, f"date_searched {r['date_searched']!r} is not a valid YYYY-MM-DD date")


def check_readings(tables, speakers):
    """Every weekly reading record in data/readings/ (docs/weekly-reading.md): the file is the
    date, every item has a verdict, two searches unless quiet with a reason, sources for every
    verdict but quiet, a for_john on every flagged item, and every search id and every appended
    row id exists. The other way round, every search-log row with a reading- prefix belongs to
    an item of the reading dated in its id."""
    search_ids = {r["search_id"] for r in tables["search_log.csv"]}
    row_ids = ({r["aggregate_id"] for r in tables["aggregates.csv"]}
               | {r["aggregate_id"] for r in tables["world_measures.csv"]}
               | {r["event_id"] for r in tables["events.csv"]})
    used_search_ids = set()
    if not READINGS.exists():
        return
    for path in sorted(READINGS.glob("*.json")):
        f = f"readings/{path.name}"
        m = READING_NAME.match(path.stem)
        if not m:
            errors.append(f"{f}: file name must be the reading's date, YYYY-MM-DD.json, with -2 on a second reading the same day")
            continue
        name_date = m.group(1)
        try:
            raw = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as e:
            errors.append(f"{f}: cannot be read as JSON: {e}")
            continue
        head = raw.get("reading") if isinstance(raw, dict) else None
        if not isinstance(head, dict):
            errors.append(f"{f}: no 'reading' object, so the record says nothing about when it ran")
            continue
        for field in READING_FIELDS:
            if field not in head or head[field] in (None, ""):
                errors.append(f"{f}: the 'reading' object is missing '{field}'")
        if head.get("date") != name_date:
            errors.append(f"{f}: the date in the record ({head.get('date')!r}) is not the date in the file name ({name_date})")
        for field in ("window_start", "window_end"):
            if head.get(field) and not valid_date(str(head[field]), "day"):
                errors.append(f"{f}: {field} {head[field]!r} is not a valid YYYY-MM-DD date")
        if head.get("window_start") and head.get("window_end") and not (
                str(head["window_start"]) <= str(head["window_end"]) <= name_date):
            errors.append(f"{f}: the window must end on or before the reading's date and start before it ends")
        if not re.match(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$", str(head.get("ran_at", ""))):
            errors.append(f"{f}: ran_at must be universal time, YYYY-MM-DDTHH:MM:SSZ")
        if head.get("scope") not in READING_SCOPES:
            errors.append(f"{f}: scope must be 'weekly' or 'monthly', not {head.get('scope')!r}")
        if head.get("by") not in READING_BY:
            errors.append(f"{f}: 'by' must be 'hand' or 'scheduled', not {head.get('by')!r}")
        if not re.match(r"^[0-9a-f]{7,40}$", str(head.get("commit_before", ""))):
            errors.append(f"{f}: commit_before must be the short hash of the commit the reading read")

        items = raw.get("items")
        if not isinstance(items, list) or not items:
            errors.append(f"{f}: a reading record needs a non-empty 'items' list")
            continue
        if head.get("items_read") != len(items):
            errors.append(f"{f}: the header says {head.get('items_read')} items were read and the record holds {len(items)}")
        seen = set()
        all_search_ids = set()
        all_new_rows = []
        flagged = 0
        for i, item in enumerate(items, 1):
            iid = item.get("id") if isinstance(item, dict) else None
            where = f"{f} item {i} ({iid or 'no id'})"
            if not isinstance(item, dict):
                errors.append(f"{where}: every item is an object")
                continue
            if not iid or not SLUG.match(str(iid)):
                errors.append(f"{where}: every item needs an 'id' that is a lowercase slug")
            elif iid in seen:
                errors.append(f"{where}: this id is used twice in the same reading")
            seen.add(iid)
            if item.get("part") not in READING_PARTS:
                errors.append(f"{where}: 'part' must be gauges, institutions or events, not {item.get('part')!r}")
            sp = item.get("speaker_id")
            if sp is not None and sp not in speakers and sp not in SEARCH_SPEAKERS_RESERVED:
                errors.append(f"{where}: speaker_id {sp!r} is not in speakers.csv (or 'events' or 'reading')")
            verdict = item.get("verdict")
            if verdict not in VERDICTS:
                errors.append(f"{where}: the verdict must be one of {', '.join(VERDICTS)}, not {verdict!r}")
            found = item.get("found")
            if not isinstance(found, str) or not found.strip():
                errors.append(f"{where}: 'found' says in plain words what the week held, and is required on every verdict")
                found = ""
            sids = item.get("search_ids")
            if not isinstance(sids, list) or any(not isinstance(x, str) or not x.strip() for x in sids):
                errors.append(f"{where}: 'search_ids' lists the search-log ids of the searches run, each a string")
                sids = []
            elif len(sids) < 2 and not (verdict == "quiet" and found):
                errors.append(f"{where}: fewer than two searches is not enough to call a week; only a 'quiet' item may list fewer, and then 'found' has to say why")
            for sid in sids:
                sm = READING_SEARCH_ID.match(sid)
                if not sm:
                    errors.append(f"{where}: search id {sid!r} is not reading-YYYY-MM-DD-NN")
                elif sm.group(1) != name_date:
                    errors.append(f"{where}: search id {sid!r} carries a different date from the reading")
                if sid not in search_ids:
                    errors.append(f"{where}: search id {sid!r} is not in search_log.csv; every search is logged")
            all_search_ids.update(sids)
            sources = item.get("sources", [])
            if not isinstance(sources, list) or any(not isinstance(x, str) or not URL.match(x.strip()) for x in sources):
                errors.append(f"{where}: 'sources' must be a list of web addresses")
            elif verdict in ("noted", "new-row", "flagged") and not sources:
                errors.append(f"{where}: a verdict of '{verdict}' has to cite the record it read; only 'quiet' may go without a source")
            new_rows = item.get("new_rows", [])
            if not isinstance(new_rows, list) or any(not isinstance(x, str) for x in new_rows):
                errors.append(f"{where}: 'new_rows' must be a list of row ids")
                new_rows = []
            if verdict == "new-row" and not new_rows:
                errors.append(f"{where}: a 'new-row' item lists the ids of the rows it appended in 'new_rows'")
            if verdict in ("quiet", "noted") and new_rows:
                errors.append(f"{where}: a '{verdict}' item appended nothing, so 'new_rows' must be empty")
            for rid in new_rows:
                if rid not in row_ids:
                    errors.append(f"{where}: appended row {rid!r} is not in aggregates.csv, world_measures.csv or events.csv")
            all_new_rows += new_rows
            fj = item.get("for_john")
            if verdict == "flagged":
                flagged += 1
                if not isinstance(fj, str) or not fj.strip():
                    errors.append(f"{where}: a flagged item needs 'for_john': what it would have done, the record, and why it stopped")
        if head.get("searches") != len(all_search_ids):
            errors.append(f"{f}: the header says {head.get('searches')} searches and the items name {len(all_search_ids)} distinct search ids")
        if head.get("flagged") != flagged:
            errors.append(f"{f}: the header says {head.get('flagged')} flagged and the items hold {flagged}")
        if isinstance(head.get("new_rows"), list):
            if sorted(head["new_rows"]) != sorted(all_new_rows):
                errors.append(f"{f}: the header's new_rows do not match the rows the items appended")
        else:
            errors.append(f"{f}: the header's new_rows must be a list of row ids (empty if none)")
        used_search_ids |= all_search_ids
    # The other way round: a reading- search that no reading item names is unaccounted for.
    for sid in sorted(search_ids):
        if sid.startswith("reading-") and sid not in used_search_ids:
            errors.append(f"search_log.csv: {sid!r} has the weekly reading's prefix but no reading item names it")


def claim_value_ok(kind, value):
    """True if value is of the kind CLAIM_FIELDS names."""
    if kind is str:
        return isinstance(value, str) and value.strip() != ""
    if kind is int:
        return isinstance(value, int) and not isinstance(value, bool)
    if kind is bool:
        return isinstance(value, bool)
    if kind == "date":
        return isinstance(value, date) and value <= pacific_today()
    if kind == "anydate":  # a due date may lie ahead
        return isinstance(value, date)
    if kind == "when":
        return isinstance(value, str) and valid_date(value)
    if kind == "dates":
        return isinstance(value, list) and value and all(isinstance(v, date) for v in value)
    if kind == "strings":
        return isinstance(value, list) and value and all(isinstance(v, str) and v.strip() for v in value)
    return False


def check_claims(tables, speakers):
    """Every claim file in data/claims/ (docs/claims-ledger-method.md): it parses, holds one
    [claim] table, every field is known and of the right kind, the required ones are there, the
    id is the file name and names the speaker and the date, the speaker is on the panel or the
    ledger-only list (A30), the
    status is one of the five words, a settled claim carries its verdict record, an
    unfalsifiable claim says why, a claim past its due date is not still not_yet_due, a quote is
    short and absent on coverage_only, a cited statement row exists and matches, a restated
    claim exists and is the same person's, no two files share an id, and every search id the
    claim names is in the search log."""
    if not CLAIMS.exists():
        return 0
    search_ids = {r["search_id"] for r in tables["search_log.csv"]}
    statements = {r["statement_id"]: r for r in tables["statements.csv"]}
    claimants = {r["speaker_id"] for r in tables["speakers.csv"]
                 if r["speaker_type"] == "individual" and r["tier"] in CLAIMS_TIERS}
    claims = {}
    files = sorted(CLAIMS.glob("*.toml"))
    for path in files:
        f = f"claims/{path.name}"
        try:
            raw = tomllib.loads(path.read_text(encoding="utf-8"))
        except (tomllib.TOMLDecodeError, UnicodeDecodeError) as e:
            errors.append(f"{f}: cannot be read as TOML: {e}")
            continue
        c = raw.get("claim")
        if not isinstance(c, dict) or set(raw) != {"claim"}:
            errors.append(f"{f}: a claim file holds exactly one [claim] table")
            continue
        for field in CLAIM_REQUIRED:
            if field not in c:
                errors.append(f"{f}: missing the required field '{field}'")
        for field, value in c.items():
            if field not in CLAIM_FIELDS:
                errors.append(f"{f}: unknown field '{field}'")
            elif not claim_value_ok(CLAIM_FIELDS[field], value):
                errors.append(f"{f}: '{field}' is not {getattr(CLAIM_FIELDS[field], '__name__', CLAIM_FIELDS[field])} (or is empty, or a date in the future)")
        cid = c.get("id")
        if isinstance(cid, str):
            if cid != path.stem:
                errors.append(f"{f}: the id {cid!r} is not the file name")
            if cid in claims:
                errors.append(f"{f}: the id {cid!r} is already used by another file")
            claims[cid] = c
            m = CLAIM_ID.match(cid)
            if not m:
                errors.append(f"{f}: the id must be <date>-<speaker_id>-<slug>")
            else:
                if m.group(1) != c.get("when"):
                    errors.append(f"{f}: the date in the id ({m.group(1)}) is not 'when' ({c.get('when')!r})")
                if m.group(2) != c.get("speaker_id"):
                    errors.append(f"{f}: the speaker in the id ({m.group(2)}) is not 'speaker_id' ({c.get('speaker_id')!r})")
        sp = c.get("speaker_id")
        if sp not in claimants:
            errors.append(f"{f}: speaker_id {sp!r} is not on the frozen panel (tier core or cohort_2020s) or the ledger-only list (tier claims_only) in speakers.csv; either list changes only by amendment")
        when = c.get("when")
        if isinstance(when, str) and not PRECISION_PATTERNS["day"].match(when) and not c.get("when_note"):
            errors.append(f"{f}: 'when' is not a full date, so 'when_note' must say how it was settled")
        if c.get("source_kind") not in CLAIM_SOURCE_KINDS:
            errors.append(f"{f}: source_kind must be one of {sorted(CLAIM_SOURCE_KINDS)}")
        elif c["source_kind"] == "coverage_only":
            if "quote" in c:
                errors.append(f"{f}: a coverage_only claim carries no quote; it carries reported_as")
            if not c.get("reported_as"):
                errors.append(f"{f}: a coverage_only claim needs reported_as, naming the reporter")
        else:
            if not c.get("quote"):
                errors.append(f"{f}: a claim from a primary source needs the words in 'quote'")
            if "reported_as" in c:
                errors.append(f"{f}: reported_as is only for coverage_only claims")
        if isinstance(c.get("quote"), str) and len(c["quote"].split()) > CLAIM_QUOTE_WORDS:
            errors.append(f"{f}: the quote is {len(c['quote'].split())} words; the limit is {CLAIM_QUOTE_WORDS}")
        if isinstance(c.get("source_url"), str) and not URL.match(c["source_url"]):
            errors.append(f"{f}: source_url is not a web address")
        if c.get("kind") not in CLAIM_KINDS:
            errors.append(f"{f}: kind must be one of {sorted(CLAIM_KINDS)}")
        due = c.get("due")
        if isinstance(due, int) and not isinstance(due, bool):
            if not 2000 <= due <= 2200:
                errors.append(f"{f}: due {due} is not a year between 2000 and 2200")
            if isinstance(c.get("due_date"), date) and c["due_date"].year != due:
                errors.append(f"{f}: due_date {c['due_date']} is not in the due year {due}")
            if isinstance(c.get("due_early"), int) and c["due_early"] > due:
                errors.append(f"{f}: due_early {c['due_early']} is later than due {due}")
            if isinstance(when, str) and int(when[:4]) > due:
                errors.append(f"{f}: due {due} is before the claim was made ({when})")
        status = c.get("status")
        if status not in CLAIM_STATUSES:
            errors.append(f"{f}: status must be one of {sorted(CLAIM_STATUSES)}")
        else:
            if status in CLAIM_SETTLED:
                for field in ("verdict_on", "verdict_why", "verdict_source", "evidence_by"):
                    if not c.get(field):
                        errors.append(f"{f}: a {status} claim needs '{field}'")
                if isinstance(c.get("verdict_source"), str) and not URL.match(c["verdict_source"]):
                    errors.append(f"{f}: verdict_source is not a web address")
                if c.get("evidence_by") not in CLAIM_EVIDENCE:
                    errors.append(f"{f}: evidence_by must be 'outside' or 'maker'")
            if status == "missed" and c.get("direction") not in ("later", "not_come"):
                errors.append(f"{f}: a missed claim needs direction 'later' or 'not_come'")
            if "direction" in c and c["direction"] not in CLAIM_DIRECTIONS:
                errors.append(f"{f}: direction must be one of {sorted(CLAIM_DIRECTIONS)}")
            if status == "unfalsifiable" and not c.get("verdict_why"):
                errors.append(f"{f}: an unfalsifiable claim says in verdict_why why no outsider could test it")
            if status == "not_yet_due":
                for field in ("verdict_on", "verdict_source", "evidence_by", "direction"):
                    if field in c:
                        errors.append(f"{f}: a not_yet_due claim has no '{field}' yet")
                if isinstance(due, int) and not isinstance(due, bool):
                    end = c["due_date"] if isinstance(c.get("due_date"), date) else date(due, 12, 31)
                    if end < pacific_today():
                        errors.append(f"{f}: the due date {end} has passed, so the claim is no longer not_yet_due; enter its verdict")
            if status in ("hit", "missed") and isinstance(c.get("verdict_on"), date) and isinstance(due, int) and not isinstance(due, bool):
                end = c["due_date"] if isinstance(c.get("due_date"), date) else date(due, 12, 31)
                if status == "missed" and c["verdict_on"] < end:
                    errors.append(f"{f}: a miss is settled only after the due date ({end}); verdict_on is {c['verdict_on']}")
                if status == "hit" and end < pacific_today() and c["verdict_on"] > end and c.get("direction") != "later":
                    errors.append(f"{f}: a hit's verdict_on ({c['verdict_on']}) is after the due date ({end}); a thing that came after the date is a miss with direction 'later'")
        sid = c.get("statement_id")
        if isinstance(sid, str):
            row = statements.get(sid)
            if row is None:
                errors.append(f"{f}: statement_id {sid!r} is not a row in statements.csv")
            else:
                if row["speaker_id"] != sp:
                    errors.append(f"{f}: statement {sid} is by {row['speaker_id']!r}, not {sp!r}")
                if isinstance(when, str) and row["date"][:7] != when[:7]:
                    errors.append(f"{f}: statement {sid} is dated {row['date']}, not the same month as 'when' ({when})")
                # The claim's words lie inside the row's quote, or the notes say why the span differs
                # (claims-ledger method, "What it must never touch"; proposal section 4, rule 1).
                q = c.get("quote")
                if isinstance(q, str) and normalise(q.replace("...", "")).split(" ... ")[0] not in normalise(row["quote"]) \
                        and "differs from the statement" not in (c.get("notes") or ""):
                    errors.append(f"{f}: the quote is not inside statement {sid}'s quote, and notes do not say why the span differs")
        arrives, form = c.get("arrives"), c.get("form")
        # A timing claim always says what arrives; a capability claim says so when it forecasts AGI or beyond.
        if c.get("kind") == "timing" or (c.get("kind") == "capability" and arrives is not None):
            if arrives not in CLAIM_ARRIVES:
                errors.append(f"{f}: a timing claim says what arrives: 'arrives' is one of {sorted(CLAIM_ARRIVES)} (A31)")
            elif arrives != "other":
                if form not in CLAIM_FORMS:
                    errors.append(f"{f}: 'form' is one of {sorted(CLAIM_FORMS)} (A31)")
                if not c.get("arrives_term"):
                    errors.append(f"{f}: 'arrives_term' gives what arrives in the person's own term (A31)")
                if form == "range" and "due_early" not in c:
                    errors.append(f"{f}: a range needs due_early")
                if (form == "not_before") != isinstance(c.get("not_before_year"), int):
                    errors.append(f"{f}: a 'not before' forecast, and only one, gives not_before_year, the first year its words leave open (A31)")
            elif form or c.get("arrives_term"):
                errors.append(f"{f}: 'form' and 'arrives_term' are only for a forecast of AGI or beyond (A31)")
        elif arrives or form or c.get("arrives_term"):
            errors.append(f"{f}: 'arrives', 'arrives_term' and 'form' are only for timing and capability claims (A31)")
        for field in ("search_ids",):
            for s_id in c.get(field) or []:
                if s_id not in search_ids:
                    errors.append(f"{f}: search id {s_id!r} is not in search_log.csv; every search is logged before the claim")
    for cid, c in claims.items():
        r = c.get("restates")
        if isinstance(r, str):
            if r not in claims:
                errors.append(f"claims/{cid}.toml: restates {r!r}, which is not a claim file")
            elif claims[r].get("speaker_id") != c.get("speaker_id"):
                errors.append(f"claims/{cid}.toml: restates a claim by someone else")
            elif r == cid:
                errors.append(f"claims/{cid}.toml: restates itself")
    return len(files)


def check_words(tables):
    """Every record in data/claims_undated/ (amendment A31): a leader's undated words on when AGI or
    beyond arrives, from a primary source, by one of the people who may have claims, carrying no year
    or length of time, every search logged."""
    if not UNDATED.exists():
        return 0
    claimants = {r["speaker_id"] for r in tables["speakers.csv"]
                 if r["speaker_type"] == "individual" and r["tier"] in CLAIMS_TIERS}
    search_ids = {r["search_id"] for r in tables["search_log.csv"]}
    statements = {r["statement_id"]: r for r in tables["statements.csv"]}
    seen = set()
    files = sorted(UNDATED.glob("*.toml"))
    for path in files:
        f = f"claims_undated/{path.name}"
        try:
            raw = tomllib.loads(path.read_text(encoding="utf-8"))
        except tomllib.TOMLDecodeError as e:
            errors.append(f"{f}: not valid TOML ({e})")
            continue
        w = raw.get("words")
        if not isinstance(w, dict) or set(raw) != {"words"}:
            errors.append(f"{f}: a file holds exactly one [words] table")
            continue
        for k, v in w.items():
            if k not in WORDS_FIELDS:
                errors.append(f"{f}: unknown field {k!r}")
            elif not claim_value_ok(WORDS_FIELDS[k], v):
                errors.append(f"{f}: {k} is not a valid value")
        for k in WORDS_REQUIRED:
            if k not in w:
                errors.append(f"{f}: missing {k!r}")
        if w.get("id") != path.stem:
            errors.append(f"{f}: id must equal the file name")
        if w.get("id") in seen:
            errors.append(f"{f}: duplicate id")
        seen.add(w.get("id"))
        if w.get("speaker_id") not in claimants:
            errors.append(f"{f}: speaker_id {w.get('speaker_id')!r} is not one who may have claims (A30)")
        if w.get("source_kind") not in CLAIM_SOURCE_KINDS - {"coverage_only"}:
            errors.append(f"{f}: undated words come from a primary source: source_kind is own_words, transcript or printed_qa")
        if w.get("arrives") not in CLAIM_ARRIVES - {"other"}:
            errors.append(f"{f}: 'arrives' is agi, superintelligence or beyond_people")
        if isinstance(w.get("quote"), str) and len(w["quote"].split()) > CLAIM_QUOTE_WORDS:
            errors.append(f"{f}: the quote runs past {CLAIM_QUOTE_WORDS} words; quote the core words and put the rest in notes")
        if re.search(r"\b(19|20)\d\d\b", w.get("quote") or ""):
            errors.append(f"{f}: the words name a year, so they are a dated claim, not undated words")
        sid = w.get("statement_id")
        if isinstance(sid, str) and sid not in statements:
            errors.append(f"{f}: statement_id {sid!r} is not a row in statements.csv")
        for s_id in w.get("search_ids") or []:
            if s_id not in search_ids:
                errors.append(f"{f}: search id {s_id!r} is not in search_log.csv")
    return len(files)


def main():
    tables = {name: read(name) for name in HEADERS}
    speakers = {r["speaker_id"] for r in tables["speakers.csv"]}
    check_speakers(tables["speakers.csv"])
    check_statements(tables["statements.csv"], speakers)
    check_aggregates(tables["aggregates.csv"], speakers)
    check_aggregates(tables["world_measures.csv"], speakers, "world_measures.csv")
    check_events(tables["events.csv"])
    check_search_log(tables["search_log.csv"], speakers)
    check_readings(tables, speakers)
    n_claims = check_claims(tables, speakers)
    n_words = check_words(tables)

    # The ledger-only list never enters the opinion record (amendment A30).
    claims_only = {r["speaker_id"] for r in tables["speakers.csv"] if r["tier"] == CLAIMS_ONLY_TIER}
    for i, r in enumerate(tables["statements.csv"], start=2):
        if r["speaker_id"] in claims_only:
            err("statements.csv", i, f"speaker {r['speaker_id']!r} is on the claims ledger's ledger-only list (tier claims_only), which never enters statements.csv (A30)")

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
    n_readings = len(list(READINGS.glob("*.json"))) if READINGS.exists() else 0
    print(f"OK: {counts}, readings {n_readings}, claims {n_claims}, undated words {n_words}")


if __name__ == "__main__":
    main()
