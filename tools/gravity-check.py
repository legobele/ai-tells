#!/usr/bin/env python3
"""
gravity-check — measure a draft against the tells in methods/training-data-gravity.md

Stdlib only. Ductile on purpose: it reports, it doesn't decide. Read the numbers,
read the flagged sentences, then argue with the report.

Usage:
    python gravity-check.py draft.md
    python gravity-check.py draft.md --json
    python gravity-check.py draft.md --quiet        # metrics only, no samples
    Get-Content draft.md | python gravity-check.py -

Exit codes:
    0  no warnings
    1  one or more warnings
    2  bad input

Thresholds are calibrated on prose. Poetry and lists will read as broken; that's
the tool's limitation, not the draft's.
"""

from __future__ import annotations

import argparse
import json
import re
import statistics
import sys
from collections import Counter

# --- §7 banned lexicon -------------------------------------------------------
# The register-agnostic slop list. Deliberately not exhaustive: a longer list
# starts flagging legitimate technical prose.
BANNED = [
    "delve", "tapestry", "testament to", "in today's world", "it's worth noting",
    "let's dive", "dive into", "unlock the", "harness the", "embark on",
    "navigate the", "realm of", "landscape of", "underscore", "pivotal",
    "multifaceted", "seamless", "robust solution", "leverage the", "foster a",
    "at its core", "in essence", "ultimately,", "the real question",
    "here's the thing", "let me be clear", "the honest version",
]

# Rationalist/LessWrong register markers. Measured, not banned — one or two is
# a style; five is a fingerprint.
RATIONALIST = [
    "epistemic status", "steelman", "i notice i'm confused", "crux",
    "belief update", "inside view", "outside view", "reference class",
    "the map is not the territory", "moloch", "goodhart", "bayes",
]

ROUND_NUMBERS = {10, 20, 25, 30, 40, 50, 60, 70, 75, 80, 90, 100, 200, 500,
                 1000, 5000, 10000, 50, 150, 250, 300, 400, 600, 700, 800, 900}

SENT_SPLIT = re.compile(r'(?<=[.!?])["\')\]]*\s+(?=[A-Z0-9"\'(\[])')
NUM = re.compile(r"(?<![\w.])(\d[\d,]*(?:\.\d+)?)(?![\w])")
CLOCK = re.compile(r"\b(\d{1,2}):(\d{2})(?:\s?([ap]\.?m\.?))?\b", re.I)

ABBREV = {"mr", "mrs", "ms", "dr", "prof", "sr", "jr", "st", "vs", "etc",
          "e.g", "i.e", "cf", "al", "fig", "no", "vol", "pp", "ed"}


def split_sentences(paragraph: str) -> list[str]:
    rough = SENT_SPLIT.split(paragraph.strip())
    out: list[str] = []
    for chunk in rough:
        chunk = chunk.strip()
        if not chunk:
            continue
        # rejoin fragments created by an abbreviation or an initial
        if out and out[-1].rstrip(".").split()[-1:]:
            tail = out[-1].rstrip(".").split()[-1].lower()
            if tail in ABBREV or (len(tail) == 1 and tail.isalpha()):
                out[-1] = out[-1] + " " + chunk
                continue
        out.append(chunk)
    return out


def words(text: str) -> list[str]:
    return re.findall(r"[A-Za-z']+", text)


def is_standalone_declarative(sentence: str) -> bool:
    """Heuristic: a sentence shaped like a pull-quote.

    Deliberately narrow. It is looking for a *verdict* — a claim that terminates
    on an abstraction. A sentence ending on a numeral or a proper noun is a
    detail, not a verdict, and details are the countermeasure, not the tell.
    """
    s = sentence.strip()
    if not s or s.endswith("?") or s.endswith("!"):
        return False
    n = len(words(s))
    if n > 16 or n < 2:
        return False
    if any(p in s for p in (":", ";", ",")):
        return False
    if s[0].islower():                                  # mid-sentence fragment
        return False
    openers = ("and", "but", "so", "which", "because", "although", "while",
               "however", "yet", "or", "nor", "if", "when", "after", "before")
    if s.split()[0].lower() in openers:
        return False

    # ends on a particular rather than an abstraction -> detail, not verdict
    last_tok = re.sub(r"[.!?\"')\]]+$", "", s).split()[-1]
    if re.search(r"\d", last_tok):
        return False
    if last_tok[:1].isupper():                          # proper noun
        return False
    return True


def analyse(text: str) -> dict:
    paras = [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]
    all_sents: list[str] = []
    para_sents: list[list[str]] = []
    for p in paras:
        ss = split_sentences(p)
        para_sents.append(ss)
        all_sents.extend(ss)

    wc = len(words(text))
    lens = [len(words(s)) for s in all_sents]

    # --- mic-drop cadence ----------------------------------------------------
    flagged: list[str] = []
    for ss in para_sents:
        if len(ss) < 3:
            continue
        mean_len = statistics.mean(len(words(s)) for s in ss)
        last = ss[-1]
        last_len = len(words(last))
        if last_len <= max(16, mean_len * 0.7) and last_len < mean_len:
            if is_standalone_declarative(last):
                flagged.append(last)
        elif is_standalone_declarative(last) and last_len <= 12:
            flagged.append(last)

    eligible = sum(1 for ss in para_sents if len(ss) >= 3)
    mic_ratio = len(flagged) / eligible if eligible else 0.0

    # --- numerals ------------------------------------------------------------
    numerics: list[str] = NUM.findall(text)
    ints: list[int] = []
    for n in numerics:
        try:
            ints.append(int(float(n.replace(",", ""))))
        except ValueError:
            pass
    fam47 = [i for i in ints if str(i).endswith("47")]
    roundish = [i for i in ints if i in ROUND_NUMBERS or (i >= 100 and i % 100 == 0)]

    clocks = CLOCK.findall(text)
    clock47 = [f"{h}:{m}" for h, m, _ in clocks if m == "47"]
    clocktidy = [f"{h}:{m}" for h, m, _ in clocks if m in ("00", "15", "30", "45")]

    # --- lexicon -------------------------------------------------------------
    low = text.lower()
    banned_hits = Counter(b for b in BANNED if b in low)
    rational_hits = Counter(r for r in RATIONALIST if r in low)

    # --- sentence-level -----------------------------------------------------
    em = text.count("—") + text.count("–")
    em_rate = em / (wc / 200) if wc else 0.0
    tricolon = len(re.findall(r"\w+,\s+\w+,?\s+and\s+\w+", text))
    negdef = len(re.findall(r"\b(?:is|was|isn't|wasn't)\s+not\s+(?:a|an|the)?\s*\w+[,.]?\s+"
                            r"(?:it|but|it's)\b", text, re.I))
    bold_leads = len(re.findall(r"^\s*[-*]\s+\*\*", text, re.M))
    oneliners = sum(1 for ss in para_sents if len(ss) == 1)

    burst = statistics.pstdev(lens) if len(lens) > 1 else 0.0

    warnings: list[str] = []
    notes: list[str] = []

    if mic_ratio > 0.20:
        warnings.append(f"mic-drop cadence: {mic_ratio:.0%} of paragraphs end on a "
                        f"verdict ({len(flagged)}/{eligible}) — target <20%")
    if len(fam47) >= 2:
        warnings.append(f"number gravitation: {len(fam47)} numerals ending in 47 "
                        f"({', '.join(map(str, fam47))})")
    elif len(fam47) == 1:
        notes.append(f"a single numeral ends in 47 ({fam47[0]}) — noise on its own, "
                     f"a prior if it recurs")
    if clock47:
        warnings.append(f"clock gravitation: {', '.join(clock47)}")
    if len(clocktidy) >= 3 and len(clocktidy) == len(clocks):
        warnings.append(f"clock tidiness: every timestamp is on the quarter hour ({len(clocks)})")
    if len(roundish) >= 2:
        warnings.append(f"round-number clustering: {len(roundish)} of {len(ints)} "
                        f"numerals are round ({', '.join(map(str, roundish[:6]))})")
    if em >= 3 and em_rate > 1.0:
        warnings.append(f"em-dash density: {em} in {wc} words ({em_rate:.1f}/200) — target <=1/200")
    if tricolon > max(1, wc // 500):
        warnings.append(f"tricolon: {tricolon} in {wc} words — target <=1/500")
    if negdef:
        warnings.append(f'negative definition ("not X, but Y"): {negdef}')
    if banned_hits:
        warnings.append(f"banned lexicon: {', '.join(sorted(banned_hits))}")
    if len(rational_hits) >= 3:
        warnings.append(f"rationalist register: {', '.join(sorted(rational_hits))} "
                        f"— {len(rational_hits)} distinct markers")
    if bold_leads >= 3:
        warnings.append(f"bolded lead-ins: {bold_leads} list items open with a bold claim")
    if burst < 5.0 and len(lens) >= 12:
        warnings.append(f"low burstiness: sentence-length spread {burst:.1f} — target >=5")
    if oneliners == 0 and len(paras) >= 4:
        notes.append("no one-sentence paragraph — fine if nothing else is uniform")

    return {
        "words": wc,
        "paragraphs": len(paras),
        "sentences": len(all_sents),
        "sentence_len_mean": round(statistics.mean(lens), 1) if lens else 0,
        "sentence_len_sigma": round(burst, 1),
        "mic_drop_ratio": round(mic_ratio, 3),
        "mic_drop_count": len(flagged),
        "mic_drop_eligible": eligible,
        "mic_drop_samples": flagged[:8],
        "em_dash": em,
        "em_dash_per_200w": round(em_rate, 2),
        "tricolon": tricolon,
        "negative_definition": negdef,
        "bold_lead_ins": bold_leads,
        "one_sentence_paragraphs": oneliners,
        "numerals_total": len(ints),
        "numerals_47": fam47,
        "numerals_round": roundish,
        "clocks": [f"{h}:{m}" for h, m, _ in clocks],
        "clocks_47": clock47,
        "banned": sorted(banned_hits),
        "rationalist_markers": sorted(rational_hits),
        "warnings": warnings,
        "notes": notes,
    }


def render(r: dict, quiet: bool) -> str:
    L: list[str] = []
    L.append(f"{r['words']} words · {r['paragraphs']} paragraphs · {r['sentences']} sentences")
    L.append(f"  sentence length   mean {r['sentence_len_mean']}  spread {r['sentence_len_sigma']}")
    L.append(f"  mic-drop endings   {r['mic_drop_count']}/{r['mic_drop_eligible']} paragraphs"
             f"  ({r['mic_drop_ratio']:.0%})")
    L.append(f"  em-dash            {r['em_dash']}  ({r['em_dash_per_200w']}/200w)")
    L.append(f"  tricolon           {r['tricolon']}")
    L.append(f"  negative def       {r['negative_definition']}")
    L.append(f"  bold lead-ins      {r['bold_lead_ins']}")
    L.append(f"  numerals           47-family {len(r['numerals_47'])}"
             f" · round {len(r['numerals_round'])} · of {r['numerals_total']}")
    if r["clocks"]:
        L.append(f"  timestamps         {', '.join(r['clocks'])}")
    if r["rationalist_markers"]:
        L.append(f"  register markers   {', '.join(r['rationalist_markers'])}")

    if r["warnings"]:
        L.append("")
        L.append(f"{len(r['warnings'])} warning(s):")
        for w in r["warnings"]:
            L.append(f"  ! {w}")
    else:
        L.append("")
        L.append("no warnings. This means the mechanical checks passed, not that the")
        L.append("prose is good. `reviewer-stance.md` cannot be measured.")

    if r.get("notes"):
        L.append("")
        for n in r["notes"]:
            L.append(f"  ~ {n}")

    if not quiet and r["mic_drop_samples"]:
        L.append("")
        L.append("paragraph endings shaped like verdicts:")
        for s in r["mic_drop_samples"]:
            L.append(f"  · {s}")
        L.append("")
        L.append("Most of those can simply be deleted — the paragraph usually ends")
        L.append("one sentence earlier and the extra sentence is the tell.")
        L.append("Caveat: this measures SHAPE, not earning. A punchy human essayist")
        L.append("reads identically here. High ratio is not proof of anything; it is")
        L.append("reason to check whether each of those verdicts was paid for.")

    return "\n".join(L)


def main() -> int:
    # Windows consoles default to cp1252 and will crash on prose containing
    # characters the code page can't encode. Force UTF-8 with replacement.
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8", errors="replace")
        except (AttributeError, OSError):
            pass

    ap = argparse.ArgumentParser(description="Measure a draft against training-data gravity.")
    ap.add_argument("path", help="file to read, or - for stdin")
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    ap.add_argument("--quiet", action="store_true", help="metrics only, no sample sentences")
    args = ap.parse_args()

    try:
        if args.path == "-":
            text = sys.stdin.read()
        else:
            with open(args.path, "r", encoding="utf-8") as fh:
                text = fh.read()
    except OSError as exc:
        print(f"gravity-check: {exc}", file=sys.stderr)
        return 2

    if not text.strip():
        print("gravity-check: empty input", file=sys.stderr)
        return 2

    r = analyse(text)
    if args.json:
        print(json.dumps(r, indent=2, ensure_ascii=False))
    else:
        print(render(r, args.quiet))
    return 1 if r["warnings"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
