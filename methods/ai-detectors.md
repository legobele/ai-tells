---
id: ai-detectors
name: AI detectors (Turnitin, Copyleaks, GPTZero, Originality)
class: signature
status: fading
fidelity: near-zero
prevalence: medium
vector: weak
surface: perplexity and burstiness versus a corpus
requires: submission through a platform that runs one
first-observed: 2023-01
last-verified: 2026-11-06
confidence: high
---

# AI detectors

## How it works
Two statistics, thresholded.

- **Perplexity** — how predictable each next token is. Model output selects high-probability tokens, so perplexity is low.
- **Burstiness** — variance in sentence length and complexity. Model output is uniform, so burstiness is low.

The tool computes both, compares against a reference corpus, and emits a percentage. There is no authorship model, no stylometry, no understanding. Turnitin, Copyleaks, GPTZero, and Originality are all variants of this.

## What it sees
A statistical shape. Nothing about authorship.

## Defeated by
- **Paraphrasing** — mechanically raises perplexity. A synonym pass defeats most scores without changing an idea.
- **Nothing, and it doesn't matter.** The tool is noise in both directions.

## Fails when
Frequently, in both directions. Documented in the field:
- Same text, four to five detectors, **0% to 75%** spread.
- Human-authored work scoring **95% AI**.
- Correctly-spelled random phrases flagged by Copyleaks.
- Master's-level human writing flagged at high rates.
- Severe, well-documented false-positive skew against non-native English speakers, technical writing, and formal registers. Several institutions stopped publishing scores because of it.

## The efficacy collapse, in one instructor's numbers
The most useful datapoint in this file, because it's a longitudinal self-report rather than a vendor claim:

> "90% of the papers I got. This semester, it's only finding it in about 20%. Looking at all the papers, **students did not stop using it.** I think they just found a new way to address the detectors."
> — r/Professors 1tivmw2

Read carefully, because the obvious reading is wrong. This is not a detector getting worse. The detector measured the same thing it always measured; **the population moved under it.** When a signature control becomes known, the population develops the counter-signature in a single semester and the control's positive rate collapses — while the underlying behavior is unchanged.

That is SKILL.md §1.7 with numbers attached, and it's the strongest argument in the whole evidence base for why signature-based detection loses by construction. The detector didn't fail. It succeeded, publicly, and was therefore eaten.

## Notes
**Field consensus among teachers is that these are worthless, and they are the ones being sold them.**

> "I've taken results directly from ChatGPT and put it into 4-5 different detectors, and gotten anywhere from 0% to 75% certainty that it was written by AI, and I've written my own work and tested it and gotten 95% certainty that it was AI. The detectors are effectively worthless; don't trust the detectors, period."
> — 1,432 points, r/Teachers, 2025-10

**The one function that survives:** a score is a *trigger for human review*, not a verdict. A 40%+ score does nothing on its own. A 40%+ score plus a teacher who already suspects you produces a conversation, and that conversation is `oral-defense.md`.

Which means detectors are not a detection method in practice. They're a routing mechanism that points at a real detection method. Optimizing the score is optimizing the wrong node.

Status set to `fading` rather than `dead` deliberately: institutions still deploy them, so the routing effect is live even though the measurement isn't.

**The literacy gap is itself a tell about the institution.** A student asked a professor to define "perplexity" and "burstiness" after being accused on the basis of both:

> "He went completely quiet, looked at his desk, and said he'd have to consult the IT department."
> — r/AIDetectionAcademia 1vdtgtf

Which means the correct response to a detector accusation is not to argue the statistics — it's to ask what they mean. Half the time the answer is that nobody in the room can say, and the accusation evaporates on contact with its own vocabulary. Filed under §1.11: *don't argue the detector, ask it to explain itself.*

## Sources
- r/Teachers 1jxsfct, 1d49d5f, 1fmpll5, 1obngrm, 1dfx61p
- r/Professors 1tivmw2 (efficacy collapse), 1tqoo6p, 1u2u89b
- r/AIDetectionAcademia 1vdtgtf (perplexity/burstiness illiteracy)
- r/academia 1oi5ska (Dickens at 95%)
- HuffPost/Brisk analysis; edweek 2025-02
