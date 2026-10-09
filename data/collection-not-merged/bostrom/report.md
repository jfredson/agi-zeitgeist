# Bostrom trace: report (stopped early at the coordinator's request)

1. Speaker id `bostrom`. 17 statements recorded, 1 of them secondhand (`bostrom-2015-02`, New Yorker). 120 search-log rows: 63 web searches (the 3 discovery searches plus all three year searches for every year 2005 to 2024), follow-ups, own-outlet checks, and 10 quiet-year rows (2006, 2007, 2010, 2011, 2017, 2019, 2020, 2021, 2022, 2024). No year had more than ten statements, so no sampling was needed.
   - Years 2005 to 2024 are fully searched (all three year searches logged).
   - Years 2025 and 2026 were not started: none of their year searches were run, so they have no quiet-year rows. The 2026 working paper (`bostrom-2026-01`) was recorded from the check of his own site, not from a year search.

2. Unfinished leads and sources I could not read, for a later session:
   - 2025 and 2026 year searches. Known leads: the Evening Standard interview (2025, reported by Futurism 2025-09-09, https://futurism.com/simulation-theory-ai-warning); Joe Rogan Experience #2525 (2026-07-14; only a summary page found in panel verification); the LessWrong linkpost of "Optimal Timing" (https://www.greaterwrong.com/posts/ZeNRKhGFAhGB8WJ7s/nick-bostrom-optimal-timing-for-superintelligence), which I did not open.
   - 2024 leads not followed up: Perfil interview, 2024-12-15, in Spanish (https://www.perfil.com/noticias/periodismopuro/nick-bolstrom-leer-este-reportaje-es-fundamental-para-ver-el-mundo-de-nuestras-proximas-generaciones-por-jorge-fontevecchia.phtml); Forbes Q&A, 2024-06-24 (https://www.forbes.com/sites/pialauritzen/2024/06/24/qa-with-nick-bostrom-who-is-in-charge-of-the-big-picture-questions/), where the fetch returned nothing usable; the Impact Theory (Tom Bilyeu) interview about degrees "because AGI is coming soon", found only in a Chinese translation (https://hub.baai.ac.cn/view/39164). For the Wired interview of 2024-05-02 (https://www.wired.com/story/nick-bostrom-fear-ai-fix-everything/) I only scanned the page text for timing and capability words; it needs a full read.
   - Could not read: the FT profile of July 2016 (the copy on the FHI site is gone and web.archive.org refused both fetch tools); the Lex Fridman Podcast #83 transcript (404); TED-adjacent videos with no transcript (2013 AGI-12 talk on IEET, 2014 Harvard talk on FLI, 2017 Marketplace, 2018 TWIML #181, 2020 Doha Debates); the China Daily page of 2017-04-05.
   - Not looked for: the 2023 New York Times interview about AI sentience (no search turned it up); the full text of the books Superintelligence (2014) and Deep Utopia (2024), for which I found no legitimately hosted copy.

3. Places where the method was silent, and what I did:
   - One row per source or occasion, even when the source answers the questions in more than one place (postscripts, the Edge essay, the TED talk, interviews). Other qualifying passages are quoted in the row's notes, as the trial rows do. The only split is the TED talk (`2015-01a`/`b`), where one passage makes two distinct claims (A15 ruling 13).
   - Survey figures he reports ("By 2050 we may ... have a 50/50 chance", CNN `2014-02`; "by mid-century", Oxford Martin `2014-04`) are coded in the timeline fields, with the hedge in timeline_text and a note that the figure is the survey's.
   - "Less than a 50% probability ... by 2033" (`2008-01`): coded uncertain with qualitative timing and the year 2033 filled in. timeline_prob is blank because he gave no number.
   - "In this century" was turned into a horizon year of 2100, marked `computed:` (`2014-03`, `2015-01a`, `2023-01`).
   - Papers he wrote with others count as his statements (A14 ruling 3): `2012-01` with Shulman, `2014-01` with Yudkowsky, `2018-01` with Dafoe and Flynn. I did not record `2014-01` as an incidental row for Yudkowsky; the coordinator can decide.
   - I recorded `2018-01`, where he explicitly declines to say whether superintelligence this century is likely, as unexpressed rather than skipping it.
   - The Big Think interview (`2023-01`) is dated by the page's published time, 2023-04-09. The recording date is not given.
   - His home page line "the birth of superintelligence presumably not very far off" is undated, so it was not recorded (logged as date not found).
   - Sources that state only a year (papers, the Edge essay) are dated to the year. Within a year, I placed them before the dated items when the publication order was known.

4. Quick checks for a checker:
   - `bostrom-2008-01`: https://nickbostrom.com/superintelligence (Postscript IV, "less than a 50% probability to superintelligence being developed by 2033").
   - `bostrom-2014-03`: https://newrepublic.com/article/119419 ("There’s a big chance that we’ll have it in this century").
   - `bostrom-2016-01`: https://www.theguardian.com/technology/2016/jun/12/nick-bostrom-artificial-intelligence-machine ("because they are not that smart").

5. Checker: `OK: speakers.csv 50, statements.csv 176, aggregates.csv 200, world_measures.csv 97, events.csv 31, search_log.csv 885`, with no PROBLEM lines (bostrom: 17 statements, 120 search rows, 0 incidental rows).
