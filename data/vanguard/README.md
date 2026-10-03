# Vanguard sub-series data (stream F)

r/singularity pilot, 2024Q4 to 2026Q3. Run record: `docs/vanguard/pilot-run-r-singularity-2026-10.md`;
codebook: `docs/vanguard/codebook.md`; report: `docs/vanguard/pilot-report-r-singularity-2026-10.md`.

| file | what it is |
|---|---|
| `r-singularity-pilot-sample.csv` | the drawn sample: ranked reserve of 60 per quarter (top posts) and 20 random posts per quarter, with inclusion probabilities. IDs and scores only |
| `r-singularity-pilot-codes.csv` | first pass, model `claude-opus-5-5`, recoded 2026-10-03 under the pilot rulings |
| `r-singularity-pilot-codes-crossfamily.csv` | blind second pass by a different model family, `gemini-3.1-pro-preview` version `3.1-pro-preview-01-2026`, on the 140-post subset |
| `r-singularity-pilot-codes-second.csv` | earlier blind second pass by the same model family (superseded by the cross-family pass; kept for the record; predates the 2026-10-03 rulings) |
| `second-coder-worksheet.csv` | the 140-post second-pass subset (30% per quarter and sample, seed 20261004) |
| `john-vanguard-worksheet.csv` | **John's 40-post blind check** (seed 20261005), drawn from the subset posts both models coded |

## For John: coding the 40-post worksheet blind

1. Open each `permalink`, read the post (and its image, or only the title for videos), and
   fill in the post's eligibility and its **main claim** using `docs/vanguard/codebook.md`.
2. **Don't open the model code files above until you've finished**, or the check isn't blind.
3. Then run `python3 scripts/vanguard_human_agreement.py` to see your agreement with each
   model, field by field.
