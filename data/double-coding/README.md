# Double-coding sample (seed phase)

For the pass check in `docs/methodology-v2.md` section 12: two independent codings of
two seed speakers should agree on `frame_primary`, `endorsement` and
`target_capability` at least 80% of the time. John codes this sample blind (amendment
A14, ruling 13).

- **Sample:** 30 statements, 15 from Geoffrey Hinton and 15 from Gary Marcus, stratified
  by era (2005 to 2015, 2016 to 2022, 2023 onward), drawn with seed **20261001** by
  `scripts/double_coding_sample.py` on 2026-10-01. Within each speaker the 15 are split
  across eras in proportion to how many statements each era holds, with at least one per
  era: Hinton 1 / 3 / 11, Marcus 1 / 4 / 10. Rows are shuffled so the file isn't grouped
  by speaker or era.
- **`john-sample.csv`:** statement id, speaker, date, source link and quote, with five
  empty columns to fill: `target_capability`, `frame_primary`, `endorsement`,
  `present_capability`, `affect`. Use the codes in `docs/codebook.md`. Read the source
  where the quote isn't enough.
- **`agent-codes.csv`:** the agent's codes for the same 30 statements as of 2026-10-01
  (after the A14 recode). **Don't open it until you've finished coding**, or the check
  isn't blind.
- **Compare:** `python3 scripts/agreement.py` prints per-field agreement, Cohen's kappa
  (agreement corrected for chance) and every disagreement.

Rerunning the sampling script overwrites both files. Don't rerun it once you've started
coding.
