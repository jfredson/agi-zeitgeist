# Cost quote: Gemini paid tier for vanguard coding (for me's approval)

Prepared 2026-10-03, before the full-sample run, as I asked. **Approved by me, 2026-10-03:**
up to $15 for the first month (the full run plus the first monthly runs), then up to $5 a
month for three venues.

**Raised by me, 2026-10-06:** October's Gemini spending reached about $17.83 with the full run
at 219 of 390 posts, because the billing account counts the trial work in the same month. I
approved finishing the run ("approve finishing the Gemini coding, go with the recommendation"),
about $4.40 more, taking October to about $22.20; do not go past about $22.50 without asking
again. Details in the run record (`pilot-run-r-singularity-2026-10.md`).

## Basis

- **Price:** Google's published paid-tier rates for `gemini-3.1-pro-preview`: $2.00 per
  million input tokens and $12.00 per million output tokens, with the model's thinking counted
  as output (prompts under 200,000 tokens, which every post is). There is no free tier for
  this model and no monthly fee. The project is on Tier 1: billed after use, with a $250
  spending cap and a limit of 250 requests per model per day.
- **Use per post, measured:** with the rules appended to the codebook, which is the size of
  today's codebook with R2 and R3, the trial used about 3,050 input and 1,580 output tokens
  per post. That is **$0.025 per post**. Without the rules it was $0.022.
- **Posts per venue:** the pilot screened about 29 top posts to reach 20 eligible per quarter,
  plus 20 random posts: about **49 posts per venue per quarter**.
- **Venues:** the three proposed enthusiast venues (r/singularity, r/accelerate,
  r/artificial). Skeptic venues, when they start, cost the same per venue.

## Quote

| item | posts | Gemini cost |
|---|---|---|
| Full-sample run: all 390 pilot posts under the final codebook | 390 | **$9.80**, one time (spread over 2 days by the daily limit) |
| Ongoing, one monthly run per venue, if each quarter's sample is coded in monthly parts | about 16 per venue | $0.41 per venue; **$1.23 a month** for 3 venues |
| Ongoing, one monthly run per venue, if a full-size sample is drawn every month | about 49 per venue | $1.23 per venue; **$3.69 a month** for 3 venues |
| A full recode of the pilot after any codebook change | 390 | $9.80 each time |

**Suggested approval:** up to $15 for the first month (the full run plus the first monthly
runs), then up to $5 a month for three venues. A budget alert in Google Cloud billing can
enforce this.

## Notes

- **Already committed today and tomorrow:** the first trial's remaining 28 posts and the two
  split-rule trials (224 requests): about $6.30, billed to the same account.
- **Cheaper option:** Google's batch mode is half price, but results arrive within hours rather
  than seconds. It would need a script change and a check that the pinned version is the same
  in batch mode.
- **The other two models, for the full picture:** GPT-6 Astra costs about $0.054 per post. The
  full-sample run would be about $21, and the monthly runs $2.60 to $7.90 for three venues.
  After today's split-rule trials, about $10 of the $25 OpenAI credit will remain, so it will
  need topping up before the full run. Claude's coding runs inside the Claude Code session and
  has no separate per-post charge.
- Prices are from Google's and third-party pages as of 2026-10-03; Google can change preview
  pricing.
