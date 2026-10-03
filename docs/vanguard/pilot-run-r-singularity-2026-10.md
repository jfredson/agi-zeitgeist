# Run record: r/singularity pilot, vanguard sub-series

Run id: `vanguard-pilot-rsing-2026-10-03`. Written and committed **before** any sample was
drawn or any post coded. Governs: `docs/amendments/2026-10-02-vanguard-stream.md`
(accepted 2026-10-02, with the 2026-10-02 video ruling and the 2026-10-03 title-only
instruction). Brief: John, 2026-10-03.

## Window and source

- r/singularity, 2024Q4 to 2026Q3 (2024-10-01 to 2026-09-30 UTC), from the Arctic Shift
  archive listing saved by `scripts/retrievability_check.py` (50,544 posts).
- Scores are the archive's recorded scores; their observation time is unknown, so the
  rewarded series is "highest recorded-score posts among archived records".

## Samples (stream F design)

- **Rewarded:** per quarter, posts ranked by recorded score (ties: earlier post first),
  screened in rank order until **20 eligible posts** are coded. Ineligible posts passed on
  the way are recorded with the reason.
- **Prevalence:** per quarter, a random sample of **20 posts**, seed **20261003**
  (Python `random.Random`, posts sorted by ID before drawing), inclusion probability 20
  divided by posts in the quarter. All 20 are screened; shares use the eligible ones.
  *Size set by the agent; stream F gives none.*
- **Comment sample: deferred.** Stream F also asks for a random sample of comments.
  Listing every r/singularity comment through the archive API isn't feasible; it needs
  the archive's monthly dump files. Not part of this pilot.
- **Cross-era sample (amendment section 6): deferred** to the next step, not in the brief.

## Eligibility and content basis

- Eligible: the post asserts, disputes or relays a claim about AI capability, timeline or
  consequence.
- Text posts: title and body. Image posts: coded from the image if it has legible text
  (the coder views the image); image-only without legible text is excluded; an image file
  that no longer loads is excluded as "content unavailable". Video posts: **title only**,
  `title_only: yes`. Link posts: title plus the linked page if it can be read; title only
  (`title_only: yes`) if not. Galleries: content needs reddit.com, which refuses scripted
  access, so they are excluded as "content unavailable". *Gallery and link handling set by
  the agent.*

## Coding

- **First pass:** model-assisted, model **`claude-opus-5-5`** (Claude Code subagents,
  model inherited from the session; no other model used). Coders see the post content
  only, not score or rank labels beyond what is needed to work down the list.
- **Instrument:** amendment section 7. Post = sampling unit; claim = coding unit; the
  post's main claim is listed first. Fields: `claim_target` (specific_capability, agi,
  self_improvement with an `si_level`, pace_singularity, consequence), `temporal_status`,
  `forecast_horizon`, `stance`, `epistemic_qualification`, `rhetorical_mode`,
  `development_preference`, `attribution`, `frame_tags`, `title_only`, plus an evidence span
  (25 words or fewer, verbatim, from the title, body or image text).
- **Second pass (interim):** a fresh model instance of the same model, **blind** to the
  first pass, codes a stratified **30% subset** of screened posts (rounded up, per quarter
  and sample, seed **20261004**). Its agreement with the first pass is reported as
  **model–model agreement**, which does **not** meet amendment section 9 (two people,
  blind to the model). A blind worksheet for the same subset is produced for human coders.
  *Fraction set by the agent; section 9 gives none.*

## Outputs

- Codes: `data/vanguard/r-singularity-pilot-codes.csv` (first pass) and
  `data/vanguard/r-singularity-pilot-codes-second.csv` (second pass). No post text beyond
  the short evidence spans.
- Agreement: per field, percentage and Cohen's kappa (agreement corrected for chance).
- Figure: shares of eligible posts by quarter for the section 8 claims (AGI already
  achieved; AGI within a stated horizon; self-improvement under way; singularity
  framing), rewarded and prevalence samples separately, each with and without
  `title_only` rows, captioned "Framing in sampled high-score posts from selected AI
  enthusiast venues; not representative of participants or the public."

## Departures from the amendment, stated up front

1. The second coder is a model, not two people (section 9). Reported as interim.
2. Section 12 preconditions not yet met: venue inventory, X decision, cross-era sample.
   This pilot covers one venue and does not choose venues.
3. Comment sample deferred (see above).
