# CLAUDE.md

Vietnamese master's thesis: PhaBERT-CNN (DNABERT-2 + CNN) for phage lifestyle prediction.
Author: Vu Quang Son · VNU-UET · Supervisor: Dr. Diep Thi Hoang · 2025

## Tech Stack
- **Language**: LaTeX (report class, A4, 13pt) + Python (model code snippets)
- **Vietnamese support**: `\usepackage[utf8]{vietnam}` + `\usepackage[utf8]{inputenc}`
- **Bibliography**: natbib, unsrt, sort&compress — single bib file: `references.bib`
- **Margins**: L=3cm R=2cm T=2.5cm B=3cm · Line spacing 1.3

## Project Map
```
thesis.tex              → Entry point (input all chapters)
references.bib          → Bibliography (single source of truth — never duplicate entries)
document/phabert_cnn.tex → OUR experimental results (authoritative source for our numbers)

chapters/c1/  → Introduction
chapters/c2/  → Background & related work
chapters/c3/  → Proposed method (PhaBERT-CNN)
chapters/c4/  → Experiments & results
chapters/c5/  → Conclusion

plans/        → Writing plans (created by /plan, consumed by /implement)
imgs/         → All figures (PNG/PDF)
snipet/       → Python code snippets included via \lstinputlisting
.claude/rules/ → Domain-specific rules (auto-loaded when relevant)
```

## Commands
```bash
# Full compile (REQUIRED after any .bib change or new \label/\ref)
pdflatex thesis.tex && bibtex thesis && pdflatex thesis.tex && pdflatex thesis.tex

# Quick compile (during active writing — no bib changes)
pdflatex thesis.tex

# Verify a citation key exists before using it
grep -c "KEY" references.bib
```

## IMPORTANT: Critical Rules

1. **Vietnamese-first.** English ONLY for model names and untranslatable technical terms.
   → Always read `.claude/rules/vietnamese-terms.md` before writing any Vietnamese content.

2. **Every number needs a source.**
   - Our results → verify in `document/phabert_cnn.tex`
   - Others' results → verify via WebFetch on the paper's DOI/arXiv URL before citing

3. **Every `\cite{key}` must exist in references.bib.**
   → Run `grep -c "KEY" references.bib` BEFORE writing any citation. Never invent keys.

4. **Every figure/table/equation needs `\label{}` + `\ref{}`.**
   → No floating figures or tables without cross-references.

5. **Full 4-command compile after any .bib changes.**
   → Quick compile is NOT enough after adding/changing references.

6. **NEVER run git commands** — blocked by hooks. Do not attempt any git operation.

## Gotchas — Read Before Every Writing Session

| Failure mode | Prevention |
|---|---|
| **Citation key hallucination** — Claude invents keys not in .bib | `grep` every key before use |
| **Vietnamese term drift** — inconsistent translations across sessions | Read `vietnamese-terms.md` first |
| **Inaccurate paper claims** — wrong numbers or wrong attribution | WebFetch the paper; verify the exact claim |
| **LaTeX special chars** — unescaped `_` or `%` break compilation | Use `\_` in text mode, `\%` outside math |
| **Stale cross-references** — `\ref{}` shows `??` in PDF | Run full compile; check `\label` spelling matches |

## Workflows

| Goal | Use skill | Flow |
|---|---|---|
| Write new section from scratch | `/thesis-writing` | auto: Plan → Write → Verify |
| Review plan before writing | `/plan <ch> <sec>` then `/implement <plan>` | manual: you confirm plan first |
| Check citations after writing | `/verify <file>` | runs citation-verifier agent |
| Compile + debug errors | `/latex-compiling` | auto-fixes common errors |
| Full citation audit | `/citation-verifying` | deep check all keys + claims |
| Review full chapter | `/thesis-reviewing` | structure, labels, consistency |
| Convert paper section to thesis | `/paper-converting` | Plan → Write → Verify |
| Manage Vietnamese terms | `/terminology-managing` | checks vietnamese-terms.md |
| Check self-plagiarism | `/plagiarism-checking` | compares against phabert_cnn.tex |

**Quick fix** (typos, small edits): Edit directly — no workflow needed. Grep-check citations after.

## Rules Files (domain-specific, auto-loaded)
- `.claude/rules/vietnamese-terms.md` — VN↔EN terminology, forbidden substitutions
- `.claude/rules/bibliography.md` — bib entry formats, citing, verifying claims
- `.claude/rules/bioinformatics-content.md` — sequence formatting, metric tables, math notation
- `.claude/rules/figures-tables.md` — figure/table LaTeX templates
- `.claude/rules/latex-commands.md` — common LaTeX patterns for this thesis
- `.claude/rules/python-code.md` — code snippet formatting
- `.claude/rules/troubleshooting.md` — compilation error fixes