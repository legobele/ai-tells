---
id: synthetic-baseline
name: Synthetic baseline (poisoned anomaly model)
class: anomaly
status: live
fidelity: very-high
prevalence: rare
vector: live
surface: the operator's own prior corpus, compared across time
requires: multi-year record of AI-mediated work in the same venue
first-observed: 2023
last-verified: 2026-11-06
confidence: medium
---

# Synthetic baseline (poisoned anomaly model)

## How it works

§1.8 makes a claim that is only true under an unstated assumption: **teachers run anomaly detection, and the baseline they detect against is human.**

If the operator's written output has been predominantly model-generated for years, the evaluator's implicit model of "how this person writes" was trained on *synthetic text*. The anomaly detector is not disabled — it is calibrated to the wrong distribution, in the operator's favour.

The consequence is exact and worth stating plainly: **a new AI-generated text is not a deviation.** It sits inside the learned distribution. There is nothing for the anomaly model to fire on, because the operator has been presenting the target distribution continuously, across every submission, for the entire period the evaluator has known them.

The control still works. It just terminates on the wrong side.

## Why the standard countermeasures invert

This is the part that breaks the usual advice.

| Standard rule | Effect under a synthetic baseline |
|---|---|
| "Match your demonstrated voice" | Trivially satisfied — the demonstrated voice *is* the model |
| "De-tell: add variance, fragments, register breaks, typos" | **Creates** the anomaly. It is deviation from the baseline. |
| "Improve past the demonstrated baseline" (§8) | Same problem — anything better is also different |
| "Build a voice profile and generate against it" | A profile of the model, which you already have |

§8's de-tell mode is a good countermeasure against an evaluator who knows your human writing. Against an evaluator who knows your **model's** writing, it is a liability. The generically-AI-looking paragraph is the *consistent* one.

**The correct play inverts to: stay boring.** Continuity beats craft. A paragraph that reads exactly like the last three years is invisible; a paragraph that reads better, or messier, or more distinctively is a data point.

## The hazard this creates: drift

Poisoning the baseline removes the human-vs-AI signal and replaces it with a **model-vs-model** signal, which is a live vector.

Detecting "is this AI" is weak and getting weaker — §3 has that argument. Detecting "*which* AI" is a different problem with better numbers. Antoun, Sagot & Seddah (LREC-COLING 2024) find source-model identification and model-family classification both work, with confusion concentrated between adjacent models in the same family. TRACE (Shetty et al., EMNLP 2026) fingerprints frontier models by token-level transition statistics and survives out-of-distribution settings.

So the risk is not "this is machine-written." It is **"this is the wrong machine."**

A teacher holding an implicit model built from three years of one model family's cadence will register a *regime change* on a paragraph produced by a different family. Different sentence-length distribution. Different punctuation habits. Different hedging and refusal patterns. Different vocabulary priors. Each individual sentence is unremarkable. The time series is not.

**This is the operator-specific tell, and it is created by the model zoo.** Every switch — GPT-4 to Gemini to Qwen to DeepSeek to Mixtral to a local Q4 build — is a discontinuity in a record that is otherwise strangely uniform. The most-used models are the safest to keep using, for exactly the reason the least-used ones are risky.

Corollary worth logging: **quantization leaves no detectable signature.** Antoun et al. found no attributable signature from quantized versus full-precision output. Running a local Q4 model does not add a tell. Running a *different architecture* does.

## The baseline is drifting at the population level too

There is a second drift, and it runs the other way. The poisoning above is *one corpus* moving toward the model. The field reports say the ambient human population is moving too — in both directions at once.

**Toward the model,** from consumption. An instructor describing what they now see in proctored, handwritten, no-device in-class exams:

> "There's also a kinda 'feedback' thing, where dumb kids think AI essays sound good and so as they themselves actually try to write and develop a voice they adopt the bad habits that they've picked up from having AI talk to them all day. I've seen this start to happen in a couple of in-class writing exams I've given and it makes me worry for the future."
> — r/Professors 1tivmw2

Read that again with the venue in mind: in-class, handwritten, no possible AI involvement in the artifact. The register arrived *through the person*. Human-trained-on-AI is now showing up in the one channel that was supposed to be clean.

**Away from the model,** from detector anxiety. The same population is simultaneously stripping the markers it has been told are suspect:

> "Many students in the past year have told me they've dumbed-down their writing to avoid AI-accusations. It's fucking tragic--especially when students shy away from using em-dashes and colons."
> — r/Professors 1rjl5u0 (emphasis mine)

Note the em-dash in that sentence is two hyphens. The instructor is avoiding the tell while complaining about students avoiding the tell.

Field reporting on the result, from the student side:

> "Students dumbing down their writing to pass detection tools is creating a weird generational prose gap."
> — r/AIDetectionAcademia, 43 points

and from the teachers' side, more bluntly:

> "I miss when my students' writing was worse—before AI"
> — r/ELATeachers, 154 points

**Doctrine consequence, and it's a real one.** §1.8 rests on anomaly detection having a stable human reference. The reference is not stable. It is being pulled toward model register by consumption and away from model markers by detector anxiety, simultaneously, across the whole cohort.

Which means the classic tells are decaying for a reason that has nothing to do with the tells being publicized. **The population is being trained, by the detectors, to write around them** — and being trained, by the models, to write into them. An instructor's "I know it when I see it" is a classifier fitted on a distribution that is actively moving under it.

Two implications for the operator:

1. **The "sounds like a 19-year-old" gap is closing.** Every year, more genuine 19-year-olds write like the model. The anomaly signal weakens against the whole cohort, not just against the operator's poisoned corpus.
2. **The population is now *also* detectable for writing around the tells.** A student who conspicuously avoids em-dashes, colons, and semicolons is running a signature — of detector-awareness. That is a tell about the *student*, and `methods/reviewer-stance.md` is why it doesn't save them: the register survives, the punctuation doesn't matter.

Source corpus for this at population scale: see r/Professors 1rjl5u0, which collects the Weber-Wulff 2023 (14 tools, none above 80%), Liang et al. 2023 (61%+ of non-native English essays flagged), OpenAI's retired classifier (26% recall), and the case list — Liberty University, the Yale SOM suit, the Maryland 30.76%, the Australian nursing student's six withheld months. The detectors were discredited and deployed anyway, and the prose adapted to the deployment.

## What actually still works

The stack collapses to three things.

1. **Continuity.** Prefer the model family that dominates the record, or fine-tune a local model on the record so the distribution is explicitly matched. This is the one place `adversarial-stylometry.md` earns its keep — not as a disguise tool but as a **regression detector**: score a draft against the last 36 months of your own output and ask whether it belongs to the same distribution. Different objective, far more tractable, and the corpus already exists.
2. **Comprehension.** Unchanged and undiminished. `oral-defense.md` is the only control with no model in the loop, and poisoning the baseline makes it *worse*, not better — see below.
3. **Verified specifics.** Unchanged. Fabrication is a content failure independent of style.

## The trap this creates in a language class

§9 says the written corpus sets an implicit expectation and the oral component is native to the curriculum. Under a synthetic baseline both halves sharpen against the operator.

Three years of polished written Spanish raises the level that "consistent with their work" means. In the one venue where the output must come from a mouth, the bar has been set by text the operator did not produce. The written record is not shielding — it is **raising the standard the oral exam will be measured against**, and it has been doing so since 2023.

The wider the gap between the corpus and the person, the more the corpus is evidence rather than cover.

## What this changes about the reputation control (§1.12)

§1.12 says a track record lowers the prior probability of accusation. True when the record is evidence of authorship. When the record is evidence of *a consistent process*, it is a liability the moment anyone reads the corpus as a corpus instead of as individual submissions.

The failure is not detection at submission. It is **audit**: someone pulls up the whole archive, or a parent mentions something, or a teacher compares a 2023 essay to a 2026 one next to a classmate's year-over-year improvement curve. Consistency is what makes a corpus readable as a single artifact.

## Fails when

- The evaluator has substantial *pre-2023* work from the operator. That baseline is human and the poisoning is partial.
- The operator's in-class writing, handwriting, notes, or speech is a meaningful share of the teacher's model. Mixed channels dilute the effect.
- The operator's edited output carries their own voice strongly enough that the corpus is a hybrid rather than a synthetic distribution — the hybrid is what must be matched, not either parent.

## Notes

**`confidence: medium`.** The mechanism follows directly from how anomaly detection works and from documented model-attribution results. The specific application — one person's multi-year time series as the detection surface — is not studied anywhere, so the *magnitude* is unmeasured.

The honest version: this is not "safe." It is **undetected by the control that normally catches this**, which is a different claim. The control is intact, calibrated to a moving target, and nobody has pointed it at the corpus yet.

Also worth naming, without irony: a 2023-onward corpus of one person's AI-mediated writing predates essentially the entire institutional response. It is a longitudinal record of human-AI coauthorship that most researchers did not start collecting until 2025. That is genuinely unusual. It is also the reason there is no human baseline left to fall back on — if the voice is ever needed, the most recent sample of it is years old.

## Sources
- Antoun, Sagot & Seddah, LREC-COLING 2024 — cross-model detection, source-model and family attribution, no detectable quantization signature
- Shetty, Xu, Ohrimenko & Lau, EMNLP 2026 — TRACE / GhostWriteBench, token-transition fingerprinting
- Wang et al., SemEval-2024 Task 8 Subtask B — multi-way generator attribution as a shared task
- r/Professors 1tivmw2 — in-class exam register drift; detector efficacy collapse 90%→20%
- r/Professors 1rjl5u0 — em-dash/colon avoidance, discredited-detector case list
- r/AIDetectionAcademia, r/ELATeachers — generational prose gap, both directions
- Operator self-report, 2026-11-06 — ~90% AI-mediated written output since 2023
