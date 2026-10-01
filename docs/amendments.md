# Amendments

Dated changes to the method, the panel or the codes, with the reason. Nothing in the method changes without an entry here. Reviews referred to below are saved verbatim in `docs/reviews/`.

## 2026-09-30: reconciliation of the two outside reviews (Gemini 3.1 Pro, GPT-6 Astra Medium)

Both reviews were read against the kickoff plan (`docs/2026-09-30-kickoff.md`). The result is `docs/methodology-v2.md`, which supersedes the method sections of the kickoff plan. The kickoff plan stays as the record of where the project started. John ruled on 2026-09-30 that no third review would be sought and that these two would be worked with.

### A1. The headline claim is replaced by three separately registered outcomes (GPT)

Was: one claim, "the central public question moved from whether, to when, to now".
Now: three outcomes measured and reported separately. What surveyed populations believed (surveys). What published outlets argued (news and opinion in fixed outlets). What specialist communities discussed (forums and the named expert panel). The whether, when, now story is tested in each, with a written failure condition, and the essay reports where the three agree and where they diverge.
Why: "central public question" had no observable definition, no specified public, and no way for a different question (jobs, deepfakes, reliability) to win. GPT's point that the old structure would read changes in attention, vocabulary and membership as changes in opinion was correct. This also absorbs Gemini's "insider projection" objection, which becomes the expected divergence between the specialist and population outcomes rather than a flaw.

### A2. The single stance code is split into endorsement, affect and agency (GPT; Gemini's disruption profile folded in)

Was: `stance` with six values from dismissive to resigned.
Now: `endorsement` (accepts, rejects, uncertain, conditional, unexpressed), `affect` (enthusiasm, fear, resignation, neutral, mixed, unexpressed), `agency` (can influence the outcome, cannot, unexpressed), `consequence_type` (existential, economic, social, mixed, unspecified).
Why: the old scale mixed a judgment (dismissive) with an emotion plus a view about control (resigned). Someone who expects AGI in five years can be thrilled, frightened, resigned or organizing. Gemini's "disruption profile" (existential, economic, social) is the `consequence_type` field. Old seed codes are recoded, not mapped, because a mapping would launder the old scale's ambiguity into the new fields.

### A3. A target-capability field is added, with self-improvement split four ways (GPT)

Was: statements were about "AGI" as one thing.
Now: `target_capability` says which capability the statement is about: passing as human in conversation, a specific task, broad competence at most economically valuable work, exceeding humans broadly, or one of four self-improvement levels (AI helps humans build AI; AI does parts of AI research on its own; AI changes its own code or weights; AI sustains successive improvements with little human involvement).
Why: Pew found in 2010 that 81% of US adults expected a computer to converse indistinguishably from a human by 2050. That is early acceptance of one capability, not of AGI, and the old scheme could not keep the two apart. The four self-improvement levels get different answers from the same person.

### A4. `question_frame` is kept but widened so other questions can win (GPT item 3; Gemini's capability-versus-impact test)

Was: six frames, all about AGI itself.
Now: the six remain, plus `consequences`, `governance` and `other_concern` with a sub-tag (jobs, reliability, privacy, bias, misinformation, military, consciousness, ownership, other). Each unit records the primary frame and every frame present. Question presence is coded separately from the answer given.
Why: if jobs or deepfakes was the leading question in mainstream outlets after 2023, the data must be able to say so. Gemini's capability-versus-impact comparison is now a standing report, not a special test.

### A5. Expert panel eligibility is made position-independent and datable (GPT)

Was: statements before 2017 and after 2024, plus "prominent enough to have shaped public discussion".
Now: statements before 2017 and after 2024, plus named in at least three distinct national-outlet pieces about AI futures dated 2017 or earlier (the prominence test is dated and checkable, not retrospective). Quiet years are recorded as rows in the search log. Within-person change is reported separately from change in who is speaking.
Why: choosing today's prominent thinkers selects for the arguments that survived. The seed session's panel-verification step is amended to collect the three-piece evidence.

### A6. Forum sampling: random samples for prevalence, top posts kept as a separate series (both reviews)

Was: the 20 top-scoring r/singularity posts per quarter.
Now: for each community and quarter, a seeded random sample of posts and, independently, of comments, with inclusion probabilities recorded, drawn without regard to score. The top-20 series is kept and labeled "what the community rewarded". Account concentration (share of sampled units from the ten most prolific accounts) is reported, and a stable-account subset is analyzed to separate changed speech from membership turnover. Communities are reported separately and never pooled as if they were independent samples of the public.
Why: scores measure virality, and Arctic Shift changed how it captures score fields in November 2023, right on the proposed period boundary.

### A7. Vocabulary: piloted across the whole period before freezing, with era terms (both reviews)

Was: a list of current terms frozen before the pull.
Now: a retrieval vocabulary built from a pilot sample spanning 2005 to 2026, including older terms (thinking machines, strong AI, human-level machine intelligence, machine intelligence, intelligence explosion, technological singularity, Skynet, robot uprising) alongside current ones. Version frozen before the main pull; precision and recall checked per era on a held-out sample; any later revision reruns every year. The 1% threshold in the vocabulary ledger is replaced by a published numerator, denominator, distinct-account count and single-thread share, with a minimum volume of 500 comments in the month and a persistence rule of three consecutive months.
Why: a list chosen today would make it look as if nobody discussed this before 2015 because they used different words.

### A8. Media sample: sized from the smallest change worth detecting, stratified, news and opinion coded separately (GPT; Gemini)

Was: 15 opinion pieces per year.
Now: outlets fixed to those with documented public archives (New York Times Archive API for metadata from 1851; Guardian Open Platform for full text from 1999; Media Cloud collections only after an outlet-by-month coverage audit). The eligible frame is enumerated per outlet and period before sampling. Periods are three years, not one. Sample size per outlet-period is set to distinguish a 20-point change in a share at 95% confidence (about 50 pieces); where fewer are eligible, all are taken. News and opinion are coded separately, and the author's own endorsement is coded separately from claims the piece quotes.
Why: with 15 pieces the margin of error on a share near 50% is about 25 points, which cannot support an annual claim. Op-eds measure what editors chose to publish, so this outcome is labeled "published argument", never reader belief.

### A9. Attention series kept as context only, never combined (GPT)

Each series (Wikipedia page views from 2015-07 with the 2007 to 2015 legacy counts marked as a different measurement; Google Trends with export settings recorded; GDELT optional pending a retrieval pilot) is normalized within itself and shown separately. No composite "public acceptance" index. Google Books Ngram moves to the vocabulary appendix, unsmoothed, because Google drops phrases found in fewer than 40 books, which makes it unusable for first appearances.

### A10. Surveys become the backbone of the population outcome, with specific early anchors (both reviews)

Added: Pew/Smithsonian 2010 and 2014 (capability expectations), Eurobarometer 2012, 2014 and 2017 (robots, multi-country), Zhang and Dafoe 2018 (GovAI, high-level machine intelligence timelines), Lloyd's Register Foundation World Risk Poll 2019, 2021 and 2023, Pew's 2025 public-versus-expert comparison (parallel questions, the model for comparability), Monmouth 2015 and 2023, YouGov 2023 onward, Gallup, Ipsos with its own note that several national samples skew urban and educated. Every row dated by fieldwork, with publication date separate, exact wording, and a construct label (concern, feasibility, timeline, impact). The absence of a comparable population series for 2005 to 2015 is stated, not papered over.

### A11. Prior work to build on, not redo (both reviews)

Fast and Horvitz 2017 (New York Times coverage of AI, 1986 to 2016; its categories are the starting point for media coding), Zhang and Dafoe 2019, Pew 2025, the AI Impacts survey series, the Stanford AI Index public-opinion chapter, Gnambs and Appel on Eurobarometer waves, Gaffney and Matias 2018 on Reddit archive gaps (reason for the coverage audit), GCRI's survey of AGI projects.

### A12. Reliability and reproducibility rules (GPT)

Double-coding of a stratified subset with dates and identities hidden where practical; disagreements and per-category agreement published; `ambiguous` and `unexpressed` kept as codes; any automated coding validated separately by era and source. Published with the data: sampling frames, queries, code, random seeds, source versions, retrieval dates, document identifiers, exclusions, missingness audits, and snapshots with checksums where the source permits.

### A13. Expert panel expanded into three tiers with written quotas (John, 2026-09-30, after discussing panel size)

Was: a core panel of 15 to 20 plus an unsized 2020s cohort.
Now: three tiers.
- Core panel, about 25, each meeting the dated rule in A5, frozen by John from the verification table. Minimum quotas, written so the panel cannot lean one way by construction: at least six sustained skeptics or critics (people whose pre-2017 statements reject or doubt AGI within decades); at least three based outside the United States and United Kingdom at the time of their pre-2017 statements; at least two philosophers or cognitive scientists; at least three with frontier-lab ties, so incentives are visible rather than screened out. Fully traced.
- 2020s cohort, ten to twelve people prominent on AGI timelines only since 2020, fully traced, reported as its own series so its arrival is visible in the data.
- Wide list, 60 to 100 names, built by an enumerable rule rather than by hand, with a light capture: one qualifying statement per person per era (2005 to 2015, 2016 to 2022, 2023 onward) found by a fixed query. Used only for composition and balance checks, never for within-person claims. Seed sources for the list: the public MIRI/AI Impacts dataset of dated AI timeline predictions (Armstrong and Sotala 2012 and its successors), the TIME100 AI lists 2023 to 2025, and every person quoted on AGI timelines in the stream M media sample.
Why: with 15 to 20 people the expert frame share is driven by whoever spoke most, and the dated prominence rule rewards the people who were loud early, mostly singularitarians and lab founders, so the "whether" era would be answered only by people who had already decided. Collection is cheap (a full trace took the seed session about thirteen minutes with a helper); coding and double-coding are the cost, which is why the wide list is a light capture. Timing: the panel freezes before full collection and the verification table is being built now, so the expansion costs an afternoon this week rather than an amendment and re-sampling later.

### Declined, with reasons

- Factiva and LexisNexis for non-US media (Gemini): paywalled, so not re-pullable by a reader. Guardian and Media Cloud's non-US collections instead; non-English corpora deferred until there is capacity for language-specific validation.
- Dropping Google Books Ngram entirely (Gemini): demoted instead (A9); the astrophysics problem with "singularity" is avoided by using the two-word term "technological singularity".
- Replacing the question-frame scheme with a proximity and disruption matrix (Gemini): proximity (distant, medium, near, present) is derived at render from the timeline fields, so it needs no new code; disruption became `consequence_type` (A2).
- Film box office as a measurement series (Gemini): kept as dated event annotations only (Her 2013, Transcendence and Ex Machina 2014, and so on), because a theme-tagged box-office series would need its own coding project.
- A single numerical common axis: used only where the source gives a probability for a specified capability by a specified date, as GPT advised; "soon" is never converted to a number.

## 2026-09-30: implementation decisions for version 2 (decided by: agent)

Made while carrying out the version 2 migration. John can reverse any of them.
- **`question_frame` retired.** `frame_primary` replaces it (A4 widened the same code),
  so `statements.csv` drops `question_frame` along with `stance` rather than keeping two
  competing frame codes. Version 1 codes remain in git history (commits up to `1508fde`).
- **Endorsement anchor.** To enforce "silence is never coded as acceptance", every
  `endorsement` other than `unexpressed` carries `basis: "<words>"` in notes, and
  `scripts/validate.py` checks those words appear in the stored quote.
- **"Not by year X" claims.** "AGI won't arrive by 2027" is not an arrival date. These
  are coded `timeline_type: qualitative` with `timeline_year` blank and the year in a
  `not_by: YYYY` notes tag, so charts can't plot them as forecasts.
- **Lower bounds.** "At least 30 years" or "no sooner than 2070" fill `timeline_year`
  with the bound and carry a `lower_bound` notes tag.
- **"National outlet" for the prominence test (A5).** A national newspaper, broadcaster,
  news agency or national magazine, including science and technology magazines such as
  Wired, MIT Technology Review and New Scientist; not blogs, newsletters, trade press,
  podcasts or the person's own outlets. Pieces count when their subject is where AI is
  going and they name the person.
- **Quiet years.** Logged in `data/search_log.csv` as one row per speaker and year with
  what_found "quiet year: no qualifying statement found" (search_id `<speaker>-q<year>`, e.g. `hinton-q2017`).
- **Tiers and quota tags in `speakers.csv` (A13).** `panel_tier` is renamed `tier`
  (`core`, `cohort_2020s`, `wide`). Surveys, markets, polls and institutions get
  `not_panel`, because every row must carry a tier. The yes/no `frontier_lab_tie`
  column is replaced by the `frontier_lab` quota tag, which carries the role, years and
  source; `skeptic`, `non_us_uk` and `philosopher` sit alongside it. Each tag is blank
  or "<justification> (<date>, <url>)". Tags judged arguable are left blank and listed
  in `docs/panel-verification-2026-10.md` for John to rule on.

## 2026-10-01: John's rulings on the fifteen open decisions

Decided by: john. The decisions were listed in `docs/status-2026-10-01.md`; the
rulings below were sent by John on 2026-10-01. Where an agent had to interpret a
ruling to apply it, the interpretation is marked as such.

### A14. Rulings on panel eligibility, the codebook, and process

**Panel**

1. Was: unclear whether a piece the person wrote counts as "naming" them for the
   three-national-pieces test. Now: it counts, but for at most one of the three.
2. Was: the skeptic tag needed statements "pre-2017". Now: "2017 or earlier",
   matching the earliest-statement test (C1).
3. Was: unclear whether co-written statements count for the 2024-or-later test (C2).
   Now: they count when the person is a named author.
4. Daniel Dennett is dropped from the core panel; his statements go to the wide list.
5. `frontier_lab` is time-varying and applies if it was true at the time of any
   statement in the record, with the dates in the justification. `philosopher` means
   the person's primary role, so Hinton and Hassabis are not tagged. Chalmers is
   `non_us_uk`. Suleyman is not a skeptic.
6. For the 2020s cohort, the three-national-pieces test is information only, not a
   condition.
7. Archive checks for prominence cases blocked by unreachable news sites will run
   later through the Guardian and New York Times APIs (application programming
   interfaces: their official data services) once John has keys. Not attempted now.
8. The wide list keeps all 184 names; its target is "whatever the rule yields", not 60
   to 100.

**Codebook**

9. Endorsement is about whether the capability will exist, ever or by the horizon the
   speaker names. Denying that it exists now is `present_capability: disputed`;
   endorsement is then coded from what the speaker says about the future, or
   `unexpressed` if they say nothing about it.
10. "May", "might" or "could" with a date is `uncertain`, with the timeline fields
    filled and the hedge kept in `timeline_text`. `accepts` requires "will", "expect",
    "I think", a stated probability of 50% or more, or a bet.
    *Agent interpretation:* when a hedge and an acceptance word govern the same date
    ("I think it may be 20 years or less"), the hedge on the date decides and the code
    is `uncertain`.
11. "Decades away" is `accepts` with a qualitative timeline.
12. "Takeoff" and "self-improvement" take the lowest self-improvement level the words
    support, marked `ambiguous`, with any speed the speaker gives noted in
    `timeline_text`. *Agent interpretation:* when the words say nothing about who does
    the improving, the lowest level is `si_assist`.

**Process**

13. John double-codes a blind sample himself (`data/double-coding/`).
14. John merges the branch himself.
15. Licence: Creative Commons Attribution 4.0 (CC BY 4.0) for the data, MIT for the
    scripts.

Why: these were the open questions found while building the panel table and while
recoding the seed under version 2; recoders were applying 9 to 12 inconsistently.
Rows recoded under rulings 9 to 12 carry `coder: claude-agent-v2.1` and a note naming
the ruling.
- *Agent interpretation of ruling 10 (2026-10-01), for John to confirm:* a firm, unhedged
  first-person date that uses none of the listed words ("I set the date for the
  Singularity as 2045", "I'm still saying 2029") is kept as `accepts`, because coding a
  stated prediction as "no position" would misreport the source. The rows concerned
  are listed in `docs/status-2026-10-01.md`.
