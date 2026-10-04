# Pilot report: r/singularity, vanguard sub-series, 2024Q4 to 2026Q3

**Model-coded, no human coder.** Updated 2026-10-03 after John's rulings: first on the
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

### Proposed codebook rules, before and after (awaiting John's ruling)

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
different field, so they were tested together. Claude and GPT coded all 140 posts. Gemini
coded 112: its project allows 250 requests per model per day, and today's main pass and
trial used them all. The last 28 posts can run after the limit clears, about 17:00 Pacific
on 2026-10-04. (Earlier stops were also money: the OpenAI account ran out of credit and was
topped up.) Kappa before and after on the same 112 posts:

| field | rule | Claude–Gemini | Claude–GPT | Gemini–GPT |
|---|---|---|---|---|
| what the main claim is about | R2 | 0.55 → 0.81 | 0.58 → 0.87 | 0.73 → 0.82 |
| whether the poster agrees | R1 | 0.42 → 0.80 | 0.35 → 0.78 | 0.71 → 0.65 |
| hedging | R3 | 0.22 → 0.86 | 0.18 → 0.62 | 0.55 → 0.62 |
| whose claim it is | (R1 side effect) | 0.72 → 0.75 | 0.66 → 0.86 | 0.80 → 0.62 |
| whether the poster wants AI sped up or slowed down | (none targeted) | 0.53 → 0.58 | 0.33 → 0.55 | 0.65 → 0.52 |
| irony | (none targeted) | 0.59 → 0.71 | 0.46 → 0.72 | 0.52 → 0.69 |
| forecast or already happened | (none targeted) | 0.63 → 0.78 | 0.63 → 0.80 | 0.73 → 0.73 |

With the rules, hedging and irony pass the test. Whether the poster wants AI sped up or
slowed down would fail (every pair below 0.6).

**How to read this:**
1. **The Gemini–GPT column is the cleanest test.** Between Gemini's and GPT's two runs only
   the rules changed. The Claude trial codes came from fresh coders, so the Claude pairs mix
   the rules' effect with the change of coder.
2. **R2 helps in every pair**, including Gemini–GPT (0.73 → 0.82). **R3 helps a lot in the
   Claude pairs, and modestly between Gemini and GPT** (0.55 → 0.62, just over the bar).
3. **R1 brings Claude into line but slightly lowers Gemini–GPT agreement**, both on whether
   the poster agrees (0.71 → 0.65) and on whose claim it is (0.80 → 0.62). The trial coders
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

## Edge calls still open

- **Reposts without comment:** affirms or neutral relay (see above).
- **"Capability" for the extrapolation field:** two first-pass coders counted AGI and
  self-improvement claims as capability claims; the figure measures extrapolation among posts
  with a `specific_capability` claim only.
- **Drama borderlines:** celebrity use of a product (Katy Perry subscribing to Claude),
  satire about labs, and government action not aimed at an AI company (the DOGE intern post,
  kept ineligible).

## Decisions for John

1. **Rules R1 to R3:** adopt, refine or reject each (evidence above).
2. **Where the figure's numbers come from.** John agreed (2026-10-03) to extend the Gemini
   and GPT passes to the whole sample (390 posts), with Gemini's share split over two days
   because of its daily limit, so the figure can use majority codes instead of Claude's,
   which are the outlier. Timing is not yet settled: the plan is to run after the ruling on
   R1 to R3, so the posts are coded once under the final codebook.

## Not done

Gemini's trial run is incomplete at 112 of 140 posts (its daily request limit); the rest can
run after about 17:00 Pacific on 2026-10-04. Also not done: the cross-era sample and the comment sample (deferred), and the section
12 preconditions (venue inventory, X decision). No other venue was collected.
