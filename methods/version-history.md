---
id: version-history
name: Document version history
class: process-forensics
status: fading
fidelity: low
prevalence: high
vector: live
surface: coarse edit shape and timestamps
requires: google-docs or word, edit-rights-or-shared-link
first-observed: 2010-01
last-verified: 2026-11-06
confidence: high
---

# Document version history

## How it works
Every cloud document keeps autosave snapshots. Google Docs groups them into named/auto versions viewable via File → Version history; Word's is coarser but same idea. Free, built in, and requires no extension or training — which is why it's the most *available* forensic control even though it's the least granular.

## What it sees
- **Block appearance** — a large contiguous chunk arriving in one increment reads as a paste.
- **Session timestamps** — when work happened, and how long the gaps were.
- **Strict linearity** — top-to-bottom with no returns.

Critically, it does **not** see keystrokes. It sees snapshots. Whether a 900-word block was typed fast or pasted is genuinely ambiguous at this resolution.

## Defeated by
Same as `draftback.md`. Typing simulators, or real typing.

Also defeated by benign explanation: students legitimately write on phones, in notes apps, in Word, offline, and paste in at the end. A big block is a question, not a verdict — and every good teacher knows this.

**This is no longer contested. The instructors have conceded it themselves.**

> "Version history has effectively been defeated in terms of it being an AI countermeasure, with plugins like naturaltypist.com. The solution is not going to be one of technology."
> — r/Professors 1tin9om

> "I'm not sure it was really worth the time involved in watching the video playback. As others have said here, there are now file extensions that allow AIs to mimic normal typing."
> — r/Professors 1ux60y1

Two independent threads, months apart, same conclusion, from the people who deployed it. Demoted `live` → `fading`, fidelity `medium` → `low`.

For the record this is `typing-simulator.md` asserting itself in the field: the low-effort version of the countermeasure (require a Doc, glance at history) tolerates the low-effort defeat (a typing-simulator extension), and the population converges on the cheap defeat.

**The "ghost prompt" variant, and why it died:** an instructor would look for the assignment prompt echoed back in early revisions — students paste the question in before answering, and AI answers pick up the phrasing. That worked until pasting the prompt in became normal, benign student behavior, at which point the signal was drowned. *"This method doesn't work in the Google Docs because so many students copy-paste the assignment questions into the document first."* Textbook signature decay — the tell was real, then the population adopted the precondition as a habit. See SKILL.md §1.7.

## Fails when
- Submission is PDF, printed, LMS-native editor, or email attachment. Most LMSs strip the history.
- The teacher doesn't have edit rights or a shared link with history access.
- **Nobody opens it.** Overwhelmingly the common case.

## Notes
The lowest-effort, highest-availability control in the stack and simultaneously the most overestimated by students. See SKILL.md §1.5 — reliance on "they won't check" is obscurity, not defense.

The genuinely informative signal here isn't the paste. It's **total elapsed time versus plausible writing time**, and **idle gaps** — real writing has staring-at-the-wall time in it that a paste doesn't.

**Which is exactly why `document-metadata.md` is the stronger instrument in the same family.** Version history lives in Google's servers and is visible only through a UI that has to be opened, interpreted, and argued about. `app.xml`'s `TotalTime` field is in the file, is a single integer, and says the same thing without a video player. The instructors are migrating from the first to the second for the same reason they abandoned detectors: they want an artifact they can point at.

Note the asymmetry in what each survives. History dies when the file leaves the cloud — PDF, print, LMS text box. Metadata survives all three.

## Sources
- r/Teachers 1jt3p6u, 1gy2z8m
- r/Professors 1tin9om, 1ux60y1, 1wxiju3 (defeat confirmed, 2026)
- r/k12sysadmin 1j9hb2h (Draftback metering)
- Brisk/Google documentation
