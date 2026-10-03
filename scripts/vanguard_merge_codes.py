#!/usr/bin/env python3
"""Merge and check coder files for the r/singularity pilot.

    python3 scripts/vanguard_merge_codes.py <out.csv> <coder file> [<coder file> ...]

Checks every code against the allowed values in the pilot coding brief, that video rows
are title-only, and (for first-pass files) that each quarter's rewarded sample has exactly
20 eligible posts. Prints problems and exits 1 if any.
"""

import csv
import sys
from collections import defaultdict

HEADER = ["run_id", "coder", "post_id", "quarter", "sample", "rank_or_draw", "post_type",
          "content_basis", "title_only", "eligible", "exclusion_reason", "claim_n",
          "claim_target", "si_level", "temporal_status", "forecast_horizon", "stance",
          "epistemic_qualification", "rhetorical_mode", "development_preference",
          "attribution", "frame_tags", "extrapolates_to_horizon", "evidence_span", "notes"]
ALLOWED = {
    "sample": {"rewarded", "prevalence"},
    "content_basis": {"text", "text_title", "image", "video_title", "link_page", "link_title", "gallery"},
    "title_only": {"yes", ""},
    "eligible": {"yes", "no"},
    "exclusion_reason": {"", "no_ai_claim", "content_unavailable", "image_no_text"},
    "claim_target": {"", "specific_capability", "agi", "self_improvement", "pace_singularity", "consequence",
                     "industry_governance"},
    "extrapolates_to_horizon": {"", "yes", "no", "na"},
    "si_level": {"", "si_assist", "si_research", "si_modify", "si_sustained"},
    "temporal_status": {"", "achieved", "under_way", "forecast", "hypothetical", "unspecified"},
    "stance": {"", "affirms", "denies", "questions", "conditional", "neutral_relay", "unclear"},
    "epistemic_qualification": {"", "unqualified", "qualified", "explicit_probability", "unclear"},
    "rhetorical_mode": {"", "literal", "ironic", "mixed", "unclear"},
    "development_preference": {"", "supports", "opposes", "conditional", "not_expressed"},
    "attribution": {"", "original", "panel_member", "lab_or_company", "news_outlet", "other_person"},
}


def main():
    out, files = sys.argv[1], sys.argv[2:]
    rows, problems = [], []
    for path in files:
        with open(path, newline="") as f:
            r = csv.DictReader(f)
            if r.fieldnames != HEADER:
                problems.append(f"{path}: header differs: {r.fieldnames}")
                continue
            rows += list(r)
    for i, r in enumerate(rows):
        where = f"{r['post_id']} claim {r['claim_n']}"
        for field, allowed in ALLOWED.items():
            if r[field].strip() not in allowed:
                problems.append(f"{where}: {field}={r[field]!r}")
        if r["post_type"] == "video" and r["title_only"] != "yes":
            problems.append(f"{where}: video row without title_only yes")
        if r["eligible"] == "yes" and not r["claim_target"]:
            problems.append(f"{where}: eligible row without claim_target")
        if r["eligible"] == "yes" and not r["extrapolates_to_horizon"]:
            problems.append(f"{where}: eligible row without extrapolates_to_horizon")
        if r["eligible"] == "no" and not r["exclusion_reason"]:
            problems.append(f"{where}: ineligible row without exclusion_reason")
    if "--first" in sys.argv[0:1] or not any("second" in f for f in files):
        elig = defaultdict(set)
        for r in rows:
            if r["sample"] == "rewarded" and r["eligible"] == "yes":
                elig[r["quarter"]].add(r["post_id"])
        for q in sorted({r["quarter"] for r in rows}):
            if len(elig[q]) != 20:
                problems.append(f"{q} rewarded: {len(elig[q])} eligible posts, expected 20")
    rows.sort(key=lambda r: (r["quarter"], r["sample"], int(r["rank_or_draw"]), int(r["claim_n"] or 0)))
    with open(out, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=HEADER, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)
    posts = {(r["quarter"], r["sample"], r["post_id"]) for r in rows}
    print(f"{len(rows)} rows, {len(posts)} posts written to {out}")
    for p in problems:
        print("  problem:", p)
    sys.exit(1 if problems else 0)


if __name__ == "__main__":
    main()
