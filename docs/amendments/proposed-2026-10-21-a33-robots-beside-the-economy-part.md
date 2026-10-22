# Proposed amendment A33: machines doing paid physical work, shown beside the economy part

**Status: proposed by the agent on 2026-10-21, at the master session's request after John's words
of the same day. Not applied. If John says yes, the section below is copied into
`docs/amendments.md` under a dated heading, with "Decided by" filled in as he rules, and this file
is deleted.**

John, 2026-10-21: "I think you are right on the optimus robot news fitting into the economy part
of the AGI Zeitgeist tracker and perhaps there is a news article worth writing there to explain
why and how we are integrating it."

---

## 2026-10-21: robots doing paid work, shown beside the economy part

Decided by: *(to be filled in when John rules)*

### A33. Machines doing paid physical work are shown beside part D, not scored

Applies to: `docs/singularity-entry-definition.md` (leg D, by a note only),
`data/world_measures.csv` (new context rows), and the economy part of the home page.

Was: part D (the economy) showed one series, the World Bank's yearly world output growth, and
nothing else. Robots appeared on the site only as dated promises in the claims ledger.

Now:

1. **The score does not change.** Part D is still scored on world real output growth alone,
   against the line of 30 percent a year. The frozen thresholds
   (`docs/singularity-entry-thresholds.json`) and the definition are untouched. No robot figure
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
   passengers or goods. Which series to collect first is a separate decision. The proposal is
   to start with the International Federation of Robotics' yearly count of industrial robots
   installed (542,000 in 2024, from its
   [press release of 2025-09-25](https://ifr.org/ifr-press-releases/news/global-robot-demand-in-factories-doubles-over-10-years)),
   and to add a humanoid row when someone other than a maker counts humanoids.
5. **Every row carries** its source address, the date of the figure, who measured it, and the
   kind (item 2). The validator gains a check that a leg D context row names its kind and is
   never read by the scoring code.

Why: John's words above. Most of the economy is physical work, so if part D ever moves, machines
doing that work are among the likeliest causes, and the first signs would show in counts of robots
at work years before world output. Showing those counts beside the score lets a reader watch for
the cause without letting a company announcement move the test. Scoring them would mean changing
the frozen test, which this amendment does not do.

What it costs: one more table to keep up. There is a yearly read of the trade body's count, and
a check for new outside counts during the weekly reading. Most weeks will add nothing, because most
robot news is announcements, which item 3 keeps out of the table.

Not decided here, and left for John:
- whether driverless vehicles belong in this table or wait for a ruling of their own (they have
  the best outside counts, from regulators, but they are a large field);
- whether the weekly reading should search for these rows, or a yearly pass is enough.
