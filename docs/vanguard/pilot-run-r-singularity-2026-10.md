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

## Changes during the run (recorded 2026-10-03, before the second pass)

1. **Missing images, fixed.** The sampling script first saved images only for rewarded
   ranks 1 to 40. Coders reached rank 41 or deeper in 2025Q1, 2025Q3 and 2026Q1 and
   excluded ten image posts as "content unavailable" because no file existed. The script
   now saves every sampled image (the sample itself is unchanged; checked byte for byte),
   those posts were recoded from their images, and each quarter's cut-off was re-applied.
2. **Removed-body text posts, made uniform.** Coders had handled text posts whose body was
   removed or deleted in three ways. Rule applied to all: if the title survives, the post is
   coded from the title with `title_only: yes` and `content_basis: text_title`. Galleries
   and image files that no longer load stay excluded.

## Recode run, 2026-10-03 (after John's rulings on the pilot report)

Same model, `claude-opus-5-5`, the same four first-pass coders (resumed, so their earlier
judgments stay consistent). Applied to every screened post in the existing sample: the new
`extrapolates_to_horizon` field and the codebook rulings of 2026-10-03
(`docs/vanguard/codebook.md`): posts not mentioning AI ineligible, demo-only video titles
eligible as capability claims, memes under the legible-text rule, company and policy drama
coded `industry_governance`. The rewarded stopping rule (20 eligible per quarter) is
re-applied, screening further down each quarter's existing ranked reserve where needed; no
new posts are drawn. Changed rows carry the note `R2:` with old and new values. The second
pass is not recoded, so the interim agreement figures predate these rulings.

## Cross-family second pass, 2026-10-03

Run under the revised section 9 (John, 2026-10-03). The models are named and pinned:

- First pass: `claude-opus-5-5`, coder label `claude-opus-5-5-first`, recoded under the 2026-10-03 rulings (424 rows, 390 posts).
- Second pass: `gemini-3.1-pro-preview`, version `3.1-pro-preview-01-2026`. The script checks the version against the Gemini models endpoint before running and stops if it doesn't match. Run id `vanguard-pilot-rsing-2026-10-03-crossfamily`, script `scripts/vanguard_crossfamily_pass.py`. The model sees the full codebook and the same content as the first pass (image, link-page text, or title only), with structured output limited to the codebook's values. It saw no first-pass codes. 140 of 140 posts coded, 177 rows.
- The same-family second pass (`r-singularity-pilot-codes-second.csv`) is superseded and was not recoded.
- John's 40-post blind worksheet (seed 20261005) was drawn, then withdrawn the same day by his ruling removing the human step; the worksheet and its scripts were deleted.

## Three-model coding, 2026-10-03

Run under section 9 as ruled by John later the same day: no human coder, three models from
different companies, final code by majority vote.

- **GPT pass:** `gpt-6-astra`, reasoning effort medium. OpenAI publishes no dated snapshot, so
  the script checks the model's listed creation time (1787853604, 2026-08-27 UTC) before
  running and stops if it changes. Script `scripts/vanguard_crossfamily_pass.py --family gpt`,
  run id `vanguard-pilot-rsing-2026-10-03-gpt`. Same codebook, instructions, content and
  structured output as the Gemini pass. All 140 posts coded.
- **Claude supplement:** 18 posts in the 140-post set fell past the recoded first pass's
  cut-off ranks. A fresh `claude-opus-5-5` coder, blind to every other file, coded them under
  the current codebook (`r-singularity-pilot-codes-claude-subset-supplement.csv`). These rows
  are used only for the three-model check, not for the figure.
- **Majority and reliability:** `scripts/vanguard_three_way.py` writes
  `r-singularity-pilot-codes-majority.csv` and `three-model-reliability.csv`.
- **Rules trial:** proposed rules R1 to R3 (`docs/vanguard/proposed-rules-2026-10-03.md`) were
  added to the codebook. Claude coded with them through two fresh blind coders, 70 posts each.
  Gemini and GPT used the script with `--rules`. Both APIs stopped answering partway through
  (Gemini at 112 posts, GPT at 86). Each was resumed once after a 10-minute pause, failed again
  without coding another post, and was stopped. Their trial files were written from the
  replies already saved (`--cached-only`). The comparison uses the 86 posts all three coded
  (`vanguard_three_way.py --compare`).

## Handover, end of 2026-10-03

Working files (post text, images, saved model replies, fetched link pages, archive cache)
moved from the session scratch folder to `~/Documents/.agi-zeitgeist/work/` (outside the
repository, because they hold post content). The scripts now point there.

**Still to run, after Gemini's daily limit resets (about 17:05 Pacific, 2026-10-04),** from the
repository root, in this order:

```
python3 scripts/vanguard_crossfamily_pass.py --family gemini --rules docs/vanguard/proposed-rules-2026-10-03.md --codebook docs/vanguard/codebook-frozen-2026-10-03-before-rules.md
python3 scripts/vanguard_crossfamily_pass.py --family gemini --ids data/vanguard/r1-split-trial-posts.csv --rules docs/vanguard/trial-rule-r1a-2026-10-03.md --tag r1a-trial
python3 scripts/vanguard_crossfamily_pass.py --family gemini --ids data/vanguard/r1-split-trial-posts.csv --rules docs/vanguard/trial-rule-r1b-2026-10-03.md --tag r1b-trial
python3 scripts/vanguard_three_way.py --compare     # first trial, now on up to 140 posts
python3 scripts/vanguard_three_way.py --r1-split    # R1a and R1b, all three pairs
```

That is 252 Gemini requests against a limit of 250 a day; if the last R1b posts are refused,
rerun the third command the next evening. Then update the pilot report and send John the R1a
and R1b kappas for all three pairs. Claude and GPT codes for both trials are already committed.
Interim Claude–GPT result: R1a raises stance agreement (0.50 without, 0.74 with); R1b doesn't
help attribution (0.75 without, 0.72 with). The trial coders found that both rules need to say
how a bare reaction or joke title ("WTF") is treated.

**Waiting on John:** a ruling on R1a and R1b; about $15 more OpenAI credit. Then the full-sample
run: all 390 posts by Gemini and GPT under the final codebook, with Gemini capped at about 240
new requests a day (`--ids data/vanguard/r-singularity-pilot-sample.csv` style list, `--max-new 240`,
a fresh `--tag` so earlier replies aren't reused).

## Gemini runs, 2026-10-04

Run from the handover's commands, in its order, starting 12:15 Pacific. The handover expected
the daily limit to clear about 17:05; a single test request (`--max-new 1`) at 12:15 was
accepted, so the runs went ahead then. All 252 requests were accepted the same day, none
refused. (Correction, same evening: the limit does apply. The full-sample run was refused
after 2 more requests, so 254 in a day was the ceiling here. Plan on 240 a day.)

- **First trial, last 28 posts:** frozen pre-rules codebook plus R1 to R3, as before. 140 of
  140 posts now coded by all three models.
- **R1a trial and R1b trial:** 112 of 112 posts each, today's codebook plus one rule.
- **Pin:** the script confirmed `gemini-3.1-pro-preview` version `3.1-pro-preview-01-2026`
  before each run.
- **Cost:** $6.28 for 252 requests, from the token counts Google returns with each reply,
  priced at the quoted rates ($0.62 for the 28, $2.77 for R1a, $2.89 for R1b). The approved
  quote put this work at about $6.30.
- **Comparisons:** `vanguard_three_way.py --compare` (first trial, 140 posts) and
  `--r1-split` (R1a and R1b), plus `scripts/vanguard_r1_bootstrap.py`, new today, which
  resamples the 112 posts 2,000 times (seed 20261004) to give a 90% range for each kappa and
  for the change each rule makes.
- **Results:** in the pilot report; recommendation in
  `docs/vanguard/decision-packet-r1a-r1b-2026-10-04.md`.

**Ruled by John, 2026-10-04:** R1a adopted with the reactions sentence; R1b rejected. The
codebook (`docs/vanguard/codebook.md`) is now final for the full-sample run.

**Waiting on John:** about $15 more OpenAI credit. Then the full-sample run as described in
the handover above, on today's codebook with a fresh `--tag`.

## Full-sample run, started 2026-10-04

John topped up the OpenAI credit and started the run the evening of 2026-10-04. Final codebook
(`docs/vanguard/codebook.md`: R2 and R3 adopted 2026-10-03, R1a adopted 2026-10-04). Posts:
the 390 screened in the first pass, listed in `data/vanguard/full-run-posts.csv` (230 top-ranked,
160 random; built from `r-singularity-pilot-codes.csv`). Label `--tag full-final`, so no earlier
reply is reused.

- **GPT:** 390 of 390 posts coded (`r-singularity-pilot-codes-gpt-full-final.csv`), pin
  confirmed. 1.41 million input and 158,000 output tokens; about $21 at the quote's $0.054 a
  post (the exact charge is on OpenAI's billing page).
- **Gemini:** 2 posts coded ($0.05), then refused with "exceeded your current quota". The
  afternoon's 252 trial requests had used the day's allowance, so the daily limit is real; it
  was not yet clear at 18:40 Pacific. To resume once it clears (saved replies are reused):

```
python3 scripts/vanguard_crossfamily_pass.py --family gemini --ids data/vanguard/full-run-posts.csv --tag full-final --max-new 240
```

  Run it twice, on two days; 388 posts remain.
