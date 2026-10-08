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

**Waiting on John:** a ruling on R1a and R1b. (John added $25 OpenAI credit on 2026-10-03, so GPT's share is covered.) Then the full-sample
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

**Claude, recoded under the final codebook (John, 2026-10-04).** Claude's earlier codes for
these posts predate R2, R3 and R1a, so a three-way majority would have mixed codebooks. Six
fresh `claude-opus-5-5` coders, 65 posts each (posts dealt out in turn, so each part mixes
quarters and post types), coded all 390 blind. They got the same instructions, codebook and
content as Gemini and GPT (brief: `docs/vanguard/claude-coding-brief-full-final.md`; link
pages from the same cache, so the 13 unreadable ones are coded from the title). Output:
`r-singularity-pilot-codes-claude-full-final.csv`, 507 rows, 265 posts eligible.

- Merge check (`vanguard_merge_codes.py`): 37 rows for galleries and dead images had no
  content source; it was filled from the post type and each row's notes say so. One code
  outside the codebook (a timing of "conditional") went back to its coder, who changed it to
  forecast and, under R3's explicit "if", set hedging to qualified.
- Each quarter's top-ranked posts no longer come to exactly 20 eligible (18 to 22). That is
  expected: the cut-off is re-applied from the majority codes when the figure is redrawn.
- Interim Claude–GPT kappas on 390 posts: whether the post counts 0.91; what the claim is
  about 0.83; whether the poster agrees 0.63 (0.36 on the old codes); hedging 0.66; whose
  claim it is 0.71; every field at 0.59 or above.
- `vanguard_three_way.py --full` builds the majority and the three-pair table once Gemini's
  file exists.

## Gemini, 2026-10-06: stopped at 219 of 390, waiting on John over the cost limit

The daily limit had reset: a one-request test at 09:14 Pacific was accepted and the pin was
confirmed (`gemini-3.1-pro-preview` version `3.1-pro-preview-01-2026`). The run went ahead with
the command from the section above, capped at 240 requests for the day.

- **Stopped by hand at 10:16 Pacific**, just after a reply was saved, so no request was cut off
  partway. It stopped because the October spending limit was found to be already passed (below),
  not because of the daily limit. No request was refused.
- **Where it stopped:** 217 new requests today, plus the 2 from 2026-10-04: **219 of 390 posts
  coded**, the first 219 in the order of `data/vanguard/full-run-posts.csv`, with no gaps. The
  next post is `1ojx1hr` (position 220); **171 remain**.
  `r-singularity-pilot-codes-crossfamily-full-final.csv` was written from the saved replies with
  `--cached-only` and holds those 219 posts.
- **Cost of today's coding:** $5.58 for 217 requests (689,343 input and 350,375 output tokens,
  thinking counted as output, at $2 and $12 per million). The full run so far: $5.63 for 219 posts,
  $0.0257 a post.

**Against the approved quote.** John approved up to $15 for October (the full run plus the first
monthly runs), with the full run itself quoted at $9.80.
- Google's billing page showed $12.25 for October before today's coding (about $5.90 on
  2026-10-03 and $6.30 on 2026-10-04, the rules trials). The quote listed the 2026-10-04 trial
  work as "already committed" beside the $15 rather than inside it, but the billing account
  counts it all in one month.
- With today's $5.58, October is about **$17.83, already over the $15**.
- Finishing the full run needs about $4.40 more (171 posts at $0.0257), taking the full run to
  about $10.03 (just over its own $9.80 line) and October to about **$22.20**.
- So **finishing would exceed the approved $15**. It is not resumed without John's go. A $25
  monthly budget alert is now set on the billing account.

**To resume once John approves** (saved replies are reused; at most about 240 requests a day):

```
python3 scripts/vanguard_crossfamily_pass.py --family gemini --ids data/vanguard/full-run-posts.csv --tag full-final --max-new 171
python3 scripts/vanguard_three_way.py --full
```

Then re-apply the 20-eligible cut-off per quarter from the majority codes, redraw the figure
from the majority codes, and check that "AGI already achieved" counts leave out ironic posts.

**Approved by John, 2026-10-06, about 10:20 Pacific** (in the planning session; recorded as a
TimeAssembler decision): "approve finishing the Gemini coding, go with the recommendation."
That is about $4.40 more, about $22.20 for October; the limit is now about $22.50 for October
without asking again. The approval is also noted under the quote in
`model-cost-quote-2026-10-03.md`. The run resumed straight after.

### Resumed 2026-10-06 after the approval: stopped at the daily limit, 254 of 390

- The resumed run coded **35 more posts** (positions 220 to 254). The 36th request was refused
  with "exceeded your current quota" at about 10:30 Pacific, after two waits. That is the daily
  limit, not the money: 252 requests were accepted today, the same ceiling as 2026-10-04 (254).
  The refused request was not saved and is not charged.
- **Where it stopped:** **254 of 390 posts coded**, the first 254 in `full-run-posts.csv`, with no
  gaps. The next post is `1rgdt31` (position 255); **136 remain**. The output file holds the 254
  posts, written from the saved replies with `--cached-only`.
- **Cost:** $6.37 today (252 requests). The full run so far is $6.42 for 254 posts ($0.0253 a post).
  October is about **$18.62** ($12.25 before today, plus today).
- **To finish:** 136 posts at about $0.0253 is about $3.45 more. That takes the full run to about
  $9.87 and October to about **$22.07**, inside John's 2026-10-06 limit of about $22.50.

**Resume after midnight Pacific (2026-10-07 or later)**, when the daily limit resets. It fits in
one day's allowance:

```
python3 scripts/vanguard_crossfamily_pass.py --family gemini --ids data/vanguard/full-run-posts.csv --tag full-final --max-new 136
python3 scripts/vanguard_three_way.py --full
```

Then re-apply the 20-eligible cut-off per quarter from the majority codes, redraw the figure
from the majority codes, and check that "AGI already achieved" counts leave out ironic posts. If
the per-post cost runs higher than expected, stop before October passes about $22.50 (full run
about $10.30) and ask John again.

## Gemini, 2026-10-07: finished, 390 of 390, and the three-way comparison

Scheduled run, started 09:34 Pacific, with the command from the section above. The daily limit
had reset and no request was refused. It ran in three batches (40, 50, 46) so the cost could be
checked between them against John's 2026-10-06 limit of about $22.50 for October; it never came
close to it.

- **Posts coded:** the remaining **136** (positions 255 to 390). **All 390 of 390 are now coded**,
  in the order of `data/vanguard/full-run-posts.csv`, with no gaps. Every reply reported
  `gemini-3.1-pro-preview` with the pinned version `3.1-pro-preview-01-2026`. Finished about
  10:20 Pacific. `r-singularity-pilot-codes-crossfamily-full-final.csv` now holds all 390 posts.
- **Cost of today's coding:** $3.41 for 136 requests (420,078 input and 213,923 output tokens,
  thinking counted as output, at $2 and $12 per million), $0.0251 a post.
- **The full run:** $9.83 for 390 posts ($0.0252 a post), 3 cents over its $9.80 quote
  and under the $10.30 stopping line.
- **October so far:** about **$22.03** ($12.25 before 2026-10-06, $6.37 on 2026-10-06, $3.41
  today), inside the approved $22.50. The figures are worked out from the saved token counts;
  Google's billing page has the exact charge and may lag by a day.

**Three-way comparison** (`python3 scripts/vanguard_three_way.py --full`). Claude, Gemini and GPT
each coded all 390 posts under the final codebook. A post counts by majority: **265 eligible**.
Output: `r-singularity-pilot-codes-majority-full-final.csv` (the majority codes) and
`three-model-reliability-full-final.csv` (the table below). The numbers are kappa, a measure of
how often two coders agree beyond what chance would give (1 is perfect, 0.6 is the usual floor
for "good enough"); n is the number of posts both coders counted. "No majority" is the share of
posts where all three gave a different answer.

| What is coded | Claude–Gemini | Claude–GPT | Gemini–GPT | No majority | Script's verdict |
|---|---|---|---|---|---|
| Whether the post counts | 0.91 (390) | 0.91 (390) | 0.94 (390) | 0% | reliable |
| What the claim is about | 0.77 (259) | 0.83 (254) | 0.76 (258) | 2% | reliable |
| Timing (already here, forecast, …) | 0.65 (259) | 0.63 (254) | 0.63 (258) | 5% | reliable |
| Whether the poster agrees | 0.75 (259) | 0.63 (254) | 0.56 (258) | 3% | reliable |
| Hedging | 0.73 (259) | 0.66 (254) | 0.54 (258) | 0% | reliable |
| Tone of the post | 0.74 (259) | 0.75 (254) | 0.79 (258) | 0% | reliable |
| Whether the poster wants it faster or slower | 0.46 (259) | 0.59 (254) | 0.45 (258) | 0% | unreliable (every pair below 0.6; ruled unreliable by John, 2026-10-03) |
| Whose claim it is | 0.72 (259) | 0.71 (254) | 0.71 (258) | 1% | reliable |
| Coded from the title alone | 0.99 (259) | 0.99 (254) | 1.00 (258) | 0% | reliable |
| Projects to a time horizon | 0.75 (259) | 0.72 (254) | 0.73 (258) | 1% | reliable |

Worth a look in the working session: Gemini and GPT agree less with each other than either does
with Claude on whether the poster agrees (0.56) and on hedging (0.54). The script still calls both
fields reliable because the other two pairs clear 0.6.

**Not done yet (left for a working session, as planned):** re-apply the 20-eligible cut-off per
quarter from the majority codes, redraw the figure from the majority codes, and check that
"AGI already achieved" counts leave out ironic posts.
