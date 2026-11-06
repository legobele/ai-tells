---
id: brisk-inspect-writing
name: Brisk Inspect Writing
class: process-forensics
status: live
fidelity: medium
prevalence: medium
vector: live
surface: full replay plus color-coded paste/delete events
requires: google-docs or onedrive-word, chrome or edge, teacher-account
first-observed: 2024-05
last-verified: 2026-11-06
confidence: high
---

# Brisk Inspect Writing

## How it works
Commercial competitor to Draftback, bundled inside a much larger teacher-productivity platform (30+ AI tools: lesson plans, quizzes, feedback). Because it ships with tooling teachers already want, adoption is spreading faster than a standalone extension would.

Replays the document history as video with color coding: **green** = created, **yellow** = pasted, **red** = deleted. Adds clipboard icons at paste points, timestamps, total time-on-doc, and edit counts.

## What it sees
Same surface as Draftback, presented more legibly, plus:
- Paste events are visually unmissable rather than something you have to infer.
- Total document lifetime in one number.
- A separate AI-detector button bolted on (see `ai-detectors.md` — that half is noise).

## Defeated by
Same as Draftback: typing simulators, or actually typing it.

## Fails when
- Only supports Google Docs and OneDrive Word — no local files, no PDF submissions, no LMS-native editors.
- Requires the teacher to have an account and the extension installed.
- **Brisk explicitly does not produce an accuracy score** and frames the output as "a conversation starter." Its own docs recommend asking the student, which is where a teacher ends up anyway.

## Notes
The commercial pressure matters: Brisk raised $15M (2025) largely on this feature set, and it's marketed as free. Assume this is the direction the field moves rather than Draftback.

Vendor—deliberate design choice worth knowing: the product positions itself as *"assistive, not a gotcha"* — which means a flagged replay usually resolves into a conversation, not an automatic zero. That conversation is `oral-defense.md` territory.

## Sources
- briskteaching.com/inspect-writing
- TechCrunch 2025-03-26
