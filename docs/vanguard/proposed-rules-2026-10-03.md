Rule R1: posts that pass something on without comment

When the poster passes on a news item, announcement, demo video, product launch or screenshot
of someone else's words, and adds no words of their own about whether the claim is true or
good, code stance = neutral_relay and set attribution to the source (lab_or_company for a
lab's own demo or announcement, news_outlet for a headline, other_person or panel_member for
a person's post or quote). A title that only restates, names or describes the item counts
as no comment, even when the poster wrote it. Code affirms only when the poster adds words
that endorse the claim ("this is huge", "crazy true", "called it"), and denies only when they
add words that reject it. Jokes and reaction titles ("WTF", "Shots fired!") are not
endorsements; code the relayed claim as neutral_relay and record the tone in rhetorical_mode.

Rule R2: company and policy news, or capability

Decide the main claim's target by the subject of the main claim, not by which company is
named. Ask: who or what does the thing the claim is about?
- A model, robot or AI system (what it can or can't do, how it behaved, a new model or
  product with what it does, benchmark scores, a demo, a deployment such as robots now
  patrolling a stadium): specific_capability. This includes a model's own output shown in a
  screenshot, even when the output is about its owner.
- A company, executive, investor or government (deals, funding, hiring, firing, lawsuits,
  feuds, regulation, pricing, access, release or withholding decisions, leaks, advertising,
  spending): industry_governance.
- People, jobs, society or the economy (effects of AI on them): consequence.
If the post makes claims of more than one kind, code each as its own claim. The main claim
is the one stated in the title; if the title states none, the one the post spends most words
on.

Rule R3: hedging

Code epistemic_qualification from the words that state the main claim: the title, plus any
body, image or page text that states the same claim, including a quoted source's own words.
Code qualified only if those words contain a hedge that limits certainty: may, might, could,
probably, likely, possibly, perhaps, I think, I suspect, I believe, seems, appears, suggests,
early signs, if, or an equivalent phrase. Otherwise unqualified. Code explicit_probability
only for a stated number or odds. Code unclear only when no claim is stated in words at all
(a title that just names a topic, such as "X's thoughts on AI").
