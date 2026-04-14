# CLAUDE.md

Vietnamese master's thesis: PhaBERT-CNN (DNABERT-2 + CNN) for phage lifestyle prediction.
Author: Vu Quang Son · VNU-UET · Supervisor: Dr. Diep Thi Hoang · 2025

## Commands
pdflatex thesis.tex && bibtex thesis && pdflatex thesis.tex && pdflatex thesis.tex  # Full compile
pdflatex thesis.tex  # Quick compile

## Project Map
thesis.tex → Entry point | references.bib → Bibliography (single source of truth)
chapters/c1/→c5/ → Chapters | document/phabert_cnn.tex → Ground truth for OUR numbers
plans/ → Writing plans | imgs/ → Figures | snipet/ → Code examples

## IMPORTANT: Critical Rules
1. Vietnamese-first. English ONLY for model names, untranslatable terms. Check .claude/rules/vietnamese-terms.md
2. Every number needs a source. Our results → document/phabert_cnn.tex. Others → verify via WebFetch
3. Every \cite{key} must exist: `grep -c "KEY" references.bib` BEFORE using
4. Every figure/table/equation needs \label{} and \ref{}
5. Full compile after bib changes (4-command sequence above)
6. NEVER run any git commands — blocked by hooks and permissions

## Gotchas — ALWAYS READ BEFORE WRITING
- **Citation key hallucination**: Claude invents keys not in references.bib. ALWAYS grep first.
- **Vietnamese term drift**: Different VN translations across sessions. ALWAYS read vietnamese-terms.md
- **Inaccurate paper claims**: Wrong numbers or wrong attribution. ALWAYS verify against source
- **LaTeX special chars**: Use \_ in text mode. Use \% outside math mode

## LaTeX Config
report, A4, 13pt · L=3cm R=2cm T=2.5cm B=3cm · Line spacing 1.3
Vietnamese: \usepackage[utf8]{vietnam} · Bibliography: natbib, unsrt, numbers, sort&compress

## Skills & Agents (type / to invoke)
| Skill | Trigger | Agent used |
|-------|---------|------------|
| /thesis-writing | Write new content | planner → writer → verifier |
| /plan \<ch\> \<sec\> | Create writing plan | thesis-planner |
| /implement \<plan\> | Write from plan | thesis-writer |
| /verify \<file\> | Check citations | citation-verifier |
| /latex-compiling | Compile + debug | — |
| /citation-verifying | Full citation check | citation-verifier |
| /thesis-reviewing | Review chapter | — |
| /paper-converting | Paper → thesis | planner → writer → verifier |
| /terminology-managing | Term management | — |
| /plagiarism-checking | Self-plagiarism check | — |

## When to use which workflow
- **Full flow** (`/thesis-writing`): Write section from scratch — auto Plan→Write→Verify
- **Step-by-step** (`/plan` → `/implement` → `/verify`): When you want to review/confirm plan before writing
- **Quick fix** (direct edit): Small fixes — no workflow needed, just grep-check citations after

## Rules (.claude/rules/) — auto-loaded when relevant
vietnamese-terms.md · bibliography.md · bioinformatics-content.md
figures-tables.md · latex-commands.md · python-code.md · troubleshooting.md
