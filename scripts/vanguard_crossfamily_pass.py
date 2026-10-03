#!/usr/bin/env python3
"""Cross-family blind second pass for the r/singularity pilot (amendment section 9 as
revised 2026-10-03): the same posts coded by a model from a different family than the
first pass, with the codebook and the post content only (no first-pass codes).

Model: Gemini, `gemini-3.1-pro-preview`, pinned by the version string Google reports
(PINNED_VERSION); every reply's reported version is recorded and checked. Default
sampling settings; structured output with the codebook's allowed values.

Input: the post IDs in data/vanguard/second-coder-worksheet.csv; content from the pilot's
scratch work file (titles, bodies, links, saved images). Link pages are fetched once and
their text passed in; if a page can't be read, the post is coded from its title.

Writes data/vanguard/r-singularity-pilot-codes-crossfamily.csv (codes schema) and keeps
raw replies in the scratch folder. Key read from GEMINI_API_KEY at run time; never printed.

    python3 scripts/vanguard_crossfamily_pass.py
"""

import base64
import csv
import html
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

MODEL = "gemini-3.1-pro-preview"
PINNED_VERSION = "3.1-pro-preview-01-2026"
CODER = f"{MODEL}@{PINNED_VERSION}"
RUN_ID = "vanguard-pilot-rsing-2026-10-03-crossfamily"
ROOT = Path(__file__).resolve().parent.parent
WORK = Path("/Users/john/.claude/jobs/f819dd6c/tmp/vanguard_pilot")
RAW = WORK / "crossfamily_raw"
OUT = ROOT / "data" / "vanguard" / "r-singularity-pilot-codes-crossfamily.csv"
SUBSET = ROOT / "data" / "vanguard" / "second-coder-worksheet.csv"
CODEBOOK = ROOT / "docs" / "vanguard" / "codebook.md"
HEADER = ["run_id", "coder", "post_id", "quarter", "sample", "rank_or_draw", "post_type",
          "content_basis", "title_only", "eligible", "exclusion_reason", "claim_n",
          "claim_target", "si_level", "temporal_status", "forecast_horizon", "stance",
          "epistemic_qualification", "rhetorical_mode", "development_preference",
          "attribution", "frame_tags", "extrapolates_to_horizon", "evidence_span", "notes"]

E = lambda *v: {"type": "STRING", "enum": list(v)}
SCHEMA = {
    "type": "OBJECT",
    "properties": {
        "eligible": E("yes", "no"),
        "exclusion_reason": E("none", "no_ai_claim", "content_unavailable", "image_no_text"),
        "content_basis": E("text", "text_title", "image", "video_title", "link_page", "link_title", "gallery"),
        "title_only": E("yes", "no"),
        "extrapolates_to_horizon": E("none", "yes", "no", "na"),
        "claims": {"type": "ARRAY", "items": {"type": "OBJECT", "properties": {
            "claim_target": E("specific_capability", "agi", "self_improvement", "pace_singularity",
                              "consequence", "industry_governance"),
            "si_level": E("none", "si_assist", "si_research", "si_modify", "si_sustained"),
            "temporal_status": E("achieved", "under_way", "forecast", "hypothetical", "unspecified"),
            "forecast_horizon": {"type": "STRING"},
            "stance": E("affirms", "denies", "questions", "conditional", "neutral_relay", "unclear"),
            "epistemic_qualification": E("unqualified", "qualified", "explicit_probability", "unclear"),
            "rhetorical_mode": E("literal", "ironic", "mixed", "unclear"),
            "development_preference": E("supports", "opposes", "conditional", "not_expressed"),
            "attribution": E("original", "panel_member", "lab_or_company", "news_outlet", "other_person"),
            "frame_tags": {"type": "STRING"},
            "evidence_span": {"type": "STRING"}},
            "required": ["claim_target", "temporal_status", "stance", "epistemic_qualification",
                         "rhetorical_mode", "development_preference", "attribution", "evidence_span"]}},
        "notes": {"type": "STRING"}},
    "required": ["eligible", "exclusion_reason", "content_basis", "title_only", "extrapolates_to_horizon", "claims"],
}
PANEL = ("Kurzweil, Bostrom, Yudkowsky, Hanson, Hinton, LeCun, Bengio, Hassabis, Legg, Altman, Marcus, "
         "Ng, Russell, Brooks, Musk, Sutskever, Chollet, Chalmers, Brynjolfsson, Schmidhuber, Kai-Fu Lee, "
         "Walsh, Tegmark, Suleyman, Amodei, Aschenbrenner, Kokotajlo, Cotra, Huang, Leike, Mollick, Cowen")
INSTRUCTIONS = f"""You are coding one Reddit post from r/singularity for a research dataset, following the codebook below exactly.
Code what the post says; don't check whether claims are true. Rules to apply:
- Video posts: code from the title only; title_only = yes; content_basis = video_title.
- Galleries, dead image files, or a title that reads "[ Removed by moderator ]": not eligible, content_unavailable.
- Image posts: code from the image only if it has legible text or a legible chart or screenshot; otherwise not eligible, image_no_text.
- Text posts whose body was removed or deleted: code from the title, title_only = yes, content_basis = text_title.
- Link posts: if linked page text is given, content_basis = link_page; if not, link_title and title_only = yes.
- Posts that don't mention AI are not eligible (no_ai_claim). Demo-only video titles are eligible specific_capability claims (temporal_status achieved).
- Ineligible posts: return claims as an empty list and extrapolates_to_horizon "none". Use "none" for an empty exclusion_reason or si_level, and title_only "no" when not title-only.
- Eligible posts: list each distinct claim, the main claim first; extrapolates_to_horizon is yes/no/na for the post.
- attribution panel_member means the claim relays one of: {PANEL}.
- evidence_span: 25 words or fewer, copied verbatim from the title, body, page or image text.
- frame_tags: words actually used, ';'-separated, from the codebook list; blank if none.

CODEBOOK:
"""


def page_text(url, cache):
    if url in cache:
        return cache[url]
    text = ""
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (research)"})
        with urllib.request.urlopen(req, timeout=25) as r:
            if "html" in (r.headers.get("Content-Type") or ""):
                raw = r.read(2_000_000).decode("utf-8", "ignore")
                raw = re.sub(r"(?is)<(script|style|noscript).*?</\1>", " ", raw)
                text = html.unescape(re.sub(r"(?s)<[^>]+>", " ", raw))
                text = re.sub(r"\s+", " ", text).strip()[:6000]
    except Exception:
        text = ""
    cache[url] = text
    return text


def call_gemini(parts, key):
    body = json.dumps({"contents": [{"role": "user", "parts": parts}],
                       "generationConfig": {"responseMimeType": "application/json",
                                            "responseSchema": SCHEMA}}).encode()
    req = urllib.request.Request(
        f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent",
        data=body, headers={"Content-Type": "application/json", "x-goog-api-key": key})
    for wait in (0, 60, 180):
        if wait:
            time.sleep(wait)
        try:
            with urllib.request.urlopen(req, timeout=300) as r:
                return json.loads(r.read())
        except urllib.error.HTTPError as e:
            if e.code in (429, 500, 503):
                continue
            raise SystemExit(f"stopped: HTTP {e.code} from the Gemini API")
        except (urllib.error.URLError, TimeoutError, OSError):
            continue
    raise SystemExit("stopped: the Gemini API kept refusing or timing out after two back-offs")


def check_pin(key):
    """Stop unless Google still reports the pinned version for this model."""
    req = urllib.request.Request(f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}",
                                 headers={"x-goog-api-key": key})
    with urllib.request.urlopen(req, timeout=60) as r:
        version = json.loads(r.read()).get("version")
    if version != PINNED_VERSION:
        raise SystemExit(f"stopped: {MODEL} now reports version {version!r}, not the pinned {PINNED_VERSION!r}")
    print(f"pinned model confirmed: {MODEL} version {version}")


def main():
    key = os.environ["GEMINI_API_KEY"]
    check_pin(key)
    limit = int(sys.argv[sys.argv.index("--limit") + 1]) if "--limit" in sys.argv else None
    with SUBSET.open(newline="") as f:
        subset = [(r["post_id"], r["quarter"], r["sample"]) for r in csv.DictReader(f)]
    if limit:
        subset = subset[:limit]
    content = {p["post_id"]: p for p in json.loads((WORK / "posts.json").read_text())}
    codebook = CODEBOOK.read_text()
    RAW.mkdir(parents=True, exist_ok=True)
    cache_path = WORK / "link_pages.json"
    cache = json.loads(cache_path.read_text()) if cache_path.exists() else {}
    rows, versions = [], set()
    for n, (pid, q, s) in enumerate(subset, 1):
        p = content[pid]
        raw_file = RAW / f"{pid}.json"
        if raw_file.exists():
            data = json.loads(raw_file.read_text())
        else:
            desc = [f"post_id: {pid}", f"post_type: {p['post_type']}", f"title: {p['title']}"]
            if p["post_type"] == "text":
                desc.append(f"body: {p['selftext'] or '(empty)'}")
            if p["post_type"] == "link":
                txt = page_text(p["url"], cache)
                desc.append(f"link: {p['url']}")
                desc.append(f"linked page text: {txt}" if txt else "linked page text: (could not be read)")
            parts = [{"text": INSTRUCTIONS + codebook + "\n\nPOST:\n" + "\n".join(desc)}]
            img = p.get("image_file") or ""
            if p["post_type"] == "image":
                if img and not img.startswith("unavailable") and Path(img).exists():
                    ext = Path(img).suffix.lower().lstrip(".")
                    mime = {"jpg": "image/jpeg", "jpeg": "image/jpeg", "png": "image/png",
                            "gif": "image/gif", "webp": "image/webp"}.get(ext, "image/jpeg")
                    parts.append({"inline_data": {"mime_type": mime,
                                                  "data": base64.b64encode(Path(img).read_bytes()).decode()}})
                else:
                    parts[0]["text"] += "\n(image file: unavailable)"
            data = call_gemini(parts, key)
            raw_file.write_text(json.dumps(data))
            time.sleep(1.0)
        versions.add(data.get("modelVersion"))
        try:
            text = "".join(x.get("text", "") for x in data["candidates"][0]["content"]["parts"]
                           if not x.get("thought"))
            out = json.loads(text)
        except (KeyError, IndexError, ValueError):
            out = {"eligible": "no", "exclusion_reason": "", "content_basis": "", "title_only": "",
                   "extrapolates_to_horizon": "", "claims": [], "notes": "unparseable reply"}
        blank = lambda x: "" if x in ("none", None) else x
        out = {k: (blank(v) if isinstance(v, str) else v) for k, v in out.items()}
        if out.get("title_only") == "no":
            out["title_only"] = ""
        out["claims"] = [{k: blank(v) for k, v in c.items()} for c in (out.get("claims") or [])]
        base = {"run_id": RUN_ID, "coder": CODER, "post_id": pid, "quarter": q, "sample": s,
                "rank_or_draw": 0, "post_type": p["post_type"], "content_basis": out.get("content_basis", ""),
                "title_only": out.get("title_only", ""), "eligible": out.get("eligible", ""),
                "exclusion_reason": out.get("exclusion_reason", ""),
                "extrapolates_to_horizon": out.get("extrapolates_to_horizon", "") if out.get("eligible") == "yes" else "",
                "notes": out.get("notes", "")}
        claims = out.get("claims") or [] if out.get("eligible") == "yes" else []
        if not claims:
            rows.append({**base, "claim_n": 0})
        for i, c in enumerate(claims, 1):
            rows.append({**base, "claim_n": i, **{k: c.get(k, "") for k in HEADER if k in c}})
        if n % 20 == 0:
            print(f"  {n} of {len(subset)} posts coded", flush=True)
    cache_path.write_text(json.dumps(cache))
    with OUT.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=HEADER, lineterminator="\n", extrasaction="ignore")
        w.writeheader()
        w.writerows({k: r.get(k, "") for k in HEADER} for r in rows)
    print(f"{len(subset)} posts coded by {CODER}; reported versions: {sorted(v for v in versions if v)}")
    if any(v and v != MODEL for v in versions):
        print("  note: a reply reported a model version other than", MODEL)


if __name__ == "__main__":
    main()
