# Pilot report: r/singularity, vanguard sub-series, 2024Q4 to 2026Q3

**Model-coded, no human coder.** Updated 2026-10-04 with Gemini's trial results (all three
models now complete on both trials). Updated 2026-10-03 after John's rulings: first on the
first version of this report, then on the reliability design, which he revised twice that
day. Coding is now fully model-based (amendment section 9; log entries of 2026-10-03). Run
record: `docs/vanguard/pilot-run-r-singularity-2026-10.md`; codebook:
`docs/vanguard/codebook.md`.

**How coding was checked.** Three models from different companies coded the same 140-post
set blind:
- `claude-opus-5-5` (Anthropic), the first pass;
- `gemini-3.1-pro-preview`, version `3.1-pro-preview-01-2026` (Google);
- `gpt-6-astra`, reasoning effort medium (OpenAI). OpenAI publishes no dated snapshot, so it
  is pinned by the creation time OpenAI lists for it (1787853604, which is 2026-08-27 UTC).

The final code for each field is the majority vote
(`data/vanguard/r-singularity-pilot-codes-majority.csv`). Models from different companies can
still share blind spots; this is a disclosed limitation.

## Figure

`site/vanguard-pilot-r-singularity.png` (counts in `site/vanguard-pilot-r-singularity.csv`),
labelled "model-coded" and captioned "Framing in sampled high-score posts from
selected AI enthusiast venues; not representative of participants or the public."

![pilot figure](../../site/vanguard-pilot-r-singularity.png)

## Results (first pass, recoded under the 2026-10-03 rulings)

These shares come from Claude's first pass over the whole sample, because the three-model
majority code exists only for the 140-post set. **Caution:** on those 140 posts Claude is the
odd one out (see Agreement). Against the majority, it codes more main claims as consequence
claims (13 against 6 of the 88 posts the majority finds eligible) and fewer as capability
claims (37 against 48). So the consequence shares below are probably too high and the
capability shares too low. Company-and-policy shares match (25 and 25).

**Primary measures.** Share of eligible posts making each kind of claim, all quarters
together:

| claim | top posts, 160 eligible | random posts, 94 eligible |
|---|---|---|
| a specific capability (a model, benchmark, robot or demo) | 80 (50%) | 46 (49%) |
| a consequence (jobs, society, the economy) | 31 (19%) | 23 (24%) |
| industry and governance (AI company and policy drama; new category) | 50 (31%) | 22 (23%) |
| capability posts that extrapolate to a timeline or consequence | 11 of 80 (14%) | 4 of 46 (9%) |

By quarter, capability claims range from about a quarter to two-thirds of eligible top
posts, and industry-and-governance claims peak in 2025Q1 (DeepSeek, Stargate, the Musk–Altman
fight) and 2026Q1 (Anthropic and the Pentagon). Extrapolation from a capability to a timeline
or consequence is uncommon throughout.

**Headline claims, near-absent** (poster affirms; any of AGI already achieved, AGI by a
stated horizon, self-improvement under way, singularity framing): at most 2 of 20 eligible
top posts in any quarter, and 1 random post in the whole window. AGI claims of any kind are
7% of top posts and 9% of random posts; self-improvement claims 0% and 2%.

**Samples.** Top posts: 230 screened to reach 20 eligible per quarter (cut-offs between rank
26 and 32); excluded: no AI claim 46, content unavailable 19, image without legible text 5.
Random posts: 160 screened, 94 eligible; excluded: no AI claim 40, content unavailable 25,
image without legible text 1. Eligible posts coded from the title only: 62 top, 38 random.

The 2026-10-03 rulings changed the sample: making company and policy drama eligible moved
most top-post cut-offs up (2025Q1 from rank 41 to 29, 2025Q3 from 44 to 27, 2026Q1 from 46
to 32), and posts that don't mention AI dropped out.

## Agreement

### Three models, the main codes (all 140 posts)

Cohen's kappa (agreement corrected for chance) for each pair of models. "Whether the post
counts" is compared on all 140 posts; the other fields on the posts both models in the pair
found eligible (78 to 85). "Unresolved" is the share of the 88 posts the majority finds
eligible where no two models agree. Full table: `data/vanguard/three-model-reliability.csv`.

| field | Claude–Gemini | Claude–GPT | Gemini–GPT | unresolved | verdict |
|---|---|---|---|---|---|
| whether the post counts | 0.82 | 0.82 | 0.91 | 0% | reliable |
| what the main claim is about | 0.57 | 0.62 | 0.75 | 6% (5 posts) | reliable |
| forecast or already happened | 0.66 | 0.66 | 0.77 | 5% | reliable |
| whether the poster agrees | 0.38 | 0.36 | 0.69 | 1% | reliable |
| hedging | 0.22 | 0.18 | 0.56 | 2% | **unreliable** |
| irony | 0.60 (0.595) | 0.57 | 0.58 | 3% | **unreliable** |
| whether the poster wants AI sped up or slowed down | 0.55 | 0.43 | 0.65 | 0% | reliable |
| whose claim it is | 0.67 | 0.64 | 0.78 | 1% | reliable |
| coded from the title only | 0.97 | 0.97 | 1.00 | 0% | reliable |
| draws a timeline or consequence from a capability | 0.71 | 0.64 | 0.65 | 0% | reliable |

Under John's test (unresolved on more than 15% of posts, or every pairwise kappa below 0.6),
**hedging and irony are unreliable** and are kept out of figures. No measure in the current
figure depends on either, so the figure keeps all five panels. No field comes close to the
15% unresolved limit.

**Claude is the outlier.** Gemini and GPT agree with each other more than either agrees with
Claude on almost every field. Whether the poster agrees passes only because the Gemini–GPT
pair reaches 0.69, and what the main claim is about passes because two pairs reach 0.6. The
same-family check (two copies of Claude, before the rulings: kappa 0.87 on what the claim is
about) badly overstated reliability.

### Codebook rules R1 to R3, before and after

**Where things stand (2026-10-04).** John adopted R2 and R3 on 2026-10-03 (now in
`docs/vanguard/codebook.md`) and split R1 into two rules to be trialled separately: R1a for
whether the poster agrees and R1b for whose claim it is. Their results are in the next
section; R1a and R1b await his ruling. The first trial below is now complete on all 140
posts.

The rules are in `docs/vanguard/proposed-rules-2026-10-03.md`:
- **R1, posts passed on without comment:** these are "passes it on without taking a side"
  unless the poster adds words endorsing or rejecting the claim, and the claim is attributed
  to its source.
- **R2, company and policy news or capability:** the target is decided by the subject of the
  main claim (a model or system, a company or government, or people and society), not by
  which company is named.
- **R3, hedging:** "qualified" only if the words stating the claim contain a hedge word from a
  set list.

All three models recoded the 140 posts with the three rules added. Each rule targets a
different field, so they were tested together. Claude and GPT coded all 140 posts on
2026-10-03. Gemini coded 112 that day, when its daily request limit ran out, and the last 28
on 2026-10-04 under the same frozen codebook
(`docs/vanguard/codebook-frozen-2026-10-03-before-rules.md`). Kappa before and after on all
140 posts:

| field | rule | Claude–Gemini | Claude–GPT | Gemini–GPT |
|---|---|---|---|---|
| what the main claim is about | R2 | 0.57 → 0.82 | 0.62 → 0.85 | 0.75 → 0.79 |
| whether the poster agrees | R1 | 0.38 → 0.75 | 0.36 → 0.74 | 0.68 → 0.63 |
| hedging | R3 | 0.21 → 0.77 | 0.18 → 0.53 | 0.56 → 0.56 |
| whose claim it is | (R1 side effect) | 0.66 → 0.69 | 0.64 → 0.81 | 0.78 → 0.57 |
| whether the poster wants AI sped up or slowed down | (none targeted) | 0.55 → 0.52 | 0.43 → 0.65 | 0.65 → 0.47 |
| irony | (none targeted) | 0.60 → 0.71 | 0.57 → 0.75 | 0.58 → 0.74 |
| forecast or already happened | (none targeted) | 0.66 → 0.75 | 0.65 → 0.74 | 0.77 → 0.71 |

With the rules, hedging and irony pass the test. On the first 112 posts (the figures John
ruled on) the rows read much the same, with two exceptions: hedging between Gemini and GPT
was 0.55 → 0.62 and is now 0.56 → 0.56, and whose claim it is between Gemini and GPT was
0.80 → 0.62 and is now 0.78 → 0.57.

**How to read this:**
1. **The Gemini–GPT column is the cleanest test.** Between Gemini's and GPT's two runs only
   the rules changed. The Claude trial codes came from fresh coders, so the Claude pairs mix
   the rules' effect with the change of coder.
2. **R2 helps in every pair**, including Gemini–GPT (0.75 → 0.79). **R3 helps a lot in the
   Claude pairs but not between Gemini and GPT** (0.56 → 0.56 on all 140 posts). Hedging
   still passes the test through Claude–Gemini (0.77); the fresh-sample check should look at
   it closely.
3. **R1 brings Claude into line but slightly lowers Gemini–GPT agreement**, both on whether
   the poster agrees (0.68 → 0.63) and on whose claim it is (0.78 → 0.57). The trial coders
   found that R1 has no default when a post names no source, and no answer for a model's own
   output in a screenshot. Refinement for John to consider: when no source is named,
   attribution = original; a model's output = lab_or_company.
4. **Optimistic by construction.** The rules were written from disagreements on these same
   posts, so they will look better here than on new posts. Any rule John adopts is checked
   again on a fresh sample (section 9).
5. **Other refinements the trial coders raised:**
   - R3: an "if" that sets a condition is not a hedge.
   - R2: a launch or release decision is the company's act, but what the product does is a
     capability claim. When a title makes both claims, the main claim needs a tie-break.
   - R1: "denies" means rejecting that the claim is true. Disliking what is reported goes in
     development preference.

The trial codes (`*-rules-trial.csv`) aren't used in any figure or count.

### R1a and R1b, each tried alone (awaiting John's ruling)

Run 2026-10-03 (Claude, GPT) and 2026-10-04 (Gemini) on the same 112 posts
(`data/vanguard/r1-split-trial-posts.csv`), with today's codebook (R2 and R3 adopted) plus one
rule each. Each run serves as the other's comparison, so "without" means the same codebook,
day and models with only the rule under test missing (`vanguard_three_way.py --r1-split`).
The 90% ranges come from resampling the posts 2,000 times (`scripts/vanguard_r1_bootstrap.py`).

| field | rule | Claude–Gemini | Claude–GPT | Gemini–GPT |
|---|---|---|---|---|
| whether the poster agrees | R1a | 0.45 → 0.78 | 0.50 → 0.74 | 0.53 → 0.65 |
| whose claim it is | R1b | 0.77 → 0.83 | 0.75 → 0.72 | 0.78 → 0.75 |

- **R1a decides whether the field is usable.** Without it every pair is below 0.6, so
  whether the poster agrees fails John's test; with it every pair passes. The gain is clear
  in both Claude pairs (+0.13 to +0.51 and +0.05 to +0.44) and likely between Gemini and GPT
  (−0.11 to +0.37; R1a higher in 82% of resamples).
- **R1b makes no measurable difference** (every range spans zero), and the field passes
  without it.
- **What's left:** most remaining stance disagreements under R1a are posts whose only words
  are a reaction or joke ("HOLY SHIT", "This… could be something…"). The original R1 had a
  sentence for this that the split dropped.

Decision packet with the recommendation (refine and adopt R1a; reject R1b):
`docs/vanguard/decision-packet-r1a-r1b-2026-10-04.md`. The split-trial codes
(`*-r1a-trial.csv`, `*-r1b-trial.csv`) aren't used in any figure or count.

## Edge calls still open

- **Reposts without comment:** affirms or neutral relay, and whose claim they are (R1a and
  R1b above; awaiting John).
- **"Capability" for the extrapolation field:** two first-pass coders counted AGI and
  self-improvement claims as capability claims; the figure measures extrapolation among posts
  with a `specific_capability` claim only.
- **Drama borderlines:** celebrity use of a product (Katy Perry subscribing to Claude),
  satire about labs, and government action not aimed at an AI company (the DOGE intern post,
  kept ineligible).

## Decisions for John

1. **Rules R1a and R1b:** adopt, refine or reject each. Packet:
   `docs/vanguard/decision-packet-r1a-r1b-2026-10-04.md`. (R2 and R3 adopted 2026-10-03.)
2. **Where the figure's numbers come from.** John agreed (2026-10-03) to extend the Gemini
   and GPT passes to the whole sample (390 posts), with Gemini's share split over two days
   because of its daily limit, so the figure can use majority codes instead of Claude's,
   which are the outlier. Timing is not yet settled: the plan is to run after the ruling on
   R1a and R1b, so the posts are coded once under the final codebook, and after the OpenAI
   account has about $15 more credit.

## Not done

All trial runs are complete (Gemini finished on 2026-10-04). Not done: the full-sample run
(waiting on the R1a and R1b ruling), the cross-era sample and the comment sample (deferred),
and the section 12 preconditions (venue inventory, X decision). No other venue was collected.
