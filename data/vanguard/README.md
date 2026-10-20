# Vanguard sub-series data (stream F)

r/singularity pilot, 2024Q4 to 2026Q3. Run record: `docs/vanguard/pilot-run-r-singularity-2026-10.md`;
codebook: `docs/vanguard/codebook.md`; report: `docs/vanguard/pilot-report-r-singularity-2026-10.md`.

Coding is fully model-based, with no human coder (my ruling of 2026-10-03). Three models
from different companies code the same 140-post set blind; the final code is their majority
vote per field.

| file | what it is |
|---|---|
| `r-singularity-pilot-sample.csv` | the drawn sample: ranked reserve of 60 per quarter (top posts) and 20 random posts per quarter, with inclusion probabilities. IDs and scores only |
| `r-singularity-pilot-codes.csv` | first pass over the whole sample, model `claude-opus-5-5`, recoded 2026-10-03 under the pilot rulings |
| `second-coder-worksheet.csv` | the 140-post set coded by all three models (30% per quarter and sample, seed 20261004) |
| `r-singularity-pilot-codes-claude-subset-supplement.csv` | Claude codes for the 18 posts in the 140-post set that fell past the recoded first pass's cut-off ranks |
| `r-singularity-pilot-codes-crossfamily.csv` | blind pass by `gemini-3.1-pro-preview`, version `3.1-pro-preview-01-2026` |
| `r-singularity-pilot-codes-gpt.csv` | blind pass by `gpt-6-astra` (created 1787853604, reasoning effort medium) |
| `r-singularity-pilot-codes-majority.csv` | final code per post and field by majority vote; `unresolved` where no two models agree |
| `three-model-reliability.csv` | kappa for each pair of models, unresolved share and verdict, per field |
| `*-rules-trial.csv` | the same 140 posts recoded by each model with the proposed codebook rules added (awaiting my ruling; not used in figures) |
| `r-singularity-pilot-codes-second.csv` | earlier same-family second pass (superseded; kept for the record) |
