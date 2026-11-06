---
id: voice-baseline
name: Voice baseline comparison
class: anomaly
status: live
fidelity: high
prevalence: high
vector: live
surface: divergence from the writer's own demonstrated style
requires: prior writing samples from the same person
first-observed: 2023-01
last-verified: 2026-11-06
confidence: high
---

# Voice baseline comparison

## How it works
Anomaly detection, not signature detection. The instructor holds an implicit model of how this specific person writes — built from in-class work, quizzes, prior submissions, discussion posts, emails — and measures the current artifact against it.

> "AI detectors don't work. You catch the kids by knowing their actual work. Which means have a decent amount of in-class assignments to gather this data."

> "I've been able to confront students by showing them their writing from early in the semester, and pointing out that the writing style is completely different."

## What it sees
Divergence. Not "is this AI" but "is this *this person*." Sentence rhythm, vocabulary band, error profile, structural habits, punctuation tics, the way they open a paragraph.

Because the reference model is individualized, it has no fixed signature to evade. Global stylistic adjustment moves you toward "generic human," which is not the target.

## Defeated by
**Matching the actual baseline rather than improving past it.** This is the whole countermeasure:

- Write at the demonstrated vocabulary band, not above it.
- Preserve the person's small habitual errors and structural tics.
- If the baseline is weak, the output must be weak in the same *shape*.
- Don't fix everything. A perfect essay from a B-student is more anomalous than a B essay.

## Fails when
- No baseline exists. New teacher, new class, first assignment, transfer student — no anomaly model to violate. Temporary advantage that closes the moment anything is written honestly.
- The instructor has a weak memory for style and only checks vibe.
- The student's writing is genuinely inconsistent (bilingual, multiple registers, different genres), which raises the baseline's variance and its false-positive rate.

## Notes
**The only control in this directory that is genuinely hard to defeat, and the one most people ignore** because it isn't a tool and can't be shopped for. See SKILL.md §1.7 — signature vs anomaly detection, and why voice is the only control that holds.

Second-order effect: `paper-in-class.md` and this control compound. Paper generates the baseline; the baseline then polices everything else.

**Read `synthetic-baseline.md` before relying on this one.** The control assumes the baseline is a human artifact. If the operator's output has been predominantly AI-mediated for years, the evaluator's implicit model of "how this person writes" was fitted on model output, and a new model output is not a deviation from it — it's a match. The control is intact and terminates on the wrong side. Under a poisoned baseline the countermeasure inverts: matching the baseline means matching the model, not underperforming it.

## Sources
- r/Teachers 1fmpll5 (13 pts), 13fj49g (10 pts)
- Repeated across essentially every thread on the topic
