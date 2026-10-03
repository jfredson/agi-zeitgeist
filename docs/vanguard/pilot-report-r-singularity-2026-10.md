# Pilot report: r/singularity, vanguard sub-series, 2024Q4 to 2026Q3

Run 2026-10-03 under the run record `docs/vanguard/pilot-run-r-singularity-2026-10.md`
(committed before sampling and coding) and the accepted amendment
`docs/amendments/2026-10-02-vanguard-stream.md`. First-pass and second-pass coding by model
`claude-opus-5-5`. **This is a pilot: the second coder is a model, not the two people
section 9 of the amendment requires, so the agreement numbers below are interim.**

## Figure

`site/vanguard-pilot-r-singularity.png` (counts in `site/vanguard-pilot-r-singularity.csv`).
Captioned "Framing in sampled high-score posts from selected AI enthusiast venues; not
representative of participants or the public."

![pilot figure](../../site/vanguard-pilot-r-singularity.png)

**What it shows.** The four claims the amendment's outputs are built around are almost
absent from r/singularity's posts in this window:

| claim (poster affirms it) | top posts, 160 eligible | random posts, 81 eligible |
|---|---|---|
| AGI already achieved | 3 (2026Q2, 2026Q3, one in 2025Q2) | 0 |
| AGI within a stated horizon | 0 | 0 |
| Self-improvement under way | 0 | 0 |
| Singularity framing | 7 | 1 |

Excluding title-only rows raises some shares (the denominators shrink more than the
numerators) but changes no pattern. The lines are flat at or near zero, so **the pilot
can't show a trend in these claims, in either direction**.

**What the posts claim instead** (main claim of each eligible post):

| claim target | top posts | random posts |
|---|---|---|
| a specific capability (a model, benchmark, robot or demo) | 95 (59%) | 41 (51%) |
| a consequence (jobs, society, politics, the economy) | 43 (27%) | 27 (33%) |
| AGI or general capability | 12 (8%) | 8 (10%) |
| pace of progress or singularity | 9 (6%) | 4 (5%) |
| self-improvement | 1 (1%) | 1 (1%) |

Main-claim stance among eligible top posts: affirms 88, passes it on without taking a side
48, denies 16, questions 4, unclear 3, conditional 1.

## Samples

| | top posts (rewarded) | random posts (prevalence) |
|---|---|---|
| posts screened | 291 (ranks 1 to 31–46 per quarter, until 20 eligible) | 160 (20 per quarter, seed 20261003) |
| eligible | 160 (20 per quarter) | 81 (6 to 15 per quarter) |
| excluded: no AI claim | 101 | 53 |
| excluded: content unavailable (galleries, dead images, title removed) | 24 | 25 |
| excluded: image with no legible text | 6 | 1 |
| eligible posts coded from the title only | 69 (43%) | 31 (38%) |

Random-post shares rest on few eligible posts per quarter (as few as 6), so the right-hand
panels are noisy.

## Agreement between the two coding passes (interim, model with model)

140 posts (30% per quarter and sample, seed 20261004), coded blind by a fresh instance of
the same model. Main-claim fields compare the 64 posts both coders found eligible.

| field | posts compared | agreement | Cohen's kappa |
|---|---|---|---|
| eligible or not | 140 | 96% | 0.91 |
| main claim: target | 64 | 92% | 0.87 |
| main claim: temporal status | 64 | 88% | 0.80 |
| main claim: stance | 64 | 80% | 0.64 |
| main claim: epistemic qualification (hedging) | 64 | 94% | 0.81 |
| main claim: rhetorical mode (irony) | 64 | 92% | 0.77 |
| main claim: development preference | 64 | 91% | 0.63 |
| main claim: attribution | 64 | 97% | 0.95 |
| main claim: title only | 64 | 98% | 0.97 |
| post level: AGI already achieved | 64 | 98% | 0.00 |
| post level: AGI within a stated horizon | 64 | 100% | 1.00 |
| post level: self-improvement under way | 64 | 100% | 1.00 |
| post level: singularity framing | 64 | 100% | 1.00 |

How to read it:
- **Stance (80%, kappa 0.64) and development preference (kappa 0.63) are the weakest
  fields**, mostly at the border between "affirms" and "passes it on without taking a side",
  and on memes.
- **The four post-level rows are uninformative.** Both coders found almost none of these
  claims, so agreeing on "no" doesn't test reliability; the 0.00 kappa for "AGI already
  achieved" comes from one disagreement on a near-empty category. Don't cite them.
- Two copies of one model agreeing is weaker evidence than two people agreeing; shared
  blind spots don't show up. The human worksheet for the same 140 posts is
  `data/vanguard/second-coder-worksheet.csv` (links only, codes blank).

## Edge calls the coders flagged (candidates for codebook rules)

1. **AI-misbehaviour and company drama** (Grok's political answers, Musk–Altman spats,
   Anthropic–Pentagon): one coder excluded these as no AI claim, another coded some as
   consequence. This boundary moved the 2025Q3 cut-off by several ranks.
2. **Video titles that only name a demo** ("Atlas … backflip", "Will Smith eating
   spaghetti in Veo 3.1"): coded as implied capability claims. A stricter rule would exclude
   them and push cut-offs deeper.
3. **Memes and irony**: "AGI achieved" memes coded as affirms with ironic mode by one coder
   and as unclear or denies by others; the hedge and irony fields carry this.
4. **Posts that never name AI** (StackOverflow decline chart, a Yang jobs tweet): coded as
   consequence by inference from the subreddit by some coders, excluded by others.
5. **Image posts whose body text makes the claim but whose image has none** (MIT 3D-printing
   post): excluded under the image rule, which cuts against the text.
6. **Frame tags from incidental words** ("ARC-AGI" as a benchmark name, "singularity of
   sight"): handled differently across coders; the singularity-framing measure depends on
   this.

## Problems found and fixed during the run

Recorded in the run record before the second pass: images for rewarded ranks below 40 had
not been saved, so ten posts were wrongly excluded; fixed and recoded (cut-offs moved in
2025Q1, 2025Q3, 2026Q1). Text posts with removed bodies were handled three ways; made
uniform (coded from the title, `title_only: yes`).

## Not done, and what the amendment still requires

- **Two-person blind coding** (section 9): worksheet ready, not done.
- **Cross-era sample** (section 6) and the **comment sample** (stream F): deferred.
- **Section 12 preconditions** (venue inventory, X decision): not done; no other venue
  collected.
