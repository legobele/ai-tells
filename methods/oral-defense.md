---
id: oral-defense
name: Oral defense / live interrogation
class: comprehension
status: live
fidelity: very-high
prevalence: high
vector: terminal
surface: whether the person can explain the artifact
requires: synchronous interaction, instructor willingness
first-observed: 2023-01
last-verified: 2026-11-06
confidence: high
---

# Oral defense / live interrogation

## How it works
Ask the student to explain something specific about their own submission. Not "explain your essay" — one narrow, targeted question about a particular choice, sentence, source, or word.

> "Choose a couple non-common words from the essay and ask them what they mean. Or a complex well-written sentence… Explain your code. You can copy it but you need to be able to explain it to use it."

Cost: one question. No tooling. No false positives. No training.

## What it sees
The comprehension gap, directly. An artifact can be outsourced; understanding cannot be outsourced at the moment of asking.

Unlike every other control in this directory, it does not measure the *artifact* — it measures the *person*, which is the actual question the evaluator is trying to answer.

## Defeated by
Only one thing: actually understanding the material.

No paraphrase, no simulator, no process hardening, no humanizer, no version history touches this. It is the only control here with no artifact-layer workaround, because it doesn't inspect an artifact.

## Fails when
- Applied unfairly — penalizing confidence, speed, or verbal fluency rather than understanding. Multilingual learners and anxious students get hit hardest. Good practitioners compensate: rotating sample, one-minute conferences, targeted single questions during circulation rather than a full interview.
- Applied as a gotcha rather than formative assessment, which corrodes trust and produces performative rather than real answers.
- The instructor can't do it at scale — 240 students × 1 minute is four hours.

## Notes
Institutional versions are emerging. A San Francisco humanities teacher dropped take-home essays entirely for a **15-question oral exam answerable in five minutes** — the whole assessment moved to this control.

This is the control that makes the entire skill's honest conclusion true: see SKILL.md §1.9 (non-repudiation) and §10. The correct defense against this control is #3 on the non-repudiation list, and it's the only item on that list that can't be manufactured at submission time.

## Sources
- r/Teachers 13fj49g, 1obngrm, 1m8w68h
- Reuters/US News 2026-10-28 (classroom redesigns), 2026-11
