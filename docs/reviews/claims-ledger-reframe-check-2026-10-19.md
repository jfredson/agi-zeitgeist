# Independent check of the claims-ledger reframe (pull request 27), 2026-10-19

**Recheck (commit `16fc6fe`): merge after two small wording and counting fixes (A and B
below). Neither needs another check from this session.** John's pending ruling on Kokotajlo and
Aschenbrenner does not change any published number. With them in or out, the academics' middle
year is 2030 and the headline is "7 of 12".

# Recheck at commit `16fc6fe`

The build, `validate.py` (328 claims, 9 undated passages, 5,007 search-log rows), `check_news.py`
and its tests pass. The panel is still 37. Each fix was checked against the data, the code and,
for the new claims, the sources.

| fix | result |
|---|---|
| 1. The academics' band | **Done as described.** Each person counted once at their latest dated guess since 2023, by the nearer year. With the two who worked at OpenAI left out, the band is five people (Yudkowsky 2027, Bengio 2030, Cotra 2030, Marcus 2036, Hanson 2094), drawn by name; the middle is 2030. With them in it is seven people, and still 2030 and still 7 of 12, so John's ruling on them moves nothing published. |
| 2. AGI forecasts filed as capability claims | **Done.** The fields are on Huang (2023-11-29, 2024-03-01) and Suleyman (2025-09-24, 2025-11-14, 2026-02-12), and the figures read them. Huang appears at "by 2029". The 2026-02-12 white-collar claim is filed as AGI on the strength of his run-up in the same answer ("human-level performance on most, if not all, professional tasks"); that is a fair reading. |
| 3. Suleyman on Decoder | **Confirmed** at the captions (01:09:12 to 01:09:25): "I don't think this is something that is going to knock on the door in the next 5 years", with his definition of the singularity beside it. It is filed as not before 2031. |
| 4. LeCun, Sciences Po | **Confirmed** at the French captions. The first quote (01:07:51 to 01:07:59) is "ça va pas arriver l'année prochaine, hein. Mais on aura des machines ... plus intelligents que les humains dans tous les domaines", and the cut ("à un certain moment qui seront") is fair. The second quote (01:00:35 to 01:00:41) is "dans 2 ou 3 ans, donnez-nous euh 300 milliards. Mais c'est faux." The undated record is withdrawn and the log says why. |
| 5. Nadella | **Done.** Withdrawn, and his third undated-words search row (`nadella-words-03`) gives the reason. |
| 6. LeCun's "non-negligible likelihood" | **Done.** It is now a chance tail. |
| 7. Ranges by their nearer end | **Done.** The "now" title is "7 of 12 industry leaders now name a year before the academics' middle one, 2030". The "moved" title is **"5 leaders brought their dates nearer, 2 held them, 3 pushed them later"**. That is not the "6 nearer, 2 held, 2 later" given in the managing session's message, but it is what the code computes, and it is right for the code. |
| 8. Undated quotes | **Done.** All nine are 25 words or fewer; the method and the validator state the limit. |
| 9 to 17 | **Done.** These cover: Pichai's locator and his 00:45:25 note; Musk's "a later model"; Suleyman's quote from the uploader's track; the own-word rule in the method; a not-before year on every such forecast (Hassabis 2011 is drawn at 2031); LeCun's "several years" as "by 2034"; the figure's note that a date may be when it was published; search-log rows for Amodei's clips, Sutskever's award message and the Yang Lan date; Legg's 13th claims search corrected; and Huang's quote cut to "AGI has arrived. Congratulations @OpenAI team." |
| Extras | **Done.** The frontier chart's builder definition now matches the tag ("led, founded or done senior research at"). The home page's five points read First to Fifth in order. |

### A. Huang's "pushed later" is a rounding effect

He said "within the next 5 years" on 2023-11-29 and "in 5 years time" on 2024-03-01. The
same five years, restated fourteen weeks later, lands in the next calendar year (2028, then
2029). The "moved" figure counts a change of a year or more as a move, so the restatement reads
as Huang pushing his date later.

Count a forecast restated with the same span as held, or compare the exact end dates (the day
said plus the span). The title then reads "5 nearer, 3 held, 2 later".

### B. Two numbers for the academics on the home page

- **Fifth point:** "the people studying them have come down ... to about 2033 in their guesses
  since 2023". This comes from the frontier-voices chart, which pools every guess since 2023
  and counts Kokotajlo and Aschenbrenner among the people who study it.
- **Claims sentence:** "the middle year of the academics' latest guesses, 2030, each person
  counted once".
- **The problem:** each sentence says how it counts, but a reader meets "about 2033" and "2030"
  for the same group a few lines apart.

Add half a sentence saying why they differ ("counting every guess since 2023 rather than each
person's latest"), or give the fifth point the per-person figure too.

### To note for John, no change needed now

- **"Generous" reversed for "will not happen" forecasts.** LeCun's "superintelligence in 2 or 3
  years is false" takes 2029 as its date and calls the later end "the generous one". For a
  forecast that something will not happen, the later end is the harder test for the speaker,
  not the generous one. The method's range rule was written for forecasts that something will
  happen. It needs a line on which end a "will not happen" range takes.
- **Still to follow, as agreed:** links inside the leader lines (18) and the figures' size on a
  phone (19).

# First check (commit `93f1e6d`)

**Verdict: merge after fixes.** Fixes 1 to 8 below come before the merge. Fix 1 needs a ruling
from John, because it changes the number in the new headline.

What holds:

- The design John agreed is built faithfully.
- Verdicts are only small notes: no count, rate, chip, chart title or share text carries one,
  and the status file has no verdict counts.
- The validator, the news check and its tests pass, and so does the build.
- The 84 timing claims are filed correctly, apart from the few named here.
- At 375 pixels wide nothing scrolls the page sideways.

What does not hold yet: the headline "8 of 11 industry leaders now name a year before the
academics' middle one, about 2033" rests on a band that is not what the page says it is, and on
a leader count that leaves out forecasts the ledger already holds. Several smaller things show
leaders saying the wrong thing now.

Checked at pull request 27's commit `93f1e6d`, in a separate checkout, by the session that
checked pull request 23. Nothing was pushed to the pull request's branch, merged or published.
The source checks were done by five helpers; their notes for each item are in
[`claims-ledger-reframe-check-2026-10-19-notes.md`](claims-ledger-reframe-check-2026-10-19-notes.md).

## Fixes before merging

### 1. The academics' band (needs John)

The band is "the middle half of their 26 dated guesses since 2023, 2028 to 2038, with its middle
at about 2033". It drives the claims page's first figure, its title, the home-page sentence and
the status file. Three things about it are not what the page says.

- **Who is in it.** The 26 guesses come from seven people: Daniel Kokotajlo (8), Yoshua
  Bengio (5), Ajeya Cotra (4), Gary Marcus (4), Leopold Aschenbrenner (2), Robin Hanson (2)
  and Eliezer Yudkowsky (1).
- **What it promises.** Amendment A31 defines the academics as the panel's members "who have
  never worked at a company that builds frontier AI". The home page calls them "the academics,
  the critics and the philosophers"; the claims page says "who have written about AGI and the
  singularity for decades".
- **Where that fails.**
  - Kokotajlo worked at OpenAI (2022 to 2024), and so did Aschenbrenner (2023 to 2024). Their
    10 guesses are 10 of the 26.
  - The frozen tag leaves them out because it marks leading, founding or a senior research
    role. A31's wording and the chart's subtitle ("anyone on the panel who has worked at a
    company that builds frontier AI systems") say something stricter.
  - Aschenbrenner's guesses date from 2024, not "decades".
- **How it is counted.** Each leader is drawn once, at their latest day. The academics are
  pooled: every guess since 2023, so Kokotajlo alone gives almost a third of the band. Older
  academic guesses sit beside the leaders' newest ones.

The middle year moves a lot with these choices, and so does the headline:

| how the academics are counted | guesses | middle half | middle |
|---|---|---|---|
| as built: every guess since 2023 by non-builders | 26 | 2028 to 2038 | about 2033 |
| without the two who worked at OpenAI | 16 | 2034 to 2073 | 2036 |
| each person once, at their latest guess (as the leaders are) | 7 | (seven people) | 2030 |

**The fix:**
- Count each person once, at their latest guess, to match how the leaders are drawn.
- Decide whether people who worked at a frontier company in a junior role belong on the
  academics' side.
- Make A31, the chart's subtitle and the home page say exactly that, and say the band is seven
  (or five) people.
- Then recompute the title and the home sentence.

On the per-person count, the headline would read about "6 of 12 name a year before 2030", with
fixes 2 and 3 applied. This is a call about what the headline means, so it is John's, not the
builder's.

### 2. Two leaders' AGI forecasts are kept off the figures by how they are filed

The figures draw only claims filed as `timing`. Two claims filed as `capability` are plainly
forecasts of AGI or beyond.

- **Jensen Huang, 2024-03-01** (SIEPR summit). The record's own prediction reads "If AGI means
  passing human tests, it is five years away". Also his 2023-11-29 DealBook claim ("AIs that
  can achieve those tests" within 5 years).
- **Mustafa Suleyman, 2025-11-14**: "achieving human level performance at most tasks ... quite
  likely in the next 5 years".

The "now" figure's footnote says Huang "has given no dated forecast of this kind". With his
2024 forecast drawn he appears at "by 2029", and the leader count becomes 12. Refile these two
(and check other capability claims for the same) as timing claims, or let the figures read the
new fields on capability claims too.

### 3. A missing dated claim that changes what Suleyman "says now"

On Decoder (The Verge) of 2026-06-08 he says, at 01:09:12 on the show's own upload:

- "I don't think this is something that is going to knock on the door in the next 5 years";
- at 01:09:16, that the singularity is "decades away".

That is a forecast that something will not happen, about superintelligence and beyond, said
as head of Microsoft AI. It is newer than his drawn forecast of 2026-02-12. Enter it: not
before 2031, with "decades away" noted for John. His "now" line then changes, and he leaves the
count of year-naming leaders. The claims search never read this episode; only the undated-words
search found it.

### 4. LeCun's undated record cuts out the words that date it

The record for 2026-09-16 (`2026-09-16-lecun-it-will-take-time`) marks a cut with "[...]". The
cut removes "ça va pas arriver l'année prochaine" ("it won't happen next year"). Its notes say
the words were dropped so the passage would stay undated.

- Under John's second reading that is a dated claim, a forecast that something will not
  happen.
- The same talk, at 01:00:36, also calls superintelligence "in 2 or 3 years" false ("c'est
  faux").

Enter both as dated claims, and drop or rewrite the undated record. Once they are in, it is no
longer newer than his latest dated forecast.

### 5. Nadella's undated record is not his view

"Today's Super Intelligence systems" (`2026-10-10-nadella-todays-super-intelligence-systems`)
uses the federal government's new name for AI. An executive order of 2026-09-29 tells agencies
to say "Super Intelligence" for "Artificial Intelligence", and The Register reported it on
2026-10-05. His article uses the name throughout ("SI inside the enterprise").

Musk's renaming posts of 2026-10-04 were already set aside as "about naming, not when", and
this is the same. Drop the record. Nadella is then shown with his latest dated prediction of
any kind, or as having said nothing on when.

### 6. A low chance drawn as a forecast, which also moves a figure's title

LeCun's "I imagine that will occur with some non-negligible likelihood within the next 10 years"
(`2026-01-lecun-humanlike-intelligence-within-ten-years`) is filed as "by 2036" and drawn.
"Some non-negligible likelihood" marks the far end of a stated chance, which is what
`chance_tail` exists for.

It also decides LeCun's "pushed later" on the "moved" figure: his first day is 2034, his last
2036, and that last day is this record. Refiled, the title's "4 pushed them later" becomes 3,
or LeCun drops out.

### 7. The "moved" figure compares the late end of each range

`nearest()` takes the late end of each forecast. A leader who gives a wide range then reads as
having moved by its width. Ilya Sutskever goes from "superintelligence ... could arrive this
decade" (2023, by 2030) to "5 to 20 years" (2025, 2030 to 2045). The figure counts that as
pushed later by fifteen years, though his near end did not move.

Compare the early end of a range (or say plainly in the footnote that the late end is used, and
why). Recompute the title.

### 8. Undated quotes run past the 25-word limit

- **The problem.** Nine of the eleven undated quotes are 29 to 48 words: Pichai, Mensch,
  Altman, Huang, Hassabis, LeCun, Suleyman, Zuckerberg and Nadella. The dated claims keep to
  25 words, the limit that keeps the page within fair quotation.
- **Why it got through.** The method's "Undated words" section never states the limit, and the
  validator's check of those records never tests it.
- **The fix.** Trim each to 25 words or fewer, taken exactly from the source (the notes give a
  cut for each), state the limit in the method, and add the check.

## Smaller fixes (before or just after the merge)

9. **Pichai's undated record.** The quote starts at 00:42:46, not 00:42:29. The notes should add
   what he says next, at 00:45:38: "three years from now ... it'll be very, very powerful". At
   most that is a vague dated line with no test, since he declines to call it AGI and says
   "that timeline doesn't matter". Keeping the passage undated is right: "three years, five"
   is other people's range.
10. **Musk's undated record.** The one-line summary calls Grok 5 "the model after" Grok 4.8, but
    his roadmap puts a Grok 4.9 in between: say "a later model". Nothing in the thread dates
    Grok 5, so keeping it undated is right.
11. **Suleyman's undated record.** The quote is fine. It was taken from the automatic captions,
    and the video owner's own track says the same without "you know"; cite that track.
12. **One term filed two ways.** "Smarter than any human" is filed as `agi` for Musk (2024-04-08)
    and Kai-Fu Lee (2025-01-16), but as `beyond_people` for Musk (2026-01-22). The method
    lists "smarter than any human" under `beyond_people`. Pick one.
13. **Hassabis 2011.** "A 20year plus project", said in January 2011, is drawn as not before
    2030. The claim is judged at the end of 2030, but the figure should draw the year his words
    name, 2031.
14. **LeCun's "several years if not a decade".** Its early end (2027) treats "several" as three
    years. Huang's "next several years" was taken out as undated under the same reading. Use
    "by 2034", or give Huang's line the same treatment.
15. **Hassabis "said 2026-07-15".** That is the upload date of a lecture whose own date is
    unconfirmed; an aggregator gives 2026-06-01. It is his latest day on the "now" figure, so
    the label "said" is not quite true. Note that it is the date it was published.
16. **The Amodei search for undated words.**
    - It misses several appearances after 2026-06-10. Bloomberg (2026-06-17) and CNN
      (2026-09-15) were read and hold nothing new on when.
    - Five short clips, from 2026-09-12 to 2026-09-30, could not be read and should get
      search-log rows. Two may also hold newer Altman and Zuckerberg words.
    - Sutskever's National Academy of Sciences message (2026-05-05) has no words on when, and
      should be logged.
    - Kai-Fu Lee's Yang Lan interview: the log says it aired 2026-10-08, but YouTube gives the
      upload as 2026-10-18. Check which is right.
17. **The Legg search-log row.** Legg's 13th claims search (`legg-claims-013`) says the
    Financial Times remark "carries no date". In the coverage it does (50% by 2028); it is not
    in his own words, which is why it stays out.
18. **Names in the leader lines.** Chase Lochmiller and Crusoe, Adam Lowisz, Alex Heath, Nilay
    Patel, Hannah Fry and the Royal Society of Arts are named without links. This is the same
    open question as links inside the claim records (open point 8 of the earlier check). It
    can follow.
19. **On a phone the two figures are hard to read.** The "moved" figure's eleven small panels
    become very small at 325 pixels. They do open full size when tapped, and nothing scrolls
    the page sideways. It can follow.

## The questions asked

1. **The 84 timing claims' new fields.** Read against each claim's own words, every category,
   term and shape is right except the items above:
   - LeCun's chance tail (fix 6);
   - one term filed two ways (fix 12);
   - Hassabis 2011 (fix 13);
   - LeCun's "several" (fix 14).

   No claim marked "other" hides a forecast of AGI or beyond. LeCun's "PhD level intelligence by
   next year it's just not happening" is the nearest, and it is reasonably "other". But two
   capability claims do hide such forecasts (fix 2).
2. **The eleven undated passages.** All eleven were opened at their sources. Nine have the right
   speaker, date, role and primary source, and carry no year or length of time.
   - **Nadella** fails (fix 5).
   - **LeCun's** was cut to stay undated (fix 4).
   - **Pichai:** "three years, five" is others' range, so undated is right.
   - **Musk:** nothing in the thread dates Grok 5, so undated is right.
   - **Suleyman:** the captions are not garbled in this passage.
   - **Huang:** "AGI has arrived" is a present-tense statement of when: now. It is from his
     verified account, the date matches on two services, and keeping it means he is not shown
     as silent.
   - **The "none found newer" searches:**
     - Sutskever, Liang Wenfeng and Kai-Fu Lee hold up.
     - Amodei's holds for what could be read (fix 16).
     - Leaving out Liang's investor-meeting transcript is right. By its own README it was
       transcribed by machine and edited by AI with no speaker labels, and it is unconfirmed by
       him or DeepSeek.
   - **Quote length:** all but two are too long (fix 8).
3. **Verdicts stay out of headlines.**
   - **What carries a verdict:** only the small grey notes on each claim, "Its date passed on
     ...; it came true / did not come true as said (...)".
   - **What carries none:** the claims page's headings and summaries, the home page, the two
     figures' titles, the page descriptions and share cards, and `site/status.json`. The status
     file's `claims_ledger` block holds counts of claims and people, the band, and the `now`
     block.
   - **Accuracy:** the notes match each claim's status, which the earlier check confirmed.
4. **The computed figures.**
   - **"8 of 11 before about 2033":** the arithmetic is right for the code as written. The
     nearest late end before 2032.75 holds for Altman, Legg, Musk, Amodei, Lee, Suleyman,
     Hassabis and Pichai. But the band (fix 1), the leader count (fixes 2, 3) and LeCun's place
     (fix 6) all need changing.
   - **"5 nearer, 4 later":** nearer are Altman, Hassabis, Suleyman, Legg and Lee; later are
     Musk, Amodei, Sutskever and LeCun. LeCun's rests on fix 6 and Sutskever's on fix 7.
   - **Repeats counted as said that day:** sound. A repeat is the person saying it again, and
     leaving repeats out would show leaders as older than they are. Two cautions:
     - a repeat dated by its upload, not the day said (fix 15);
     - a repeat shown under the term of its first saying, though the person's words that day
       may differ. Legg's 2010 "roughly human-level AGI" shows on 2025-12-11, when he spoke of
       "minimal AGI".
5. **The frontier-voices chart.**
   - **Drawn correctly:** Huang's three guesses since 2023 are among the builders, and the
     builders' rows rise to 93 of 144.
   - **The title matches the figures it is computed from:** "The builders say about 2030; the
     people who study it say about 2033", with the home sentence the same.
   - **Readable,** but it carries fix 1's problem. The subtitle defines a builder as "anyone on
     the panel who has worked at a company that builds frontier AI systems", which is not true
     for Kokotajlo and Aschenbrenner.
   - **"Come down ... to about 2033 since 2023"** pools four years. The 2026 median for the
     people who study it is about 2036, so the sentence should not read as the latest position.
6. **Public text.**
   - The claims page speaks in John's first person ("I keep this page as one of the tracker's
     two voices"), and the home page's new paragraph is plain.
   - No tool is named in new public text. The home page's existing disclosure of how the work
     is done was already on main, and is the kind the rules allow.
   - Every leader is linked; other names in the leader lines are not (fix 18).
   - Not from this pull request: the home page says "Four things stand out so far" and then
     numbers First, **Fifth**, Second, Third, Fourth. That was already on main; worth a
     one-line fix.
7. **The possibly-missing claims.**
   - **Suleyman on Decoder (2026-06-08)** must go in first (fix 3).
   - **Suleyman on The Rest Is Politics (2026-09-28)** can follow. It is "a coding moment for
     healthcare" in "the next few years" (undated), with a hope of 18 months and an outer "might
     be 5 years". That is borderline and about a health model, not general superintelligence,
     so it would not be drawn.
   - **Legg's "50% chance of minimal AGI by 2028"** can follow. It is in the Financial Times'
     words only (his own words are just "comfortable" and "minimal"), it repeats a forecast the
     ledger already holds, and he said it himself as late as 2025-12-11.
