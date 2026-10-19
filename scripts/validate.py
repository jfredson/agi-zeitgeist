#!/usr/bin/env python3
"""Check every row in data/*.csv against the codebook and methodology.

Exits 1 and lists every problem found, or exits 0 and prints row counts.
Standard library only, so anyone can run it: python3 scripts/validate.py
"""

import csv
import json
import re
import sys
from datetime import date
from pathlib import Path

DATA = Path(__file__).resolve().parent.parent / "data"
# One file per run of the weekly reading (docs/weekly-reading.md), never edited.
READINGS = DATA / "readings"

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
NOTE_TAGS = {"secondhand", "incidental", "sampled", "lower_bound"}
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
            return floor <= d <= date.today()
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
            if r["tier"] not in PANEL_TIERS:
                err(f, i, f"individual needs tier core, cohort_2020s or wide, got {r['tier']!r}")
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
    print(f"OK: {counts}, readings {n_readings}")


if __name__ == "__main__":
    main()
