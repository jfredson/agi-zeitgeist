# AGI Zeitgeist Tracker

A dated, sourced record of how expert and public opinion about artificial general
intelligence (AGI: AI that can do most intellectual work a person can) has moved
from 2005 to the present. Every row links to where it came from, every search that
produced a row is logged, and the coding rules are written down, so anyone can
check the record or extend it.

The working question: did the main public argument move from *whether* AGI is
possible, to *when* it arrives, to *whether today's systems are already close or
improving themselves*? The method is built so the data can say no.

**Live page:** https://agizeitgeist.com (the data, the documents and the singularity
status, rebuilt from this repository).

**Status (2026-10-08):** seed phase complete; five people traced (Ray Kurzweil, Geoffrey
Hinton, Yann LeCun, Gary Marcus, Sam Altman), plus surveys, prediction markets, polls and
dated events, coded under methodology version 2. The expert panel is frozen (core 25,
2020s cohort 12; amendment A16 era rulings), and the r/singularity pilot of the online
communities stream is model-coded by three model families on all 390 sampled posts. The
four-leg definition of entering the singularity was adopted on 2026-10-08 (amendment A17)
and the page scores it from frozen thresholds. Full panel traces and the other public
streams have not started.

## What's here

| path | what it is |
|---|---|
| `data/speakers.csv` | one row per person, survey, market, pollster or institution |
| `data/statements.csv` | one row per public statement, with a verbatim quote, link and codes |
| `data/aggregates.csv` | survey results, prediction market readings and poll results |
| `data/events.csv` | dated events (open letters, government actions, reports) for chart labels |
| `data/world_measures.csv` | world measures, kept apart from belief: capability readings (METR time horizon), company self-reports of AI-done work, and world output growth (World Bank), for the singularity-entry definition |
| `data/search_log.csv` | every search run to build the record, and what it found |
| `docs/methodology-v2.md` | the method (version 2, 2026-09-30): four streams, coding scheme, panel rule, preregistered tests |
| `docs/methodology.md` | pointer to version 2, plus details carried over from version 1 |
| `docs/codebook.md` | how each statement is coded under version 2, with decision rules and examples |
| `docs/reviews/` | the two outside reviews behind version 2 |
| `docs/panel-verification-2026-10.md` | evidence for each panel candidate, for John's freeze decision |
| `docs/amendments.md` | dated changes to the panel or the codes |
| `docs/2026-09-30-kickoff.md` | the original plan |
| `docs/singularity-entry-definition.md` | adopted 2026-10-08: the four-leg measurable definition of entering the singularity (pace, forecasts, AI doing the improving, the economy), with gauges and a mark |
| `docs/singularity-entry-thresholds.json` | the frozen values the page scores from; any change is an amendment |
| `docs/singularity-entry-definition-draft-2026-10-07.md` | the three-leg draft the definition grew from, kept unchanged |
| `scripts/validate.py` | checks every row: codes, dates, sources, links between files |
| `scripts/charts.py` | builds the charts from the CSV files |
| `scripts/site.py` | builds `site/index.html`, the leg A to D figures, `site/status.json`, the rendered documents (`site/docs/`, via pandoc) and the data copies (`site/data/`) |
| `site/` | the static site; serve locally with `python3 -m http.server 8765 --directory site` |
| `wrangler.jsonc`, `worker/` | how the site is published: a Cloudflare Worker serving `site/` at agizeitgeist.com (`npx wrangler deploy`) |

## How to cite

> Fredrickson, J. (2026). *AGI Zeitgeist Tracker* [dataset]. Version of
> <commit date>, commit <short hash>. https://agizeitgeist.com

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

## Building the charts and the site

```
python3 -m venv .venv && .venv/bin/pip install matplotlib
.venv/bin/python scripts/charts.py
.venv/bin/python scripts/vanguard_figure.py
.venv/bin/python scripts/site.py        # needs pandoc on the path
npx wrangler deploy                      # publishes site/ to agizeitgeist.com
```
