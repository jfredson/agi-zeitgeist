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

## 2026-10-01: John's rulings on the eight calls raised after A14

Decided by: john. The eight calls were listed in `docs/status-2026-10-01.md` (section
"New questions for John").

### A15. Firm dates, routes, minimum years, split statements and time-varying tags

1. **Firm, unhedged first-person dates** ("I'm still saying 2029") are `accepts`. Added
   to the list of what `accepts` requires.
2. **A hedge and an acceptance word on the same date:** the hedge decides (`uncertain`).
   Confirmed.
3. **A bare "takeoff"** is `si_assist`. Confirmed.
4. Was: rejecting a route ("language models are not a road to AGI") kept as `rejects`.
   Now: a route claim says nothing about whether the capability will exist, so
   endorsement is `unexpressed`, with the route claim kept in `claim_summary` and notes.
   Applies to LeCun's four route rows.
5. Was: "at least a decade" and "at least thirty or fifty years" kept as `rejects` with a
   minimum year. Now: they assert arrival with a minimum, so under A14 ruling 11 they
   are `accepts`, `timeline_type: range` with the low bound filled, the high bound left
   open, and "at least" kept in `timeline_text`.
6. **"Predict", "almost certainly" and "going to"** count as acceptance words. Confirmed.
7. **New ruling 13: one row per capability.** When one statement makes distinct claims
   about distinct target capabilities, it gets one row per capability, with ids suffixed
   `a`, `b`, and the shared quote and source. Applied to `marcus-2026-04` (split into a
   `si_assist` row and a `si_sustained` row) and `altman-2025-06` (a self-improvement row
   and a superintelligence row).
8. **`frontier_lab` is time-varying** (A14 ruling 5), so Kurzweil, Chollet, Kai-Fu Lee
   and Karnofsky are tagged, with the dates in the justification. Kokotajlo is not tagged
   `philosopher`, since the tag means primary role.

Why: these were the cases where applying A14 needed a reading John hadn't given.
Validator changes that follow: statement ids may carry a one-letter suffix, and a
`range` may leave the high bound open when the row carries the `lower_bound` tag.

- **2026-10-02, vanguard sub-series of stream F (accepted; decided by: john):** after the Gemini 3.1 Pro and GPT-6 Astra Medium reviews, John ruled: enthusiast venues only, plus an event-by-event comparison with skeptic venues once one exists, no monthly gap; claims coded on separate fields, six-rung proximity ladder as a display for AGI claims only; stream F's sampling reused; image posts with legible text included; GPT's caption on every figure and heading, "leading indicator" only in the essay as a hypothesis; shares only; folded into stream F as a labelled sub-series never pooled with F's other venues. Full text: `docs/amendments/2026-10-02-vanguard-stream.md`. Only the r/singularity retrievability check may run.

## 2026-10-02: the newspaper-prominence rule loosened

Decided by: mixed. The seed-phase agent raised the question on 2026-10-01 and offered the
looser wording; John chose it on 2026-10-02 when asked in the management session.

### A16. What counts as "named in" a national piece

Was: an archive hit counted toward the three national pieces only if the person's name was
in the headline or abstract (the agent's rule for the 2026-10-01 archive checks).
Now: a piece counts if the person is named anywhere in its text and its headline or
abstract shows the piece is about where AI is going. Business news, obituaries and pieces
on other subjects do not count, on a reading of the headline and abstract.

Why: the strict rule excluded 1,037 of 1,184 archive hits and moved seven candidates to
fail, among them people quoted at length on AI's future (Shanahan in twelve Guardian
pieces). Being quoted in the text is what "named in" meant in the original rule.

Effect: Legg, Cowen and Yudkowsky pass (all thin); Shanahan, Bengio and Floridi are
unclear, each on one remaining point; Pinker, Sutskever, Wooldridge and Goertzel still
fail. Core passes go from 19 to 22. Details and the agent's three judgment calls are in
`docs/panel-verification-2026-10.md`, section "Re-marking under A16".

- **2026-10-02, vanguard sub-series, video posts (decided by: john):** video posts are coded from their title only; the video is not watched or coded, and a video post is eligible only if its title makes a claim about AI capability, timeline or consequence. Written into section 6 of `docs/amendments/2026-10-02-vanguard-stream.md`.
- **2026-10-03, vanguard sub-series, title-only rows (decided by: john):** retrievability is always reported as two figures (fully recoverable; including video posts coded by title only) with per-quarter counts; a `title_only` field marks rows coded from the title alone so their hedge and claim fields can be excluded; section 8 notes that title-only coding likely overstates unhedged claims.
- **2026-10-03, vanguard sub-series, pilot rulings (decided by: john):** capability and consequence claims become the primary measures, the four headline claims are kept and reported as near-absent; new field `extrapolates_to_horizon`; figures labelled "interim, model-coded" until two people have coded the worksheet; codebook rulings: new target `industry_governance` for AI company and policy drama, demo-only video titles are eligible capability claims, posts not mentioning AI are ineligible, memes follow the legible-text rule. Instrument: `docs/vanguard/codebook.md`.
- **2026-10-03, reliability design (decided by: john):** the requirement that two people code a blind subset (amendment section 9, and the double-coding in methodology-v2 section 10) is withdrawn because this is a single-researcher project. Replaced by a blind second pass from a different model family (both models named and pinned), a 40-post blind subsample coded by John with his agreement against each model reported, and a plain-language note that coding is model-assisted with one human check, disclosed as a limitation, not a second coder. **This departs from both outside reviews**, which asked for independent human double-coding.
- **2026-10-03, reliability design, second revision (decided by: john):** the human coding step is removed. John's 40-post blind check (part (b) of the earlier ruling the same day) is withdrawn, with its worksheet and agreement script. Coding is fully model-based: Claude, Gemini and GPT-6 Astra code the same 140-post set blind; the final code is the majority vote per field, unresolved where no two agree; pairwise kappa is reported for all three pairs. A field unresolved on more than 15% of posts, or with every pairwise kappa below 0.6, is excluded from figures and listed as unreliable. Recurring disagreements get a proposed codebook rule with kappa before and after, for John to rule on. **This departs from both outside reviews**, which asked for independent human double-coding, and goes further than the earlier revision, which kept one human check.
- **2026-10-03, vanguard codebook rules (decided by: john):** R2 (target decided by the subject of the main claim: a model or system, a company or government, or people and society) and R3 (hedging coded only from hedge words in the words stating the claim) adopted into `docs/vanguard/codebook.md`. R1 not adopted as written; split into R1a (a post passed on without comment has no stated stance) and R1b (such a post attributes the claim to the linked source), each trialled separately on the 112 posts all three models coded in the first trial. "Whether the poster wants AI sped up or slowed down" is dropped from reported measures and listed as unreliable. A monthly cost quote for Gemini's paid tier is required before the full-sample run. The codebook as it stood before R2 and R3 is kept as `docs/vanguard/codebook-frozen-2026-10-03-before-rules.md`, so the first trial's remaining Gemini posts are coded on the same codebook as the rest of that run.
- **2026-10-03, Gemini spending (decided by: john):** the cost quote in `docs/vanguard/model-cost-quote-2026-10-03.md` is approved: up to $15 for the first month (the full-sample run, about $9.80, plus the first monthly runs), then up to $5 a month for three venues. The full-sample run waits for the ruling on rules R1a and R1b, so the 390 posts are coded once under the final codebook.

## 2026-10-06: John's rulings on the A16 readings, Sutskever, the thin readings and the freeze

Decided by: john (rulings 1, 2, 3 and 5); mixed (ruling 4: recommended by the coordinating
session, chosen by John). Sent by John on 2026-10-06 in the management session, in answer
to the open points in `docs/panel-verification-2026-10.md`, and relayed to this branch by
the coordinating session.

### A17. Panel rulings before the freeze

1. **Legg, Cowen and Yudkowsky stay in the core.** John confirmed the verifier's three
   judgement calls: "Legg named in passing, Cowen on jobs-and-automation pieces, and
   Yudkowsky on two edge outlets". They stay marked thin.
2. **Sutskever: "Not a timeline statement".** His co-signed 2015 "hard to predict when" is
   not an AGI timeline statement from before 2018, so he meets the cohort's first test and
   passes the 2020s cohort. His 2024-or-later statement was checked against the record:
   the 2025-11-25 Dwarkesh Patel interview, "I think like 5 to 20" (years), in his own
   words.
   *Correction recorded:* John's first answer the same day said the 2015 line *does*
   count as a timeline statement and that Sutskever passes. That answer was given to a
   question the coordinating session had framed backwards; read literally, it would have
   failed him (as the agent flagged, the same reason failed Suleyman and Karnofsky). This
   ruling is John's answer to the question framed correctly, and replaces the first.
3. **Freeze after the three gaps are closed. Don't freeze now.** The three unclear core
   cases (Shanahan, Bengio, Floridi) were closed the same day; all three pass thin.
4. **Both thin readings count.** Shanahan's 2025 podcast remark that it is hard to tell
   "whether we really are on the road to producing general intelligence that is comparable
   to human general intelligence" counts as his 2024-or-later statement on whether AGI
   arrives. Floridi's 2017 Financial Times column on robot rights counts as a piece about
   where AI is going under A16. Both stay marked thin; the core stays at 25.
5. **"Search first, then freeze".** Before the freeze, search for one to three more 2020s
   cohort members at no cost, with the same method and the rules exactly as written,
   drawing on the wide list and other prominent voices of the 2020s, preferring people who
   broaden the cohort. Done the same day: Liang Wenfeng, Arthur Mensch and Arvind
   Narayanan pass (all thin), taking the cohort to 12. The freeze was drafted as A18 and
   first marked PROPOSED; John then said "Freeze and merge" (A18, below).

Why: these were the last open points before the freeze. Effect: core passes 22 to 25;
cohort 8 to 12; the three new cohort members leave the wide list (308 names). Details in
`docs/panel-verification-2026-10.md`, sections "Closing the three unclear cases
(2026-10-06)", "Cohort search (2026-10-06)" and "Freeze candidates as of 2026-10-06";
evidence in `docs/panel-evidence-2026-10/gaps-2026-10-06.md` and
`docs/panel-evidence-2026-10/cohort-search-2026-10-06.md`.

## 2026-10-06: the expert panel is frozen

Decided by: john ("Freeze and merge", 2026-10-06). The three readings under "Readings
chosen at the freeze" are decided by: mixed (recommended by Claude, chosen by John).
Drafted by claude-agent on 2026-10-06 under A17 rulings 3 and 5 and first recorded as a
proposal; John's yes was relayed to this branch by the coordinating session the same day.
The tiers and quota tags are written into `data/speakers.csv`.

### A18. The panel is frozen

Was: candidates checked in `docs/panel-verification-2026-10.md`; no one frozen.
Now: the three tiers below are fixed for full collection. Any later addition,
removal or tag change needs its own amendment entry (methodology-v2 section 3).

**Core panel (25).** Kurzweil, Bostrom, Hanson, Hinton, LeCun, Hassabis, Altman, Marcus,
Ng, Russell, Brooks, Musk, Chalmers, Brynjolfsson, Schmidhuber, Kai-Fu Lee, Walsh,
Tegmark, Suleyman, Legg, Cowen, Yudkowsky, Shanahan, Bengio, Floridi. Fifteen of them pass
on thin evidence, named in the verification table; thin passes are frozen as thin and the
reason travels with the row.

Quota tags (minimums met, all four):

| quota | minimum | count | who |
|---|---|---|---|
| `skeptic` | 6 | 8 | Hanson, Hinton, LeCun, Marcus, Ng (medium confidence), Brooks, Kai-Fu Lee, Floridi |
| `non_us_uk` | 3 | 6 | Hinton, Chalmers, Schmidhuber, Kai-Fu Lee, Walsh, Bengio |
| `philosopher` | 2 | 4 | Bostrom, Marcus, Chalmers, Floridi |
| `frontier_lab` | 3 | 11 | Hinton, LeCun, Hassabis, Altman, Ng, Musk, Suleyman, Kurzweil, Kai-Fu Lee, Legg, Shanahan |

**2020s cohort (12).** Amodei, Aschenbrenner, Kokotajlo, Cotra, Huang, Leike, Mollick,
Chollet, Sutskever, Liang Wenfeng, Arthur Mensch, Arvind Narayanan. At the top of the
ten-to-twelve range. Six pass thin (Huang, Leike, Mollick, Liang, Mensch, Narayanan).
Tags: `frontier_lab` 5 (Amodei, Leike, Chollet, Sutskever, Liang); `non_us_uk` 2 (Liang,
Mensch). No cohort member can carry `skeptic` as defined, since the tag rests on
statements from 2017 or earlier; Mensch and Narayanan are skeptics in outlook and that is
recorded in their rows.

**Wide list (308).** Every name in `data/wide_list_candidates.csv` as of 2026-10-06: the
MIRI and AI Impacts predictions dataset and the full TIME100 AI lists 2023 to 2025, less
core and cohort members, plus Dennett (A14 ruling 4). Names quoted on AGI timelines in the
stream M media sample are added by rule when that stream runs, without a new amendment,
because the rule already names that source.

**Not on the panel:** Pinker, Wooldridge, Goertzel, Mitchell, Etzioni, Davis, Pearl and
Karnofsky (each fails a core test as searched); Dennett (dropped, A14 ruling 4; on the
wide list); from the cohort search, Sayash Kapoor (meets the rule on the essay co-written
with Narayanan, not added: no independent statement, and the cohort would exceed 12),
Abeba Birhane and Katja Grace (near misses; on the wide list). A later find that would
pass one of them is recorded, not acted on, unless John amends the panel.

**Readings chosen at the freeze** (decided by: mixed, recommended by Claude, chosen by
John, 2026-10-06):
1. **`frontier_lab`: Liang yes, Mensch no.** DeepSeek counts as a company building the
   most capable models of its time; Mensch's research-scientist role at DeepMind
   (2020 to 2023) and Mistral do not meet the tag.
2. **Mensch's April 2024 "I don't believe in AGI" counts** as his 2024-or-later statement,
   consistent with the Shanahan reading in A17 ruling 4 (a statement on whether AGI
   arrives, with no date, counts).
3. **Narayanan, not Kapoor**, for the essay they wrote together. Kapoor stays on the wide
   list.

Why: A17 rulings 3 and 5 asked for the freeze once the three gaps were closed and the
cohort search was done; both were done, and John said "Freeze and merge".

Effect: `data/speakers.csv` gains 32 rows (20 core, 12 cohort) beside the five seed
speakers, each with `tier`, quota tags (justification, date, link) and an inclusion note
naming the evidence and any reason the pass is thin. The wide list's frozen record is
`data/wide_list_candidates.csv`; methodology-v2 section 3 puts `tier: wide` on the
light-capture rows, so wide-list people enter `data/speakers.csv` when their statement is
collected, not before (many are listed by surname only in the MIRI dataset, so a speaker
row could not yet be filled in honestly). Next step: full collection for the 37 core and
cohort members.

## 2026-10-08: the singularity-entry definition adopted, with a fourth leg

Decided by: john, on four questions the agent put to him with recommendations; John
followed the recommendation on the anchor, the thresholds and the backward test, and
overruled it on the economic leg. Full text: `docs/singularity-entry-definition.md`; frozen
values: `docs/singularity-entry-thresholds.json`.

### A19. Singularity entry: anchor, thresholds, leg D, and publication

Was: a draft (`docs/singularity-entry-definition-draft-2026-10-07.md`) with three legs
(pace accelerating; forecasts failing; AI doing the improving), placeholder thresholds and
no gauge published.
Now:
1. **Anchor.** METR's 50% task-completion time horizon anchors legs A and B. A successor
   must be named before it saturates, with the overlap published.
2. **Thresholds frozen as the draft wrote them:** doubling time at or below one month;
   forecast horizon at or below one year; AI share of frontier research work at or above
   one half; reference year 2019; four consecutive quarters to count as entered.
3. **Backward test owed, not met.** The definition must return "not entered" for 1995 to
   2019; the series to run it do not exist yet. Adopted anyway, with the gap stated on the
   page. If the test later fires on those years, the thresholds are amended.
4. **Leg D, the economy, added (John's ruling against the agent's recommendation).** World
   output doubling time from World Bank annual world growth. Threshold: growth at or above
   30 percent a year, Davidson's published "explosive growth" line (2021). Reference: the
   1961 to 2019 mean of the same series. One annual reading covers its four quarters;
   revisions reset the count. The agent had recommended publishing the economic reading
   beside the mark, not inside it, because output lags capability by years and the
   progress number (the smallest gauge) will track the economy until it moves. John
   accepted that cost for the sake of a leg measured outside the AI field.
5. **Gauges and status are published** at agizeitgeist.com from the frozen
   file. Leg B is shown as not yet measurable until the forecast-versus-outcome ledger
   exists; progress is then reported as "at most" the smallest measured gauge.

Agent decisions inside the adoption (John can reverse any):
- T_ref for leg A is METR's own whole-series fit (187.8 days, row `metr-th11-doubling-all`,
  the fit over all frontier models since 2019), because the trailing-window series cannot
  be computed in 2019 itself. Windows that include a reading past 16 hours are not scored,
  following METR's own exclusion.
- Leg C is scored from Anthropic's "leads" share only; the Google code-share row is a proxy
  and is shown unscored.
- The World Bank series is stored in `data/world_measures.csv` as one row per year (unit
  `percent_growth`), and the validator's date floor for that file is 1960.

## 2026-10-08: the 2022 survey's even-odds year recorded as 2060

Decided by: mixed. The agent re-read both sources and recommended the change; John approved
("make it 2060").

### A20. aiimpacts-2022-hlmi50 changed from 2059 to 2060

The 2022 survey page reported the aggregate 50% year for high-level machine intelligence as
2059. The 2023 paper (arXiv 2401.02843) restates it as 2060, footnoted "Reported as 2059 in
2022; small code changes and improvements to data cleaning between surveys shifted the
aggregate slightly." The two other 2022 figures in `data/aggregates.csv` (the 10% year,
2029, and the full-automation year, 2164) already came from that recomputation, so the row
mixed two calculations, and the site's chart of the researcher surveys showed 2059 beside
2164 as if from one. The row now holds 2060 with the 2023 paper as its source; 2059 and the
original page stay quoted in its notes. One reading on the page moves with it: the forecasts
part now says about 15 years of expected waiting disappeared between the 2022 and 2023
surveys, where it said about 14. The card's comparison with the 2016 survey does not use the
2022 figure and is unchanged.

## 2026-10-08: AI releases added to the events list

Decided by: john ("add the product launches to the events list"). The inclusion rule below
is the agent's, made so that the list is not chosen by taste; John can change it.

### A21. A new kind of event, `ai_release`, and seven releases

The events list (`data/events.csv`) held only institutional moments: open letters, public
statements, government actions and reports. It had no AI releases, so the record could not
be read against the launches people were reacting to (ChatGPT, GPT-4). It now has a fifth
kind, `ai_release`: the public release of an AI system, or a public demonstration such as a
match.

Inclusion rule: a release is listed when the system is named in at least one statement in
`data/statements.csv` (quote or claim summary). The scan (search log `events-016`) found
seven: AlphaGo (the 2016 match with Lee Sedol), GPT-2 (2019), GPT-3 (2020), ChatGPT (2022),
GPT-4 (2023), DeepSeek-R1 (2025) and GPT-5 (2025). Each date was read from the maker's own
page or the paper that introduced the system (`events-017` to `events-021`). AlphaGo's row
is at month precision because no source read gave the match dates; GPT-3 is dated by its
paper (28 May 2020), since the API announcement of 11 June 2020 does not name it. As the
statement record grows, releases its statements name are added under the same rule.

## 2026-10-08: institutional events since November 2023 added

Decided by: john ("add the post-2024 institutional events too"). The inclusion rule below is
the agent's, written to match the events already listed; John can change it.

### A22. Fifteen institutional events, May 2024 to September 2026

The events list stopped at November 2023. It now runs to September 2026, under the founding
plan's own description of these rows ("institutional moments"), made explicit:

1. Open letters and statements signed by many leading AI researchers, heads of AI companies
   or AI-company employees.
2. International AI summits and the declarations they end with.
3. Government actions that set or replace national or EU policy on advanced AI as a whole,
   and California's actions on the largest AI models, since most leading AI companies are
   based there. US executive orders that only touch on AI, or set up a programme (the
   Genesis Mission, Executive Order 14363), are left out.
4. Reports written for governments jointly, such as the International AI Safety Report.

Added: the Seoul summit and declaration (2024-05-21); A Right to Warn about Advanced AI
(2024-06-04); the EU AI Act's entry into force (2024-08-01); California's veto of SB 1047
(2024-09-29); Executive Order 14179 (2025-01-23); the International AI Safety Report
(2025-01-29); the Paris summit statement (2025-02-11); America's AI Action Plan
(2025-07-23); California's SB 53 (2025-09-29); the Statement on Superintelligence
(2025-10-22); Executive Order 14365 on state AI laws (2025-12-11); the New Delhi summit
declaration (February 2026); Executive Order 14409 (2026-06-02); Pacing the Frontier (July
2026); and Executive Order 14434, "Inaugurating the Era of Super Intelligence" (2026-09-29).
Each date was read from the primary page (search log `events-022` to `events-027`). Two are
at month precision because their own pages give no day: the New Delhi declaration and Pacing
the Frontier.

## 2026-10-12: rulings on the forecast ledger and the backward test

Decided by: mixed. The agent put five questions from the forecast ledger
(`docs/leg-b-ledger-2026-10.md`) and one from the backward test (`docs/backward-test-method.md`)
to John with recommendations; John approved all of them ("all as recommended"). Only the first
changes a document's wording; the rest are recorded here so that no later session reopens
them without knowing they were settled. Each ruling is also recorded in the document it bears
on, and in section 8 of the definition.

### A23. The definition's "mostly arrived early" sentence replaced by what the ledger shows

Was (leg B, "Direction is recorded"): "Milestones from the 2016 Grace survey mostly arrived
early."
Now: of the survey's 32 milestones, every one that has arrived came early, but most have not
arrived, and eleven are past their forecast date. The sentence cites the ledger.
Why: the sentence had no source. The ledger built on 2026-10-09 checked it against the
survey's own table: 1 milestone has clearly arrived and 5 arguably, all 6 early; 22 have not
arrived, of which 11 are already past their forecast date and 11 are not yet due; 4 set no
bar to check against. So "mostly arrived early" is true of the arrivals and false of the
survey as a whole. The frozen thresholds are untouched; the gauge's definition is untouched.

Rulings that changed no wording:

- **The ledger is the record of which way forecasts missed, and nothing more.** Leg B's
  gauge stays defined on forecasts of METR's task-length measure. The survey's milestones
  are yes-or-no events with no trend to extend, so they cannot fill that formula.
- **The ledger's four milestones with no bar stay out of the scores.** Their verdict is
  recorded as "no bar" (it was "left for John" in the ledger's data, script and method
  until this ruling; the meaning is the same). A bar set now would be chosen after seeing
  the answers.
- **None of the five "arguably arrived" milestones is promoted to arrived.** Both the strict
  total and the generous one keep being reported.
- **No fifth verdict.** The ledger's one-condition rule stays as written, and the four rows
  moved to "not arrived" on 9 October stay there with their nearest demonstration recorded.
- **The pace rule stays as written and is read the stricter way:** the last three
  twelve-month windows must each be quicker than the one before. The backward test's
  near-firings in late 2014 and late 2019, with training compute standing in for the
  task-length measure, are noise in the stand-in (it measures what went into systems, not
  what they could do, and windows of three or four systems swing a lot), not a flaw in the
  rule. The definition is not changed for it.

## 2026-10-17: the pace gauge's anchor series has stopped updating; the successor question is opened

Decided by: mixed. The first weekly reading (2026-10-16) flagged that METR's time-horizon
page says it is no longer actively updated (last update 2026-09-08) and that METR's Frontier
Risk Report of 2026-05-19 says the Time Horizon 1.1 suite cannot measure above 16 hours and
the strongest agents have saturated it. The agent and the master session recommended asking
METR whether a successor is coming and recording the question here as open, so the page says
the gauge is running out rather than going quiet; John accepted ("ask METR and record the
successor question as open", 2026-10-17, confirmed in the review session the same day after
asking what METR is).

### A24. Successor to the leg A anchor: question opened, nothing changed yet

Status: **open.** No frozen value changes with this entry. `docs/singularity-entry-thresholds.json`
is untouched; leg A keeps scoring from the METR rows already in `data/world_measures.csv`
under the rules as written (windows holding a reading past 16 hours are not scored).

What is true: the anchor series for leg A (and the reference series for leg B's ledger) has
stopped moving. The record's top frontier reading (Claude Mythos Preview, early, 1,044.78
minutes on 2026-04-07) is already past the 16-hour bar, so a trailing twelve-month window will
soon hold no scorable frontier readings and the gauge will show no current value.

What the successor rule requires (A19): a replacement measure named before the series stops,
an overlap period published, and the switch recorded here as an amendment.

What happens next:
1. John asks METR whether a Time Horizon 1.2 or 2.0 is planned, whether it will overlap the
   1.1 series, and if not which public series they would point to (note drafted and sent by
   John from his own address on 2026-10-17).
2. On METR's answer, or after a stated wait if none comes, candidate successors are proposed
   with pictures of the overlap, and the switch is ruled as A25 or later.
3. Until then the page says the gauge's source has stopped updating, with this entry linked.
   The weekly reading keeps checking METR's results file and adds "Time Horizon 2.0" to its
   search terms for the leg A item.

## 2026-10-17: the headline becomes the average share of the way, with an on-current-trends crossing sentence

Decided by: mixed. The agent's proposal of 2026-10-17 (`docs/headline-proposal-2026-10-17.md`)
recommended a count of parts past halfway; John ruled it that afternoon and, after seeing "1 of
4" on the parent site's shelf ("'1 in 4' is just not a very interesting headline"), revised it
the same evening in his words: "Rule the AGI Zeitgeist headline as the average share of the way
across the parts as the number, with the slowest part named, and an on-current-trends crossing
sentence as the words, the trend method as a numbered amendment." The agent built it on his
ruling.

### A25. The headline average and the on-current-trends sentence

**What changes.** Two things the page and `status.json` publish; nothing that is scored.

1. **The number** is the average of the measured legs' gauges (each gauge is its leg's scored
   measure against its reference value and frozen threshold, clipped to 0 to 1), written as a
   percentage "of the way". An unmeasured leg is left out of the average and named as
   unmeasured. The words beneath always name the slowest leg and its share ("all four must
   cross, and the slowest, the economy, is at 0%"). On 2026-10-17 the number is 32% (pace 43%,
   AI doing the research 52%, economy 0%; forecasts unmeasured).
2. **The words** are one sentence saying, on current trends, when each measured leg crosses its
   line, and whether the test is met on current trends. The method:
   - *Pace (leg A).* A straight line fitted to the logarithm of the trailing twelve-month
     doubling time against time, over every scorable window from the first (2024-06) to the
     latest. The slow end of the range is the year that line reaches the threshold; the fast
     end is the year reached if the doubling time halved every year from the latest scorable
     window, the rate seen between 2024 and 2025. If the fitted line does not fall, the leg
     "does not cross on the fitted trend", and the fast end is still stated. Today: 2028 to
     2048.
   - *AI doing the improving (leg C).* The last two readings of the scored series. The fast
     end extends them proportionally (the same multiplying factor per year), the slow end in a
     straight line; both floored at one month ahead. Today: 2027 on both. A leg already at its
     threshold "has crossed".
   - *The economy (leg D).* A straight line fitted to annual growth from 2010 to the latest
     year. If its slope is zero or negative, or the crossing lies more than a hundred years
     out, the leg "does not cross its line" and the sentence says the test is not met on
     current trends. Today: does not cross (the slope is −0.04 points a year).
   - *Forecasts (leg B).* Unmeasured; named as such until the ledger exists.
   - Crossing years are calendar years, counted from the date of the latest reading used.
     Where a leg's two ends differ the sentence gives both as a range; it never gives a single
     year for a fit that is unstable.
   - The same sentences, with their ranges and the thin-basis caveats, stay in each leg's panel
     as landed on 2026-10-17.

**What does not change.** The frozen thresholds, the reference year, the scored series, the
persistence rule and the verdict's wording. The status words (not entered, approaching, mark
crossed, entered) are still computed from the gauges as section 3 says, never from the average
or the sentence. P(t) in section 4, the weakest leg's gauge, stays the definition's own progress
number and is still published as `progress` and written out in the test section.

**The argument section 4 makes against an average, and how it is kept.** Section 4 says an
average would let one runaway leg hide stalled ones. That stands for P(t), which is why P(t)
is not replaced. The headline average is a reading aid for the shelf, and the rule that keeps
it honest is that it is never printed without the slowest leg and its share in the same
breath, and never used to decide the status. Methodology section 9's rule that series are
never combined into an index is read the same way: the gauges are combined only in this
labelled headline, with the parts shown beside it, not in any series or score.

**Published fields** (`site/status.json`): `headline` ("32%"), `headline_label` (the average
sentence with the slowest leg), `average_share` (0.315), `crossing_sentence` (the
on-current-trends sentence), `crossings` (per leg, the earliest and latest crossing year, or
null where the leg does not cross), and `parts_past_half` (kept from the afternoon's ruling);
`status`, `progress`, `progress_is_upper_bound`, `bottleneck`, `gauges` and `unmeasured` as
before.

**The weekly reading** recomputes the number and the sentence at every site rebuild; nothing
is written for them by hand.

**The next question, not built now.** John named a version two for a later day: a computed
probability and a year on the siblings' pattern (The Belt Equation, The Quiet Galaxy), from a
model that draws each leg's crossing year from a range and reports the chance the test is met
by a given year and the middle year. It would need a stated distribution for each leg's
crossing, a rule for the unmeasured leg, and a run record; it is logged here as the question
that follows this amendment.

## 2026-10-17: the busy-year sampling rule keeps the "now" statements

Decided by: mixed. The frontier-lab traces of 2026-10-17 (pull request 13) applied section
3's busy-year rule as written, keeping every timeline-bearing statement and sampling the rest at
every third item, and so dropped the statements closest to the project's third question, whether
today's systems are already improving themselves: six of Dario Amodei's 2026 statements and four
of Demis Hassabis's from 2025 to 2026. The managing session recommended keeping that frame in
full; John ruled "as recommended" on 2026-10-17 through the master session.

### A26. Statements on the "now" question are never sampled out

Was (methodology version 2, section 3, "Collection"): where a person made more than ten
qualifying statements in a year, all timeline-bearing statements are kept and the rest sampled
at a fixed interval, logged.

Now: all timeline-bearing statements are kept, and so are all statements that bear on the "now"
question, meaning any whose `frame_primary` or `frames_present` includes `self_improvement`, or
whose `present_capability` is coded `claimed`; the rest are sampled at a fixed interval, logged.

Why: the project's story has three questions, whether, when and now, and the sampling rule
protected only the second. Sampling the "now" frame biases the series exactly where the
frontier-lab voices matter most, since a lab head's claim that his systems are already improving
themselves is the kind of statement the vanguard and the self-improvement gauge are compared
against. The ten rows dropped on 2026-10-17 are added under this rule when the full panel
collection (pull request 4, reconciled with pull request 13) lands, with their searches already
in the log; the rows carry a note naming this amendment. Nothing scored changes: statements never
score a gauge.


## 2026-10-17: a dated-claims ledger per person, scored against delivery

Decided by: mixed. John asked on 2026-10-17 for more from the industry leaders at the front of
the AGI claims: are they a front-row seat or salesmen? The agent proposed a ledger of each
person's dated claims scored against what happened, on the pattern of the sibling trackers'
claims logs (`docs/claims-ledger-proposal-2026-10-17.md`, with the seed list in
`docs/claims-ledger-seed-2026-10-17.md`), and John ruled "as recommended" on all ten of its
rulings the same evening, through the master session. The method is
`docs/claims-ledger-method.md`, written before any row.

### A27. The claims ledger: a new record kind, its status words and its rules

Was: the record held what people said (`data/statements.csv`, coded), what the world did
(`data/world_measures.csv`), the surveys, polls and markets (`data/aggregates.csv`), and one
scored set of forecasts, the 2016 researcher survey's milestones (`data/leg_b_ledger.csv`). No
named person's dated prediction was set against what happened.

Now: a claims ledger, one file per claim in `data/claims/<id>.toml`, for anyone on the frozen
panel, built in the order Altman and Musk, then Amodei, then Huang, then the other members tied
to the frontier labs. A claim is admitted when the speaker is on the panel, the words look
forward, the words carry a date or a length of time, and there is a primary source (coverage
alone enters as `coverage_only`, marked, with no quote). An undated claim is not a claim record
and stays a coded statement; the page counts them. Five status words: `not_yet_due`, `hit`,
`missed`, `withdrawn` (counted as missed in every total), `unfalsifiable` (a date but no bar an
outsider could test, decided at entry; a bar is never supplied after the fact). A hit needs
every condition of the bar; there is no "partly". The due year is the end of the named year, a
span runs from the day it was said, a range takes its later end with the earlier recorded, a
point year with a spread is scored at the point, a month or quarter in the words sets a due
date within the year. A stated goal is admitted, marked and scored. A numeric chance is kept,
flagged and left out of the plain count. An unchanged repeat is one claim with its repeat dates;
a changed date is a new claim naming the one it restates. The rate is per person, never pooled,
hits over hits plus missed, with the due count beside it, the misses' direction reported, no
percentage under five due claims, and no percentage at all until the person has been traced
year by year with the searches logged (a `<speaker_id>-claims-traced` row in the search log);
until then the page says "seed only: not a rate". It shows at `/claims/` with one sentence on
the home page, a "Claims" handle in the top bar's heavier tier, and the four gauges' shares
repeated in a strip at the top of the page. `scripts/validate.py` checks every claim file.

Why: the tracker records what these people said and already scores forecasts against outcomes
in one place; what it lacked was the joint, a named person's own dated words set against what
happened, one claim at a time, which is where a tracker earns trust (tracker pattern rule 6.4).
The admission rule never looks at whether a claim came true, so the ledger cannot be built to
flatter or to damn. The undated rule keeps "soon" and "close" out of the score and in view. The
collection-pass rule keeps a rate from measuring which claims were easy to find.

What does not change: the frozen panel (A18), the coded statements (no row is edited, added or
deleted because of a claim), the scored series, the frozen thresholds, the definition including
leg B's gauge, the verdict and the headline (A25), and the weekly reading's rule. A claim's
verdict is never a measure of the world and never enters the headline. The correction in the
proposal's section 0 stands: Jensen Huang is already on the panel (2020s cohort, A18), so no
panel amendment is needed to give him claims.

## 2026-10-12: John's rulings on the open calls from the panel collection (numbered A28 when the collection landed on 2026-10-17, after A24 to A27)

Decided by: mixed. The open calls were listed in the body of pull request 4 (the full
collection for the 32 frozen panel members), under "Departures from the written method"
and "Places the method is silent". The recommendations were the session's; John ruled on
2026-10-12, in his words, "all as recommended". The rulings are recorded on the pull
request as a comment of 2026-10-12 and applied by the commits that follow it.

### A28. Self-improvement levels, hedge words, the silent points, and the panel record

1. **The self-improvement level: amendment A14 ruling 12 governs, with its agent
   reading.** "The lowest level the words support" applies when the words say nothing
   about who does the improving. Codebook section 1 had listed "the AI will improve
   itself" among the words that don't say who improves; that contradicted the codebook's
   own first question ("The AI itself → go on") and is corrected. Of the 18 rows a sweep
   on 2026-10-09 had moved down (the agent's own decision, later returned to their earlier
   codes): 3 stay at the lowest level (`yudkowsky-2008-01` on large jumps in intelligence,
   `yudkowsky-2008-02` on FOOM, `walsh-2020-01` on a bare "technological singularity",
   which the codebook table lists under superintelligence); 9 go to `si_modify`, the level
   where the system changes itself (`bengio-2016-01b`, `bengio-2026-01`, `musk-2014-02`,
   `russell-2014-02b`, `schmidhuber-2017-01`, `schmidhuber-2017-06`, `schmidhuber-2024-03`,
   `schmidhuber-2026-01a`, `schmidhuber-2026-01b`); 6 rejections or doubts of runaway
   growth keep their earlier codes (`walsh-2016-01b`, `walsh-2017-01b`, `chollet-2012-01`,
   `chollet-2017-02a`, `hanson-2016-01`, `hanson-2024-01`). Four rows the sweep had treated
   unevenly get the same reading: `hassabis-2025-08` (`hassabis-2025-05` when ruled) (a bare "hard takeoff") to the lowest
   level under A15 ruling 3; `musk-2015-01` ("recursive self improvement") to `si_modify`;
   `schmidhuber-2016-03` and `schmidhuber-2017-09` ("self-improve") stay at `si_modify`.
2. **Statements by people not on the panel** found while tracing a panel member are kept
   as leads, not recorded. Accepted as the practice (kickoff rule 4 said "still
   recorded", but a person outside the panel gets a `speakers.csv` row only through the
   wide list's light capture).
3. **The ten places the method was silent** are adopted as the practice stated in the
   pull request body and added to `docs/methodology.md` under "Points of detail not
   spelled out in version 2": the start year for the 2020s group; the coder label;
   "probably"; a reporter's paraphrase in the reporter's own interview; reading through a
   reader service or an archive; statements found later for a year already logged; where
   the every-third count starts; the self-improvement level as ruled in item 1; the date
   of an interview published later; co-written documents. The codebook's uncertain-words
   rule gains "probably", "likely" and "perhaps": a position resting on them is coded
   `accepts` with `ambiguous: yes`, unless "may", "might" or "could" governs the same
   claim, which makes it `uncertain`. A later pass sweeps the "likely" and "perhaps" rows.
   The departure that core members are searched from 2005, not from their first
   documented year, is accepted.
4. **Chollet's 2017 "timescales we can barely comprehend"** is not a public timeline
   statement. Chollet stays in the 2020s group, with a note on the panel record. The
   earlier first statements the collection found (Floridi 2015, Amodei 2023, Aschenbrenner
   2021, Chollet 2012) go into the panel record.
5. **The paid three-model reliability check** (methodology-v2 section 10) is deferred;
   not run. The three untraced members (Liang Wenfeng, Arthur Mensch, Arvind Narayanan)
   get their own session with web searches.

*Status, 2026-10-17:* items 1 to 4 were applied on the collection branch between 2026-10-12 and
2026-10-17; the three members named in item 5 were traced on 2026-10-17 in the same pull request
(Liang Wenfeng 11 statements, Arthur Mensch 6, Arvind Narayanan 29), so the collection covers all
32 members. The paid check stays deferred.

*Ruled by John, 2026-10-18 (relayed by the master session; applied 2026-10-19):* what counts as
one statement for the busy-year line, which the collection raised. The codebook said a unit is
"one statement by one speaker on one occasion", while the whole record has always counted each
distinct passage of an essay, talk or interview as its own row. John ruled the passage count, as
recommended. Methodology version 2 section 3, `docs/methodology.md` ("Busy years") and the
codebook's section 0 now say so. Nothing is re-sampled: the collection's busy-year counts were
already made by passage.

Why: the second independent check of the collection (pull request 4, comment of
2026-10-09) found that the codebook example conflicted with the ruling it illustrated,
and that the method said nothing on ten points the collection had to decide. Recording
the practice makes the next trace follow the same rules.

## 2026-10-18: tip intake, a way in for panel statements found between full passes

Decided by: mixed. The procedure (`docs/tip-intake.md`) and this amendment were drafted on
2026-10-18 after John sent a link to Nick Bostrom's interview on The Roman Forum; the first run
on that interview (pull request 18) added a fourth open decision and a reading of "checked
against the audio". John ruled on 2026-10-18, through the master session, "all as
recommended": the four open decisions, the reading, and this amendment.

### A29. Tip intake

Applies to: `docs/methodology-v2.md` section 3 (stream E, collection), `docs/weekly-reading.md`
("Deferred: the frozen panel's new statements") and codebook section 9. Procedure:
`docs/tip-intake.md`.

Was: stream E rows come only from the year-by-year trace, run per person with fixed queries
(methodology section 3; version 1 query set D1 to D3, Y1 to Y3). The weekly reading may not
add a statement by a panel member; part 4, which will find and log the panel's new
statements, is deferred until full collection lands. A statement John comes across has no
defined way in.

Now:

1. **One way in.** A panel statement found outside a full pass (sent by John, or, once part 4
   is live, found by the weekly reading) enters through `docs/tip-intake.md`: primary source
   archived with a checksum in `sources/manifest.csv`; speaker checked against the frozen
   tiers; the person's fixed year queries and own outlets searched and logged; candidate
   statements coded under the codebook by the same procedure as the collection; notes tagged
   `tip`, and `tip; tip_only` where the fixed searches do not find the source. People not on
   any tier are not coded; they are listed in `docs/panel-candidates.md` for the next panel
   review. Part 4 of the weekly reading, when it goes live, follows the same file.
2. **`tip_only` rows are kept and not counted.** They stay in `data/statements.csv` and are
   left out of every figure and share. The site lists them on the changelog page under "Noted,
   outside the measured record", written from the table at each build. At the person's next
   full pass the same searches are run again and logged, and `tip_only` is lifted from a row
   if they then find the source or a report of the same appearance; the re-run only ever lifts
   the tag.
3. **Transcripts stay local.** Archived source files are kept out of the repository
   (`sources/*/` in `.gitignore`); only `sources/manifest.csv` is committed, with each file's
   address, dates and checksum.
4. **Quotes from machine captions.** "Checked against the audio" means two automatic
   transcripts from separate programs agree on the quoted words (the platform's captions and a
   local Whisper transcription of the audio), word for word, ignoring case, punctuation and
   filler sounds; nobody listens by ear. A quote they disagree on, or that has no second
   transcript, carries `asr_unverified` and `coding_confidence` no higher than `medium`. This
   is the rule John ruled for The Upgrade Tree on 2026-10-17.
5. **Panel watch notes** are drafted in `docs/panel-watch/`, beside the rows they cite; Claude
   drafts and John posts.
6. **Codebook section 9** gains three notes tags: `tip`, `tip_only` and `asr_unverified`.
7. **Enforcement.** `scripts/chart_style.py` gains `tip_only()` and `measured()`;
   `scripts/charts.py` and `scripts/site.py` compute every figure and the site's statement
   count from `measured()` rows only. `scripts/validate.py` knows the three tags, rejects
   `tip_only` without `tip`, and rejects `asr_unverified` with `coding_confidence: high`.

Why: prominent panel members now speak mostly in long interviews and podcasts, and those are
where the "now" question gets answered. The trace already misses them when no transcript
exists: Bostrom's Joe Rogan Experience appearance of 2026-07-14 is logged as "not recorded:
summary writer's paraphrase only, no transcript" (search log `bostrom-120`). Tip intake
supplies the transcript and the archive. The `tip_only` rule keeps the hand route from
becoming a sampling frame: a tip can make the record faster, never different from what the
rule would produce. The re-run in item 2 is there because a test run the day a tip arrives
measures how fast search engines index a new source as much as the rule's reach; the first
case, two days old, was not found even by a search for its exact title (`bostrom-127`).

Effect on the first case: the nine Bostrom rows of 2026-10-16 (`bostrom-2026-02a` to
`bostrom-2026-08`) are `tip_only` and change no figure. The draft panel watch note on them
(`docs/panel-watch/2026-10-18-bostrom.md`) is not posted; John ruled it is not one of the
Sentient Horizons outreach trials, and it goes to the first outreach review on 2026-10-24 as a
proposal. Nothing scored changes: statements never score a gauge.

## 2026-10-19: the claims ledger widened to the industry's figureheads, with a ledger-only list

Decided by: mixed. The claims ledger opened on 2026-10-19 with thirty claims by Sam Altman and
Elon Musk. John read the news post announcing it the same day and asked, in his words, "why is
it just Altman and Musk. This should be a collection of all of the figureheads including Amodei
and Huang and any others that you feel are relevant to include in that category". The managing
session proposed an inclusion rule and fourteen names, and John accepted them. Of the three
company heads who are not on the frozen panel he ruled: "Those three should be included,
whatever that means". This amendment records how they are included without touching the panel.

### A30. The figureheads: who the claims ledger covers, and the ledger-only list

Applies to: `docs/claims-ledger-method.md` (what the ledger is for, the `speaker_id` field, the
admission rule's first condition, what the ledger must never touch, the order of work);
`data/speakers.csv` (a new tier value); `scripts/validate.py`, `scripts/chart_style.py`,
`scripts/charts.py` and `scripts/site.py` (the checks and the tier filters).

Was: a claim was admitted only if its speaker was on the frozen panel (amendment A18), and the
ledger was to be built in the order Altman and Musk, then Amodei, then Huang, then the other
panel members tied to the frontier labs, then anyone else on the panel with a dated claim
(amendment A27). Nothing said who counts as one of "the people who run the AI companies", and
nobody off the panel could be entered.

Now:

1. **The inclusion rule.** The ledger covers the industry's figureheads. A figurehead is the
   chief executive, founder-leader or chair of a company that builds frontier AI models or the
   chips they are trained on, or that company's named chief scientist speaking for it. **A claim
   counts only if it was made while the person held that role.** A claim made before or after
   it, or in a gap between two such roles, is left out, and the search-log row that found it
   says why.
2. **The fourteen people** (John, 2026-10-19). On the frozen panel already: Sam Altman, Elon
   Musk, Dario Amodei, Jensen Huang, Demis Hassabis, Mustafa Suleyman, Ilya Sutskever, Liang
   Wenfeng, Arthur Mensch, Shane Legg and Yann LeCun. Not on the panel: Mark Zuckerberg (Meta),
   Sundar Pichai (Google and Alphabet) and Satya Nadella (Microsoft).
3. **The ledger-only list.** The three who are not on the panel enter `data/speakers.csv` with
   a new tier, `claims_only`. A `claims_only` row is never a panel member: it never enters
   `data/statements.csv`, the opinion charts, the experts' dates or any of the panel's counts,
   and it carries no panel quota tag. The panel stays 37 people. Adding a name to the list, or
   taking one off, is itself an amendment.
4. **The admission rule's first condition** becomes "the speaker is on the frozen panel or on
   the ledger-only list, and held a qualifying role when the words were said". The other three
   conditions (the words look forward, they carry a date or a length of time, there is a
   primary source) are unchanged.
5. **Each figurehead's role, with its dates,** is written in the speaker row's notes
   (`inclusion_note`) for the three new rows, and in each claim's `notes` for everyone, so the
   role-at-the-time rule can be checked one claim at a time. The eleven panel rows keep their
   frozen notes; their role histories were already in `role_summary` and the `frontier_lab`
   tag.
6. **The order of work** for the twelve people beyond Altman and Musk: Amodei and Huang first,
   then Hassabis, Suleyman, Sutskever, Legg, LeCun, Liang Wenfeng, Mensch, Zuckerberg, Pichai
   and Nadella. Panel members with dated claims in the seed list who are not figureheads under
   the rule (Geoffrey Hinton and Ray Kurzweil, who never ran such a company) are not entered.
   Kai-Fu Lee, on the panel and in the seed list, has been the founder and chief executive of
   01.AI, a company that builds AI models, since 2023, so he appears to meet the rule for claims
   made since then; he is not on John's list, and whether to add him is a call for John.
7. **Enforcement.** `scripts/validate.py` accepts `claims_only` as a tier for a person, refuses
   a claim whose speaker is not `core`, `cohort_2020s` or `claims_only` (so the wider list of
   candidates, tier `wide`, cannot have claims either), refuses a quota tag on a `claims_only`
   row, and refuses any row of `data/statements.csv` by a `claims_only` speaker.
   `scripts/chart_style.py` defines the panel's two tiers once (`PANEL_TIERS`, `panel()`), and
   `scripts/charts.py` and `scripts/site.py` read the panel through them, so a `claims_only` row
   cannot reach a figure, the experts' dates or the panel count on the home page.

Why: John asked for all the figureheads, not two. The rule makes the list checkable: anyone can
see why a name is on it, and the role-at-the-time condition keeps a person's words from before
or after they ran such a company from being scored as if they had. The ledger-only list is how
John's "those three should be included" is met without touching the frozen panel: the panel was
frozen (A18) so that it could not drift toward the story, and widening it to fit the ledger would
do exactly that. A separate tier keeps the two records apart in the data itself, not only in the
prose.

Applied to the thirty claims already entered: twenty-seven were made while the speaker held a
qualifying role (Altman as OpenAI's co-chair in January 2019 and its chief executive after;
Musk as OpenAI's co-chair in January 2016 and as the founder and head of xAI from 2023). Three
Musk claims were made when he headed Tesla but held no role at OpenAI (he left its board in
February 2018) or xAI (founded in 2023): the million robotaxis of 2019-04-22, the "level five"
basic functionality of 2020-07-09, and the Tesla robot prototype of 2021-08-19. Whether Tesla
counted then as a company that builds frontier AI models or the chips they are trained on (it
designed its own driving chip, shown on 2019-04-22, and announced its own training chip, Dojo,
on 2021-08-19) is a call for John. The three files are left as entered until he rules; nothing
in them changes.

What does not change: the frozen panel's membership (A18), `data/statements.csv`, the scored
series, the frozen thresholds, the definition, the verdict and the headline (A25), and every
other rule of the ledger (A27 and John's rulings of 2026-10-19 in the method).
