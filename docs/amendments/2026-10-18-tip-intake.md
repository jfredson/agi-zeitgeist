# Amendment draft: tip intake for panel statements found between full passes

Status: **PROPOSED**, drafted 2026-10-18. Number assigned at merge (the next free after A28).
Applies to: `docs/methodology-v2.md` section 3 (stream E, collection) and
`docs/weekly-reading.md` ("Deferred: the frozen panel's new statements"). Procedure:
`docs/tip-intake.md`.

## Was

Stream E rows come only from the year-by-year trace, run per person with fixed queries
(methodology section 3; version 1 query set D1 to D3, Y1 to Y3). The weekly reading may not
add a statement by a panel member; part 4, which will find and log the panel's new
statements, is deferred until full collection lands. A statement John comes across has no
defined way in.

## Now

A panel statement found outside a full pass (sent by John, or, once part 4 is live, found by
the weekly reading) enters through `docs/tip-intake.md`: primary source archived with a
checksum in `sources/manifest.csv`; speaker checked against the frozen tiers; the person's
fixed year queries run and logged; candidate statements coded under the codebook by the same
procedure as the collection; notes tagged `tip`, and `tip; tip_only` where the fixed queries
do not retrieve the source. `tip_only` rows are kept in the record and left out of every
figure and share. People not on any tier are not coded; they are listed in
`docs/panel-candidates.md` for the next panel review. Part 4 of the weekly reading, when it
goes live, follows the same file.

Two notes tags are added to codebook section 9: `tip` (entered through tip intake) and
`tip_only` (the fixed queries did not retrieve the source). A third, `asr_unverified`, marks a
quote taken from machine captions that could not be checked against the audio.

## Why

Prominent panel members now speak mostly in long interviews and podcasts, and those are where
the "now" question gets answered. The trace already misses them when no transcript exists:
Bostrom's Joe Rogan Experience appearance of 2026-07-14 is logged as "not recorded: summary
writer's paraphrase only, no transcript" (search log `bostrom-120`). Tip intake supplies the
transcript and the archive. The `tip_only` rule keeps the hand route from becoming a sampling
frame: a tip can make the record faster, never different from what the rule would produce.

Nothing scored changes: statements never score a gauge.
