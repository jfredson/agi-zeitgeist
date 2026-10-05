# Coding brief: Claude's pass over the 390 pilot posts, final codebook (2026-10-04)

Given to six fresh `claude-opus-5-5` coders, 65 posts each, for the full-sample run. They
get the same instructions, codebook and post content that `scripts/vanguard_crossfamily_pass.py`
sends Gemini and GPT; only the output format differs (a CSV file instead of structured
output). Each coder is blind: it sees no other coder's or model's codes.

---

You are coding Reddit posts from r/singularity for a research dataset, following the codebook
exactly. The codebook is `docs/vanguard/codebook.md` in
`/Users/john/Code/agi-zeitgeist/.claude/worktrees/happy-nobel-b75d37/`. Read all of it first,
including the decision rules adopted on 2026-10-03 (R2, R3) and 2026-10-04 (R1a).

**Stay blind.** Do not open any file under `data/`, any other `docs/` file, or any other
file in the work folder except your own input file, the image files it names, and your own
output file. Don't search the web or fetch links: linked page text, where it could be read,
is already in your input. Code what the post says; don't check whether claims are true.

Rules to apply:
- Video posts: code from the title only; title_only = yes; content_basis = video_title.
- Galleries, dead image files ("(image file: unavailable)"), or a title that reads
  "[ Removed by moderator ]": not eligible, content_unavailable.
- Image posts: open `image_file` with the Read tool. Code from the image only if it has legible
  text or a legible chart or screenshot; otherwise not eligible, image_no_text.
- Text posts whose body was removed or deleted: code from the title, title_only = yes,
  content_basis = text_title.
- Link posts: if `linked_page_text` is given, content_basis = link_page; if it says "(could
  not be read)", link_title and title_only = yes.
- Posts that don't mention AI are not eligible (no_ai_claim). Demo-only video titles are
  eligible specific_capability claims (temporal_status achieved).
- Eligible posts: list each distinct claim, the main claim first; extrapolates_to_horizon is
  yes/no/na for the post, repeated on each of its rows.
- attribution panel_member means the claim relays one of: Kurzweil, Bostrom, Yudkowsky,
  Hanson, Hinton, LeCun, Bengio, Hassabis, Legg, Altman, Marcus, Ng, Russell, Brooks, Musk,
  Sutskever, Chollet, Chalmers, Brynjolfsson, Schmidhuber, Kai-Fu Lee, Walsh, Tegmark,
  Suleyman, Amodei, Aschenbrenner, Kokotajlo, Cotra, Huang, Leike, Mollick, Cowen.
- evidence_span: 25 words or fewer, copied verbatim from the title, body, page or image text.
- frame_tags: words actually used, `;`-separated, from the codebook list; blank if none.

**Output:** a CSV with exactly this header, one row per claim:

```
run_id,coder,post_id,quarter,sample,rank_or_draw,post_type,content_basis,title_only,eligible,exclusion_reason,claim_n,claim_target,si_level,temporal_status,forecast_horizon,stance,epistemic_qualification,rhetorical_mode,development_preference,attribution,frame_tags,extrapolates_to_horizon,evidence_span,notes
```

- `run_id` = `vanguard-pilot-rsing-2026-10-04-claude-full-final`; `coder` =
  `claude-opus-5-5-full-final-pN` (N = your part number). `post_id`, `quarter`, `sample`,
  `rank_or_draw`, `post_type` copied from the input.
- An ineligible post is one row: `claim_n` 0, `eligible` no, `exclusion_reason` set, claim
  fields and `extrapolates_to_horizon` blank.
- Eligible claims are numbered 1, 2, ... Empty values are blank (never "none"); `title_only`
  is `yes` or blank.
- `notes`: a short reason for any hard call, especially under R1a, R2 and R3.
- Every one of your posts gets at least one row. Quote fields containing commas.
