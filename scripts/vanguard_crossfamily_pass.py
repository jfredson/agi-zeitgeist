#!/usr/bin/env python3
"""Blind passes by models from other families for the r/singularity pilot (amendment
section 9 as revised 2026-10-03): the same 140 posts coded with the codebook and the post
content only (no other coder's codes).

  --family gemini  `gemini-3.1-pro-preview`, pinned by the version string Google reports
                   (3.1-pro-preview-01-2026); default sampling settings.
  --family gpt     OpenAI `gpt-6-astra`, reasoning effort medium. OpenAI publishes no
                   dated snapshot, so the pin is the model name plus the creation time
                   OpenAI lists for it (1787853604, i.e. 2026-08-27 UTC); the run stops if
                   that changes. The model each reply reports is recorded.
  --rules FILE     add trial codebook rules (proposals awaiting John's ruling) after the
                   codebook; writes a separate trial file and keeps separate raw replies.

Both use structured output limited to the codebook's allowed values.

Input: the post IDs in data/vanguard/second-coder-worksheet.csv; content from the pilot's
scratch work file (titles, bodies, links, saved images). Link pages are fetched once and
their text passed in; if a page can't be read, the post is coded from its title.

Writes data/vanguard/r-singularity-pilot-codes-crossfamily.csv (codes schema) and keeps
raw replies in the scratch folder (GPT: ...-codes-gpt.csv; with --rules, ...-rules-trial.csv).
Keys read at run time (GEMINI_API_KEY from the environment; OPENAI_API_KEY from
~/Documents/.agi-zeitgeist/credentials.env); never printed or written anywhere.

    python3 scripts/vanguard_crossfamily_pass.py --family gemini|gpt [--rules FILE] [--limit N] [--cached-only]

--ids FILE codes the post ids listed in FILE (a CSV with post_id, quarter, sample columns,
such as the full pilot sample) instead of the 140-post set, into a separate "-full" file.
--max-new N stops after N new API requests, so a run fits a daily limit (Gemini allows
250 requests per model per day on the project's tier); rerun the next day to continue.

--codebook FILE sends that codebook instead of docs/vanguard/codebook.md (a frozen copy keeps
a run on the codebook it started with).
--tag TAG names a separate trial: replies saved in their own folder, output
...-TAG.csv, run id ...-TAG. Use one tag per rule being trialled.

--cached-only writes the output from replies already saved, without calling the API, and
skips posts with no saved reply (used when an API stopped answering partway through a run).
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

FAMILIES = {
    "gemini": {"model": "gemini-3.1-pro-preview", "pin": "3.1-pro-preview-01-2026",
               "run_id": "vanguard-pilot-rsing-2026-10-03-crossfamily", "raw": "crossfamily_raw",
               "out": "r-singularity-pilot-codes-crossfamily.csv"},
    "gpt": {"model": "gpt-6-astra", "pin": 1787853604, "effort": "medium",
            "run_id": "vanguard-pilot-rsing-2026-10-03-gpt", "raw": "gpt_raw",
            "out": "r-singularity-pilot-codes-gpt.csv"},
}
FAMILY = sys.argv[sys.argv.index("--family") + 1] if "--family" in sys.argv else "gemini"
RULES = Path(sys.argv[sys.argv.index("--rules") + 1]) if "--rules" in sys.argv else None
F = FAMILIES[FAMILY]
MODEL = F["model"]
PINNED_VERSION = F["pin"]
CODER = f"{MODEL}@{PINNED_VERSION}" if FAMILY == "gemini" else f"{MODEL}@created-{PINNED_VERSION}-effort-{F['effort']}"
IDS = Path(sys.argv[sys.argv.index("--ids") + 1]) if "--ids" in sys.argv else None
TAG = sys.argv[sys.argv.index("--tag") + 1] if "--tag" in sys.argv else None
RUN_ID = F["run_id"] + (f"-{TAG}" if TAG else ("-rules-trial" if RULES else "") + ("-full" if IDS else ""))
ROOT = Path(__file__).resolve().parent.parent
WORK = Path("/Users/john/.claude/jobs/f819dd6c/tmp/vanguard_pilot")
RAW = WORK / (F["raw"] + (f"_{TAG}" if TAG else ("_rules" if RULES else "")))
OUT = ROOT / "data" / "vanguard" / (F["out"].replace(".csv", "-rules-trial.csv") if RULES else F["out"])
if TAG:
    OUT = ROOT / "data" / "vanguard" / F["out"].replace(".csv", f"-{TAG}.csv")
elif IDS:
    OUT = OUT.with_name(OUT.name.replace(".csv", "-full.csv"))
SUBSET = ROOT / "data" / "vanguard" / "second-coder-worksheet.csv"
CODEBOOK = Path(sys.argv[sys.argv.index("--codebook") + 1]) if "--codebook" in sys.argv else \
    ROOT / "docs" / "vanguard" / "codebook.md"
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
    last = ""
    for wait in (0, 60, 180):
        if wait:
            time.sleep(wait)
        try:
            with urllib.request.urlopen(req, timeout=300) as r:
                return json.loads(r.read())
        except urllib.error.HTTPError as e:
            if e.code in (429, 500, 503):
                last = f"HTTP {e.code}: {e.read().decode('utf-8', 'ignore')[:200]}"
                continue
            raise SystemExit(f"stopped: HTTP {e.code} from the Gemini API")
        except (urllib.error.URLError, TimeoutError, OSError) as e:
            last = f"connection problem: {e}"
            continue
    raise SystemExit(f"stopped: the Gemini API kept refusing or timing out after two back-offs (last: {last})")


def strict(schema):
    """Gemini-style schema to the strict JSON Schema OpenAI requires (every key required)."""
    t = schema["type"].lower()
    out = {"type": t}
    if "enum" in schema:
        out["enum"] = schema["enum"]
    if t == "object":
        out["properties"] = {k: strict(v) for k, v in schema["properties"].items()}
        out["required"] = list(schema["properties"])
        out["additionalProperties"] = False
    if t == "array":
        out["items"] = strict(schema["items"])
    return out


def openai_key():
    path = Path.home() / "Documents" / ".agi-zeitgeist" / "credentials.env"
    for line in path.read_text().splitlines():
        if line.startswith("OPENAI_API_KEY="):
            return line.split("=", 1)[1].strip().strip('"').strip("'")
    raise SystemExit("stopped: OPENAI_API_KEY not found in the credentials file")


def call_openai(parts, key):
    content = []
    for x in parts:
        if "text" in x:
            content.append({"type": "input_text", "text": x["text"]})
        else:
            d = x["inline_data"]
            content.append({"type": "input_image", "image_url": f"data:{d['mime_type']};base64,{d['data']}"})
    body = json.dumps({"model": MODEL, "input": [{"role": "user", "content": content}],
                       "reasoning": {"effort": F["effort"]},
                       "text": {"format": {"type": "json_schema", "name": "post_codes",
                                           "schema": strict(SCHEMA), "strict": True}}}).encode()
    req = urllib.request.Request("https://api.openai.com/v1/responses", data=body,
                                 headers={"Content-Type": "application/json", "Authorization": f"Bearer {key}"})
    last = ""
    for wait in (0, 60, 180):
        if wait:
            time.sleep(wait)
        try:
            with urllib.request.urlopen(req, timeout=600) as r:
                return json.loads(r.read())
        except urllib.error.HTTPError as e:
            if e.code in (429, 500, 502, 503):
                last = f"HTTP {e.code}: {e.read().decode('utf-8', 'ignore')[:200]}"
                continue
            detail = e.read().decode("utf-8", "ignore")[:300]
            raise SystemExit(f"stopped: HTTP {e.code} from the OpenAI API: {detail}")
        except (urllib.error.URLError, TimeoutError, OSError) as e:
            last = f"connection problem: {e}"
            continue
    raise SystemExit(f"stopped: the OpenAI API kept refusing or timing out after two back-offs (last: {last})")


def check_pin_openai(key):
    req = urllib.request.Request(f"https://api.openai.com/v1/models/{MODEL}",
                                 headers={"Authorization": f"Bearer {key}"})
    with urllib.request.urlopen(req, timeout=60) as r:
        created = json.loads(r.read()).get("created")
    if created != PINNED_VERSION:
        raise SystemExit(f"stopped: {MODEL} now lists creation time {created!r}, not the pinned {PINNED_VERSION!r}")
    print(f"pinned model confirmed: {MODEL} created {created}")


def reply_text(data):
    if FAMILY == "gemini":
        return "".join(x.get("text", "") for x in data["candidates"][0]["content"]["parts"] if not x.get("thought"))
    return "".join(c.get("text", "") for o in data["output"] if o.get("type") == "message"
                   for c in o.get("content", []) if c.get("type") == "output_text")


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
    cached_only = "--cached-only" in sys.argv
    if cached_only:
        key, call = None, None
    elif FAMILY == "gemini":
        key = os.environ["GEMINI_API_KEY"]
        check_pin(key)
    else:
        key = openai_key()
        check_pin_openai(key)
    if not cached_only:
        call = call_gemini if FAMILY == "gemini" else call_openai
    limit = int(sys.argv[sys.argv.index("--limit") + 1]) if "--limit" in sys.argv else None
    with (IDS or SUBSET).open(newline="") as f:
        subset = list(dict.fromkeys((r["post_id"], r["quarter"], r["sample"]) for r in csv.DictReader(f)))
    max_new = int(sys.argv[sys.argv.index("--max-new") + 1]) if "--max-new" in sys.argv else None
    new_calls = 0
    if limit:
        subset = subset[:limit]
    content = {p["post_id"]: p for p in json.loads((WORK / "posts.json").read_text())}
    codebook = CODEBOOK.read_text()
    if RULES:
        codebook += "\n\nADDITIONAL RULES (apply these; they take precedence over the codebook where they conflict):\n" + RULES.read_text()
    RAW.mkdir(parents=True, exist_ok=True)
    cache_path = WORK / "link_pages.json"
    cache = json.loads(cache_path.read_text()) if cache_path.exists() else {}
    rows, versions = [], set()
    for n, (pid, q, s) in enumerate(subset, 1):
        p = content[pid]
        raw_file = RAW / f"{pid}.json"
        if raw_file.exists():
            data = json.loads(raw_file.read_text())
        elif cached_only or (max_new is not None and new_calls >= max_new):
            continue
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
            data = call(parts, key)
            new_calls += 1
            raw_file.write_text(json.dumps(data))
            time.sleep(1.0)
        versions.add(data.get("modelVersion") or data.get("model"))
        try:
            out = json.loads(reply_text(data))
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
    print(f"{len({r['post_id'] for r in rows})} of {len(subset)} posts coded by {CODER}; reported versions: {sorted(v for v in versions if v)}")
    if any(v and not v.startswith(MODEL) for v in versions):
        print("  note: a reply reported a model version other than", MODEL)


if __name__ == "__main__":
    main()
