# Public track review: GPT-6 Astra Medium

Received 2026-09-30 (Pacific). Prompt: `docs/reviews/public-track-review-prompt.md`. Reply saved verbatim below; reconciliation goes in `docs/amendments.md`, not here. Links are as the model supplied them and have not yet been checked.

---

**I would redesign this before collecting.** The project can support a strong history of AGI discourse alongside a more limited history of public beliefs. Its present structure would make it too easy to interpret changes in attention, vocabulary, community membership, and editorial selection as changes in opinion.

The largest problem is the headline's phrase **"the central public question."** You need an observable definition of *central*, a specified public, and a sampling frame that allows other questions to win.

**1. What each layer can actually measure**

| Layer | Defensible interpretation | Main failure | Recommended change |
|---|---|---|---|
| Attention | Relative visibility within a particular medium | Searches, page views, books, and news counts have different denominators. None establishes agreement or belief. | Keep separate series, normalized within each source. Avoid a composite "public acceptance" index. |
| Forums | Expressed discourse among participating accounts | Participation changes over time; prolific users dominate; specialist communities select for interest in advanced AI. | Report community-specific trends, with separate comment-, thread-, and account-weighted analyses. |
| Polls | Responses to specified questions in specified populations | General AI concern, AGI feasibility, and expectations about automation are different constructs. Prompted answers provide limited evidence of spontaneous salience. | Make matched survey questions the backbone of claims about population beliefs. |
| Mainstream argument | Published editorial framing | Editors and contributors select the arguments. Op-eds cannot establish what readers believe. | Treat this as an editorial agenda series; separately code news reporting and quoted speakers. |
| Vocabulary ledger | Recorded lexical diffusion within bounded corpora | Earliest retrieved occurrence depends on coverage, indexing, spelling, and archive survival. | Record "earliest verified occurrence in this corpus," with explicit coverage limits. |

Three failures cut across all five layers.

First, **AI, AGI, superintelligence, conversational competence, and recursive self-improvement require separate target codes**. Someone can believe current systems write useful software, doubt that they possess general intelligence, and expect transformative automation. Your scheme must preserve that combination.

Second, **"dismissive through resigned" is not a defensible ordinal scale**. Dismissal describes a judgment or rhetorical posture; resignation combines expectation with emotion and perceived agency. A person expecting imminent AGI could be enthusiastic, terrified, resigned, or politically mobilized. Separate those dimensions.

Third, **silence is missing information**. An article about regulation does not establish that its author accepts AGI's feasibility. A commenter asking about timelines might be entertaining a hypothetical. Require explicit endorsement before assigning a belief.

Your named expert panel has an analogous problem: it measures the public statements of selected people. Choosing today's prominent thinkers retrospectively can select for people whose arguments survived or became fashionable. Define eligibility independently of their eventual positions, retain quiet years, and distinguish within-person changes from changes in who is speaking.

**2. What I would keep, demote, drop, and add**

I would prioritize repeated polls, a small audited media corpus, and probability samples from clearly labeled specialist communities. Five overlapping attention sources will add less value than careful validation of those three components.

Specific source decisions:

- **Wikipedia: keep as attention context.** The modern pageviews series begins in July 2015; legacy raw counts extend to December 2007. The legacy data have different counting and bot/mobile coverage characteristics. Mark the measurement break, document titles and redirects, and leave 2005–2007 unavailable. [Meta-Wiki](https://meta.wikimedia.org/wiki/Research%3ATimeline_of_Wikimedia_analytics)
- **Google Trends: keep, with reproducibility limits.** Google describes sampled, normalized search data, scaled to 0–100. Preserve geography, query/topic choice, category, time window, download date, and exports. Early zeros can reflect insufficient volume. Repeated pulls need not yield identical estimates. [Trends Help](https://support.google.com/trends/answer/4365533?hl=en)
- **Google Books Ngram: demote to the vocabulary appendix.** It measures text frequency in a book corpus, without weighting for readership. Google also excludes n-grams occurring in fewer than 40 books, which makes it unsuitable for establishing first appearances. Preserve corpus version and use unsmoothed values for timing claims. [books.google.com](https://books.google.com/ngrams/info)
- **GDELT: make optional.** "GDELT coverage since 2015" does not specify a reproducible full-text counting method. Its datasets and search APIs have different coverage and capabilities. Require a successful historical retrieval pilot for your exact query and denominator before committing. [gdeltproject.org](https://gdeltproject.org/data.html)
- **Media Cloud: keep conditionally.** Its current documentation says searchable dates change as historical data are ingested. A fixed outlet list therefore does not ensure fixed historical coverage. Audit outlet-by-month coverage before interpreting counts. [mediacloud.org](https://www.mediacloud.org/documentation/search-tool-guide)
- **NYT: keep as one outlet series.** The Archive API supplies monthly article metadata going back to 1851. Metadata availability and access to the text needed for coding are separate requirements. Label headline/abstract searches accordingly. [GitHub](https://github.com/NYTimes/public_api_specs/blob/master/archive_api/archive_api.json)
- **Reddit, HN, LessWrong: keep as specialist discourse.** Analyze them separately. Their agreement would not constitute three independent samples of the public.
- **Drop "full archives" as an assumption.** Establish what each archive actually captured and what remains retrievable.

The strongest additions I found are these:

| Addition | What it contributes | Boundary |
|---|---|---|
| **Pew/Smithsonian, 2010** | An early population-level expectation about humanlike machine conversation | A specific capability forecast |
| **Pew/Smithsonian, 2014** | Expectations about computer-generated art and other technologies | Broader technology expectations |
| **Eurobarometer 382, fielded 2012** | Multicountry survey data reaching beyond English-speaking technical communities | Attitudes toward robots |
| **Guardian Open Platform** | A documented archive extending back to 1999 | Another editorial institution |
| **Slashdot** | Publicly accessible technical discussion during the early period | Adds historical depth with similar demographic selection |
| **GovAI's 2018 U.S. survey** | Explicit high-level machine intelligence expectations and governance attitudes | One survey instrument and population |

The 2010 Pew result is especially relevant: **81% expected that by 2050 a computer would probably or definitely converse indistinguishably from a human**. That establishes substantial early acceptance of one ambitious capability and makes a blanket "the public was still asking whether it was possible" framing harder to sustain. [Pew Research Center](https://www.pewresearch.org/politics/2010/06/22/section-1-science-technology-and-the-environment/)

In 2014, 51% expected human-indistinguishable computer-created art within 50 years. Eurobarometer's 2012 robotics survey has publicly documented data and questionnaires. Keep both as adjacent constructs with their own labels. [Pew Research Center](https://www.pewresearch.org/internet/2014/04/17/us-views-of-technology-and-the-future/)

The Guardian documents archive coverage from 1999. Slashdot has surviving 2005 discussions of Kurzweil and the singularity, although complete historical sampling would still require an archive audit. [Open Platform](https://open-platform.theguardian.com/)

For demographic and geographic breadth, **put resources into national surveys and country-specific analysis**. Ipsos is useful, but its methodology notes that samples in several countries are more urban, educated, or affluent than the population. A multinational online survey cannot automatically support a world-population estimate. [ipsos.com](https://www.ipsos.com/sites/default/files/ct/publication/documents/2025-06/Ipsos-AI-Monitor-2025.pdf)

Adding translated media corpora can broaden the history of discourse. It requires locally validated terminology, language-specific coding checks, and separate country results. Another forum alone will do little to solve population representativeness.

I found useful early anchors, but this review did not establish a continuous, comparable public-AGI survey series for 2005–2015. Preserve those gaps.

**3. A better basis for comparing public and expert opinion**

Use **matched propositions with separate dimensions**. A shared coding manual helps, but it cannot make an unsolicited essay equivalent to a prompted survey response.

For each statement or survey item, record:

| Dimension | Example |
|---|---|
| Target capability | Conversational imitation; broad economically useful competence; autonomous AI research |
| Proposition | "Systems meeting definition X will exist by year Y" |
| Endorsement | Accepts; rejects; uncertain; conditional; unexpressed |
| Probability and horizon | Explicit probability, date or interval, and original wording |
| Present capability | Already demonstrated; claimed; disputed; hypothetical |
| Expected consequences | Beneficial, harmful, mixed, unspecified |
| Affect and agency | Excitement, fear, resignation; perceived ability to influence outcomes |
| Elicitation | Unprompted statement, interview question, survey prompt, quotation |

For self-improvement, distinguish at least:

- Helping humans develop AI.
- Autonomously conducting parts of AI research.
- Modifying a system's own code or weights.
- Sustaining successive improvements with reduced human involvement.

Those propositions can receive different answers from the same person.

If you want a numerical common axis, **probability of a specified capability by a specified horizon** is the strongest candidate. Use it only where the source supports it. "AGI soon" cannot responsibly become a numerical forecast, and accepting eventual possibility does not imply a probability above 50% within ten years.

Pew's 2025 public/expert comparison is an excellent methodological anchor. It surveyed 5,410 U.S. adults and 1,013 U.S. AI experts during 2024, with parallel questions. Pew explicitly limits the expert findings to respondents, whose responses were unweighted. Date your observations by fieldwork, preserving publication date separately. [Pew Research Center](https://www.pewresearch.org/internet/2025/04/03/how-the-us-public-and-ai-experts-view-artificial-intelligence/)

For historical text, compare **shares of sampled statements explicitly endorsing matched propositions**. For surveys, compare **shares of respondents**. Put these in adjacent panels with their units visible.

**4. The strongest objection to the headline, and a fair test**

A skeptical reader's strongest objection would be:

> Your chronology may be produced by changing vocabulary, changing participants, and a retrospective category scheme. The sources may show a specialist conversation becoming more visible while the broader public continues to care about employment, reliability, control, and everyday consequences.

There are already reasons to take that objection seriously.

The early Pew findings complicate the feasibility era. Recursive self-improvement also appears in Yudkowsky's 2008 discussion of AI risk. That establishes an earlier intellectual lineage; its historical prevalence still needs measurement. [intelligence.org](https://intelligence.org/files/AIPosNegFactor.pdf)

Monmouth supplies a particularly useful mixed result: several impact attitudes were largely stable between 2015 and 2023, while concern about a possible threat to humanity's existence increased from 44% to 55%. Your method should be able to preserve that combination of continuity and movement. [Monmouth University](https://www.monmouth.edu/polling-institute/reports/monmouthpoll_US_021523/)

To test the headline fairly:

1. **Specify the population.** For example, U.S. adults, selected national media, or participants in named forums. Report each separately.
2. **Define "central."** Largest share of articles? Largest share of primary questions? Most commonly volunteered concern? These require different evidence.
3. **Allow competing questions to win.** Include jobs, reliability, privacy, bias, ownership, regulation, military uses, consciousness, and "other." Sample broadly enough to retrieve them.
4. **Keep all your proposed categories available in every year.** Code question presence separately from the answer given.
5. **Estimate timing without forcing your preferred breaks.** Compare the proposed eras against stable mixtures, gradual trends, and alternative break dates.
6. **Test stable-source and stable-participant subsets.** A within-account analysis helps distinguish changed speech from membership turnover, while requiring its own attrition caveat.
7. **Preregister a failure condition.** For example: the proposed leading question must rank first within each claimed period under the primary sampling weights, and the ordering must survive specified sensitivity analyses.

Evidence capable of supporting the **population** claim would include repeated comparable surveys measuring question priority, preferably with unprompted responses. Agreement across media and forums could support a claim about public discourse. It would leave population-level salience uncertain where survey evidence is absent.

Also separate your two proposed post-2023 developments. "What should we do about demonstrated capabilities?" is much broader than "Can systems already improve themselves?" Success for the first does not establish the second.

**5. Existing work worth building on**

These are the highest-value starting points:

- **Fast and Horvitz, "Long-Term Trends in the Public Perception of Artificial Intelligence" (2017).** Direct precedent for longitudinal NYT analysis, covering 1986–2016. Build on its categories and findings, while keeping the measured object, newspaper discourse, explicit. [ojs.aaai.org](https://ojs.aaai.org/index.php/AAAI/article/view/10635)
- **Zhang and Dafoe, *Artificial Intelligence: American Attitudes and Trends* (2019; fieldwork 2018).** Includes a defined high-level machine intelligence question, timelines, governance, and demographic differences. Its preregistration and instrument are particularly useful. [governanceai.github.io](https://governanceai.github.io/US-Public-Opinion-Report-Jan-2019/)
- **Pew's 2025 public/expert comparison.** The clearest bridge for your comparability problem. [Pew Research Center](https://www.pewresearch.org/internet/2025/04/03/how-the-us-public-and-ai-experts-view-artificial-intelligence/)
- **AI Impacts' Expert Survey on Progress in AI series.** The 2016, 2022, and 2023 surveys contain largely repeated questions. They provide a benchmark alongside your named panel; inspect question framing and respondent composition before interpreting differences. [wiki.aiimpacts.org](https://wiki.aiimpacts.org/ai_timelines/predictions_of_human-level_ai_timelines/ai_timeline_surveys/2023_expert_survey_on_progress_in_ai)
- **Eurobarometer robotics surveys and Gnambs and Appel's "Are robots becoming unpopular?"** Existing cross-national work using 2012, 2014, and 2017 waves. Useful for broader technology attitudes and longitudinal survey practice. [gesis.org](https://www.gesis.org/en/eurobarometer-data-service/data-and-documentation/standard-special-eb/study-overview/eurobarometer-771-za-5597-feb-mar-2012)
- **Gaffney and Matias, "Caveat Emptor, Computational Social Science" (2018).** Documents missingness in an earlier widely used Reddit corpus. It supplies reasons to audit coverage, without establishing the missingness of your particular Arctic Shift extract. [arxiv.org](https://arxiv.org/abs/1803.05046)

**6. Your sampling rules need substantial changes**

**Twenty top-scoring posts per quarter selects for rewarded visibility.** It can describe what each community promoted. It cannot estimate the distribution of expressed views across all posts or participants. Scores also reward humor, outrage, timing, and format, and historical scores may have been captured at different ages.

There is a concrete archive issue here: Arctic Shift documents a collection change beginning in November 2023, when content was retrieved again after 36 hours and score-related fields were updated. Your proposed period boundary overlaps a change in measurement. [GitHub](https://github.com/ArthurHeitmann/arctic_shift/blob/master/file_content_explanations.md)

Keep the top-20 series as a separate "highly rewarded discourse" sample. For prevalence, draw a reproducible random sample within community and quarter, retain inclusion probabilities, and sample comments independently of post popularity. Report account concentration and sensitivity to prolific contributors.

**Fifteen op-eds per year is enough for illustrative close reading, with weak precision for annual proportions.** Even under simple random sampling, a proportion near 50% with n=15 has an approximate 95% margin of error of ±25 percentage points. Clustering by author, event, and outlet further complicates uncertainty.

Choose sample size from the smallest change you want to distinguish. Stratify by outlet and period; enumerate the eligible frame before drawing. If sparse years contain fewer eligible pieces, take the census. Keep news and opinion genres identifiable, and distinguish the author's stance from quoted claims.

**A frozen vocabulary prevents one kind of discretion while preserving another.** A list chosen today can systematically miss earlier expressions such as "thinking machines," "strong AI," "human-level intelligence," and "intelligence explosion." Generic terms such as "alignment," "doom," and "timelines" require contextual disambiguation.

Use a broad retrieval vocabulary developed on a pilot spanning the entire period. Freeze its version before the main analysis, validate precision and recall separately by era, and maintain a held-out sample for checking omissions. Any later vocabulary revision should trigger a rerun across all years.

**The 1% threshold needs denominator and persistence rules.** One thread can drive a crossing in a small month. Publish numerator, denominator, distinct-account count, and single-thread concentration. Predefine minimum volume and a persistence rule. Treat alternative thresholds as sensitivity checks.

Finally, double-code a stratified subset, hide dates and identities where practical, and publish disagreements and category-specific reliability. Preserve "ambiguous" and "unexpressed" codes. If automated coding is used, validate it separately across eras and sources.

For reproducibility, publish the sampling frames, queries, code, random seeds, source versions, retrieval dates, document IDs, exclusions, and missingness audits. State whether a reader can reproduce an aggregate from public tables or needs accessible microdata. A working URL today does not guarantee an identical future retrieval; preserve permissible snapshots and checksums.

**My recommendation is to preregister three distinct outcomes: population beliefs, published argument, and specialist discourse.** Let the headline emerge from their agreement or divergence. That structure gives the project room to discover something more informative than a single sequence of eras.
