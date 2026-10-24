# Claims-ledger reframe check, notes for each item (2026-10-19)

Source checks for pull request 27 at commit 93f1e6d by helpers of the checking session. Summary and verdict: claims-ledger-reframe-check-2026-10-19.md beside this file.

## Undated words: the six hardest cases

# Round 4, undated words, batch 1: six records checked at their sources

Checked 2026-10-19 against the pull request 27 checkout (read only; nothing edited there).
Captions were fetched with yt-dlp into new folders `dl4-u1-1` (Pichai), `dl4-u1-2` (Suleyman) and
`dl4-u1-3` (LeCun); X posts through api.fxtwitter.com and X's own embed service
(cdn.syndication.twimg.com) into `dl4-u1-4`.

## A problem across the whole folder: quote length

The brief's rule is a quote of at most 25 words. The validator's check for undated words
(`scripts/validate.py`, the undated-words function from line 784) never tests length; only
timing claims are tested (line 688). Ten of the eleven files in `data/claims_undated/` are over 25 words:
Pichai 31, Mensch 39, Altman 41, Huang 29, Hassabis 41, LeCun 45 (48 counting the `[...]`
markers), Suleyman 30, Zuckerberg 41, Nadella 29. Only Musk (5) and Legg (13) are within it.
Either the quotes are trimmed and the validator gains the check, or the method says plainly that
the limit does not apply to undated words. I count this once here, not as a fix on each item
below, but trims are suggested where they help.

---

## 1. Pichai, "sooner rather than later" (Decoder, 2026-05-26): FIX NEEDED (small)

- **Source and date.** YouTube `ANV3tE5ywv0`, channel "Decoder with Nilay Patel", uploaded
  2026-05-26, "How Sundar Pichai is rethinking Google for the AI era". The uploader's own English
  track exists and was used. Role: chief executive of Google and Alphabet, which qualifies.
- **Quote.** It matches the uploader's track word for word. But the words sit at **00:42:46 to
  00:42:58**, not from 00:42:29. At 00:42:29 he is saying "By the way, I think it's important for
  us to understand that this technology's progressing very rapidly". The automatic track gives
  00:42:46 too.
- **Judgement point, is "three years, five" his own?** No, not as said there. He reports "wide
  consensus" among the frontier labs, then "people may quibble around like, you know, is it like
  three years, five", and his own words are "sooner rather than later". The clincher comes at
  00:45:21, when Patel asks "what is your timeline? Is it three years, five years to AGI?" and he
  declines: "that timeline doesn't matter". So the record is right to keep these words undated, and
  the `about` sentence is fair.
- **What needs fixing.** The notes quote only "timeline doesn't matter" (00:45:25). They leave out
  the very next thing he says, at 00:45:38: "three years from now, whether you and I call it AGI or
  not doesn't matter because it'll be very, very powerful". That sentence carries a length of
  time. It belongs in the notes, and someone should rule whether it is a dated claim. My reading:
  it is a three-year forecast that AI will be "very, very powerful", and he explicitly will not call
  that AGI, so it is at most an `other` timing claim with no test. It does not make this undated
  record wrong.
- Fixes: set the locator to 00:42:46 to 00:42:58; add the 00:45:38 sentence to the notes and
  decide whether it is a claim; trim the quote to 25 words if the limit applies. A possible trim:
  "people may quibble around like, you know, is it like three years, five, but the technology is
  sooner rather than later" (21 words).

## 2. Nadella, "today's Super Intelligence systems" (X article, 2026-10-10): FIX NEEDED (drop the record)

- **Source and date.** Post `2108931348857827686` by @satyanadella, 2026-10-10T14:43:10Z on both
  the embed service and fxtwitter. The article is titled "Models as Insider Risks in the Super
  Intelligence Era". The quote matches the second paragraph exactly, apart from a straight
  apostrophe where the original has a curly one. Role: chief executive of Microsoft, which
  qualifies.
- **Judgement point, is this his view that superintelligence is here?** No. The Register
  (2026-10-05, "Musk follows Trump's lead, swaps AI for SI in SpaceX rebrand") reports that the
  President's executive order of 2026-09-29 tells federal agencies to replace "Artificial
  Intelligence" with "Super Intelligence" in their communications. Nadella's article uses the
  phrase in exactly that capitalised, renamed sense, all the way through:
  - "SI inside the enterprise";
  - "today's Super Intelligence systems ... the frontier models powering these systems";
  - "The most trustworthy Super Intelligence system will not be the one with the model we trust most".

  He means today's AI products under their new official name. He makes no claim that AI has
  passed people, and the article has no other words on when anything arrives.
- **It is also inconsistent with the record on Musk.** That record sets aside Musk's posts of
  2026-10-04 ("No more AI / SI", "SpaceX is a super intelligence company") as "about naming, not
  when". Nadella's usage is the same kind of renaming. The `about` sentence already hedges ("as if
  ... may follow the US government's preferred name"), which is a sign the record does not belong.
- Fix: remove the record. Log the search result as "renaming under the order of 2026-09-29; nothing
  about when". Nadella then has no undated words, which is accurate.

## 3. Musk, "That will be Grok 5" (X reply, 2026-09-14): CONFIRMED, with one wording fix to `about`

- **Source and date.**
  - The reply: `2099455592670634034`, "@AdamLowisz That will be Grok 5", 2026-09-14T11:09:53Z on
    both the embed service and fxtwitter.
  - The question: `2099308480372875729`, 01:25:19Z, "Elon, how close do you think Grok 4.8 will be
    towards achieving AGI?".
  - The question quotes Musk's own post `2099308197802631191` (01:24:12Z): "Grok 4.8 ... will finish
    training this week and start RL".
  - That post answers techdevnotes `2099124531172434084` (2026-09-13): "what are we even expecting
    from SpaceXAI in september".

  Role: he leads SpaceXAI, which builds frontier models, so it qualifies. The quote, date and time
  are right.
- **Is there a date or length of time for Grok 5 in the thread?** None. The only time in the chain
  is "this week", and that is for finishing Grok 4.8's training, not for Grok 5. Coverage of the
  same roadmap agrees there was no date:
  - Yellow.com, 2026-09-14: "His Grok 5 claim did not include a benchmark or timetable".
  - AIToolsRecap, 2026-09-14: "Musk named it as the version where he expects AGI, with no timeline
    attached".
  - Digital Today, 2026-09-15, citing Cryptopolitan: also no date.
- **Is it about AGI arriving?** Yes. It answers a question about how close a model comes to AGI,
  and it names the model that will reach it. The time is undated: a model, not a year.
- **Wording fix.** The `about` sentence says "the model after it, Grok 5". The same roadmap, in
  posts reported by Yellow.com and Digital Today, puts a Grok 4.9 ("Astra or Fable class") between
  them. I did not find that post itself. Suggest "a later model, Grok 5".

## 4. LeCun, "it will take time" (Sciences Po, 2026-09-16): FIX NEEDED (the cut is not honest)

- **Source and date.**
  - YouTube `Y4s8NadbZfU`, channel "Sciences Po", uploaded 2026-09-17, "Yann Le Cun : où va
    l'intelligence artificielle ?".
  - The description gives "Mercredi 16 septembre 2026, de 18h30 à 20h" and calls him "président
    exécutif d'Advanced Machine Intelligence", so the date and the qualifying role are right.
  - The only track is French automatic captions. As the file says, it spells AMI Labs "Mila Labs".
- **What the captions say (01:07:42 to 01:08:12):**
  - "Il y a il y a pas de doute. Ça va arriver. On aura des machines, ça va pas arriver l'année
    prochaine, hein. Mais on aura des machines à un certain moment qui seront plus intelligents que
    les humains dans tous les domaines, à peu près."
  - Then "Et probablement beaucoup plus intelligent dans certains domaines ... Ça va venir. Pas avec
    les LLM ... Mais ça va prendre du temps."

  The quoted fragments are accurate. Dropping the stutter "il y a" is fine.
- **Judgement point, is the cut honest?** No. The first `[...]` removes "ça va pas arriver l'année
  prochaine" ("it won't happen next year"). That is a length of time, and it is a forecast that
  something will not happen by a date. The method, reading 2, says such a forecast is a claim. The
  ledger already holds LeCun claims of exactly this shape, for example
  `2024-04-09-lecun-not-surpass-human-intelligence-next-year` and
  `2026-01-22-lecun-human-level-not-next-year-or-two` (form `not_before`). The notes admit the words
  were left out "so that these words stay undated". That is fitting the quote to the folder, which
  the rule forbids: words that carry a length of time go to the dated claims.
- **A second dated forecast in the same talk.** At 01:00:30 to 01:00:41 he says Silicon Valley
  people claim "on pourra faire des systèmes super intelligents dans 2 ou 3 ans ... Mais c'est faux"
  (they say superintelligent systems can be built in 2 or 3 years; "but it's false"). That is a
  forecast that superintelligence will not come within two or three years of 2026-09-16. It is
  another `not_before` claim, and the stronger of the two.
- **What follows for the page.** Once either is entered, LeCun's latest dated forecast is
  2026-09-16. Undated words are shown only when they are newer than that, so this record would not
  be shown in any case.
- Fixes: enter the "not next year" forecast (01:07:51), and probably the "2 or 3 years ... false"
  forecast (01:00:36), as timing claims. Use arrives `beyond_people` or `superintelligence`; he
  glosses it as "super intelligent, c'est-à-dire plus intelligent que les humains dans tous les
  domaines" at 01:07:40. Use form `not_before` and log the searches. Then delete this undated
  record, or keep it only with the full sentence restored, knowing it will not show.

## 5. Suleyman, "superintelligence further out" (Decoder, 2026-09-17): CONFIRMED (suggest the uploader's track)

- **Source and date.** YouTube `T7VOrTLMg74`, channel "Decoder with Nilay Patel", uploaded
  2026-09-17, title as in the file. Role: chief executive of Microsoft AI, which qualifies.
- **The best caption track** is the uploader's own English (en-US) track, not the automatic one
  the record used. At 00:41:58 to 00:42:08 it reads: "Yeah, I think the thing, roughly speaking,
  obviously, I think superintelligence is a point at which, further out into the future, a model is
  smarter and more capable than all humans combined."
- **The record's quote** matches the automatic track exactly: "you know" is included, and
  "super intelligence" is two words. The uploader's track drops "you know". Neither track is garbled
  in this passage, and the two agree on every word that matters. So the quote is a fair verbatim
  rendering, but the uploader's track is the better source.
- **Fair `about`?** Yes. He is answering Patel's request to tell superintelligence from AGI, so the
  passage is partly a definition, but "further out into the future" is his own placing in time, and
  it names no span. The notes rightly treat 00:43:13, "if we are approaching that point,
  superintelligence, in the next few years", as a supposition and not a forecast.
- Suggestions: change `checked_how` to the uploader's track, and if the 25-word limit applies,
  quote "superintelligence is a point at which, further out into the future, a model is smarter and
  more capable than all humans combined" (21 words).

## 6. Huang, "AGI has arrived" (X reply, 2026-09-06): CONFIRMED

- **Source and date.**
  - The post: `2096700264569090384` by @JensenHuang, 2026-09-06T20:41:12Z on both the embed
    service and fxtwitter. 13:41 Pacific is correct.
  - It is a reply to Chase Lochmiller's post `2096445087505055891` (2026-09-06 03:47Z),
    "Congratulations to our friends at @OpenAI! I guess this makes Abilene the birthplace of AGI!".
  - The account is verified as an individual, describes itself as "Founder and CEO of NVIDIA", and
    has about 1.14 million followers. Coverage of his first posts on X, in late July 2026, matches,
    as does broad coverage of this post (Fox Business, The Next Web, the Washington Examiner).

  The text matches the quote exactly, line breaks aside. Role: chief executive of NVIDIA, a chip
  company, which qualifies.
- **Judgement point, does a present-tense "it's here" belong here?** Yes. The folder holds words
  on when AGI arrives that name no year and no span, and "AGI has arrived" answers "when" with "now".
  Amendment A30 kept his "we've achieved AGI" remarks out of the dated claims because they forecast
  nothing that a later date could check. That reason keeps them out of the claims, not out of this
  folder, which did not exist then. Leaving the record out would show the industry's loudest "it's
  here" as silence. The `about` sentence is fair.
- **Small points.**
  - "in 4 years" is a length of time inside the quote. It looks back, as the notes say, and the
    validator catches only written years. Trimming the quote to "AGI has arrived. Congratulations
    @OpenAI team." avoids the question and meets the 25-word limit.
  - The notes cite the Lex Fridman remark of 2026-03-23, but not the softer remark of 2026-08-26
    ("for many tasks, we could say that we've already achieved AGI"), which
    `docs/claims-ledger-proposal-2026-10-17.md` already records. It is worth one line.

---

## Counts

CONFIRMED 3 (Musk, with a one-phrase wording fix; Suleyman; Huang). FIX NEEDED 3. COULD NOT VERIFY 0.
Cross-cutting: ten of eleven undated-words quotes are over the 25-word limit, and the validator does not check it.

- **Pichai, "sooner rather than later": FIX NEEDED.** The quote starts at 00:42:46, not 00:42:29. The notes leave out his
  "three years from now ... it'll be very, very powerful" (00:45:38), which needs a ruling on whether it is a dated claim.
- **Nadella, "today's Super Intelligence systems": FIX NEEDED.** "Super Intelligence" is the official new name for AI under
  the order of 2026-09-29, used that way throughout the article. It is not a view on when superintelligence arrives, and
  Musk's renaming posts were set aside for the same reason. Drop the record.
- **LeCun, "it will take time": FIX NEEDED.** The `[...]` cut removes "ça va pas arriver l'année prochaine", a forecast that
  it will not happen by a date, which the method makes a claim. The same talk also says superintelligence "in 2 or 3 years"
  is "faux". Enter these as dated claims, not undated words.

## Undated words: the other five, and the 'none found newer' searches

# Check of the claims-ledger reframe (pull request 27): five undated-words files, and four "nothing newer" searches

Read only. Nothing in the pull request's checkout was changed. Checked on 2026-10-19.
New downloads are in scratchpad folders `dl4-u2-1` to `dl4-u2-14`, `dl4-u2-web` and `dl4-u2-liang`.

**A problem that affects four of the five files: the quotes are too long.** The brief, and the
method's field table for claims, cap a quote at 25 words. The four spoken quotes run 41 words
(Altman), 41 (Hassabis), 39 (Mensch) and 41 (Zuckerberg). Legg's is 13. The validator does not
catch this: `check_words` in `scripts/validate.py` does not apply the 25-word limit
(`CLAIM_QUOTE_WORDS`) that `check_claims` applies at line 688. The method's "Undated words"
section does not state the limit either. Either cut the quotes and add the check, or have the
method say plainly that the limit does not apply to undated words. Suggested cuts, each
copied exactly from the source, are given under each item.

**What the page shows.** I ran the page's own selection logic (`leaders_now` in
`scripts/chart_style.py` and the test at `scripts/site.py` line 1127) again over the data. All
five files come out newer than the person's latest dated forecast of AGI or beyond, so all five
are shown:
- Altman: latest dated forecast 2026-08-26.
- Hassabis: 2026-07-15, a repeat of an earlier forecast.
- Legg: 2025-12-11.
- Mensch and Zuckerberg: none.

YouTube refused caption downloads with "429 Too Many Requests" for most of this session (I made
more than six attempts per video, spread over about 30 minutes). Where that stopped a check, I say so.

---

## Part A

### 1. Altman, 2026-09-01, "superintelligence may happen short-term": FIX NEEDED (quote length); exact wording COULD NOT VERIFY

- **Source and date: confirmed.** The video VeizK1M7V7E is on the official "Sources Podcast"
  channel, titled "Sam Altman on Astra, AGI, and the future of OpenAI", uploaded 2026-09-01.
  Alex Heath posted the episode on X at 2026-09-01 17:00 universal time. The description says
  the conversation "was recently filmed in two parts and in collaboration with TIME". Its
  chapter "Recursive Self-Improvement and IPO" starts at 57:07, which fits the file's locator
  (57:59 to 58:15).
- **Exact wording: not verified by me.** The captions returned 429 on every attempt. The words
  are corroborated in a cleaned-up form by Andrew Curran's post of 2026-09-01 17:16 universal
  time (https://x.com/AndrewCurran_/status/2094836825420685465, read through api.fxtwitter.com).
  It quotes "I did not think we would be on a short-term trajectory to superintelligence a year
  ago. Now I think it may happen." So the substance and the date hold. The filler words in the
  file ("kind of like you know like") could not be checked against the captions.
- **Role:** chief executive of OpenAI. Qualifies.
- **No year or length of time:** correct. "Short-term" and "a year ago" do not date the arrival.
- **`about`: fair.**
- **Newer than his latest dated forecast:** yes, by publication date (2026-09-01 against
  2026-08-26). Note that the dated claim of 2026-08-26 comes from Heath's TIME profile, and the
  podcast was filmed with TIME, probably in the same sittings. The ordering therefore rests on
  publication dates, not on two separate occasions. The `when_note` already says this. That is
  enough, but the master may want it said on the page.
- **Fix:** 41 words. A 23-word cut, exact from the file's own text: "a short-term trajectory of
  super intelligence a year ago. Now I think it may happen. Um I'm not confident it's going to
  happen." Check it against the captions when YouTube allows.

### 2. Hassabis, 2026-09-11, "a few years from full AGI": FIX NEEDED (quote length); exact wording COULD NOT VERIFY

- **Source and date: confirmed.** The video rDteJAuKiBI is on the Royal Society of Arts'
  channel, uploaded 2026-09-11, 63 minutes long. The description says he receives the RSA
  Albert Medal, in conversation with Hannah Fry, recorded at the RSA in London. No event date is
  given, so the `when_note` is right. Chapter marks put "Demis Hassabis' acceptance remarks"
  between 13:13 and 23:02. The quote at 20:10 is therefore in his own prepared remarks, not an
  answer to a question.
- **Exact wording: not verified by me.** The captions returned 429 on every attempt. I found no
  published transcript.
- **Role:** the description calls him "Co-founder and Chair of Google DeepMind and Chief
  Scientist at Alphabet". Qualifies under A30 (chair of the company, or its chief scientist).
  The file's note says the same.
- **No year or length of time:** "a few years" is undated, as John ruled on 2026-10-19.
  "The eve", "the foothills" and "a few years" carry no number.
- **`about`: fair.**
- **Newer than his latest dated forecast:** yes. 2026-09-11 against 2026-07-15, which is a
  repeat recorded through `repeated_on` of the forecast of 2026-06-02.
- **A point for the master: his newest words are five days later.** On 2026-09-16 he signed,
  with Shane Legg and James Manyika, the DeepMind Institute's launch essay
  (https://institute.deepmind.com/essays/introducing-the-deepmind-institute/, read 2026-10-19,
  byline of all three, dated Sep 16, 2026). It says "we're now approaching artificial general
  intelligence" and "we expect those gaps to be closed soon". The file's note gives a reason for
  keeping his spoken words instead: they are his own, while the essay has three signers. The
  page itself says its pieces "should not be read as Google's official view". Keeping the spoken
  words is defensible. But under the "latest words" rule this is a choice someone should own,
  ideally with a line in the method.
- **Fix:** 41 words. A 25-word cut: "on the eve of you know the foothills of the singularity I
  like to call it you know a few years away from full AGI." Check it against the captions.

### 3. Legg, 2026-09-16, "AGI on the horizon": CONFIRMED (one point for the master)

- **Source:** his own post on X. Read through api.fxtwitter.com on 2026-10-19: written by
  @ShaneLegg, created "Wed Sep 16 14:25:57 +0000 2026". The second sentence reads exactly "AGI is
  on the horizon - we need deeper understanding of its implications." The attached article is
  "Introducing the DeepMind Institute".
- **Date, role (chief AGI scientist of Google DeepMind) and primary source:** all correct.
- **No year or length of time:** none.
- **Quote length:** 13 words.
- **`about`:** "AGI is within sight; he gives no date." Fair.
- **Newer than his latest dated forecast:** yes. 2026-09-16 against 2025-12-11.
- **Point for the master: a possible dated restatement on the same day.** The Reuters copy
  (investing.com, "Published Sep 16, 2026, 11:23 AM") reports, citing the Financial Times:
  "Legg remains 'comfortable' with his forecast of a 50% chance of achieving 'minimal' AGI by
  2028". Only "comfortable" and "minimal" are his quoted words; the rest is the reporter's
  paraphrase. The builder logged it as not a primary source (legg-words-03, the Reuters copy).
  The method does allow an entry marked `coverage_only` for a claim found only in coverage. If
  this restatement were entered, his latest dated forecast would become 2026-09-16, and the X
  post would no longer count as newer, so the page would not show it. Leaving it out is within
  the rules. If it is entered, these words drop off the page.

### 4. Mensch, 2026-06-03, "AGI a direction, not an arrival": FIX NEEDED (quote length)

- **Source:** video 325gGv0eWV8 on CNBC International, "Europe Wants an AI Champion. Can
  Mistral Deliver?", uploaded 2026-06-03. I read the English caption track (`en`; the separate
  automatic track is `en-orig`).
- **Exact wording: confirmed.** At 00:44:23 to 00:44:36: "So, if you take AGI as the definition
  of accelerating technological progress, which is rather a direction than a point of arrival,
  then really, we are building AGI, but it's really a direction and it's a very messy
  direction." The supporting passage at 00:39:08 to 00:39:18 is also as the file says: "I think
  it's too simple an idea ... We are not there yet."
- **Role:** chief executive of Mistral AI. Qualifies.
- **No year or length of time:** none in the quote. Nearby, "15 years in between 2010 and 2025"
  is about the past, not about when AGI arrives.
- **`about`: fair.** "We are not there yet" does follow his point that AGI needs "a very strong
  understanding of the physical space".
- **Newer than his latest dated forecast:** he has no dated forecast of AGI or beyond, so it is
  shown.
- **Newer words:** my search found nothing after 2026-06-03 on when. Note that mensch-words-05
  (the France Inter clips) were not read.
- **Fix:** 39 words. A 24-word cut: "AGI as the definition of accelerating technological
  progress, which is rather a direction than a point of arrival, then really, we are building
  AGI".

### 5. Zuckerberg, 2026-09-23, "personal superintelligence within reach": FIX NEEDED (quote length)

- **Source:** video SdKFDIAGF24 on Meta's channel, "Meta Connect Keynote 2026". The upload time
  is 2026-09-24 03:02:55 universal time, which is 2026-09-23 20:02 Pacific, so `when` is right.
  Strictly, YouTube's own upload date (in universal time) reads 2026-09-24; `checked_how` could
  say "Pacific".
- **Exact wording: confirmed.** At 00:01:19 to 00:01:43 the captions read exactly as the file
  quotes them, from "What a wild time to be building" to "help you achieve them".
- **Who is speaking: confirmed.** At 00:00:42 he is greeted with "Hey, Mark". At 00:13:55
  someone says "I'll pass it back to Mark", and at 00:14:04 he resumes with "Alex, and
  congrats."
- **Role:** founder and chief executive of Meta. Qualifies.
- **No year or length of time:** "now within reach" and "soon" carry neither.
- **The two passages in `notes` are confirmed:** 00:04:11 ("in the coming years, I expect that
  Muse is going to grow into the personal superintelligence") and 00:15:35 ("personal
  superintelligence will not only come first").
- **`about`: fair.** It might add that "personal superintelligence" is Meta's own name for its
  assistant product, but the term is his.
- **Newer than his latest dated forecast:** he has none, so it is shown.
- **Fix:** 41 words. A 25-word cut: "What a wild time to be building. Delivering personal
  superintelligence is now within reach. Soon, everyone is going to have an extremely capable
  personal agent". Or just the second sentence.

---

## Part B

### Dario Amodei, after his latest dated forecast of 2026-06-10: nothing found that qualifies; search log incomplete

His four "words" search rows (amodei-words-01 to 04) cover:
- his essay of 2026-09-12;
- CBS Sunday Morning's extended interview of 2026-09-13;
- a 93-second CNN clip;
- one web search.

**What I read:**
- **"We must pace the frontier"** (darioamodei.com, 2026-09-12). Its spans are not about when
  powerful AI arrives:
  - "in 6–12 months such a swarm could be capable of taking over the entire internet"
  - "an extra year or two before models reach critical levels of capability"
  - "1–2 years" of interpretability work
  - "the next 3–5 years" for China policy

  I agree with amodei-words-01: nothing qualifying.
- **Bloomberg Originals, "Inside the Mind of Anthropic CEO Dario Amodei | The Circuit |
  Extended Interview"** (x2VHFgyawPE, uploaded 2026-06-17, 70 minutes, captions read). This is
  newer than 2026-06-10 and is not in the log. Nothing qualifies:
  - 00:26:41: "I don't know how far we are from Claude being able to write better than me.
    We're not quite there yet." That is about his own writing, not AI better than people at
    most things.
  - The rest is about the "smooth exponential", spending on computing, jobs, and cyber
    capabilities "12 months from now".
- **CNN, "Anthropic CEO tells CNN how AI 'agent swarms' could threaten humanity"**
  (_JbDZ2Rj2SA, uploaded 2026-09-15, 8 minutes, captions read). He restates the essay's "6 or
  12 months" swarm worry, which is not about arrival. The second half is another guest. Nothing
  qualifying.

**Found but could not read** (YouTube 429 on captions). These are newer than 2026-06-10 and are
not in the log; each should get a log row:
- USA TODAY, Dreamforce 2026 (KLH4Y-S2lMc, 2026-09-15, 7 minutes)
- USA TODAY, "Dario Amodei, Sam Altman on AI ... 'the world is right to be afraid'"
  (WobvAD-lHPQ, 2026-09-16, 12 minutes). It may also hold newer Altman words.
- USA TODAY, Amodei, Zuckerberg and Pichai with Donald Trump (D8lDoI4yLLA, 2026-09-29,
  4 minutes). It may also hold newer Zuckerberg words.
- Forbes Breaking News (N9GHj5ZFqrs, 2026-09-30, 1 minute)
- Forbes Breaking News (--15jyEWE3I, 2026-09-12, 6 minutes)

Coverage of the Dreamforce session of 2026-09-15 (kioncentralcoast.com, cryptobriefing.com)
describes it as about safety and slowing down. No timing words are reported.

**Verdict:** "none found newer" holds for what could be read. The log is incomplete, and five
short clips remain unread.

### Ilya Sutskever, after his latest dated forecast of 2025-11-25: CONFIRMED, nothing found

- **National Academy of Sciences award message** (ZCX1ag0URUk, uploaded 2026-05-05, captions
  read). "AI will unquestionably and unequivocally will continue to grow in impact" and
  "staggering" impact. No words on when AGI or superintelligence arrives. Not in the log; worth
  a row.
- **His posts on X** (texxr.com archive, newest 2026-07-27/28 "Time to scale that SSI:"):
  nothing on when. This agrees with sutskever-words-04.
- **The Nvidia partnership statement of 2026-07-27:** about scaling, as the log says.
- **Web searches for September and October 2026:** only rumours about Safe Superintelligence's
  first model, and the TIME100 AI profile of 2026-08-27, which is someone else's words.
- **"Smarter Than Us | Ilya Sutskever"** (Signal Labs, QpCYiIFHyws, uploaded 2026-10-09): a
  third-party channel, probably a compilation of old clips. The captions were refused (429), so
  it was not read. It is not a primary new appearance unless it holds new footage.

### Liang Wenfeng, after his latest dated forecast of 2024-07-22: CONFIRMED, nothing primary found; leaving out the investor-meeting transcript is right

- **No public interview, speech or post** after 2024-07-22 turned up in English or Chinese
  searches. This agrees with liangwenfeng-words-04.
- **The closed investor meeting.** The meeting was on 2026-05-20, and the text circulated from
  2026-07-22 and 23. The fullest version is a GitHub repository
  (github.com/iamsophie/deepseek-liang-wenfeng-investor-meeting). Its own README says the text
  is:
  - "语音识别自动转写 + AI 整理" (machine speech recognition, then edited by AI),
  - "未区分说话人" (no speaker labels),
  - and that "个别专名与数字可能存在识别误差，引用请以原录音为准" (names and numbers may be
    misrecognised; cite the original recording).

  The recording itself is not public. Neither Liang nor DeepSeek has published or confirmed
  the text.
- **Leaving it out is right under the primary-source rule.** A primary source is the person's
  own words, a transcript or recording that can be traced to the event, or a printed question
  and answer. This text is none of those: an anonymous, machine-made and AI-edited text of a
  closed meeting, whose words cannot be checked against any recording. The ledger needs exact
  words, and these cannot be confirmed.
- **What the log should add.** Bloomberg reported (through thenextweb.com and sedaily.com,
  2026-07-26) that DeepSeek paused a fundraising round partly over Liang's "frustration over
  online reports about his comments". National Business Daily (每日经济新闻) reported that
  investing institutions confirmed the meeting took place and that the content was accurate. So
  the meeting is real and the substance is probably right. But "the substance is accurate" is
  not exact wording. liangwenfeng-words-03 should record these two reports beside "not
  authenticated", so the ruling reads as made with them in view.
- **It would not have changed the date picture anyway.** Asked "AGI 还需要多久？" (how long
  until AGI?), the transcript has him answer that Chinese models can match foreign ones within
  "一两年" (one or two years), or this year, "但它还不是 AGI" (but that is not yet AGI), and
  "它得能够持续学习吧" (it must at least be able to learn continually). There is no date for
  AGI. If it were admitted, it would only be undated words. It would then be shown on the page,
  so the exclusion does affect what the page says.

### Kai-Fu Lee, after his latest dated forecast of 2026-09-23: CONFIRMED, nothing found (one borderline line, two small log fixes)

- **Bloomberg New Economy panel** (ACr_u7EnaCQ, "Tech Leaders on Moving AI From Pilot to
  Scale", uploaded 2026-10-14, captions read). At 00:03:13 to 00:03:18: "these are so smart.
  You can say they're like IQ 300 models." That describes today's models as an image for hiring,
  not a forecast of when AI is better than people at most things. It is borderline next to
  Huang's admitted "AGI has arrived", but I agree with leaving it out. The log could say
  "borderline" rather than just "nothing on when". The rest of the panel is about AI agents in
  companies.
- **Yang Lan interview** (-MmI1WvOaKY, Yang Lan Studio, "從模型到企業，AI如何真正創造價值？",
  42 minutes). YouTube reports no captions of any kind, so I could not read it. Note that
  YouTube gives an upload date of 2026-10-18, while kaifulee-words-03 says "aired 2026-10-08".
  One of them should be checked; it may have been broadcast earlier.
- **Globalization think tank (CCG) conference, 2026-10-17 to 18.** CCG's own Weibo post
  (sina.cn, posted 2026-10-20 10:50 Beijing time) quotes him: "人工智能正在自我快速迭代" (AI is
  rapidly improving itself) and "AI作为一项技术并没有泡沫" (AI as a technology is not a bubble).
  It links a video (t.cn/AXlkuxpm) that I did not open. Nothing on when. I found no full text.
- **Other uploads since 2026-09-23** are either older, already in the log, or not his own
  appearances:
  - The Semafor conversation of 2026-09-17 is logged as kaifulee-claims-049.
  - A 大师兵法 re-upload of 2026-09-16 is a third-party compilation.
  - A Weibo video of 2026-10-18 seems to be a clip of the September Bloomberg interview.

---

## Counts

- **Part A:** 1 CONFIRMED (Legg); 4 FIX NEEDED (Altman, Hassabis, Mensch, Zuckerberg); exact
  wording COULD NOT VERIFY for 2 of those (Altman, Hassabis).
- **Part B:** 3 CONFIRMED with nothing newer found (Sutskever, Liang, Lee); 1 holds for what
  could be read but needs log rows and five unread clips (Amodei). No qualifying newer words
  were found for any of the four.

Why each FIX NEEDED:
- **Altman:** the quote is 41 words against the 25-word limit. The captions could not be
  fetched, so the filler words are unchecked; the substance is confirmed by a post of the same
  day.
- **Hassabis:** the quote is 41 words against 25. The captions could not be fetched, so the
  exact words are unchecked. His co-signed essay of 2026-09-16 is newer; the choice between
  them needs owning.
- **Mensch:** the quote is 39 words against 25. Everything else is confirmed at the captions.
- **Zuckerberg:** the quote is 41 words against 25. Everything else is confirmed at the
  captions.
- **Across the board:** the validator's check of undated words does not enforce the 25-word
  limit, so this went through unnoticed.

## The three possibly-missing dated claims

# Three possibly missing dated claims (pull request 27 check, read only)

Checked 2026-10-19 against the checkout at `scratchpad/pr27` (commit 93f1e6d). Rules applied: the
admission rule in `docs/claims-ledger-method.md` (looks forward, about AI, carries a date or a length
of time, primary source); John's readings of 2026-10-19 ("a few years" and "as little as X" are
undated; a forecast that something will NOT happen by a date is a claim); and the page code in
`scripts/chart_style.py`. In that code, a person's "what they say now" entry holds only the drawn
forecasts (AGI, superintelligence or AI better than people; no chance tails) from the **latest day**
they gave one. `nearest` ignores "not before" forecasts. The "latest dated prediction of any kind"
line takes the newest claim of any kind by its date said.

Nothing in the checkout was edited.

---

## 1. Mustafa Suleyman, Decoder (The Verge), 2026-06-08: not in five years, the singularity decades away

**Verdict: FIX NEEDED. A dated claim is missing, and it must go in before the page publishes.**

**Source.** YouTube, channel "Decoder with Nilay Patel", upload date 2026-06-08. Title: "Microsoft AI
chief thinks superintelligence is near, but won't take your job | Decoder".
https://www.youtube.com/watch?v=Z4bwAjR7azM . I read the automatic captions (the original-language
track) as text with timestamps on 2026-10-19. Captions are in
`scratchpad/dl4-m-1/`, flattened copy in `scratchpad/scripts-m/decoder0608.txt`.

**The question (01:08:04 to 01:08:30).** The host cites Demis Hassabis saying "we are in the foothills
of the singularity" and asks whether Suleyman agrees.

**His words.**
- 01:09:12 to 01:09:16: "to be clear I don't think this is something that is going to knock on the door in the next 5 years."
- 01:09:16 to 01:09:25: "what Demis is referring to in the singularity is something that at least my take is you know decades away."
- 01:09:28 to 01:09:36: he defines the singularity as "the point at which a super intelligence can recursively self-improve" (paraphrased here).
- 01:09:40: "I think that's a long way off".
- 01:10:44 to 01:10:52, giving his definitions: "The singularity is a point way beyond that where a super intelligence can actually self-improve itself."

**Does it meet the admission rule?** Yes.
- Speaker and role: chief executive of Microsoft AI, the same role as his other 2026 claims.
- About AI and looking forward: yes.
- Date: "the next 5 years" is a length counted from the day it was said. Under John's reading 2 it is a forecast that something will not happen by a date, so it is a claim, scored at about 2031-06.
- Primary source: a recording on the show's own channel.

One judgement to flag. "This" in "I don't think this is something…" follows a sentence about society's job shifting to deciding what to invent. Its plainest reading is the singularity: that was the question, and the next sentence names it. The entry should quote both sentences and say so in its notes.

**What it says arrives, and in what shape.**
- What arrives: the singularity, which he defines as a superintelligence that improves itself, "way beyond" superintelligence. The nearest category is `superintelligence`, with `arrives_term` "the singularity". It is beyond AGI, so it is drawn.
- Shape: `not_before`, with `due` 2031 (five years from 2026-06-08).
- "Decades away" adds a later floor of at least about twenty years, which would be not before about 2046. This is like "it will take at least a decade", which reading 2 admits, but "decades" names no exact number, close to reading 3's "a few". I suggest scoring the clean five-year part and recording "decades away" in the notes, with the question flagged for John.

**Is it his latest dated forecast of AGI or beyond?** Yes. His drawn forecasts in `data/claims/`:
- 2024-12-09: AGI in 5 to 7 years.
- 2025-04-04: AGI "a good decade or so away".
- 2026-02-12: "professional-grade AGI" in 2028 to 2029 (`2026-02-12-suleyman-professional-agi-coming-into-view`). This is the latest now.

2026-06-08 is newer. His only later timing words are the undated record of 2026-09-17 ("superintelligence … further out into the future"). The 2026-09-25 claims are about Microsoft models (`other`).

**Effect if it is left out.** Because the page keeps only the latest day's drawn forecasts, adding this record changes his "now" entry:
- It would move from "professional-grade AGI 2028 to 2029" to "the singularity not before 2031".
- His `nearest` year would go from 2028 to none, because "not before" forecasts are ignored.
- So he would drop out of the leaders who name a year in the figure's title and the home-page sentence.

Without the record, the page shows a February forecast as what he says now, when he spoke on a dated horizon four months later.

Side note for John: entering it also pushes his February AGI date off the "now" line, although the two do not contradict each other. Whether the "latest day" rule should keep the latest forecast for each kind of arrival is a question for him. Under the rule as written, the record must go in.

**Other words in the same episode.**
- 00:07:23: "super intelligence is coming. I think it's just around the corner." Undated words, older than the 2026-09-17 record, so not needed.
- 01:00:29 to 01:00:50: ambient AI "not in the next like three to five years", with the supporting infrastructure "probably going to end up emerging in the 2030s". This is a possible `other` claim and is not drawn.
- 01:02:43 to 01:02:56: LLMs "enough to take us a very long way in the next three years", with full superintelligence "still an open question". Not a dated forecast of arrival.

**Search gap.** The claims search log has no row for this episode. `suleyman-claims-040` read the Decoder episode of 2026-09-17 and two CNBC uploads, but not Z4bwAjR7azM. Only the undated-words search (`suleyman-words-03`) found it, and it flagged the episode.

---

## 2. Mustafa Suleyman, The Rest Is Politics: Leading, 2026-09-28: healthcare in 18 months to 5 years

**Verdict: CONFIRMED that a possible dated claim exists. It is not about AGI or beyond, so it can follow.**

**Source.** YouTube, channel "The Rest Is Politics: Leading", upload date 2026-09-28. Title: "Can AI
Stay Under Human Control? | CEO of Microsoft AI, Mustafa Suleyman".
https://www.youtube.com/watch?v=_VyF0naZ4AI . YouTube refused the first caption download (HTTP 429, too many requests). The second try returned the original-language automatic track. Captions are in `scratchpad/dl4-m-2/`, flattened copy in `scratchpad/scripts-m/trip0928.txt`. The claims pass's row `suleyman-claims-045` recorded this episode as not read.

**His words.**
- 00:27:35 to 00:27:48: "I absolutely guarantee that sometime in the next few years we are going to have a coding moment for healthcare". By this he means streaming "an accurate prediction of what's going to happen in the electronic health record".
- 00:28:02 to 00:28:04: "It is going to happen. I hope it happens in the next 18 months."
- 00:28:06 to 00:28:13: a Mayo Clinic partnership to train a new foundation model for health.
- 00:28:13 to 00:28:16: "It might be 5 years, I don't know, but it is definitely going to happen."
- 00:28:20 to 00:28:26: it "will reduce the cost of production of super intelligent healthcare to near zero marginal cost".
- 00:28:33 to 00:28:39: "The same thing's going to happen … in energy, in material sciences, in drug discovery. Um it might take a little longer like 5 to 10 years".

**Does it meet the admission rule?** Borderline, leaning yes. The firm forecast is undated ("the next few years", reading 3). The dated words are a hope (18 months) and an outer possibility (5 years). Read together, they give a range of about 18 months to 5 years: `due_early` about 2028-03, `due` about 2031. If it is judged too hedged, the method says a truly borderline case stays out and is logged as borderline. The energy, materials and drug-discovery line ("5 to 10 years") is a second possible claim of the same kind.

**What it says arrives.** `other`. The thing forecast is a health prediction model, "a coding moment for healthcare". "Super intelligent healthcare" is his name for its effect in one field, not general superintelligence. This matches how `suleyman-words-06` read his Bloomberg "medical super intelligence" (one field only). It is not drawn.

**Is it his latest dated forecast of AGI or beyond?** No, it is not about AGI or beyond. Two other effects:
- If admitted, it would be his latest dated prediction of **any kind**. It is newer than the 2026-09-25 Microsoft-model claims, so the "latest prediction of any kind" line under his entry would be one claim out of date until it is entered.
- His newest timing words on AGI or beyond stay the undated record of 2026-09-17.

Elsewhere in the episode:
- 00:36:38 to 00:36:53: "extrapolate three more orders of magnitude to GPT9 in let's say 2028 or 2029". An invitation to extrapolate computing power, so a hypothetical and a compute forecast. It stays out.
- 00:40:49: training runs costing tens of billions "in the next couple of years". A business forecast. It stays out.

**Can follow.** The figure and the home-page sentence are unaffected.

---

## 3. Shane Legg, 50% chance of minimal AGI by 2028, reported by the Financial Times, 2026-09-16

**Verdict: COULD NOT VERIFY a primary source. It repeats a forecast already in the ledger, so it can follow.**

**What exists.**
- **The FT article:** https://www.ft.com/content/0fc3ae6d-732e-4f08-950e-8669b1fcfd8e . It returned HTTP 403 (a security check) on two tries with curl. Web search cannot reach ft.com.
- **The Reuters copy** on investing.com, dated 2026-09-16:
  https://www.investing.com/news/stock-market-news/deepmind-cofounder-warns-ai-capabilities-must-not-outrun-safety-controls-ft-reports-4904088 .
  It reads: Legg remains "comfortable" with his forecast of a 50% chance of achieving "minimal" AGI by 2028, "the report said". Only the words "comfortable" and "minimal" are his. The rest is the reporter's paraphrase.
- **aiweekly.co** (https://aiweekly.co/alerts/legg-opens-deepmind-institute-calls-agi-claims-premature) repeats the same paraphrase from the Reuters copy.
- **His own posts:** I read his recent posts on X through api.fxtwitter.com, back to late September 2026. They include the 2026-09-29 consciousness survey and the 2026-10-08 essay announcement, and his 2026-09-16 launch post is already a record. None names 2028 or a chance.
- **The institute's home page** (institute.deepmind.com) has no 2028 and no chance figure.
- **Video, podcast or printed Q&A:** I found none for this interview.

**Does it meet the admission rule?** Not as a primary-source claim. It is coverage only, with the forecast in the reporter's words. At most it could be noted as a `coverage_only` sighting.

**What it says arrives, and in what shape.** `agi` ("minimal AGI"). A 50% chance by 2028, which the ledger reads as `year` 2028.

**Is it his latest dated forecast of AGI or beyond?** It would be on its date, but it is an unchanged repeat. The ledger already holds "50% by 2028" in `2010-12-10-legg-human-level-agi-mean-2028`. Its `repeated_on` list runs to 2025-12-11, including "are you still 50/50 by 2028?" "Yes" on Google DeepMind's podcast. That same 2025-12-11 episode gives his other current forecasts: minimal AGI in "about two or so" years (2027), a 1-to-5-year range, and full AGI within a decade.

So his "now" entry already shows 2028 among his latest forecasts, in his own words. His undated record of 2026-09-16 ("AGI is on the horizon") is already shown as newer words, and its notes record this FT report.

If 2026-09-16 were added to `repeated_on` from coverage, it would become his latest day. The page would then show **only** the 2028 record and drop the 2027 and full-AGI forecasts from "now". That would make his entry thinner, not more correct, and would rest on a paraphrase.

**Can follow.** Leaving it out does not make the "now" figure wrong.

**A small fix to the search log.** `legg-claims-013` says the 2026-09-16 remark "carries no date". In the coverage it does carry one (the 50%-by-2028 paraphrase). It is simply not in his own words. `legg-words-03` describes it correctly.

---

## Counts

- CONFIRMED: 1 (item 2: the claim exists, it is `other`, and it can follow)
- FIX NEEDED: 1 (item 1)
- COULD NOT VERIFY: 1 (item 3: no primary source; an unchanged repeat; can follow)

Reason for the FIX NEEDED: on Decoder of 2026-06-08 (01:09:12) Suleyman said the singularity is not coming "in the next 5 years". That is a dated "will not happen" forecast of beyond-superintelligence, and it is newer than his 2026-02-12 professional-AGI forecast. Under the page's latest-day rule, his "what they say now" entry and the computed headline are wrong until it is entered. The claims search also never read this episode.
