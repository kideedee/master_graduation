# CLAUDE.md

Vietnamese master's thesis on phage genome classification using deep learning (PhaBERT-CNN).

**Author:** Vũ Quang Sơn · **Institution:** VNU-UET · **Supervisor:** Dr. Diep Thi Hoang · **Year:** 2025

## Commands

```bash
# Full compile (ALWAYS use when citations or references.bib change)
pdflatex thesis.tex && bibtex thesis && pdflatex thesis.tex && pdflatex thesis.tex

# Quick compile (no bib changes)
pdflatex thesis.tex

# Other documents
pdflatex cover.tex      # Cover pages
pdflatex slide.tex      # Beamer slides

# Clean aux files
rm -f *.aux *.log *.out *.toc *.lof *.lot *.bbl *.blg *.synctex.gz
```

## Project Map

```
thesis.tex                  ← Entry point
cover.tex                   ← Cover pages (VN, VN+author, EN)
references.bib              ← Bibliography (single source of truth for all citations)
slide.tex                   ← Beamer presentation
chapters/c1/ → c5/          ← Chapters (c1:Intro, c2:Theory, c3:Method, c4:Experiments, c5:Conclusion)
document/phabert_cnn.tex    ← Source research paper (ground truth for ALL numbers from this work)
implementation/             ← Python models (Dnabert2CnnModel, Dnabert2DenseModel)
imgs/                       ← Figures and diagrams
snipet/                     ← Python code examples for listings
plans/                      ← Writing plans (created by skills before writing)
```

## LaTeX Config

Document class: `report`, A4, 13pt · Margins: L=3cm R=2cm T=2.5cm B=3cm · Line spacing: 1.3
Vietnamese: `\usepackage[utf8]{vietnam}` + `\usepackage[utf8]{inputenc}`
Bibliography: `natbib` with `unsrt` style, numbers, sort&compress

## Critical Rules

1. **Vietnamese-first.** Write entirely in Vietnamese. English ONLY for: model names, untranslatable terms (BPE, attention pooling...), citations, math, code. ALWAYS check `.claude/rules/vietnamese-terms.md` before writing.
2. **Every number needs a source.** Our results → verify against `document/phabert_cnn.tex`. Other works → verify against cited paper via WebFetch. NEVER guess or hallucinate numbers.
3. **Every `\cite{key}` must exist in `references.bib`.** Run `grep -c "KEY" references.bib` BEFORE using any citation key.
4. **Every figure/table/equation needs `\label{}` and `\ref{}`.** No orphan floats.
5. **Full compile after bib changes.** Always run the 4-command sequence.
6. **Never use git commands.** All git operations are manual. See Git section below.

## Gotchas — Recurring Mistakes

**IMPORTANT: Read these before every writing task.**

- **Citation key hallucination.** Claude invents keys not in references.bib. ALWAYS grep first.
- **Vietnamese term drift.** Claude uses different VN translations for the same EN term across sessions (e.g., "mạng nơ-ron" vs "mạng thần kinh"). ALWAYS read `.claude/rules/vietnamese-terms.md` before writing.
- **Inaccurate paper claims.** Claude gets exact numbers wrong or attributes results to wrong papers. ALWAYS verify against the actual source before writing any numerical claim.
- **LaTeX special chars.** Use `\_` for underscores in text mode. Use `\%` outside math mode.
- **Bib entry format.** New entries must use lowercase `@article{key,` — match existing style in references.bib.

## Rules (domain-specific guidance)

See `.claude/rules/` — Claude loads these automatically when relevant:
- `vietnamese-terms.md` — Canonical VN↔EN mappings (**check before every writing task**)
- `bioinformatics-content.md` — Genomic sequences, model diagrams, metrics tables
- `bibliography.md` — Bib entry formats and citation verification procedure
- `figures-tables.md` — Figure/table LaTeX templates
- `latex-commands.md` — Common commands for this thesis
- `python-code.md` — Code listings integration
- `troubleshooting.md` — Common LaTeX compilation fixes

## Skills (on-demand workflows)

Available via `/skill-name`. Claude also auto-triggers when relevant:
- `/thesis-writing` — 3-step Plan→Write→Verify workflow for new content
- `/latex-compiling` — Compile thesis + auto-debug errors
- `/citation-verifying` — Verify all citations exist and claims match papers
- `/thesis-reviewing` — Review chapter for consistency, structure, terminology
- `/paper-converting` — Convert paper sections to expanded thesis format
- `/terminology-managing` — Add terms, check abbreviations, verify consistency
- `/plagiarism-checking` — Check self-plagiarism against source paper

### Agent shortcuts

Quick slash commands that invoke agents directly:
- `/plan <chapter> <section>` — Invoke `thesis-planner` to create a writing plan
- `/implement <plan file>` — Invoke `thesis-writer` to write LaTeX from a confirmed plan
- `/verify <file>` — Invoke `citation-verifier` to check claims against papers

## Agents (specialized subagents)

Defined in `.claude/agents/`. Auto-triggered by skills or invoked directly:
- `thesis-planner` — Read-only exploration + plan creation (used by `/thesis-writing` Step 1, `/plan`)
- `thesis-writer` — Writes LaTeX from confirmed plans (used by `/thesis-writing` Step 2, `/implement`)
- `citation-verifier` — WebFetch verification of claims against papers (used by `/citation-verifying` Phase 2, `/verify`)

Direct invocation: `@thesis-planner`, `@thesis-writer`, or `@citation-verifier` in chat.

## Git

- Main branch: `master`
- LaTeX aux files gitignored
- PDF tracked in repository
- **NEVER run any git commands** (git add, git commit, git push, git status, git diff, git log, git reset, etc.). All git operations are handled manually by the user. This applies to Claude Code and all subagents.