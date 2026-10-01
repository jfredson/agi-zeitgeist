# Panel verification, October 2026

Checked 2026-09-30 by claude-agent, under amendment A13 (three tiers with quotas) and
methodology-v2 section 3. **Re-marked 2026-10-01 under John's rulings in amendment A14**
(rulings 1 to 6); the section "Freeze candidates as of 2026-10-01" at the end is the
current summary. **Nothing here changes the panel.** John freezes it; this is
the evidence. `data/speakers.csv` holds only the five seed speakers and the survey,
market and poll sources.

Full evidence (quotes, every link, every query run) is in
[`panel-evidence-2026-10/`](panel-evidence-2026-10/). The tables below give one link per
criterion; the evidence files give the rest.

## The rules being checked

| tier | rule |
|---|---|
| **Core** (about 25) | **C1** a public statement on whether or when AGI arrives dated 2017 or earlier; **C2** one dated 2024 or later; **C3** named in three distinct pieces about where AI is going, in national outlets, dated 2017 or earlier |
| **2020s cohort** (10 to 12) | **C1** no public AGI *timeline* statement found before 2018; **C2** one dated 2024 or later. C3 was collected but only as information (see the note under the cohort table) |
| **Wide list** (60 to 100) | every person in the MIRI/AI Impacts predictions dataset and on the TIME100 AI lists 2023 to 2025, minus core and cohort candidates |

**Core quotas** (minimums among those frozen): 6 `skeptic` (pre-2017 statements reject or
doubt AGI within decades), 3 `non_us_uk` (based outside the United States and United
Kingdom when making their pre-2017 statements), 2 `philosopher` (philosopher or cognitive
scientist), 3 `frontier_lab` (led, ran, co-founded or held a senior research role at a
company building the most capable models of its time).

**Verdicts:** `PASS`; `PASS (thin)` = meets the rule only on weak evidence, named in the
notes; `UNCLEAR` = depends on a ruling or a missing check; `FAIL` = does not meet the rule
as searched. Nothing thin is rounded up to a plain pass.

## How far to trust this

- **Blocked outlets.** The search and page-reading tools could not reach the New York
  Times, the Guardian, The New Yorker, Wired, the BBC, the Economist, the Financial
  Times, the Wall Street Journal, The Atlantic or New Scientist. Pieces from them are
  marked "seen in search result" or were read in copies elsewhere. Several **C3 failures
  are probably the tools, not the record**, especially for UK-based candidates
  (Shanahan, Wooldridge) and Pinker. A library database check would settle them.
- **"Seen in search result"** items count toward C3 here. They were not opened; the
  search showed the outlet, the date and the name.
- **One copy carries four passes.** The 2015 New Yorker profile "The Doomsday Invention"
  was read in full from a course-page printout. It names Kurzweil, Bostrom, Hassabis
  and Hinton, and counts toward all four.
- **Page reading went through a summarising tool.** Quotes should be checked against
  the live page before going into `data/statements.csv`.
- Earlier in the session one helper fetched on-site search pages after the search
  limit ran out; nothing in these tables depends on them.

## Rulings applied (A14, 2026-10-01)

1. **Self-written pieces** count toward the three national pieces, but for at most one
   of the three. This turns Marcus, Russell and Brooks into passes, and confirms Tegmark.
2. **Skeptic window** is "2017 or earlier". Kai-Fu Lee gains the tag ("hundreds of years,
   if ever", 2017-06-24); LeCun's tag is strengthened by "still quite far from building
   artificial general intelligence" (2017, `lecun-2017-01`).
3. **Co-written statements** count for C2 when the person is a named author: Davis and
   Brynjolfsson meet C2 on co-written items.
4. **Dennett** is dropped from the core; he is added to the wide list.
5. **Tags.** `frontier_lab` applies if true at the time of any statement in the record,
   with dates in the justification. `philosopher` means primary role: Hinton and
   Hassabis are not tagged. Chalmers is `non_us_uk`. Suleyman is not a skeptic. Under
   A15 ruling 8, Kurzweil (Google engineering director from 2012), Chollet (Google senior
   engineer 2015 to 2024), Kai-Fu Lee (01.AI from 2023) and Karnofsky (OpenAI board 2017
   to 2021, Anthropic staff from 2025) are tagged `frontier_lab`. Kokotajlo (trained in
   philosophy, works as an AI forecaster) is not tagged `philosopher` (A15 ruling 8).
6. **Cohort prominence** is information only.

Still open: archive checks through the Guardian and New York Times APIs (application
programming interfaces, their official data services) once John has keys (ruling 7).
---

## Core panel candidates

Abbreviations in the table: "co-wr." = co-written; "search" = seen in search result, not
opened; "2nd" = secondhand.

| Candidate | C1: statement 2017 or earlier | C2: statement 2024 or later | C3: three national pieces 2017 or earlier | Quota tags | Verdict |
|---|---|---|---|---|---|
| Ray Kurzweil (seed) | 2002, Long Bet 1 ([longbets.org](https://longbets.org/1/)); in window 2005 ([singularity.com](https://singularity.com/qanda.html)) | 2026-01 (`kurzweil-2026-01`, 2nd); 2025-03-12 primary ([TWiT](https://twit.tv/posts/transcripts/intelligent-machines-810-transcript)) | Time 2011-02-10 ([link](https://time.com/archive/6595274/2045-the-year-man-becomes-immortal/)); New Yorker 2015-11-23; NYT 2014-07-08 (search) | frontier_lab (Google engineering director from 2012-12; A15 ruling 8) | PASS |
| Nick Bostrom | 1997 and 2008-03-12 ([nickbostrom.com](https://nickbostrom.com/superintelligence)) | 2026-02-13 working paper ([copy](https://www.greaterwrong.com/posts/ZeNRKhGFAhGB8WJ7s/nick-bostrom-optimal-timing-for-superintelligence)); no dated forecast | New Yorker 2015-11-23; Washington Post 2015-12-27 (search); MIT Technology Review 2015-12-15 ([link](https://www.technologyreview.com/2015/12/15/247302/what-will-it-take-to-build-a-virtuous-ai/)) | philosopher | PASS |
| Eliezer Yudkowsky | 2008-12-01 ([LessWrong](https://www.lesswrong.com/posts/JBadX7rwdcRFzGuju/recursive-self-improvement)) | 2024-02-18, 2nd ([Futurism](https://futurism.com/the-byte/ai-destroy-humankind-yudkowsky)) | New Yorker 2011-11-28 (Thiel profile); Slate 2014-07-17; Scientific American blog column 2016-03-01. Each weak on one point | none | UNCLEAR (C3) |
| Robin Hanson | 2012-08-27, "at least a century" ([Overcoming Bias](https://www.overcomingbias.com/p/ai-progress-estimatehtml)) | 2025-04-15, about economic impact ([link](https://www.overcomingbias.com/p/ai-is-gpt-and-gpts-go-slow)) | Guardian 2016-06-15 (search); Reason 2016-06-03; Scientific American blog column 2016-06-21 | skeptic | PASS (thin): C2 is about economic impact; C3 relies on edge outlets |
| Geoffrey Hinton (seed) | 2015-05, "No sooner than 2070" (`hinton-2015-01`) | 2026-09 (`hinton-2026-02`, 2nd); 2024-12-06 Nobel interview primary | New Yorker 2015-11-23; Guardian 2015-05-21 (search); Fortune 2016-09-28 ([link](https://fortune.com/longform/ai-artificial-intelligence-deep-machine-learning/)) | skeptic, non_us_uk, frontier_lab (Google Brain 2013 to 2023) | PASS |
| Yann LeCun (seed) | 2005 slide; 2015-02-18 (`lecun-2015-01`) | 2026-02-27 (`lecun-2026-04`) | MIT Technology Review 2015-08-06 ([link](https://www.technologyreview.com/2015/08/06/10909/teaching-machines-to-understand-us/)); Fortune 2016-09-28; Popular Science 2015-09-22 | skeptic (2015 and 2017 statements), frontier_lab (Facebook/Meta 2013 to 2025) | PASS (thin): one C3 outlet is borderline |
| Yoshua Bengio | 2016-01, about remaining science, not explicitly AGI (2nd, [excerpt](https://www.lesswrong.com/posts/4qPy8jwRxLg9qWLiG/yoshua-bengio-on-ai-progress-hype-and-risks)) | 2025-06-03 ([blog](https://yoshuabengio.org/en/blog/introducing-lawzero)) | MIT Technology Review 2016-01-29 ([link](https://www.technologyreview.com/2016/01/29/162084/will-machines-eliminate-us/)); Forbes contributor 2017-11-06 (search); Globe and Mail 2017-07-05 (co-wr., about policy) | non_us_uk | UNCLEAR (C1 not explicit; C3 needs the byline ruling) |
| Demis Hassabis | 2010, talk titled "…building AGI" (title only, [video](https://www.youtube.com/watch?v=Qgd3OK5DZWI)) | 2026-05, Google I/O, 2nd ([Decoder](https://the-decoder.com/deepminds-hassabis-sees-humanity-in-the-foothills-of-the-singularity-while-lecun-says-current-ai-isnt-intelligent/)) | New Yorker 2015-11-23; Fortune 2016-09-28; Vanity Fair 2017-03 (search) | frontier_lab (DeepMind co-founder 2010 on) | PASS (thin): C1 is a talk title, not a sentence |
| Shane Legg | 2009-12, "human level AGI in the year 2025" ([vetta.org](https://www.vetta.org/2009/12/tick-tock-tick-tock-bing/)) | 2025-12-14, paraphrase only ([Decoder](https://the-decoder.com/deepmind-co-founder-shane-legg-sees-50-percent-chance-of-minimal-agi-by-2028/)) | none on the outlet list; HuffPost and Business Insider 2014 only | frontier_lab (non_us_uk possible) | FAIL (C3; C2 thin) |
| Sam Altman (seed) | 2014-02 (`altman-2014-01`) | 2026-08-26 (`altman-2026-04`, 2nd); 2026-02-14 primary | Fortune 2015-12-11 ([link](https://fortune.com/2015/12/11/open-ai/)); MIT Technology Review 2015-12-15; New Yorker 2016-10-10 (search) | frontier_lab | PASS |
| Gary Marcus (seed) | 2013, "smarter than us before the end of the century" (`marcus-2013-01`, 2nd); 2016-05-04 primary | 2026-09-10 (`marcus-2026-08`) | MIT Technology Review 2015-12-17 ([link](https://www.technologyreview.com/2015/12/17/164285/can-this-man-make-ai-more-human/)) and 2017-03-29; NYT op-ed 2017-07-29 (his own byline, search) | skeptic, philosopher | PASS (one of the three pieces is his own, allowed by A14 ruling 1) |
| Andrew Ng | 2015-03-19, 2nd ([The Register](https://www.theregister.com/2015/03/19/andrew_ng_baidu_ai/)) | 2026-01-02 ([The Batch](https://www.deeplearning.ai/the-batch/issue-334/)) | Fortune 2016-03-09 ([link](https://www.fortune.com/2016/03/09/baidu-robots-ai)) and 2017-01-05; MIT Technology Review 2017-11-07 | skeptic (medium), frontier_lab | PASS (thin): C1 is secondhand; skeptic tag rests on "far future" |
| Stuart Russell | 2014-04-19, co-wr. ([HuffPost](https://www.huffpost.com/entry/artificial-intelligence_b_5174265)) | 2025-01-31 ([Newsweek](https://www.newsweek.com/deepseek-openai-race-human-extinction-2023482)) | Independent 2014-05-01 (co-wr.); Wired reprint of Quanta 2015-04-21; Fox News 2017-11-21 ([link](https://foxnews.com/tech/uc-berkeley-professors-slaughterbots-video-on-killer-drones-goes-viral.print)) | none | PASS (one co-written piece, allowed by A14 ruling 1) |
| Rodney Brooks | 2008-06-01 ([IEEE Spectrum](https://spectrum.ieee.org/i-rodney-brooks-am-a-robot)); 2014-11-11 "centuries" ([Robohub](https://robohub.org/artificial-intelligence-is-a-tool-not-a-threat/)) | 2026-01-01 ([scorecard](https://rodneybrooks.com/predictions-scorecard-2026-january-01/)) | MIT Technology Review 2015-10-06 ([link](https://www.technologyreview.com/2015/10/06/165915/can-we-shape-the-robot-revolution/)); ABC Australia 2016-04-18; MIT Technology Review 2017-10-06 (his essay) | skeptic | PASS (one piece is his own essay, allowed by A14 ruling 1) |
| Elon Musk | 2014-10, paraphrase (2nd); 2017-10-05 post, seen quoted | 2026-01-04 post, seen quoted ([copy](https://garymarcus.substack.com/p/sorry-sam-and-elon-we-have-not-reached)) | NBC News 2014-08-04 ([link](https://www.nbcnews.com/news/amp/wbna55795017)); Fortune 2014-10-27; NPR 2017-07-17 (search) | frontier_lab | PASS (thin): C1 and C2 are secondhand copies |
| Ilya Sutskever | 2015-12-11, co-signed company post ([copy](https://tm.durusau.net/?p=66175)) | 2025-11-25 ([Dwarkesh](https://www.dwarkesh.com/p/ilya-sutskever-2)) | MIT Technology Review 2017-03-29 only; Wired 2016-04 and NYT 2015-12 seen, naming not confirmed | frontier_lab | FAIL (C3 as searched); checked for the cohort below |
| François Chollet | 2017-07-18, possibility only ([Keras blog](https://blog.keras.io/the-future-of-deep-learning.html)) | 2026-03-27, 2nd ([OfficeChai](https://officechai.com/ai/agi-likely-by-early-2030s-when-arc-agi-6-or-7-will-be-released-arc-prizes-francois-chollet/)) | none found | frontier_lab (Google senior engineer 2015 to 2024; A15 ruling 8) | FAIL (C3); checked for the cohort below |
| Melanie Mitchell | not found (earliest dated item 2018) | 2025-09-15 ([newsletter](https://aiguide.substack.com/p/magical-thinking-on-ai)) | none found | philosopher likely, unsourced | FAIL (C1, C3) |
| Oren Etzioni | 2014-12-16, reported speech in NYT; 2016-09-20 own piece ([MIT TR](https://www.technologyreview.com/2016/09/20/70131/no-the-experts-dont-think-superintelligent-ai-is-a-threat-to-humanity/)) | not found (GeekWire 2026 lead would not load) | MIT Technology Review 2015-12-15, 2016-09-01, 2016-11-02 (one outlet) | skeptic | FAIL (C2) |
| Ernest Davis | 2014-10-23 preprint, published 2015 ([paper](https://cs.nyu.edu/~ed1/papers/Bostrom.pdf)) | 2025-07-22, co-wr. with Marcus ([post](https://garymarcus.substack.com/p/deepmind-and-openai-achieve-imo-gold)) | none about AI futures | skeptic | FAIL (C3). C2 now met on co-written items (A14 ruling 3) |
| Steven Pinker | 2008-06-01, "not the slightest reason to believe in a coming singularity" ([IEEE Spectrum](https://spectrum.ieee.org/tech-luminaries-address-singularity)) | 2024-06-18 podcast, no verbatim quote; latest verbatim 2023-12-20 | IEEE Spectrum 2008 only (borderline) | skeptic, philosopher | FAIL (C3, C2 unclear). Likely the tools; worth an archive check |
| David Chalmers | 2010 paper, "would be surprised… within the next three decades" ([paper](https://consc.net/papers/singularity.pdf)) | 2026-07-10, about current models, not timing ([Berkeley](https://news.berkeley.edu/2026/07/10/berkeley-talks-when-we-talk-to-ai-what-are-we-talking-to/)) | Forbes 2009-10-02 ([link](https://www.forbes.com/2009/10/02/machine-intelligence-technology-breakthroughs-singularity.html)) and 2009-10-12; Scientific American 2010-12-22 | philosopher, non_us_uk (A14 ruling 5) | PASS (thin): C2 is about current capability |
| Daniel Dennett | 1985 / 1998 essay; 2015 "urban legend" ([Edge](https://www.edge.org/response-detail/26035)) | 2024-04 last interview, published 2024-04-25 after his death ([Spectator](https://spectator.com/?p=485505)) | Time 1996-03-25 ([link](https://time.com/archive/6728762/can-machines-think/)); Time 2013-06-17; NPR blog column 2017-06-16 (search) | skeptic, philosopher | DROPPED (A14 ruling 4); moved to the wide list |
| Erik Brynjolfsson | 2017-11-30, "a long way from" AGI ([MIT TR](https://www.technologyreview.com/2017/11/30/147363/progress-in-ai-isnt-as-impressive-as-you-might-think/)) | 2025-10, group-authored paper ([agidefinition.ai](https://www.agidefinition.ai/)) | MIT Technology Review 2013-06-12; Slate 2014-05-04; MIT Technology Review 2017-11-30. Two are about jobs | none | PASS (thin): C1 by one month; C3 mostly about jobs (C2 co-written, allowed by A14 ruling 3) |
| Jürgen Schmidhuber | 2006, convergence "around 2040" ([own site](https://people.idsia.ch/~juergen/history.html)) | 2024-10, TED talk; quote is TED's description ([TED](https://www.ted.com/talks/juergen_schmidhuber_why_2042_will_be_a_big_year_for_ai)) | NYT 2016 (search, date unverified); Polish Press Agency 2017-11-20 ([link](https://scienceinpoland.pl/en/node/27249)); Guardian 2017 (search) | non_us_uk | PASS (thin): C2 is TED's paraphrase; two C3 items unopened |
| Kai-Fu Lee | 2017-06-24 NYT op-ed, "hundreds of years, if ever" (read via repost) | 2025-10-02, "about five years" ([Kazinform](https://qazinform.com/amp/ai-will-surpass-90-of-people-in-five-years-2c7ca2/)) | CNBC 2017-04-27 (search); MIT Technology Review 2017-06-27 ([link](https://www.technologyreview.com/2017/06/27/150705/chinas-tech-moguls-warn-of-ais-troubling-trajectory/)); CNBC 2017-11-13 (search) | non_us_uk, skeptic (2017-06-24, A14 ruling 2); frontier_lab (01.AI founder from 2023-03; A15 ruling 8) | PASS (thin): two C3 items unopened |
| Toby Walsh | 2016-02-20, "30 or 40 years away" ([arXiv](https://ar5iv.labs.arxiv.org/html/1602.06462)) | 2025-07-04 ([China Daily HK](https://www.chinadailyhk.com/article/615214)) | ABC Australia 2015-10-20 ([link](https://www.abc.net.au/news/2015-10-20/australian-ai-expert-calls-for-ban-on-killer-robots-at-un/6868834)) and 2017-08-21; CNN 2017-08-21 (search) | non_us_uk (not skeptic: 30 to 40 years is within decades) | PASS |
| Murray Shanahan | 2014-07, "better than fifty-fifty" within 30 years (2nd, [KitGuru](https://www.kitguru.net/gaming/anton-shilov/ai-will-match-human-intelligence-in-the-next-30-years-robot-expert/)) | not found | BBC 2014-12-02, seen only as a Wikipedia citation | frontier_lab | FAIL (C2, C3). UK outlets blocked; worth an archive check |
| Ben Goertzel | 2006 talk, "ten year time-frame or less" ([copy](https://www.thekurzweillibrary.com/we-could-get-to-the-singularity-in-ten-years)) | 2024-03-01, "three to eight years" ([Futurism](https://futurism.com/artificial-superintelligence-agi-2027-goertzel.md)) | none found | non_us_uk partly supported | FAIL (C3) |
| Michael Wooldridge | 2017-10-10, about conscious machines (2nd, [Oxford](https://cs.ox.ac.uk/innovation/research-impact/case-AI.html)) | 2025-11-14 ([IMD](https://www.imd.org/ibyimd/videos/the-interview/real-story-of-ais-rise-from-winters-to-workplaces/)) | none found | skeptic probable (2017-10-10 statement now inside the window, but it is about conscious machines) | FAIL (C3; C1 ambiguous). UK outlets blocked |
| Judea Pearl | 2011-12-27, possibly a paraphrase ([JTA](https://jta.org/?p=442604)) | 2024-09-09 ([Globes](https://en.globes.co.il/en/article-1001488789)) | JTA 2011 only (specialist agency) | none | FAIL (C3) |
| Max Tegmark | 2014-05-01 co-wr. op-ed (Independent) | 2025-06-03, implies nearness, no date ([repost](https://lifeboat.com/blog/2025/09/max-tegmark-can-we-prevent-ai-superintelligence-from-controlling-us)) | Independent 2014-05-01 (co-wr.); Christian Science Monitor 2015-01-16 ([link](https://csmonitor.com/Science/2015/0116/Elon-Musk-spends-10-million-to-stop-robot-uprising)); WSJ review 2017-08-29 (reviewer's reprint) | none | PASS (thin): C2 implies nearness without a date. The co-written op-ed counts for C1 (named author) and as his one allowed own piece |
| Luciano Floridi | 2016-05-09, "utterly implausible" ([Aeon](https://aeon.co/essays/true-ai-is-both-logically-possible-and-utterly-implausible)) | 2024-06-14, "no such thing coming" ([SciELO](https://scielo.br/j/fun/a/8xsLKmCytRX9w7p9q8jG6GF/?lang=en)) | none found (an FT piece by him, 2017, unconfirmed) | skeptic, philosopher | FAIL (C3) |
| Mustafa Suleyman (from cohort list) | 2016-12-05, "20 years out or decades way" (2nd, [TechCrunch](https://techcrunch.com/2016/12/05/deepmind-ceo-mustafa-suleyman-says-general-ai-is-still-a-long-way-off)) | 2025-11-14 ([transcript](https://singjupost.com/mustafa-suleyman-on-silicon-valley-girl-podcast-transcript/)) | Fortune 2016-10-10 ([link](https://fortune.com/2016/10/10/google-artificial-intelligence-deepmind-jobs/)); NPR 2016-09-28 (search); MIT Technology Review 2017-10-04 | frontier_lab (DeepMind 2010 to 2019, Inflection 2022, Microsoft AI from 2024); not skeptic (A14 ruling 5) | PASS. Fails the cohort rule (2016 timeline), so he belongs here |
| Tyler Cowen (from cohort list) | 2005-09-21, skeptical of the Singularity ([Marginal Revolution](https://marginalrevolution.com/marginalrevolution/2005/09/the_singularity.html)) | 2025-04-16, "I think it is AGI, seriously" ([link](https://marginalrevolution.com/marginalrevolution/2025/04/o3-and-agi-is-april-16th-agi-day.html)) | Economist, WSJ and Daily Beast reviews of *Average Is Over*, 2013 (listed on Wikipedia, not opened; borderline topic) | skeptic near miss | UNCLEAR (C3 unopened and borderline) |
| Holden Karnofsky (from cohort list) | 2016-05-16, "nontrivial likelihood of transformative AI within the next 20 years" ([mirror](https://forum.nunosempere.com/posts/zmBnKnpECErWsCiYq/some-background-on-open-philanthropy-s-views-regarding)) | 2025-08-28, about takeoff speed ([podcast](https://podcast.clearerthinking.org/episode/277/holden-karnofsky-the-most-important-century)) | none found | frontier_lab (OpenAI board 2017 to 2021, Anthropic staff from 2025-01; A15 ruling 8) | FAIL (C3). Also fails the cohort rule |

### Quota totals among core candidates who pass (as of 2026-09-30, superseded below)

Counted over the 16 with `PASS` or `PASS (thin)`: Kurzweil, Bostrom, Hanson, Hinton,
LeCun, Hassabis, Altman, Ng, Musk, Chalmers, Brynjolfsson, Schmidhuber, Kai-Fu Lee,
Walsh, Tegmark, Suleyman.

| quota | minimum | among the 16 passes | if bylines count (+ Marcus, Russell, Brooks = 19) | reachable? |
|---|---|---|---|---|
| skeptic | 6 | **4**: Hanson, Hinton, LeCun (medium), Ng (medium) | **6**: + Marcus, Brooks | **Only with the byline ruling**, and then exactly at the minimum with two medium-confidence tags. Kai-Fu Lee would add one if ruling 2 allows a 2017 statement; Dennett one if he is kept |
| non_us_uk | 3 | **5**: Hinton, Schmidhuber, Kai-Fu Lee, Walsh, Chalmers (judgment call) | 5 | Yes, even without Chalmers |
| philosopher | 2 | **2**: Bostrom, Chalmers | **3**: + Marcus | Yes, just. Dennett would add one if kept |
| frontier_lab | 3 | **7**: Hinton, LeCun, Hassabis, Altman, Ng, Musk, Suleyman | 7 | Yes, comfortably |

**What this shows.** The dated prominence rule does what A13 predicted: it rewards
people who were loud early, mostly lab founders and singularity forecasters, so the
skeptic quota is the one at risk. Six of the skeptic candidates fail on C3 (Pinker,
Floridi, Davis, Etzioni on C2, Wooldridge, Mitchell on C1), several probably because
the tools could not reach UK and US newspapers. The core reaches 19 with the byline ruling,
and 23 if the four unclear cases (Yudkowsky, Bengio, Dennett, Cowen) are all resolved in
their favour, short of about 25; an archive check on the C3 failures
(Pinker, Shanahan, Wooldridge, Goertzel, Floridi, Legg) is the cheapest way to grow it,
and would mostly add skeptics.

---

## 2020s cohort candidates

| Candidate | C1: no AGI timeline statement before 2018 | C2: statement 2024 or later | C3 (information only) | Quota tags | Verdict |
|---|---|---|---|---|---|
| Dario Amodei | 2017-07-21 statement is about possibility, not timing ([80,000 Hours](https://80000hours.org/podcast/episodes/the-world-needs-ai-researchers-heres-how-to-become-one/)); first timeline 2024-10 | 2026-01, "as little as 1–2 years away" ([essay](https://www.darioamodei.com/essay/the-adolescence-of-technology)) | 2 of 3 (MIT TR 2016-06-22; NYT 2017-08, search) | frontier_lab | PASS (he also cleared the old core bar on possibility; the cohort rule is about timelines) |
| Leopold Aschenbrenner | earliest 2023-03-29 ([blog](https://www.forourposterity.com/nobodys-on-the-ball-on-agi-alignment/)) | 2024-06, "AGI by 2027 is strikingly plausible" ([Situational Awareness](https://situational-awareness.ai/)) | none | none (frontier_lab near miss) | PASS |
| Daniel Kokotajlo | earliest 2020-08-23 ([forum](https://www.greaterwrong.com/posts/hQysqfSEzciRazx8k/forecasting-thread-ai-timelines)) | 2026-08-16 ([AI Futures Project](https://blog.aifutures.org/p/q25-2026-timelines-update-uplift)) | none | none (trained in philosophy; primary role AI forecasting, A14 ruling 5) | PASS |
| Ajeya Cotra | earliest 2020-09-18 (summary by Rohin Shah, 2nd); own words 2022-08-02 | recorded 2025-10-20, published 2026-02 ([80,000 Hours](https://80000hours.org/podcast/episodes/ajeya-cotra-transformative-ai-crunch-time/)) | none | none | PASS |
| Jensen Huang | earliest 2023-11-29 (2nd, [CNBC copy](https://nbcnewyork.com/news/business/money-report/nvidia-ceo-jensen-huang-says-ai-will-be-fairly-competitive-with-humans-in-5-years/4904935)) | 2026-03, "I think we've achieved AGI" (2nd, [TechSpot](https://www.techspot.com/news/111797-weve-achieved-agi-nvidia-ceo-but-own-examples.html)) | 3 (MIT TR 2017-05-12; Fortune 2016-09-28 and 2016-01-13) | none (frontier_lab near miss: chips, not models) | PASS (thin): both statements secondhand |
| Jan Leike | earliest 2019-12-16, possibility ([FLI](https://futureoflife.org/?p=39550)) | 2024-05-17, no date given (2nd, [Decrypt](https://decrypt.co/231294/openai-exec-quit-safety-took-backseat-shiny-products)) | none | frontier_lab | PASS (thin): few timeline statements; a full trace may find little |
| Ethan Mollick | earliest 2023-01-21 ([newsletter](https://www.oneusefulthing.org/p/becoming-strange-in-the-long-singularity)) | 2025-04-20, "Jagged AGI" ([newsletter](https://www.oneusefulthing.org/p/on-jagged-agi-o3-gemini-25-and-everything)) | none | none | PASS (thin): rarely gives a date |
| François Chollet (failed core C3) | 2017-07-18 is about possibility; first timeline found 2025 | 2026-03-27 (2nd) | none | frontier_lab (Google 2015 to 2024; A15 ruling 8) | PASS |
| Ilya Sutskever (failed core C3) | 2015-12-11 co-signed post says "it's hard to predict when human-level AI might come within reach": a statement about timing, though not a date | 2025-11-25, "5 to 20" years | 1 confirmed | frontier_lab | UNCLEAR: does a co-signed "hard to predict when" count as a timeline statement? |
| Mustafa Suleyman | 2016-12-05 timeline ("20 years out or decades way") | 2025-11-14 | 3 | frontier_lab | FAIL (pre-2018 timeline). Passes core instead |
| Holden Karnofsky | 2016-05-16 timeline ("within the next 20 years") | 2025-08-28 | none | frontier_lab arguable | FAIL (pre-2018 timeline); also fails core C3 |
| Tyler Cowen | 2005-09-21 skeptical of a Singularity timeline | 2025-04-16 | 2013 book reviews | skeptic near miss | FAIL (pre-2018 timeline). Core UNCLEAR |

**Cohort count:** 8 pass (Amodei, Aschenbrenner, Kokotajlo, Cotra, Huang, Leike,
Mollick, Chollet) and Sutskever is unclear, against a target of 10 to 12. Three of the
passes are thin.

**Note on C3 for the cohort.** Information only, confirmed by John (A14 ruling 6).

---

## Wide list

Built by the enumerable rule and saved as
[`data/wide_list_candidates.csv`](../data/wide_list_candidates.csv) (name, source list,
link, notes): **184 names** by the rule after removing the 18 who are core or cohort
candidates, plus Dennett (A14 ruling 4): 185.

| source | names added | notes |
|---|---|---|
| MIRI AI predictions dataset, AI Impacts amended copy ([page](https://aiimpacts.org/miri-ai-predictions-dataset/)) | 56 | the "Data" sheet; authors kept as printed (often surname only) with the source title so a reader can identify them; the sheet of deleted entries left out |
| TIME100 AI 2023 | 43 | partial: the page-reading tool returned 50 of 100 entries |
| TIME100 AI 2024 | 43 | partial: 50 entries returned |
| TIME100 AI 2025 | 46 | partial: 51 entries returned |
| stream M media sample | not yet | added when the media stream runs |

time.com refuses scripted requests, so the TIME lists could only be read through a
page-reading tool, which returned about half of each list (mostly the "Leaders" and
"Innovators" sections). The missing names were **not** filled in from memory; the gap is
recorded on each row. The full lists need a manual export before the wide list is used.
The target is now whatever the rule yields (A14 ruling 8). Daniel Dennett was added on
2026-10-01 when he was dropped from the core (A14 ruling 4), so the file holds 185 names.

---

## Gaps to close before freezing

Archive checks (library database or someone with newspaper access) on the C3 failures:
Pinker, Shanahan, Wooldridge, Goertzel, Floridi, Legg, Sutskever; a 2024-or-later
statement from Etzioni (GeekWire 2026 lead) and Shanahan (2024 and 2025 podcasts); the
original 2016 Bengio interview; a transcript of Hassabis's 2010 talk; opening the three
Cowen reviews; the full TIME100 AI lists.

---

## Freeze candidates as of 2026-10-01

For John's freeze. Nothing has been frozen.

### Core: pass now (19)

Kurzweil, Bostrom, Hanson, Hinton, LeCun, Hassabis, Altman, Marcus, Ng, Russell, Brooks,
Musk, Chalmers, Brynjolfsson, Schmidhuber, Kai-Fu Lee, Walsh, Tegmark, Suleyman.
Ten of these pass on thin evidence (named in the table): Hanson, LeCun, Hassabis, Ng,
Musk, Chalmers, Brynjolfsson, Schmidhuber, Kai-Fu Lee, Tegmark.

| quota | minimum | count among the 19 | who |
|---|---|---|---|
| skeptic | 6 | **7** | Hanson, Hinton, LeCun, Marcus, Ng (medium confidence: "far future"), Brooks, Kai-Fu Lee |
| non_us_uk | 3 | **5** | Hinton, Chalmers, Schmidhuber, Kai-Fu Lee, Walsh |
| philosopher | 2 | **3** | Bostrom, Marcus, Chalmers |
| frontier_lab | 3 | **9** | Hinton, LeCun, Hassabis, Altman, Ng, Musk, Suleyman, Kurzweil, Kai-Fu Lee (the last two tagged under A15 ruling 8) |

All four minimums are met by the 19, the skeptic minimum with one to spare (two if Ng's
medium-confidence tag holds). The core is six short of "about 25".

### Core: unclear, pending the archive checks or a missing source (10)

| candidate | what is missing | tags if they pass |
|---|---|---|
| Yudkowsky | C3: three pieces, each weak on one point | none |
| Bengio | C1: the original 2016 MIT Technology Review interview (link dead) | non_us_uk |
| Cowen | C3: three 2013 reviews not yet opened; topic borderline | none (skeptic near miss) |
| Pinker | C3 (one piece found) and a verbatim 2024 statement | skeptic, philosopher |
| Floridi | C3 (none found; an FT piece by him, 2017, unconfirmed) | skeptic, philosopher |
| Legg | C3 (only HuffPost and Business Insider) and a verbatim 2024+ quote | frontier_lab (non_us_uk possible) |
| Sutskever | C3 (one confirmed; Wired 2016 and NYT 2015 seen, naming unconfirmed) | frontier_lab |
| Shanahan | C3 and C2 (2024 and 2025 podcasts not transcribed) | frontier_lab |
| Wooldridge | C3 (UK outlets blocked); C1 ambiguous | skeptic probable |
| Goertzel | C3 (none found) | non_us_uk partly supported |

Quota totals within this group, if all ten passed: skeptic 3 (Pinker, Floridi,
Wooldridge), non_us_uk 1 to 3 (Bengio; Legg and Goertzel partly supported), philosopher 2
(Pinker, Floridi), frontier_lab 3 (Legg, Sutskever, Shanahan). All ten passing would make
a core of 29.

### Core: fail as searched (7)

Chollet (checked for the cohort instead), Mitchell (C1), Etzioni (C2), Davis (C3),
Pearl (C3), Karnofsky (C3; also fails the cohort rule), and Dennett, dropped by ruling.

### 2020s cohort: pass now (8)

Amodei, Aschenbrenner, Kokotajlo, Cotra, Huang, Leike, Mollick, Chollet. Unclear:
Sutskever (whether a co-signed "hard to predict when" counts as a timeline statement;
he is also on the core unclear list). Quota tags among the 8: frontier_lab 3 (Amodei,
Leike, Chollet); no others. The target is ten to twelve.

### Wide list

185 names (184 by the rule, plus Dennett). The TIME100 AI lists are still only partly
retrieved.
