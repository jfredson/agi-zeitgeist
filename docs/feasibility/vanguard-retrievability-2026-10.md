# Retrievability check: r/singularity, vanguard sub-series pilot

Run 2026-10-02 under the accepted amendment `docs/amendments/2026-10-02-vanguard-stream.md`
(section 5). Script: `scripts/retrievability_check.py`. Nothing was coded and no post text
was stored; the output files hold post IDs, times, scores and status flags only.

## Revised headline, after John's video ruling (2026-10-02)

John ruled that video posts are coded from their title only. All 120 titles are in the
archive, so the 38 videos move from "not verifiable" to "recoverable":

| status | posts | share |
|---|---|---|
| **Recoverable for coding** (3 text posts, 61 images that load, 4 links, 38 videos by title) | 106 | **88%** |
| **Known lost** (image files deleted, HTTP 404) | 9 | **7.5%** |
| **Not verifiable** (5 galleries; their content needs reddit.com, which refused the lookup) | 5 | **4%** |

These are the top 20 per quarter. Image loading was checked only for the top 20, so no
comparable figure exists for the top 50. The original headline, before the ruling, follows.

## Headline (before the video ruling)

Of the **120 top posts** (stream F's top 20 by recorded score per quarter, six complete
quarters, 2024Q4 to 2026Q1):

| status | posts | share |
|---|---|---|
| **Content recoverable for coding** (3 text posts with their body; 61 images that still load; 4 links with title and address) | 68 | **57%** |
| **Known lost** (image file deleted from Reddit's image host, HTTP 404) | 9 | **7.5%** |
| **Not verifiable with public tools today** (38 videos, 5 galleries) | 43 | **36%** |

So between **57% (confirmed)** and **92.5% (if every unverified video and gallery still
plays)** of top posts can be coded from public sources; 7.5% are known to be lost.

The **titles and links of all 120** are in the public archive, and every one carries a
settled score, so listing and ranking can be reproduced exactly. What fails is the
content: top posts in r/singularity are overwhelmingly images (70 of 120) and videos (38),
and only 3 are text posts.

## What was tested, against section 5 of the amendment

| requirement | result |
|---|---|
| Reach the versioned source | Yes: the Arctic Shift archive API, `subreddit=singularity`, paged by post time, 100 posts per request |
| List every post in the period | **Partly.** 43,700 posts listed from 2024-10-01 before the archive replied "Timeout. Maybe slow down a bit" (HTTP 422) at request 438, reaching 2026-06-09. Under the overnight rule the run stopped there. **Six complete quarters** (2024Q4 to 2026Q1, 40,454 posts) were analysed; 2026Q2 is partial and 2026Q3 is not listed. No gap longer than 24 hours within the listed period |
| Reproduce the ranking | Yes: every listed post's ID, time and recorded score is in `r-singularity-pilot-index.csv`; the top-50 per quarter, ranked by score then post time, is in `r-singularity-pilot-top-posts.csv` |
| Retrieve the text needed to check the coding | Titles: 120 of 120. Content: see the headline |
| Score observation time | **Unknown.** The archive's capture-time field (`retrieved_on`) equals the posting time for all top posts, so it records the first capture, not when the settled score was taken. Scores are clearly settled (top-20 minimums of 1,904 to 5,310 per quarter), but their observation time can't be stated. Coverage class for scores: **unknown** |
| Status on Reddit itself (removed, deleted, live) | **Not checked.** reddit.com refused the bulk lookup (HTTP 403); not retried |

## Detail

Posts per quarter (listed): 2024Q4 9,039; 2025Q1 8,077; 2025Q2 6,428; 2025Q3 6,360; 2025Q4
5,195; 2026Q1 5,355.

Top-20 post types: image 70, video 38, gallery 5, link 4, text 3. Top-50 per quarter (300
posts): image 160, video 106, gallery 12, link 12, text 10. The image share is similar,
so the result isn't an artefact of looking only at the very top.

Images that no longer load (HTTP 404): `1gw9wjo`, `1gsa8dm`, `1i85th6`, `1ia8m4w`, `1jqc0hw`,
`1pd9rue`, `1oiyl0f`, `1ojx1hr`, `1ox8job`.

These are top posts **before** eligibility screening. The rewarded series ranks eligible
posts, so screening (claims about AI capability, timeline or consequence; image posts only
with legible text) will drop some and pull in lower-ranked posts.

## What this means for the design

1. **The rewarded series in r/singularity is mostly pictures and video.** Under John's ruling,
   image posts with legible text are coded; that requires the image, and about one in eight
   top images is already gone after one to two years. The loss will be larger for older
   periods.
2. **Video posts: settled.** John ruled on 2026-10-02 that they are coded from the title only (see the revised headline). Previously: 38 of 120 top posts are videos. The amendment covered
   image posts but not videos; a ruling is needed (code from the title only, code from the
   video, or exclude), and whichever is chosen decides most of the 36% unverified band.
3. **Reddit's own status can't be checked by a public script** (HTTP 403), so removal and
   deletion rates for top posts can't be reported from Reddit; only from what the archive
   and image host expose.
4. **The archive throttles a full listing.** A reader can reproduce the listing only slowly,
   and probably only from Arctic Shift's monthly dump files rather than the API for longer
   spans. The amendment's own note ("use the monthly dumps instead" for large pulls, per
   the archive's guidance) points the same way.
5. **Score timing is unknown**, so the rewarded series should be labelled "highest
   recorded-score posts among archived records", as the amendment already requires.

## Not done

The last two quarters of the pilot window (2026Q2, 2026Q3), the Reddit status lookup, and
checks of video, gallery and linked-page availability. Nothing else was collected.
