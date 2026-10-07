# AGI Zeitgeist Tracker

A dated, sourced record of how expert and public opinion about artificial general
intelligence (AGI: AI that can do most intellectual work a person can) has moved
from 2005 to the present. Every row links to where it came from, every search that
produced a row is logged, and the coding rules are written down, so anyone can
check the record or extend it.

The working question: did the main public argument move from *whether* AGI is
possible, to *when* it arrives, to *whether today's systems are already close or
improving themselves*? The method is built so the data can say no.

**Status (2026-09-30):** seed phase. Five people traced (Ray Kurzweil, Geoffrey
Hinton, Yann LeCun, Gary Marcus, Sam Altman), plus surveys, prediction markets,
polls and dated events. Coded under methodology version 2, adopted the same day after
two outside reviews. **The expert panel was frozen on 2026-10-06** (amendment A18): 25
core members and a 2020s cohort of 12 in `data/speakers.csv`, and a wide list of 308 in
`data/wide_list_candidates.csv`. Full collection for the panel is next; the public
streams (surveys, published argument, online communities) have not started.

## What's here

| path | what it is |
|---|---|
| `data/speakers.csv` | one row per person, survey, market, pollster or institution |
| `data/statements.csv` | one row per public statement, with a verbatim quote, link and codes |
| `data/aggregates.csv` | survey results, prediction market readings and poll results |
| `data/events.csv` | dated events (open letters, government actions, reports) for chart labels |
| `data/search_log.csv` | every search run to build the record, and what it found |
| `docs/methodology-v2.md` | the method (version 2, 2026-09-30): four streams, coding scheme, panel rule, preregistered tests |
| `docs/methodology.md` | pointer to version 2, plus details carried over from version 1 |
| `docs/codebook.md` | how each statement is coded under version 2, with decision rules and examples |
| `docs/reviews/` | the two outside reviews behind version 2 |
| `docs/panel-verification-2026-10.md` | evidence for each panel candidate, for John's freeze decision |
| `docs/amendments.md` | dated changes to the panel or the codes |
| `docs/2026-09-30-kickoff.md` | the original plan |
| `scripts/validate.py` | checks every row: codes, dates, sources, links between files |
| `scripts/charts.py` | builds the charts from the CSV files |
| `site/` | chart images, and later a static page |

## How to cite

> Fredrickson, J. (2026). *AGI Zeitgeist Tracker* [dataset]. Version of
> <commit date>, commit <short hash>. https://github.com/<to be published>

Cite a specific commit: the data changes as rows are added, and a commit pins the
version you used. To cite a single statement, give its `statement_id`
(e.g. `hinton-2023-02`) along with the commit.

**Licence.** The data in `data/` is under Creative Commons Attribution 4.0 (CC BY 4.0,
see [`LICENSE-DATA`](LICENSE-DATA)): reuse it freely, with credit. The scripts in
`scripts/` are under the MIT licence (see [`LICENSE`](LICENSE)). When you reuse the
data, cite it as above, with the commit you used and a link to the licence:
"AGI Zeitgeist Tracker by John Fredrickson, CC BY 4.0".

## How to add a row

1. Read `docs/methodology-v2.md` (especially section 3) and `docs/codebook.md`.
2. Log your search first: add a row to `data/search_log.csv` with the exact query,
   where you searched, and the date.
3. Add the statement to `data/statements.csv`:
   - `statement_id` is `<speaker_id>-<year>-<NN>`, numbered in date order.
   - The quote is verbatim, 60 words or fewer, from the linked source.
   - Code the version 2 fields (target capability, frames, endorsement, affect, agency
     and the rest) and the timeline fields as the codebook says. Endorsement needs a
     `basis: "..."` note quoting the words that carry it; without them it is `unexpressed`.
   - If you only found someone else's report of the statement, tag `notes` with
     `secondhand` and set `coding_confidence` to `low`.
   - Put your name in `coder` (add it to `CODERS` in `scripts/validate.py`).
4. Go back to the search log row and fill `what_found` with the new statement id.
5. Run the checks and fix anything they report:

   ```
   python3 scripts/validate.py
   ```

6. New people can't be added without a dated entry in `docs/amendments.md`
   saying why: the panel is fixed so that it can't drift toward the story.

## Building the charts

```
python3 -m venv .venv && .venv/bin/pip install matplotlib
.venv/bin/python scripts/charts.py
```
