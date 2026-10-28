# Amendments

Dated changes to the method, the panel or the codes, with the reason. Nothing in the method changes without an entry here. Reviews referred to below are saved verbatim in `docs/reviews/`.

## 2026-09-30: reconciliation of the two outside reviews (Gemini 3.1 Pro, GPT-6 Astra Medium)

Both reviews were read against the kickoff plan (`docs/2026-09-30-kickoff.md`). The result is `docs/methodology-v2.md`, which supersedes the method sections of the kickoff plan. The kickoff plan stays as the record of where the project started. I ruled on 2026-09-30 that no third review would be sought and that these two would be worked with.

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

### A13. Expert panel expanded into three tiers with written quotas (my ruling, 2026-09-30, after discussing panel size)

Was: a core panel of 15 to 20 plus an unsized 2020s cohort.
Now: three tiers.
- Core panel, about 25, each meeting the dated rule in A5, frozen by me from the verification table. Minimum quotas, written so the panel cannot lean one way by construction: at least six sustained skeptics or critics (people whose pre-2017 statements reject or doubt AGI within decades); at least three based outside the United States and United Kingdom at the time of their pre-2017 statements; at least two philosophers or cognitive scientists; at least three with frontier-lab ties, so incentives are visible rather than screened out. Fully traced.
- 2020s cohort, ten to twelve people prominent on AGI timelines only since 2020, fully traced, reported as its own series so its arrival is visible in the data.
- Wide list, 60 to 100 names, built by an enumerable rule rather than by hand, with a light capture: one qualifying statement per person per era (2005 to 2015, 2016 to 2022, 2023 onward) found by a fixed query. Used only for composition and balance checks, never for within-person claims. Seed sources for the list: the public MIRI/AI Impacts dataset of dated AI timeline predictions (Armstrong and Sotala 2012 and its successors), the TIME100 AI lists 2023 to 2025, and every person quoted on AGI timelines in the stream M media sample.
Why: with 15 to 20 people the expert frame share is driven by whoever spoke most, and the dated prominence rule rewards the people who were loud early, mostly singularitarians and lab founders, so the "whether" era would be answered only by people who had already decided. Collection is cheap (a full trace took the seed session about thirteen minutes with a helper); coding and double-coding are the cost, which is why the wide list is a light capture. Timing: the panel freezes before full collection and the verification table is being built now, so the expansion costs an afternoon this week rather than an amendment and re-sampling later.

### Declined, with reasons

- Factiva and LexisNexis for non-US media (Gemini): paywalled, so not re-pullable by a reader. Guardian and Media Cloud's non-US collections instead; non-English corpora deferred until there is capacity for language-specific validation.
- Dropping Google Books Ngram entirely (Gemini): demoted instead (A9); the astrophysics problem with "singularity" is avoided by using the two-word term "technological singularity".
- Replacing the question-frame scheme with a proximity and disruption matrix (Gemini): proximity (distant, medium, near, present) is derived at render from the timeline fields, so it needs no new code; disruption became `consequence_type` (A2).
- Film box office as a measurement series (Gemini): kept as dated event annotations only (Her 2013, Transcendence and Ex Machina 2014, and so on), because a theme-tagged box-office series would need its own coding project.
- A single numerical common axis: used only where the source gives a probability for a specified capability by a specified date, as GPT advised; "soon" is never converted to a number.

## 2026-09-30: implementation decisions for version 2 (decided by: the model, not reviewed by me)

Made while carrying out the version 2 migration. I can reverse any of them.
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
  in `docs/panel-verification-2026-10.md` for me to rule on.

## 2026-10-01: my rulings on the fifteen open decisions

Decided by: me. The decisions were listed in `docs/status-2026-10-01.md`; the
rulings below were sent by me on 2026-10-01. Where an agent had to interpret a
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
   interfaces: their official data services) once I have keys. Not attempted now.
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

13. I double-code a blind sample myself (`data/double-coding/`).
14. I merge the branch myself.
15. Licence: Creative Commons Attribution 4.0 (CC BY 4.0) for the data, MIT for the
    scripts.

Why: these were the open questions found while building the panel table and while
recoding the seed under version 2; recoders were applying 9 to 12 inconsistently.
Rows recoded under rulings 9 to 12 carry `coder: claude-agent-v2.1` and a note naming
the ruling.
- *Agent interpretation of ruling 10 (2026-10-01), for me to confirm:* a firm, unhedged
  first-person date that uses none of the listed words ("I set the date for the
  Singularity as 2045", "I'm still saying 2029") is kept as `accepts`, because coding a
  stated prediction as "no position" would misreport the source. The rows concerned
  are listed in `docs/status-2026-10-01.md`.

## 2026-10-01: my rulings on the eight calls raised after A14

Decided by: me. The eight calls were listed in `docs/status-2026-10-01.md` (section
"New questions for me").

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

Why: these were the cases where applying A14 needed a reading I hadn't given.
Validator changes that follow: statement ids may carry a one-letter suffix, and a
`range` may leave the high bound open when the row carries the `lower_bound` tag.

- **2026-10-02, vanguard sub-series of stream F (accepted; decided by: me):** after the Gemini 3.1 Pro and GPT-6 Astra Medium reviews, I ruled: enthusiast venues only, plus an event-by-event comparison with skeptic venues once one exists, no monthly gap; claims coded on separate fields, six-rung proximity ladder as a display for AGI claims only; stream F's sampling reused; image posts with legible text included; GPT's caption on every figure and heading, "leading indicator" only in the essay as a hypothesis; shares only; folded into stream F as a labelled sub-series never pooled with F's other venues. Full text: `docs/amendments/2026-10-02-vanguard-stream.md`. Only the r/singularity retrievability check may run.

## 2026-10-02: the newspaper-prominence rule loosened

Decided by: me, on the model's recommendation. The seed-phase agent raised the question on 2026-10-01 and offered the
looser wording; I chose it on 2026-10-02 when asked in the management session.

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

- **2026-10-02, vanguard sub-series, video posts (decided by: me):** video posts are coded from their title only; the video is not watched or coded, and a video post is eligible only if its title makes a claim about AI capability, timeline or consequence. Written into section 6 of `docs/amendments/2026-10-02-vanguard-stream.md`.
- **2026-10-03, vanguard sub-series, title-only rows (decided by: me):** retrievability is always reported as two figures (fully recoverable; including video posts coded by title only) with per-quarter counts; a `title_only` field marks rows coded from the title alone so their hedge and claim fields can be excluded; section 8 notes that title-only coding likely overstates unhedged claims.
- **2026-10-03, vanguard sub-series, pilot rulings (decided by: me):** capability and consequence claims become the primary measures, the four headline claims are kept and reported as near-absent; new field `extrapolates_to_horizon`; figures labelled "interim, model-coded" until two people have coded the worksheet; codebook rulings: new target `industry_governance` for AI company and policy drama, demo-only video titles are eligible capability claims, posts not mentioning AI are ineligible, memes follow the legible-text rule. Instrument: `docs/vanguard/codebook.md`.
- **2026-10-03, reliability design (decided by: me):** the requirement that two people code a blind subset (amendment section 9, and the double-coding in methodology-v2 section 10) is withdrawn because this is a single-researcher project. Replaced by a blind second pass from a different model family (both models named and pinned), a 40-post blind subsample coded by me with his agreement against each model reported, and a plain-language note that coding is model-assisted with one human check, disclosed as a limitation, not a second coder. **This departs from both outside reviews**, which asked for independent human double-coding.
- **2026-10-03, reliability design, second revision (decided by: me):** the human coding step is removed. My 40-post blind check (part (b) of the earlier ruling the same day) is withdrawn, with its worksheet and agreement script. Coding is fully model-based: Claude, Gemini and GPT-6 Astra code the same 140-post set blind; the final code is the majority vote per field, unresolved where no two agree; pairwise kappa is reported for all three pairs. A field unresolved on more than 15% of posts, or with every pairwise kappa below 0.6, is excluded from figures and listed as unreliable. Recurring disagreements get a proposed codebook rule with kappa before and after, for me to rule on. **This departs from both outside reviews**, which asked for independent human double-coding, and goes further than the earlier revision, which kept one human check.
- **2026-10-03, vanguard codebook rules (decided by: me):** R2 (target decided by the subject of the main claim: a model or system, a company or government, or people and society) and R3 (hedging coded only from hedge words in the words stating the claim) adopted into `docs/vanguard/codebook.md`. R1 not adopted as written; split into R1a (a post passed on without comment has no stated stance) and R1b (such a post attributes the claim to the linked source), each trialled separately on the 112 posts all three models coded in the first trial. "Whether the poster wants AI sped up or slowed down" is dropped from reported measures and listed as unreliable. A monthly cost quote for Gemini's paid tier is required before the full-sample run. The codebook as it stood before R2 and R3 is kept as `docs/vanguard/codebook-frozen-2026-10-03-before-rules.md`, so the first trial's remaining Gemini posts are coded on the same codebook as the rest of that run.
- **2026-10-03, Gemini spending (decided by: me):** the cost quote in `docs/vanguard/model-cost-quote-2026-10-03.md` is approved: up to $15 for the first month (the full-sample run, about $9.80, plus the first monthly runs), then up to $5 a month for three venues. The full-sample run waits for the ruling on rules R1a and R1b, so the 390 posts are coded once under the final codebook.

## 2026-10-06: my rulings on the A16 readings, Sutskever, the thin readings and the freeze

Decided by: me (rulings 1, 2, 3 and 5); mixed (ruling 4: recommended by the coordinating
session, chosen by me). Sent by me on 2026-10-06 in the management session, in answer
to the open points in `docs/panel-verification-2026-10.md`, and relayed to this branch by
the coordinating session.

### A17. Panel rulings before the freeze

1. **Legg, Cowen and Yudkowsky stay in the core.** I confirmed the verifier's three
   judgement calls: "Legg named in passing, Cowen on jobs-and-automation pieces, and
   Yudkowsky on two edge outlets". They stay marked thin.
2. **Sutskever: "Not a timeline statement".** His co-signed 2015 "hard to predict when" is
   not an AGI timeline statement from before 2018, so he meets the cohort's first test and
   passes the 2020s cohort. His 2024-or-later statement was checked against the record:
   the 2025-11-25 Dwarkesh Patel interview, "I think like 5 to 20" (years), in his own
   words.
   *Correction recorded:* my first answer the same day said the 2015 line *does*
   count as a timeline statement and that Sutskever passes. That answer was given to a
   question the coordinating session had framed backwards; read literally, it would have
   failed him (as the agent flagged, the same reason failed Suleyman and Karnofsky). This
   ruling is my answer to the question framed correctly, and replaces the first.
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
   first marked PROPOSED; I then said "Freeze and merge" (A18, below).

Why: these were the last open points before the freeze. Effect: core passes 22 to 25;
cohort 8 to 12; the three new cohort members leave the wide list (308 names). Details in
`docs/panel-verification-2026-10.md`, sections "Closing the three unclear cases
(2026-10-06)", "Cohort search (2026-10-06)" and "Freeze candidates as of 2026-10-06";
evidence in `docs/panel-evidence-2026-10/gaps-2026-10-06.md` and
`docs/panel-evidence-2026-10/cohort-search-2026-10-06.md`.

## 2026-10-06: the expert panel is frozen

Decided by: me ("Freeze and merge", 2026-10-06). The three readings under "Readings
chosen at the freeze" are decided by: me, on the model's recommendation (recommended by the model, chosen by me).
Drafted by claude-agent on 2026-10-06 under A17 rulings 3 and 5 and first recorded as a
proposal; my yes was relayed to this branch by the coordinating session the same day.
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
pass one of them is recorded, not acted on, unless I amend the panel.

**Readings chosen at the freeze** (decided by: me, on the model's recommendation, 2026-10-06):
1. **`frontier_lab`: Liang yes, Mensch no.** DeepSeek counts as a company building the
   most capable models of its time; Mensch's research-scientist role at DeepMind
   (2020 to 2023) and Mistral do not meet the tag.
2. **Mensch's April 2024 "I don't believe in AGI" counts** as his 2024-or-later statement,
   consistent with the Shanahan reading in A17 ruling 4 (a statement on whether AGI
   arrives, with no date, counts).
3. **Narayanan, not Kapoor**, for the essay they wrote together. Kapoor stays on the wide
   list.

Why: A17 rulings 3 and 5 asked for the freeze once the three gaps were closed and the
cohort search was done; both were done, and I said "Freeze and merge".

Effect: `data/speakers.csv` gains 32 rows (20 core, 12 cohort) beside the five seed
speakers, each with `tier`, quota tags (justification, date, link) and an inclusion note
naming the evidence and any reason the pass is thin. The wide list's frozen record is
`data/wide_list_candidates.csv`; methodology-v2 section 3 puts `tier: wide` on the
light-capture rows, so wide-list people enter `data/speakers.csv` when their statement is
collected, not before (many are listed by surname only in the MIRI dataset, so a speaker
row could not yet be filled in honestly). Next step: full collection for the 37 core and
cohort members.

## 2026-10-08: the singularity-entry definition adopted, with a fourth leg

Decided by: me, on four questions the agent put to me with recommendations; I
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
4. **Leg D, the economy, added (my ruling against the agent's recommendation).** World
   output doubling time from World Bank annual world growth. Threshold: growth at or above
   30 percent a year, Davidson's published "explosive growth" line (2021). Reference: the
   1961 to 2019 mean of the same series. One annual reading covers its four quarters;
   revisions reset the count. The agent had recommended publishing the economic reading
   beside the mark, not inside it, because output lags capability by years and the
   progress number (the smallest gauge) will track the economy until it moves. I
   accepted that cost for the sake of a leg measured outside the AI field.
5. **Gauges and status are published** at agizeitgeist.com from the frozen
   file. Leg B is shown as not yet measurable until the forecast-versus-outcome ledger
   exists; progress is then reported as "at most" the smallest measured gauge.

Agent decisions inside the adoption (I can reverse any):
- T_ref for leg A is METR's own whole-series fit (187.8 days, row `metr-th11-doubling-all`,
  the fit over all frontier models since 2019), because the trailing-window series cannot
  be computed in 2019 itself. Windows that include a reading past 16 hours are not scored,
  following METR's own exclusion.
- Leg C is scored from Anthropic's "leads" share only; the Google code-share row is a proxy
  and is shown unscored.
- The World Bank series is stored in `data/world_measures.csv` as one row per year (unit
  `percent_growth`), and the validator's date floor for that file is 1960.

## 2026-10-08: the 2022 survey's even-odds year recorded as 2060

Decided by: me, on the model's recommendation. The agent re-read both sources and recommended the change; I approved
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

Decided by: me ("add the product launches to the events list"). The inclusion rule below
is the agent's, made so that the list is not chosen by taste; I can change it.

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

Decided by: me ("add the post-2024 institutional events too"). The inclusion rule below is
the agent's, written to match the events already listed; I can change it.

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

Decided by: me, on the model's recommendation. The agent put five questions from the forecast ledger
(`docs/leg-b-ledger-2026-10.md`) and one from the backward test (`docs/backward-test-method.md`)
to me with recommendations; I approved all of them ("all as recommended"). Only the first
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
  recorded as "no bar" (it was "left for me" in the ledger's data, script and method
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

Decided by: me, on the model's recommendation. The first weekly reading (2026-10-16) flagged that METR's time-horizon
page says it is no longer actively updated (last update 2026-09-08) and that METR's Frontier
Risk Report of 2026-05-19 says the Time Horizon 1.1 suite cannot measure above 16 hours and
the strongest agents have saturated it. The agent and the master session recommended asking
METR whether a successor is coming and recording the question here as open, so the page says
the gauge is running out rather than going quiet; I accepted ("ask METR and record the
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
1. I ask METR whether a Time Horizon 1.2 or 2.0 is planned, whether it will overlap the
   1.1 series, and if not which public series they would point to (note drafted and sent by
   me from my own address on 2026-10-17).
2. On METR's answer, or after a stated wait if none comes, candidate successors are proposed
   with pictures of the overlap, and the switch is ruled as A25 or later.
3. Until then the page says the gauge's source has stopped updating, with this entry linked.
   The weekly reading keeps checking METR's results file and adds "Time Horizon 2.0" to its
   search terms for the leg A item.

## 2026-10-17: the headline becomes the average share of the way, with an on-current-trends crossing sentence

Decided by: me, on the model's recommendation. The agent's proposal of 2026-10-17 (`docs/headline-proposal-2026-10-17.md`)
recommended a count of parts past halfway; I ruled it that afternoon and, after seeing "1 of
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

**The next question, not built now.** I named a version two for a later day: a computed
probability and a year on the siblings' pattern (The Belt Equation, The Quiet Galaxy), from a
model that draws each leg's crossing year from a range and reports the chance the test is met
by a given year and the middle year. It would need a stated distribution for each leg's
crossing, a rule for the unmeasured leg, and a run record; it is logged here as the question
that follows this amendment.

## 2026-10-17: the busy-year sampling rule keeps the "now" statements

Decided by: me, on the model's recommendation. The frontier-lab traces of 2026-10-17 (pull request 13) applied section
3's busy-year rule as written, keeping every timeline-bearing statement and sampling the rest at
every third item, and so dropped the statements closest to the project's third question, whether
today's systems are already improving themselves: six of Dario Amodei's 2026 statements and four
of Demis Hassabis's from 2025 to 2026. The managing session recommended keeping that frame in
full; I ruled "as recommended" on 2026-10-17 through the master session.

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

Decided by: me, on the model's recommendation. I asked on 2026-10-17 for more from the industry leaders at the front of
the AGI claims: are they a front-row seat or salesmen? The agent proposed a ledger of each
person's dated claims scored against what happened, on the pattern of the sibling trackers'
claims logs (`docs/claims-ledger-proposal-2026-10-17.md`, with the seed list in
`docs/claims-ledger-seed-2026-10-17.md`), and I ruled "as recommended" on all ten of its
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

## 2026-10-12: my rulings on the open calls from the panel collection (numbered A28 when the collection landed on 2026-10-17, after A24 to A27)

Decided by: me, on the model's recommendation. The open calls were listed in the body of pull request 4 (the full
collection for the 32 frozen panel members), under "Departures from the written method"
and "Places the method is silent". The recommendations were the session's; I ruled on
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

*Decided, 2026-10-18 (relayed by the master session; applied 2026-10-19):* what counts as
one statement for the busy-year line, which the collection raised. The codebook said a unit is
"one statement by one speaker on one occasion", while the whole record has always counted each
distinct passage of an essay, talk or interview as its own row. I ruled the passage count, as
recommended. Methodology version 2 section 3, `docs/methodology.md` ("Busy years") and the
codebook's section 0 now say so. Nothing is re-sampled: the collection's busy-year counts were
already made by passage.

Why: the second independent check of the collection (pull request 4, comment of
2026-10-09) found that the codebook example conflicted with the ruling it illustrated,
and that the method said nothing on ten points the collection had to decide. Recording
the practice makes the next trace follow the same rules.

## 2026-10-18: tip intake, a way in for panel statements found between full passes

Decided by: me, on the model's recommendation. The procedure (`docs/tip-intake.md`) and this amendment were drafted on
2026-10-18 after I sent a link to Nick Bostrom's interview on The Roman Forum; the first run
on that interview (pull request 18) added a fourth open decision and a reading of "checked
against the audio". I ruled on 2026-10-18, through the master session, "all as
recommended": the four open decisions, the reading, and this amendment.

### A29. Tip intake

Applies to: `docs/methodology-v2.md` section 3 (stream E, collection), `docs/weekly-reading.md`
("Deferred: the frozen panel's new statements") and codebook section 9. Procedure:
`docs/tip-intake.md`.

Was: stream E rows come only from the year-by-year trace, run per person with fixed queries
(methodology section 3; version 1 query set D1 to D3, Y1 to Y3). The weekly reading may not
add a statement by a panel member; part 4, which will find and log the panel's new
statements, is deferred until full collection lands. A statement I come across has no
defined way in.

Now:

1. **One way in.** A panel statement found outside a full pass (sent by me, or, once part 4
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
   is the rule I ruled for The Upgrade Tree on 2026-10-17.
5. **Panel watch notes** are drafted in `docs/panel-watch/`, beside the rows they cite; Claude
   drafts and I post.
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
(`docs/panel-watch/2026-10-18-bostrom.md`) is not posted; I ruled it is not one of the
Sentient Horizons outreach trials, and it goes to the first outreach review on 2026-10-24 as a
proposal. Nothing scored changes: statements never score a gauge.

## 2026-10-19: the claims ledger widened to the industry's figureheads, with a ledger-only list

Decided by: me, on the model's recommendation. The claims ledger opened on 2026-10-19 with thirty claims by Sam Altman and
Elon Musk. I read the news post announcing it the same day and asked, in his words, "why is
it just Altman and Musk. This should be a collection of all of the figureheads including Amodei
and Huang and any others that you feel are relevant to include in that category". The managing
session proposed an inclusion rule and fourteen names, and I accepted them. Of the three
company heads who are not on the frozen panel he ruled: "Those three should be included,
whatever that means". This amendment records how they are included without touching the panel.
Later the same day, reading the pull request that carried it, I ruled two of the questions it
left open, in his words: "Yes Musk's claims from 2019-2021 should count", and "Sure, add Kai-Fu
Lee." Both rulings are written into the items below. An independent check of the pull request
(`docs/reviews/claims-ledger-check-2026-10-19.md`) then found the claim files read the same
phrases in different ways; I ruled four readings the same day, each as the check
recommended, and they are items 9 and 10 below.

### A30. The figureheads: who the claims ledger covers, and the ledger-only list

Applies to: `docs/claims-ledger-method.md` (what the ledger is for, the `speaker_id` field, the
admission rule's first and second conditions, the `bar` field, a new section "Readings I
ruled", the `hit` status word, when a claim is due, what the ledger must never touch, the order
of work);
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
2. **The fifteen people** (my ruling, 2026-10-19). On the frozen panel already: Sam Altman, Elon
   Musk, Dario Amodei, Jensen Huang, Demis Hassabis, Mustafa Suleyman, Ilya Sutskever, Liang
   Wenfeng, Arthur Mensch, Shane Legg, Yann LeCun and Kai-Fu Lee (added by my second ruling
   of the day; his claims count only from 2023, as founder and chief executive of 01.AI, a
   company that builds AI models). Not on the panel: Mark Zuckerberg (Meta), Sundar Pichai
   (Google and Alphabet) and Satya Nadella (Microsoft).
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
   role-at-the-time rule can be checked one claim at a time. The twelve panel rows keep their
   frozen notes; their role histories were already in `role_summary` and the `frontier_lab`
   tag.
6. **The order of work** for the twelve people beyond Altman and Musk: Amodei and Huang first,
   then Hassabis, Suleyman, Sutskever, Legg, LeCun, Liang Wenfeng, Mensch, Zuckerberg, Pichai
   and Nadella, then Kai-Fu Lee, added last. Panel members with dated claims in the seed list who
   are not figureheads under the rule (Geoffrey Hinton and Ray Kurzweil, who never ran such a
   company) are not entered. Lee's earlier dated claims (his "half of jobs in the next decade"
   of 2017 and his 2019 forecasts, made as a venture investor) are left out under the
   role-at-the-time rule.
7. **Enforcement.** `scripts/validate.py` accepts `claims_only` as a tier for a person, refuses
   a claim whose speaker is not `core`, `cohort_2020s` or `claims_only` (so the wider list of
   candidates, tier `wide`, cannot have claims either), refuses a quota tag on a `claims_only`
   row, and refuses any row of `data/statements.csv` by a `claims_only` speaker.
   `scripts/chart_style.py` defines the panel's two tiers once (`PANEL_TIERS`, `panel()`), and
   `scripts/charts.py` and `scripts/site.py` read the panel through them, so a `claims_only` row
   cannot reach a figure, the experts' dates or the panel count on the home page.
8. **When a claim is due.** A claim counts as due once its date has passed (31 December of its
   due year, or its `due_date`), whatever its status. A claim that cannot be tested used to
   count as due from the day it was entered, so the page's "now due" included untestable claims
   dated 2030 and later. `scripts/site.py` now counts this way (decided by the agent while
   widening the page, 2026-10-19; the independent check found it right). It changes a published
   number: for the first thirty claims, 17 are due, not the 20 the news post of 2026-10-19
   gives (Altman 6, not 9).
9. **What gets in, and what a hit needs** (given by the managing session on 2026-10-19 while
   the ledger was widened). Only claims about AI: a company's spending, revenue, order book,
   headcount, chip count, computing or data-centre build-out, training costs and labour-market
   forecasts not about what AI will do stay out (a forecast that AI will displace jobs is about
   AI and is admitted), and so does a plain hardware date. A hypothetical ("let's imagine",
   "suppose", "I could imagine", a date given only for an extrapolation the speaker disowns) is
   not a prediction. A borderline case stays out. A hit needs a dated record of the event
   itself, not an argument that it had become possible. A test uses the speaker's own words and
   usage in the same source and is never shaped to fit a verdict.
10. **Four readings, decided on 2026-10-19, each as the check recommended.** (1) "Early"
   in a year is its first quarter, by 31 March. (2) A forecast that something will not happen by
   a date is a claim, scored at that date: it came true if there is no public record of the
   thing by then, and did not if there is. (3) "A few years" and "as little as X" are undated,
   so they are not claim records (the agent applied the same reading to "the next few months"
   and "the coming months", which took out three Zuckerberg files, flagged for me). (4) Bare "human level" with no comparison in the same source
   is a named stage and cannot be tested; a stated comparison gives a plain test. Every claim
   file was passed again against them before merging.

Why: I asked for all the figureheads, not two. The rule makes the list checkable: anyone can
see why a name is on it, and the role-at-the-time condition keeps a person's words from before
or after they ran such a company from being scored as if they had. The ledger-only list is how
My "those three should be included" is met without touching the frozen panel: the panel was
frozen (A18) so that it could not drift toward the story, and widening it to fit the ledger would
do exactly that. A separate tier keeps the two records apart in the data itself, not only in the
prose.

Applied to the thirty claims already entered: twenty-seven were made while the speaker held a
qualifying role (Altman as OpenAI's co-chair in January 2019 and its chief executive after;
Musk as OpenAI's co-chair in January 2016 and as the founder and head of xAI from 2023). Three
Musk claims were made when he headed Tesla but held no role at OpenAI (he left its board in
February 2018) or xAI (founded in 2023): the million robotaxis of 2019-04-22, the "level five"
basic functionality of 2020-07-09, and the Tesla robot prototype of 2021-08-19. I ruled on
2026-10-19 that they count ("Yes Musk's claims from 2019-2021 should count"): Tesla counted then
as a company that builds frontier AI, training its own driving models and designing its own
chips (its driving chip was shown on 2019-04-22, and its own training chip, Dojo, announced on
2021-08-19), so his claims as its chief executive qualify. The three files stay as entered.

What does not change: the frozen panel's membership (A18), `data/statements.csv`, the scored
series, the frozen thresholds, the definition, the verdict and the headline (A25), and every
other rule of the ledger (A27 and my rulings of 2026-10-19 in the method).

## 2026-10-19: two voices of one zeitgeist, and the claims ledger as the industry's voice

### A31. The claims ledger becomes a record of what the industry's leaders predict, beside the academics, not a scorecard

**Decided 2026-10-19 (decided by: me, on the model's recommendation).** The managing session proposed it on three rulings
I gave that day (quoted below); I then agreed the remaining choices, in his words "Agreed on
all", to the master session's recommendations, which took the managing session's recommendation
on what leads the page and its alternative on undated words. The proposal, with its draft
pictures, is `docs/claims-ledger-reframe-proposal-2026-10-19.md`.

Applies to: `docs/claims-ledger-method.md` (the title; "What this ledger is for"; "The rate, and
what stops it being gamed"; "Where it shows"); `docs/methodology-v2.md` (a new section 0, what
the tracker is for); `scripts/site.py` (the claims page, the home page's zeitgeist section,
its claims sentence and the frontier-voices caption, the `claims_ledger` block of
`site/status.json`); `scripts/validate.py`
(three new fields on timing claims, and the undated-words records); `scripts/charts.py` and
`scripts/chart_style.py` (two new figures and the logic they share with the page); a new folder,
`data/claims_undated/`.

Was: the ledger existed to score each figurehead's dated predictions once they came due: how
many came true, how many did not, and which way the misses went. A per-person hit rate was to be
printed once a person's claims had been searched year by year and five were due (amendment A27).
The page led with a table of counts per person, and the home page and the status file gave the
totals. The home page described the panel's builders as having "a product to sell".

My rulings, 2026-10-19, in his words:

- "The goal is not to score people on their success at predicting the future, the goal is to
  track the zeitgeist of what these people are saying to get a feel for what the vanguard of
  the industry is predicting at any given time."
- "The goal is to make a tracker of the Zeitgeist around AGI and the Singularity. We need to
  track both the traditional academics who have been talking about this for decades as well as
  the new industry leaders who are actually making it happen but tend to run way out in front of
  their skis with their predictions. Both of these are valuable for the Zeitgeist though."
- "Sure, we can keep the verdicts as small notes, but they are not the point of the tracker."

And my "Agreed on all", 2026-10-19, to the remaining choices.

Now:

1. **Two voices of one zeitgeist.** The tracker follows the academics and long-time thinkers
   (the frozen panel's members who don't run AI companies and are not tagged as builders, read
   through their coded statements) and the industry's leaders (the claims ledger). The panel's
   builders are in the coded statements too, and the frontier-voices chart draws the two groups
   apart. Both
   are valuable and neither is scored. The site shows what each says now, how far apart they
   are, and how both have moved. The home page and the method say so.
2. **The ledger's purpose** is a dated record of what the industry's leaders say the future
   holds, read for what they predict now and how that has shifted.
3. **The claims page** leads with each leader's latest dated forecast of AGI, superintelligence
   or AI better than people at most things, in their own term, set against the academics; with
   each leader's latest prediction of any kind beside it. The other side is the panel's long-time
   thinkers who don't run AI companies (not tagged as builders and not among the fifteen),
   counted as the leaders are: each person once, at their latest dated guess since 2023, by the
   nearer year it names. The figure draws each of them and their middle year. **Decided by me
   on 2026-10-20 (decided by: me), "(b)":** Daniel Kokotajlo and Leopold Aschenbrenner, who
   worked at OpenAI earlier in their careers, stay among them, and the page says so plainly
   rather than calling the group people who never worked at such a company. The independent
   check of 2026-10-19 had found that the first build pooled 26 guesses from these seven people,
   ten of them from those two; counted once each, their middle year is 2030 whether the two are
   in or out. Then how the leaders' forecasts have moved. Then every
   claim, by person, in date order.
4. **Verdicts are small notes.** Each claim keeps its status and evidence. On the page,
   the status is a small note on the claim saying whether its date has passed and what
   happened. Verdicts appear in no headline, summary, count, chart title or share post. The
   status file keeps the number of claims and people and gains a `now` block, with no verdict
   counts. The downloadable table keeps each claim's status.
5. **No hit rates,** per person or pooled, and no per-person line of counts. The floor of five due claims and the "seed
   only: not a rate" label go with them. The year-by-year search and its "claims traced" row
   stay, as the record that a person's latest forecast is really their latest.
6. **What arrives, on each timing claim and on each capability claim that forecasts AGI or
   beyond,** entered by hand and checked by the validator:
   `arrives` (agi, superintelligence, beyond_people for AI better than people at most or all
   things, or other), `arrives_term` (the person's own term) and `form` (a year, a range, by a
   year, not before a year, or the far tail of a stated chance, which is not drawn). Only
   forecasts of AGI or beyond are drawn. A `not_before` forecast also gives `not_before_year`,
   the first year its words leave open. A range counts by its nearer end when years are
   compared.
7. **Undated words are let in, as words only.** A leader's latest words on when AGI or beyond
   arrives that carry no year or length of time ("AGI is close") are kept in
   `data/claims_undated/`, one file each, from a primary source, quoted and dated by when they
   were said, every search logged. They appear in the "what they say now" section when they are
   newer than the person's latest dated forecast, or the person has none, so that leaders who
   never name a year are not shown as silent. They are never drawn on a chart and never scored.
   A quote runs to 25 words at most; a cut never removes a date; and words that only use another
   body's name for AI are left out.

8. **The frontier-voices chart's builders** (my ruling, 2026-10-19, "Yes", to the master session's
   recommendation). The home page's chart draws as builders everyone with the panel's
   frontier-lab tag and all fifteen industry leaders. It moves Jensen Huang's three dated
   guesses since 2023 to the builders' side; his tag was left off when the panel was frozen
   (A18), and under the two-voices framing he is plainly one of the industry's leaders. The
   frozen tags themselves are not changed. `scripts/charts.py` reads the fifteen from
   `scripts/chart_style.py`. The academics' band on the claims page leaves the fifteen out
   either way.

Unchanged: who is in the ledger (A30), the admission rule for dated claims, the five status words and what
counts as a hit (now used for the notes), the readings I ruled on 2026-10-19, and everything
A27 and A30 say the ledger must never touch (the frozen panel, the coded statements, the scored
series, the thresholds, the definition, the verdict and the headline).

Why: my rulings. A scorecard answers whether a person was right, which says little about
where expectations stand. Read side by side over time, the record of what the academics and the
industry's leaders say is what the tracker exists to follow.

## 2026-10-21: every tip counts, and every person on the panel is searched every week

Decided by: me. On 2026-10-21 I ruled, in my words: "I want a rule that includes everything I find
and gives every other person on the tracker ample search time to find things they have said too
that I otherwise miss." The master session proposed the seven parts below to carry it out, and I
started the work on them. The details of each part (the tag names, the eight-day line, the cost
estimate) were worked out while building and are the model's proposals inside my ruling. The
standing rule in item 4 was proposed the same way, and I accepted it later on 2026-10-21: "Yes,
apply them automatically."

### A32. Every tip counts; the panel is searched weekly

Applies to: A29 (tip intake), `docs/tip-intake.md` decisions 1 and 4, `docs/weekly-reading.md`
("Deferred: the frozen panel's new statements", decision 1), codebook section 9, and the
claims ledger's fields (`docs/claims-ledger-method.md`).

Was: a statement I sent in counted in figures only if the tracker's own fixed searches also found
it. One the searches did not find was tagged `tip_only`, kept in the record, left out of every
figure and share, and listed on this page under "Noted, outside the measured record", until a
later full pass found it. The rule kept my own reading from becoming the sample. The panel itself
was searched only in occasional full passes (2026-09-30, 2026-10-09, 2026-10-17, 2026-10-19), and
part 4 of the weekly reading, which would search it, was deferred.

Now:

1. **Every tip counts at once.** Rows from a tip are ordinary rows in every figure, in the site's
   statement count and on the claims page. They are marked "added from a tip": on the claims page
   beside the claim, and on this page in the list "Added from a tip", which also gives the count
   per person. The `tip_only` tag is retired and the validator refuses it. The step 3 search
   still runs and is logged, because it now measures whether the searches would have found the
   tip: a row whose source they did not find carries `tip; tip_missed`, and is counted like any
   other. A claim from a tip carries `from_tip = true`.
2. **The rows that were `tip_only`.** The nine rows from Nick Bostrom's interview on The Roman
   Forum (`bostrom-2026-02a` to `bostrom-2026-08`, taken in on 2026-10-18) become ordinary tip
   rows, `tip; tip_missed`, counted from 2026-10-21, each with a note that it was left out from
   2026-10-18 to 2026-10-21.
3. **Every person on the panel, every week.** The weekly reading gains part 4: for each of the 37
   panel members and the three ledger-only industry leaders, the three fixed year searches for
   the current year, one search for the past week's news, and their own outlets, every search
   logged in `data/search_log.csv` in the columns a full pass uses. A new statement found is taken
   in by the tip intake steps but is not a tip; a new dated forecast by an industry leader is
   flagged for the claims ledger. The second coding that the agreement test needs is done by a
   separate agent coding the same passages blind, as tip intake does. Full collection landed on
   2026-10-17, which settles the other reason the panel was deferred.
4. **A tip the searches missed improves them for everyone.** The intake says why the searches
   missed it, and if their words did not match, adds one search worded for any person, tested on
   the tip. It goes in `data/added_searches.csv`, and from the next weekly reading it is run for
   every person on the panel, never only the person in the tip, and in every full pass. Searches
   are only ever added, never removed or narrowed. Each is listed on this page under "Searches
   added from tips", with its date and the tip that prompted it, and every run is in the search
   log. **Ruled by me on 2026-10-21, later the same day,** on the master session's proposal of a
   standing rule, in my words: "Yes, apply them automatically." No added search waits for my
   approval, and no amendment is needed for each one; the validator checks every row (worded for
   any person, prompted by a tip, its searches logged).
5. **Freshness on comparisons.** Every chart or headline that compares people states "every
   person here searched for new words through" a date: for each person, the latest day a search
   for the current year's words was logged; the earliest of those across the people compared.
   It is computed from the search log at each build. The weekly reading names anyone not
   searched in the last eight days, and a comparison is not shared while anyone in it is overdue.
6. **Tip spread.** `scripts/panel_status.py` prints, each week, how many statements and claims
   came in by tip, per person, and what share of each person's statements that is, so I can see
   whether my reading tilts the record.
7. **Enforcement.** `scripts/chart_style.py` drops `tip_only()` and `measured()` and gains
   `from_tip()`, `searched_through()` and `freshness()`; `scripts/charts.py` and
   `scripts/site.py` count every row and print the freshness line on the four comparing charts
   and their captions; `scripts/validate.py` knows `tip_missed`, refuses `tip_only`, accepts
   `from_tip` on a claim, and accepts a reading item of part `panel` whose new rows are
   statements. It also checks `data/added_searches.csv` (item 4), which `scripts/site.py` lists on
   this page.

Why: my ruling. The old rule protected the record from my reading by leaving out what I found;
the new one protects it by making sure everyone else is looked for as often as I might look, and
by showing which rows came from me. A tip the searches missed is now evidence about the searches,
and fixing them helps every person on the panel.

Effect on the record: the nine Bostrom rows enter the figures. None of them names a year for
machines matching people at most thinking work, so no chart's numbers move: the frontier-voices
reading and the long-time thinkers' middle year (2030) were computed before and after the change
and are the same. The site's statement count rises by nine. On the first build under this
amendment, every panel member was searched for 2026 words through 2026-09-30, the date of the
first full pass, because 23 of the 37 have not been searched since 2026-10-09 or earlier; the
first weekly part 4, on Monday 2026-10-26, brings that to the week. Nothing scored changes:
statements never score a gauge.

Cost: the reading runs on my Claude plan as a cloud routine, so part 4 spends no API credits.
Were it moved to a script on the API, the estimate is about $9 a week, $40 a month
(`docs/weekly-reading.md`, "Part 4").

## 2026-10-21: robots doing paid work, shown beside the economy part

Decided by: me. On 2026-10-21 I said the Optimus news fits the economy part of the test, in my
words: "I think you are right on the optimus robot news fitting into the economy part of the AGI
Zeitgeist tracker and perhaps there is a news article worth writing there to explain why and how we
are integrating it." The model drafted the amendment below and the news post that explains it, and
I approved both as written later the same day: "The optimus essay is ready to publish." The details
(the three kinds of row, the first series, the validator check) are the model's proposals inside my
approval. The two open questions at the end were not ruled.

### A33. Machines doing paid physical work are shown beside part D, not scored

Applies to: `docs/singularity-entry-definition.md` (leg D, by a note only),
`data/world_measures.csv` (new context rows), and the economy part of the home page.

Was: part D (the economy) showed one series, the World Bank's yearly world output growth, and
nothing else. Robots appeared on the site only as dated promises in the claims ledger.

Now:

1. **The score does not change.** Part D is still scored on world real output growth alone,
   against the line of 30 percent a year. The frozen thresholds
   (`docs/singularity-entry-thresholds.json`) and the definition's rules are untouched; the definition gains
   only a dated note pointing here. No robot figure
   enters the gauge, the progress number or the headline.
2. **A table beside part D** shows measured evidence that machines are doing paid physical work.
   These are rows in `data/world_measures.csv`, marked as context for leg D and never scored, the
   same footing part C gives company code figures (Anthropic's figure of more than 80 percent,
   shown and not scored since 2026-10-21). Each row says which of three kinds it is:
   - `outside`: a count made by someone other than the maker, such as a trade body's census, a
     government survey or a regulator's register;
   - `customer`: a customer's own published figures for work done by robots in its operations
     (hours, tasks, units handled), in an annual report or a filing;
   - `maker`: a maker's own count of robots built, shipped, or working for paying customers. It
     is marked as the company's word about itself.
3. **What is not a row:** a statement that production has begun with no number, a target or
   capacity rate, a demonstration or video, a forecast. When a figurehead on the ledger's list
   makes a dated promise of this kind, it goes to the claims ledger under its own rules. Otherwise
   it is left out.
4. **What "paid physical work" covers:** machines doing physical tasks in the world for a
   customer or employer, without a person steering them in real time: humanoid and other
   general-purpose robots, factory and warehouse robots, and driverless vehicles carrying paying
   passengers or goods. The first series is the International Federation of Robotics' yearly count of industrial robots
   installed (542,000 in 2024, from its
   [press release of 2025-09-25](https://ifr.org/ifr-press-releases/news/global-robot-demand-in-factories-doubles-over-10-years)),
   entered 2026-10-21 with its count of industrial robots in use; a humanoid row is added when someone other than a maker counts humanoids.
5. **Every row carries** its source address, the date of the figure, who measured it, and the
   kind (item 2). The validator gains a check that a leg D context row names its kind and is
   never read by the scoring code.

Why: my words above. Most of the economy is physical work, so if part D ever moves, machines
doing that work are among the likeliest causes, and the first signs would show in counts of robots
at work years before world output. Showing those counts beside the score lets a reader watch for
the cause without letting a company announcement move the test. Scoring them would mean changing
the frozen test, which this amendment does not do.

What it costs: one more table to keep up. There is a yearly read of the trade body's count, and
a check for new outside counts during the weekly reading. Most weeks will add nothing, because most
robot news is announcements, which item 3 keeps out of the table.

Not decided here, and left for me:
- whether driverless vehicles belong in this table or wait for a ruling of their own (they have
  the best outside counts, from regulators, but they are a large field);
- whether the weekly reading should search for these rows, or a yearly pass is enough.

## 2026-10-24: the "now" rule covers statements that point to evidence, and video interviews are searched

Decided by: me, on the model's recommendation. Both came out of the intake of Sam Altman's
interview with Matthew Berman (pull request 42, merged 2026-10-23). The intake flagged two things
for me: that A26, read literally, would sample out two of his statements about today's systems
because they were coded as the stronger form (search log `altman-123`), and that a trial search of
YouTube found at least eight of his 2026 video interviews with no row in the record (search log
`altman-120`). On 2026-10-24 the master session put both to me as recommendations and I answered
"agreed".

### A34. A26 protects statements coded "claimed or demonstrated"

Applies to: A26, methodology version 2 section 3 ("Collection"), the busy-year line of
`docs/methodology.md`, and step 4 of `docs/tip-intake.md`.

Was (A26): in a busy year, all timeline-bearing statements are kept, and so are all statements
that bear on the "now" question, meaning any whose `frame_primary` or `frames_present` includes
`self_improvement`, or whose `present_capability` is coded `claimed`; the rest are sampled at a
fixed interval, logged.

Now: the same, with `present_capability` coded `claimed` **or `demonstrated`**. A statement in
which the speaker says a capability exists today is kept whether or not they point to evidence
for it.

Why: the codebook (section 4) has two codes for "it exists now": `claimed`, when the speaker says
so without pointing to evidence, and `demonstrated`, when they point to it. A26 named only the
first. Its stated purpose is to keep the "now" question whole, and the stronger form of the claim
is the one that question most needs. Read literally, A26 would have sampled out two of Altman's
statements of 2026-10-21: that AI is "now ... figuring out very complicated, important new
knowledge" (`altman-2026-05`), and that OpenAI's maths results are beyond "any model currently
widely available" (`altman-2026-10`). The intake kept them on the reading that A26 meant both
codes, and flagged that reading for me.

Effect on the record: the two Altman rows stay as they are, now under the rule as written rather
than a reading of it. A34 by itself changes nothing in the every-third count of 2026-10-23
(`altman-123`); the count was redone the same day for the rows A35's first run added (below). The other busy years were sampled before this change (search log `lecun-133`,
`sutskever-153`, `hassabis-words-12`; Amodei 2026 and Hassabis 2025 and 2026 left nothing out).
Read by the model against the words quoted in those records, none of the eight passages left out
there says a capability exists today and points to it, so none comes back. The codes those
passages were given are not kept in the repository, so this is a reading of the quotes, not a
check of codes. Nothing scored changes: statements never score a gauge.

### A35. A standing video search, V1, joins the fixed searches

Applies to: the fixed query set (`docs/methodology.md`, "Fixed query set for each panel member";
methodology version 2 section 3), part 4 of the weekly reading (`docs/weekly-reading.md` and
`docs/weekly-reading-prompt.md`), step 3 of `docs/tip-intake.md`, and `scripts/validate.py`.

Was: each person is searched with three discovery queries (D1 to D3), three queries for each
year (Y1 to Y3), their own outlets, and, since A32, any search added because the searches missed
a tip (`data/added_searches.csv`). None of them looks at video pages on purpose. The three year
queries are worded for articles that say "AGI", "human-level" or "superintelligence", so an hour
of someone talking on camera is found only if a written report of it uses those words.

Now:

1. **The search.** V1 is `"<name>" interview <year>`, limited to youtube.com (the search tool's
   domain filter, or `site:youtube.com` where the tool has none). It is part of the fixed set,
   beside Y1 to Y3.
2. **When it runs.** For every person on the panel and the three ledger-only industry leaders:
   every week in part 4 of the weekly reading, for the current year, from the reading of
   2026-10-26; at every full pass, for every year the pass covers; and at step 3 of every tip
   intake. Every run is logged in `data/search_log.csv` like any other search, with "V1" named in
   `what_found`. The first weekly run covers 2026 for everyone. Earlier years are searched at each
   person's next full pass, not all at once now.
3. **What counts from it.** A result counts only if the person is heard speaking in the
   recording, and the channel is the person's own, the host's or outlet's, the event organiser's,
   or a news channel carrying the event whole. A channel that narrates over clips or re-cuts them
   is a report of the interview, not the interview: it is logged, and used only to find the
   original. Everything else is the existing rules: the statements are found, coded and
   double-coded as the collection does (tip intake steps 1, 2, 4 and 5); quotes are checked by two
   automatic transcripts from separate programs (A29 item 4), or carry `asr_unverified`; the
   transcripts are archived with a checksum in `sources/manifest.csv` and kept out of the
   repository; and the busy-year rule (A26, as reworded by A34) applies to the person's year as a
   whole. A row V1 finds is not a tip: the rule's own search found it.
4. **Not an added search.** V1 is not a row of `data/added_searches.csv`. That file holds searches
   added because the searches missed a tip, each tested on the tip it missed (A32 item 4). V1
   did not find the tip that prompted it, so it comes in by this amendment instead. The validator
   reserves the name, as it does D1 to D3 and Y1 to Y3.

Why: leading voices now speak mostly in long recorded interviews (the reason given in A29), and
the searches were built for articles. Run once as a trial on 2026-10-23, a YouTube search for
Altman's 2026 interviews listed at least eight with no row in the record (`altman-120`). The gap
is in how videos are searched, not in any one person, so the fix is a search for everyone.

What it costs: one more search per person per week, about 40 searches, and the reading time of
whatever it finds, which is most of the cost, since an interview is up to an hour of transcript.
The weekly reading runs on my Claude plan, so it spends no API credits. Making the second
transcript runs on this Mac and costs nothing.

Effect on the record, from the first run (Altman, 2026, search log `altman-125` to `altman-136`):
ten results; six are 2026 recordings of Altman speaking on a channel that counts, and all six were
read in full (The Indian Express, 2026-02-20; BlackRock's infrastructure summit, 2026-03-11; the
OpenAI Forum, 2026-04-07; TIME, 2026-09-01; the G20 meeting with Howard Lutnick, 2026-09-02;
Dreamforce, 2026-09-16). Two results are clip or commentary channels; the original behind one of
them, a podcast with David Senra, could not be found, so nothing from it is recorded. One result,
from December 2025, looks like the original of a 2025 row now held only secondhand, and is left for
his next full pass. The six videos give 73 coded rows; with Altman's 2026 now far past the busy-year
line, every row with a timeline or on the "now" question is kept and the rest are sampled, so 58
of them join the record (`altman-2026-14` to `altman-2026-71`), each quote checked against a second
transcript and each row coded a second time, blind. Redoing the every-third count over the whole year changes two rows from the
interview of 2026-10-21: the passages on coders (04:01, `altman-2026-07`) and on cures bought with
human agency (42:44, `altman-2026-12`) are left out, and the passage on the gap between the most
competitive people and everyone else (19:00, now `altman-2026-72`) comes in. That follows the
written rule, every third by date across the year. The other reading was to carry on the count of
2026-10-23 so that rows already published stay. On 2026-10-24 the master session put the choice to
me and I answered "Yes" to the written rule: the two rows are sampled out, as the search log
records (`altman-136`), and they stay out of the record like any other passage the count leaves
out.

None of the new rows names a year for machines matching people at most thinking work, so the
frontier-voices reading is the same before and after (builders 2029.5, everyone else 2032.75), and
the site's statement count rises by 57. Nothing scored changes: statements never score a gauge.

## 2026-10-27: the source-overlap rule is shown beside the pace part

Decided by: me, on a reader's suggestion. On 2026-10-25 a reader on
[r/SentientHorizons](https://www.reddit.com/r/SentientHorizons/), commenting on my post there
about this site, suggested that the rule for replacing the pace part's source should be printed
on the page next to that part now, before any replacement is chosen, so that a reader sees in
advance that a new source must run alongside the old one before it counts, and so that the
switch, when it comes, cannot read as moving the goalposts after the fact. I accepted the
suggestion on 2026-10-27.

### A36. The successor rule is printed beside part A

Status: wording only. No rule changes, no frozen value changes, and nothing scored changes.
`docs/singularity-entry-thresholds.json` is untouched, and the successor rule of A19 (a
replacement measure named before the series stops, the overlap period published, the switch an
amendment) stands exactly as written in `docs/singularity-entry-definition.md`, section 2.

Was: the home page's paragraph on part A ended by saying that METR's series had stopped updating,
that the rules call for a replacement with an overlap, and that the question was open (A24).

Now: the same paragraph says, in two sentences, that the question of a replacement is open (A24),
and that if the source is replaced, the replacement has to run alongside the old one, with the
overlap published, before it counts, with the switch recorded here; and it links the successor
rule where it is written in full, noting that the rule was set down before the series stopped.

Why: the rule already existed, but a reader had to open the working document to find it. The
point of fixing a rule in advance is lost if it is only visible after it is used. Printing it
beside the part it governs, before any replacement is proposed, lets a reader check the switch
against the rule when it comes. Credit for the suggestion goes to the reader on Reddit.
