# Trace report: schmidhuber (Jürgen Schmidhuber, core tier)

The coordinator told me to stop early because the laptop was overloaded. I stopped at a clean point.

1. **Summary.** Years covered: 2005 to 2026. All three year searches were run and logged for every one of the 22 years, plus the three discovery searches. 34 statement rows (31 distinct statements; three were split one row per capability). 4 rows are secondhand: 2016-08, 2017-03, 2017-08a/b and 2017-09 (one TelecomTV talk report), and 2023-01. 126 search-log rows, including 11 quiet-year rows: 2005, 2008, 2009, 2010, 2013, 2014, 2015, 2019, 2021, 2022 and 2025. No year needed busy-year sampling: 2017 has the most, at 10 statements, which is not more than ten. About 73 web searches were used. There are no incidental rows.

2. **Partly done work and leads not read.** The year searches are complete. The follow-up work is not: these leads are still open.
   - **Could not be read:**
     - Reddit AMA, 2015 (thread 2xcyrl). Reddit blocked it, the mirrors were down, Arctic Shift returned error 522 and archive.org returned 429. This is the main gap for 2015.
     - Lex Fridman podcast, 2018-12-23. There is no transcript.
     - Big Technology Podcast, 2026-07 (podscripts.co). The connection was refused.
     - TED talk, 2024-10 (ted.com/talks/juergen_schmidhuber_why_2042_will_be_a_big_year_for_ai). The site did not serve the transcript.
     - Bloomberg, 2018-05-15. A robot check blocked it.
     - Blick (blick.ch). The site returned a block page.
     - Machine Learning Street Talk, 2025-01-16, and Europe on Edge, 2026-09-08. Neither has a transcript.
   - **Found but never fetched:**
     - Axios, 2017-12-15.
     - Singularity Summit talk video, 2009 (youtube Ipomu0MLFaI), and the New Atlantis write-up of it.
     - UCSD talk abstract, 2013-07-26.
     - AGI-10 paper, 2010.
     - TEDx videos.
     - His X account, @SchmidhuberAI. No own social posts were checked at all.
     - Event listings: FIAS 2026-03-23, ai4i Turin 2026-03-30, ICLR 2026 workshop, 4YFN 2025.
     - Sakana AI recursive self-improvement lab announcement.
     - inverse.com article 25521.
     - clubic.com and goethe.de articles.
     - LMU talk, 2023-07-14.
     - The 2012 update in Singularity Hypotheses (people.idsia.ch/~juergen/newmillenniumai2012.pdf).
     - CNBC, 2018-05-16.
     - Unsupervised Learning podcast, episode 90.
   - **Quiet years most likely to change:** 2015 (if the AMA can be read), 2009 and 2010 (talks), and 2025 to 2026 (podcasts).

3. **Places where the method said nothing, and what I did.**
   - **One row per capability on each occasion.** When the same capability came up more than once in one interview, I kept the most timeline-bearing passage and noted the others. Examples: the second "far cleverer than us" line in Computerwoche 2016, and the 2041 cortex-size hardware line in BCG.
   - **Reporter paraphrase in an interview the reporter did:** NYT 2016 (2016-08) and Guardian 2023 (2023-01). The brief would call these primary interviews, but the codebook says a paraphrase is secondhand. I tagged them secondhand, kept elicitation as interview, and set coding_confidence to low.
   - **Talk lines quoted inside an interview article** (Guardian 2017-03) and **outlet reports of a keynote** (TelecomTV 2017): tagged secondhand, following the precedent of lecun-2026-03.
   - **Non-English quotes** (Le Temps in French, Computerwoche in German, swissinfo in French) are kept in the original language, with a plain translation in the notes.
   - **PDF line-break hyphens.** I removed them from quotes taken from arXiv and journal PDFs, and said so in the notes.
   - **The Omega point or historic singularity** (2006-01, 2007-02) is coded as superintelligence, marked ambiguous.
   - **Animal-level AI claims** (crow, capuchin monkey) are not a target capability, so I did not record them.
   - **Interviews published later than the conversation:** I used month precision. Examples: Guardian 2017, BCG 2017, PAP 2017, Futurism 2018, Jazzyear 2024.
   - **"High" as an answer to a probability question** (LessWrong 2011) is coded accepts, with timeline_prob left blank.
   - **"Good hope"** (Le Temps 2020) is coded uncertain, marked ambiguous.
   - **Dates I settled:** the NYT 2016 date conflict is explained (the syndicated copy is dated 2016-12-08; the original URL path gives 2016-11-27). The Le Temps "machines superintelligentes" interview turned up in the 2023 and 2024 searches but is dated 2016-03-03, so it is recorded under 2016.
   - **Start year.** For the core tier the start year is fixed at 2005, but I logged one "start year" row anyway.

4. **Quick checks** (the source opens and the quote is on the page):
   - **schmidhuber-2017-10:** https://scienceinpoland.pl/en/node/27249. Quote: "I would be very surprised if artificial intelligence does not become more intelligent than we are within a few decades".
   - **schmidhuber-2011-01:** the greaterwrong.com Q&A. Quote: "High for the next few decades".
   - **schmidhuber-2016-04:** https://www.infoq.com/articles/interview-schmidhuber-deep-learning/. Quote: "a few years or decades later we may have human-level AI".

5. **Checker result:** `OK: speakers.csv 50, statements.csv 193, aggregates.csv 200, world_measures.csv 97, events.csv 31, search_log.csv 891`. It printed no PROBLEM lines (schmidhuber: 34 statements, 126 search rows, 0 incidental rows).

Files are in the staging folder: statements.csv, search_log.csv, report.md, build.py (rebuilds both CSVs and checks every quote against the saved source text), and dl/ (the saved source pages).
