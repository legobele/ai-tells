---
id: document-metadata
name: Document metadata / file provenance
class: process-forensics
status: live
fidelity: very-high
prevalence: low
vector: live
surface: author string, producing application, cumulative edit minutes, and revision IDs baked into the file itself
requires: the actual file (not a screenshot, not a printout), and someone who knows properties exist
first-observed: 2023-01
last-verified: 2026-11-06
confidence: high
---

# Document metadata / file provenance

## How it works
Office and PDF files carry a provenance record that survives every copy, email, and upload — it is structurally part of the format, not a feature anyone chose to enable. Right-click → Properties shows the friendly face of it. Unzip an OOXML file and it's plain XML.

The instructor doesn't need to understand any of this. They need to open Properties once and read four fields.

## What it sees
**OOXML (`.docx` / `.pptx` / `.xlsx`)** — unzip and read:

- `docProps/core.xml`
  - `<dc:creator>` — original author string
  - `<cp:lastModifiedBy>` — last editor (a *different* name here than creator is already a question)
  - `<cp:revision>` — save count. `1` means the file was written once and closed.
  - `<dcterms:created>` / `<dcterms:modified>` — 2 seconds apart on a 1,800-word essay is not a human writing session
- `docProps/app.xml`
  - `<Application>` and `<AppVersion>` — `Microsoft Office Word` vs `LibreOffice` vs `WPS`
  - `<TotalTime>` — **cumulative editing minutes.** A 2,000-word essay with `TotalTime` of 2 is the single cleanest artifact in the stack, and it's the one that actually got someone caught in the field.
  - `<Company>` — often blank on a student machine, populated on an institutional one
- `word/document.xml` + `word/settings.xml` — `w:rsid` revision-save IDs. Real Word sessions generate a sprawling tree of them. A document with one or zero rsids was not typed in Word.

**PDF** — `/Producer` and `/Creator` in the Info dictionary, plus XMP:

| Producer | What it means |
|---|---|
| `Microsoft® Word for Microsoft 365` | exported from Word |
| `Skia/PDF m###` | printed from Chrome — i.e. content arrived via the browser |
| `Google` / `Skia` via Docs export | exported from Google Docs |
| `pdfTeX` / `XeTeX` | LaTeX |
| `ReportLab` / `WeasyPrint` | scripted generation |
| `Pandoc` | markdown pipeline |

A "Word document" submitted as a PDF whose producer is `Skia/PDF` was printed from a browser tab. That is not proof of anything by itself, but it is a question with an easy answer, and it stacks.

## The field case
A professor reported a submitted `.docx` with a **two-minute edit history and `python` as the original author**.

That string is not an inference. `python-docx` defaults `core_properties.author` to `python-docx` and leaves `TotalTime` at zero. Whoever generated the file never opened it in Word. It never touched a human editor, and the file says so in a field designed to be read.

## Defeated by
The countermeasure is not clever, it's just annoying:

- **Actually write the file in the editor you're claiming to have used.** One save from Word populates rsids, `TotalTime`, and a plausible revision count for free.
- If scrubbing a generated file instead: rewrite `dc:creator` / `cp:lastModifiedBy` to a plausible name, set `cp:revision` to a realistic count (not 1, not 200), set `TotalTime` to something that matches the word count at a human typing rate, backdate `dcterms:created` well before `dcterms:modified`, strip or synthesize rsids, and set `Application`/`AppVersion` to match the file's actual internal structure.
- The last clause is the trap. A file claiming `Microsoft Office Word` while containing Word's structure imperfectly is *worse* than a file that honestly came from LibreOffice. Metadata has to agree with the document's own XML shape, and that is genuinely hard to fake convincingly.

`exiftool -a -G1 file` reads all of it in one command, which is also how you audit your own output before submitting.

## Fails when
- **Nobody opens Properties.** Overwhelmingly the common case — same failure as `version-history.md`.
- The file passed through a converter that normalizes metadata. Uploading to Google Drive and downloading rewrites the header to Google's. That laundering is incidental, not a designed defense, and it also destroys your own process evidence.
- The venue takes plain text, an LMS rich-text box, or a printout. Nothing survives.
- The instructor sees `python-docx` and files it as "a glitch" rather than a finding. This happens.

## Notes
The highest-fidelity control in the entire stack on a per-unit-of-effort basis. It is binary, it is reproducible, it survives being forwarded to an administrator, and it requires about nine seconds of instructor attention.

It is also the one that most cleanly separates the two populations. Students who genuinely write in Word have nothing to fix — their files are already correct. Students who generate and submit have a field that says `python-docx` and a `TotalTime` of zero.

That asymmetry is the point. This isn't a statistical estimate of authorship; it's the document's own testimony about how it was made.

Treat it as the first thing to check on any `.docx`, and the first thing to scrub on any artifact you produce through a script.

## Sources
- r/Professors 1wxiju3 (the `python`-as-author report, 2026-10)
- r/Professors 1tin9om, 1ux60y1
- ECMA-376 Part 2 (`docProps`), ISO 32000-1 §14.3.3 (PDF info dictionary)
- `python-docx` default core properties
