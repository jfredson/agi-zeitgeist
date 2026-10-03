# Pilot report: r/singularity, vanguard sub-series, 2024Q4 to 2026Q3

**Interim, model-coded.** Updated 2026-10-03 after John's rulings on the first version of
this report and his revision of the reliability design (amendment section 9, log entries of
2026-10-03). Run record: `docs/vanguard/pilot-run-r-singularity-2026-10.md`; codebook:
`docs/vanguard/codebook.md`.

**How coding was checked.** Coding is model-assisted with one human check, a disclosed
limitation, not a second coder. First pass: `claude-opus-5-5` (Anthropic). Blind second
pass on a 140-post subset: `gemini-3.1-pro-preview`, version `3.1-pro-preview-01-2026`
(Google), confirmed against the pinned version before the run. Human check: a 40-post blind
worksheet for John (`data/vanguard/john-vanguard-worksheet.csv`), **not yet coded**.

## Figure

`site/vanguard-pilot-r-singularity.png` (counts in `site/vanguard-pilot-r-singularity.csv`),
labelled "Interim, model-coded" and captioned "Framing in sampled high-score posts from
selected AI enthusiast venues; not representative of participants or the public."

![pilot figure](../../site/vanguard-pilot-r-singularity.png)

## Results (first pass, recoded under the 2026-10-03 rulings)

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

### Cross-family (current check): Claude first pass against Gemini blind pass

122 posts of the 140-post subset are still in the first pass after the recode; main-claim
fields compare the 69 posts both models found eligible.

| field | posts | agreement | Cohen's kappa |
|---|---|---|---|
| eligible or not | 122 | 91% | 0.81 |
| main claim: target | 69 | 72% | 0.55 |
| main claim: temporal status | 69 | 83% | 0.67 |
| main claim: stance | 69 | 67% | 0.39 |
| main claim: epistemic qualification (hedging) | 69 | 87% | 0.26 |
| main claim: rhetorical mode (irony) | 69 | 90% | 0.64 |
| main claim: development preference | 69 | 90% | 0.55 |
| main claim: attribution | 69 | 80% | 0.67 |
| main claim: title only | 69 | 99% | 0.97 |
| extrapolates to a timeline or consequence | 69 | 81% | 0.68 |

The four headline-claim rows (99 to 100%) are left out: almost no post makes those claims,
so agreeing on "no" doesn't test anything.

**Where the two models disagree, and what would fix it:**
1. **Stance on reposts:** 17 of 23 stance disagreements are Claude coding "passes it on
   without taking a side" where Gemini codes "affirms". The codebook doesn't say how to code
   a bare repost with no comment. A rule here would likely lift stance agreement the most.
2. **Target:** the new boundary between `industry_governance` and `specific_capability`
   (9 posts, both directions), then `consequence` against `specific_capability` (4).
3. **Hedging:** Claude marks 9 of 69 main claims as qualified, Gemini 3. Qualified claims are
   rare, so the kappa (0.26) is low despite 87% agreement.
4. **Eligibility:** Gemini found 9 posts eligible that Claude excluded, and 2 the other way:
   Gemini is more inclusive.

### Same-family (superseded): Claude against Claude, before the 2026-10-03 rulings

On the same 140 posts, a second Claude instance agreed far more often (target kappa 0.87,
stance 0.64, hedging 0.81, attribution 0.95). The gap to the cross-family figures is the
reason for the revised design: two copies of one model share blind spots and overstate
reliability. File kept as `data/vanguard/r-singularity-pilot-codes-second.csv`.

### Human check (pending)

`python3 scripts/vanguard_human_agreement.py` reports John's agreement with each model once
`data/vanguard/john-vanguard-worksheet.csv` is coded. Until then, figures stay labelled
"interim, model-coded".

## Edge calls still open

- **Reposts without comment:** affirms or neutral relay (see above).
- **"Capability" for the extrapolation field:** two first-pass coders counted AGI and
  self-improvement claims as capability claims; the figure measures extrapolation among posts
  with a `specific_capability` claim only.
- **Drama borderlines:** celebrity use of a product (Katy Perry subscribing to Claude),
  satire about labs, and government action not aimed at an AI company (the DOGE intern post,
  kept ineligible).

## Not done

John's 40-post human check; the cross-era sample and the comment sample (deferred); section 12
preconditions (venue inventory, X decision). No other venue collected.
