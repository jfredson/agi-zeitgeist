# Spending record: the AGI Zeitgeist

Every run paid for from the monthly Anthropic API credits, and any spend out of pocket, one row
each. Started 2026-11-16 with the first credit-paid run. Earlier spending is not gathered here
yet: the Gemini costs of October 2026 are in `docs/vanguard/model-cost-quote-2026-10-03.md` and
`docs/amendments.md`.

The rule (`timeassembler/docs/session-routing.md`, "Spend gate"): a credit-paid job expected to
cost more than about $50 goes to John first; smaller ones are run and recorded here. Spend out
of pocket always needs his go first.

| Date | Vendor | What it bought | Cost | Go |
|---|---|---|---|---|
| 2026-11-16 | Anthropic credits (`zeitgeist-coder` key) | Trial of the year-by-year claims search script (`scripts/claims_search.py`) on Sam Altman, 2015 to 2026, on Claude Opus 5.5: one test year at the first settings ($0.21), then twelve years at 12 searches and 6 pages each ($7.47). 120 searches billed, 29 candidate claims, none yet checked on the page. | $7.68 measured from the token counts the API returned. One reply timed out and was run again; a timed-out reply returns no count, so the Console figure may be slightly higher. | Under $50, no separate go needed. John chose "Run the pilot" in the session of 2026-11-16. |
| 2026-11-16 | Anthropic credits (`zeitgeist-coder` key) | The same search for the other fourteen figureheads, 157 person-years, on Claude Opus 5.5 at 12 searches and 6 pages a year: Musk 2015 to 2026 ($7.14), Amodei 2021 to 2026 ($3.58), Huang 2014 to 2026 ($7.97), Hassabis 2010 to 2026 ($9.36), Suleyman 2010 to 2019 and 2022 to 2026 ($8.03), Sutskever 2015 to 2026 ($7.29), Legg 2010 to 2026 ($9.32), LeCun 2013 to 2026 ($9.15), Liang Wenfeng 2023 to 2026 ($2.11), Mensch 2023 to 2026 ($2.41), Zuckerberg 2013 to 2026 ($11.51), Pichai 2015 to 2026 ($8.32), Nadella 2014 to 2026 ($9.45), Kai-Fu Lee 2023 to 2026 ($2.48). 1,589 searches billed, 272 candidate claims (55 match claims already recorded), none yet checked on the page. | $98.12 measured from the token counts the API returned. No year failed or was run twice. | Over $50, so it went to John first with an estimate of $90 to $115. His go, 2026-11-16: "Run all fourteen". |
| 2026-11-25 | Anthropic credits (`zeitgeist-coder` key) | A first sort of the 232 unchecked claim candidates from the year-by-year search (thirteen people; Altman's and Musk's were already checked) against the admission rule, by the new script `scripts/claims_prescreen.py` on Claude Opus 5.5: one request per candidate, opening its source page and reading it against the rule's four parts. A trial of 20 ($1.99), then the other 212 ($17.33). Output: a worksheet per person (`data/claims-search/<speaker>-prescreen.csv`), which admits nothing; sessions still check every candidate. | $19.32 measured from the token counts the API returned. No request failed. | Under $50. Proposed by the month-end credit check of 2026-11-25 at about $10 to $20; John's go the same day: "Yes, pre-screen only". |
