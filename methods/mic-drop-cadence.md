---
id: mic-drop-cadence
name: Mic-drop cadence (per-paragraph resolution)
class: signature
status: live
fidelity: high
prevalence: very-high
vector: weak
surface: the distribution of where units end and whether each ending resolves
requires: reading for shape, not content
first-observed: 2023-01
last-verified: 2026-11-06
confidence: high
---

# Mic-drop cadence

## How it works
Preference tuning scores a response as a set of complete units. Raters, and the models trained to imitate raters, reward *landing*. Every paragraph that ends on a resolution reads as a paragraph that did its job.

So the model learns: each paragraph terminates on a punchline. A short declarative. An aphorism. A reveal. The last sentence of the paragraph is the shortest one in it, and it is the sentence the whole paragraph was built to set up.

Human prose doesn't do this. Human prose ends paragraphs on a citation, a subordinate clause, an unfinished list, a detail that doesn't symbolize anything, or plain exhaustion. Most paragraphs in anything written by a person end *badly* — and that's the tell, because a model physically cannot let a paragraph end badly. It will add a sentence to fix it.

## What it sees
- **The shortest sentence is last.** Consistently. Measure sentence length per paragraph and look at position.
- **Standalone declaratives.** The final sentence has no conjunction, no subordinate clause, no qualifier. It could be a pull-quote.
- **Aphorism shape.** *"Continuity beats craft."* *"The map isn't the territory."* *"Speed is the feature."* Two clauses, opposition or equation, no hedging.
- **The em-dash reveal.** *"and that's — well, that's the problem."* The pause before the verdict.
- **Rhetorical question as closer.** *"And isn't that the real issue?"*
- **One-line paragraph.** A whole paragraph holding one sentence, placed after a long one, existing purely to land.
- **Fractal resolution.** It isn't only paragraphs. Sentences resolve, sections resolve, subsections resolve, the piece resolves. Everything terminates.

The measurable version: **ratio of terminal sentences that would survive as a pull-quote.** Above ~20% is a signature. Human academic prose runs 5–10%. Human blog prose can hit 20% legitimately — but it does it unevenly, three in a row and then eight paragraphs that just stop.

## Defeated by
Let paragraphs end badly on purpose, and unevenly.

- End on a **subordinate clause** — "which is why the second attempt didn't work either."
- End on a **citation or a number** — nothing lands when the last thing is `p. 214`.
- End on a **detail that doesn't symbolize anything** — "the room was on the third floor."
- End on a **list item that isn't the most important one**.
- **Delete the punchline.** Most of the time the paragraph is complete one sentence earlier and the extra sentence is the tell. This is the single highest-yield edit and it takes two seconds per paragraph.
- Allow **one** landed ending per piece, placed where you've paid for it.

The structural counter: if the argument is actually going somewhere, paragraphs don't need to land individually — they're carrying. Mic-drop cadence is a symptom of an essay with no accumulation, which is why removing this tell also makes the thing better. Same pattern as `reviewer-stance.md`.

## Fails when
- The genre wants it. Op-eds, manifestos, marketing, and effective-altruism forum posts all land hard on purpose. Distinguishing the model's cadence from a human landing every paragraph is a matter of *evenness*, not presence.
- Short-form writing. Under ~150 words there aren't enough paragraphs for a distribution to be visible.
- Vertical/formatting-heavy writing — slides, bulleted memos — where resolution is the format.
- The reader is reading for content, which is everyone, always. This tell requires reading for shape and almost nobody does it deliberately. Vector `weak` for exactly that reason.

## Notes
The cleanest mechanically-checkable tell in the whole stack, which is why `tools/gravity-check.py` implements it: split on blank lines, measure sentences per paragraph, flag final-sentence-is-shortest, flag standalone declaratives, emit a ratio.

False-positive rate is real but low: good essayists land hard too. The discriminator isn't the presence of punchlines, it's the **absence of paragraphs that fail to land.** A human can write nine boring paragraphs and one devastating one. A model writes nine decent paragraphs and nine small resolutions.

**Measured, 2026-11-06.** `tools/gravity-check.py` was run against a deliberately gravity-saturated AI sample and a punchy human control written to be the hardest honest case: the control scored **40%** (2 of 5 eligible paragraphs), against a 20% threshold. That is a hard false positive on competent human prose, not a near miss. Two consequences: (a) the tool measures *shape*, not whether a punchline was earned — a human essayist with actual opinions trips it exactly like a model does, so a high ratio is a reason to look, never proof; (b) the ratio is only meaningful against the operator's own corpus. A writer whose natural rate is 35% and stays at 35% is invisible. A writer who jumps from 8% to 35% is a data point. Absolute thresholds are a first pass for strangers; deltas are the real signal.

Companion observation, same mechanism, different unit: the **bolded lead-in**. Every bullet opening with a bolded claim phrase is the paragraph-level mic drop pushed down to the item level. Same fix — bold nothing, or bold once.

## Sources
- `methods/training-data-gravity.md` (parent mechanism)
- Operator observation, 2026-11-06
- r/ELATeachers 1rmeg3y ("their conclusion was especially broad")
