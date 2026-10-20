# Methodology, version 2

Date: 2026-09-30
Supersedes: the method sections of `docs/2026-09-30-kickoff.md`. Reasons for every change are in `docs/amendments.md` under the 2026-09-30 entry.
Status: frozen for the seed phase. Changes require an amendment entry.

## 1. What the project measures

Four streams of evidence about artificial general intelligence (AGI, meaning AI that can do most intellectual work a person can), 2005 to the present, each with its own unit and its own population, reported separately and compared only with units visible:

| stream | population | unit | what a share means |
|---|---|---|---|
| E, named experts | a fixed panel of individuals chosen by a dated rule | one public statement | share of statements by panel members |
| P, population beliefs | the respondents of named surveys | one survey item | share of respondents |
| M, published argument | a fixed set of national outlets with public archives | one article or opinion piece | share of published pieces |
| F, specialist discourse | named online communities | one post or comment | share of sampled units in that community |

The story I set out to test (the leading question moved from whether AGI is possible, to when it arrives, to whether current systems can already improve themselves) is tested inside each stream under section 7. The essay reports where the streams agree and where they diverge. Divergence between F and P is an expected finding, not a failure.

## 2. Coding scheme (applies to E, M and F; P items are mapped where the wording allows)

One row per coded unit. Fields in addition to source, date, date precision, quote, retrieval date and coder:

| field | values | rule |
|---|---|---|
| target_capability | `conversation` (passes as human in conversation), `narrow_task`, `broad_competence` (most economically valuable work), `superintelligence` (exceeds humans broadly), `si_assist` (AI helps humans build AI), `si_research` (AI does parts of AI research on its own), `si_modify` (AI changes its own code or weights), `si_sustained` (successive improvements with little human involvement), `none` | which capability the unit is about; `none` when no capability is claimed |
| frame_primary | `possibility`, `timeline`, `capability_now`, `self_improvement`, `definition`, `consequences`, `governance`, `other_concern` | the question the unit leads with |
| frames_present | any of the above, semicolon separated | every question raised, so presence is coded apart from the answer |
| concern_tag | `jobs`, `reliability`, `privacy`, `bias`, `misinformation`, `military`, `consciousness`, `ownership`, `other`, blank | required when `other_concern` is present |
| endorsement | `accepts`, `rejects`, `uncertain`, `conditional`, `unexpressed` | whether the speaker endorses the proposition that the target capability will exist (or exists); `unexpressed` when the unit discusses it without taking a position. Silence is never coded as acceptance |
| present_capability | `demonstrated`, `claimed`, `disputed`, `hypothetical`, `na` | the speaker's view of whether the capability exists now |
| timeline_type | `point_year`, `range`, `prob_by_year`, `qualitative`, `none` | as in version 1 |
| timeline_year, timeline_year_high, timeline_prob, timeline_text | as in version 1 | probability only when the source gives one; "soon" stays text |
| consequence_type | `existential`, `economic`, `social`, `mixed`, `unspecified` | the kind of consequence the unit expects |
| consequence_valence | `beneficial`, `harmful`, `mixed`, `unspecified` | |
| affect | `enthusiasm`, `fear`, `resignation`, `neutral`, `mixed`, `unexpressed` | emotional posture, coded only from explicit cues |
| agency | `can_influence`, `cannot_influence`, `unexpressed` | whether the speaker thinks the outcome can be shaped |
| elicitation | `unprompted`, `interview`, `survey`, `quoted` | how the statement came about; a quoted claim inside an article is coded as its own unit with `quoted` |
| definition_note | free text | what the speaker means by AGI if they say |
| coding_confidence | `high`, `medium`, `low` | |
| ambiguous | `yes`, blank | kept as a code, never resolved by guessing |

Derived at render, never stored: proximity (distant: more than 30 years or never; medium: 10 to 30; near: under 10; present: `capability_now` with `demonstrated` or `claimed`).

Coding rules: code what was said, not what the speaker is known for. Require explicit endorsement before assigning a belief. An article about regulation does not establish that its author accepts feasibility. When a unit gives both a date and a hedge, record both. Secondhand reports are `coding_confidence: low` until replaced by the primary source.

## 3. Stream E: named experts

Three tiers (amendment A13).

Core panel, about 25 people, fully traced. Eligibility (position-independent, datable): at least one public statement on AGI possibility or timing dated 2017 or earlier; at least one dated 2024 or later; named in at least three distinct national-outlet pieces about AI futures dated 2017 or earlier. A piece the person wrote or co-wrote counts toward the three, but for at most one of them (A14). A piece counts when the person is named anywhere in its text and its headline or abstract shows the piece is about where AI is going (A16). Co-written statements count for the earliest and latest tests when the person is a named author (A14). Minimum quotas: six sustained skeptics or critics (statements dated 2017 or earlier reject or doubt AGI within decades; A14); three based outside the United States and United Kingdom at the time of their pre-2017 statements; two philosophers or cognitive scientists; three with frontier-lab ties (recorded, not screened out; time-varying, so the tag applies if true at the time of any statement in the record, with dates in the justification; A14). `philosopher` means the person's primary role (A14). Candidates and the evidence for each criterion and quota go in `docs/panel-verification-2026-10.md`. The panel is frozen by me before full collection; later changes need an amendment entry.

2020s cohort, ten to twelve people prominent on AGI timelines only since 2020 with no public AGI timeline statement before 2018 and at least one dated 2024 or later, fully traced, reported as its own series. National-outlet prominence is recorded for the cohort as information only (A14).

Wide list, as many names as the rule yields (A14; 184 at 2026-10-01), built by an enumerable rule: every person with a dated prediction in the public MIRI/AI Impacts timeline-predictions dataset, every person on the TIME100 AI lists 2023 to 2025, and every person quoted on AGI timelines in the stream M sample, de-duplicated against the other tiers. Light capture only: one qualifying statement per person per era (2005 to 2015, 2016 to 2022, 2023 onward) found by a fixed query logged in the search log, with `tier: wide` on the row. Used for composition and balance checks across eras, never for within-person claims.

`speakers.csv` gains a `tier` field (`core`, `cohort_2020s`, `wide`) and quota tags (`skeptic`, `non_us_uk`, `philosopher`, `frontier_lab`), each with a one-line justification and a dated source.

Collection: year-by-year search per person from first statement to present, queries logged in `data/search_log.csv`. Years with no statement found are logged as rows, so quiet years are visible. Where a person made more than ten qualifying statements in a year (counted by passage: each distinct passage of one essay, talk or interview is its own statement, which is how the whole record counts; decided 2026-10-18, see amendment A28), all timeline-bearing statements are kept, and so are all statements that bear on the "now" question (a `self_improvement` frame, or `present_capability` coded `claimed`; amendment A26, 2026-10-17); the rest are sampled at a fixed interval, logged. Within-person change (the same person's codes over time) is reported separately from composition change (who is speaking in a given year).

Benchmarks alongside the panel: the AI Impacts expert surveys (2016, 2022, 2023), Müller and Bostrom 2014, Pew's 2025 expert sample, with question framing and respondent composition recorded before any comparison.

## 4. Stream P: population beliefs

One row per survey item in `data/surveys.csv`: survey, fieldwork dates (publication date separate), population, sample size, mode, exact wording, construct label (`concern`, `feasibility`, `timeline`, `impact`, `capability_expectation`), target capability where the wording names one, result, source link, comparability notes.

Backbone series and anchors: Pew/Smithsonian 2010 (81% of US adults expected a computer that converses indistinguishably from a human by 2050) and 2014; Monmouth 2015 and 2023; Zhang and Dafoe 2018 (GovAI, high-level machine intelligence timelines and governance); Pew's concerned-versus-excited series 2021 onward; Pew 2025 public-versus-expert comparison (parallel questions, the model for section 7); Eurobarometer 2012, 2014, 2017 (multi-country, robots); Lloyd's Register Foundation World Risk Poll 2019, 2021, 2023; YouGov 2023 onward; Gallup; Ipsos AI Monitor with its own caveat that several national samples skew urban and educated.

Stated gap: no continuous, comparable population series on AGI exists for 2005 to 2015. The essay says so.

## 5. Stream M: published argument

Outlets: those with documented public archives. New York Times (Archive API, metadata from 1851; headline and abstract searches labeled as such), the Guardian (Open Platform, full text from 1999), and Media Cloud collections only after an outlet-by-month coverage audit shows stable coverage for the period claimed. Non-English corpora deferred.

Frame: for each outlet and three-year period, enumerate every piece matching the frozen retrieval vocabulary (section 8); record the count. Sample: a seeded random sample sized to distinguish a 20-point change in a share at 95% confidence (about 50 pieces per outlet-period); census where fewer are eligible. Stratify by outlet and period. Code news and opinion separately. The author's own endorsement is coded separately from claims the piece quotes (each quoted speaker is its own unit with `elicitation: quoted`).

Starting categories for media framing: Fast and Horvitz 2017, which coded New York Times AI coverage from 1986 to 2016; its categories are reconciled to section 2 in the codebook so results can be compared.

This stream measures what editors published. It is never reported as reader belief.

## 6. Stream F: specialist discourse

Communities, each reported separately and never pooled: r/singularity (Arctic Shift archive, 2008 onward), r/artificial, Hacker News (public search API, 2007 onward), LessWrong, Slashdot (2005 onward, after an archive audit).

Coverage audit first: for each community, posts and comments per month in the archive against any independent count (Gaffney and Matias 2018 documents gaps in an earlier Reddit corpus). Arctic Shift's capture change in November 2023, after which score fields were re-captured at 36 hours, is marked as a measurement break.

Vanguard sub-series (accepted 2026-10-02, `docs/amendments/2026-10-02-vanguard-stream.md`): selected AI-enthusiast venues (r/singularity, r/accelerate, r/artificial, to be confirmed by a published venue inventory), sampled with this stream's design, coded claim by claim, reported as shares in its own figure, never pooled with this stream's other venues, captioned "not representative of participants or the public"; an event-by-event comparison with skeptic venues starts when one exists.

Prevalence sample: per community and quarter, a seeded random sample of posts and, independently, of comments, drawn without regard to score, inclusion probabilities recorded. Rewarded sample: the top 20 posts by score per quarter, kept as a separate series labeled "what the community rewarded". Reports include account concentration (share of sampled units from the ten most prolific accounts) and a stable-account subset (accounts active in both halves of the period) to separate changed speech from membership turnover.

## 7. Preregistered tests of the whether, when, now story

The claimed periods: whether, 2005 to 2015; when, 2016 to 2022; now (capability_now or self_improvement), 2023 onward.

T-F (specialist discourse): in r/singularity and Hacker News separately, the claimed leading frame ranks first by `frame_primary` share in each claimed period under the random prevalence sample, and the ordering holds in the comment-weighted, post-weighted and stable-account subsets. The periods are compared against a no-change model, a gradual-trend model, and break dates moved two years either way.

T-M (published argument): the same test on the media sample, with `other_concern` tags allowed to win. The capability-versus-impact report (share of pieces whose primary frame concerns capability against share concerning jobs, reliability, misinformation and so on) is published for every period.

T-P (population beliefs): matched survey items show a rising share accepting feasibility or near-term timelines over the period where comparable items exist. The 2010 Pew result is recorded as evidence that the population did not treat conversational capability as impossible even in the claimed whether period.

Failure condition: the story fails for a stream when the claimed leading frame does not rank first in any claimed period under the primary weights, or when the ordering does not survive the sensitivity checks. A failure in one stream is reported as such; it does not overturn another stream.

The two post-2023 claims are kept apart: "what do we do about demonstrated capabilities" (frames `consequences`, `governance`) is broader than "can systems already improve themselves" (`self_improvement` with `si_*` targets). Success for the first does not establish the second.

## 8. Retrieval vocabulary

Built from a pilot: random units from each era are read and every expression for the concept listed. Starting list: thinking machines, strong AI, human-level AI, human-level machine intelligence, machine intelligence, intelligence explosion, technological singularity, the singularity (AI sense, disambiguated by context), Skynet, robot uprising, artificial general intelligence, AGI, superintelligence, ASI, takeoff, recursive self-improvement, self-improving AI, alignment (AI sense), doom, p(doom), timelines (AI sense), feel the AGI, AI slop. Version frozen before the main pull; precision and recall measured per era on a held-out sample; any revision reruns all years.

Vocabulary ledger (`data/vocabulary.csv`): per term, earliest verified occurrence in each corpus with the corpus's coverage limits stated, and the first month it exceeded a stated share of r/singularity comments, published with numerator, denominator, distinct-account count and single-thread share, under a minimum of 500 comments in the month and a persistence rule of three consecutive months.

## 9. Attention series (context only)

Shown separately, each normalized within itself; never combined into an index. Wikipedia monthly page views for the AGI, Technological singularity, Superintelligence, Existential risk from AI and AI takeover articles from 2015-07, with 2007-12 to 2015-06 legacy counts shown as a separate series because counting methods differ; titles and redirects documented. Google Trends with geography, query or topic, category, window and export date recorded, early zeros noted as low volume. GDELT optional, used only if a retrieval pilot reproduces a historical count for the exact query. Google Books Ngram appears only in the vocabulary appendix, unsmoothed, corpus version recorded.

## 10. Reliability and reproducibility

**How coding is checked (plain-language note, 2026-10-03).** This is a one-person
project, and coding is fully model-based: no human codes the posts. Three AI models from
different companies (Anthropic, Google and OpenAI) code the same sample independently,
without seeing each other's codes. The final code for each field is the one at least two of
them agree on; where none agree, it is marked unresolved. Agreement between each pair is
published, and any field the models can't code consistently is left out of the figures and
listed as unreliable. Models from different companies can still share blind spots, so this
is a disclosed limitation: there is no human coder. It replaces the two-person double-coding
described below wherever the two conflict.

A stratified subset of every coded stream is double-coded with dates and identities hidden where practical; disagreements and per-category agreement are published. Automated coding, if used, is validated separately by era and by source. Published with the data: sampling frames, queries, code, random seeds, source versions, retrieval dates, document identifiers, exclusions, coverage and missingness audits, and snapshots with checksums where the source permits. The README states, per table, whether a reader can reproduce it from public pages or needs the archived microdata.

## 11. Charts (final set decided after the seed)

Each chart carries its stream letter and unit in the title. Candidates: frame share by period for F and M side by side; panel members' timeline estimates over time against survey medians (E and P); capability-versus-impact shares in M; endorsement and affect mix over time in E; attention series as a context strip under the others.

## 12. Seed phase under version 2

Same five people (Kurzweil, Hinton, LeCun, Marcus, Altman); collected rows are kept and recoded under section 2, not mapped from the old stance code. Panel verification collects the three-piece prominence evidence from section 3. Pass check before scaling: at least 60 statements with working sources across the five; double-coding of two speakers agrees on `frame_primary`, `endorsement` and `target_capability` at least 80% of the time; codes spread across more than one bucket. Public streams begin with the coverage audits (section 6) and the vocabulary pilot (section 8), both of which must finish before any prevalence sample is drawn.
