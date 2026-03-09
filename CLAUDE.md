# CLAUDE.md

This file provides guidance to Claude Code when working with this repository.

## Project Overview

Vietnamese master's thesis on bacteriophage genome classification using deep learning.

**Title (VN):** Phân loại lối sống thực khuẩn thể dựa trên phương pháp học sâu
**Title (EN):** Deep Learning Based Methods for Phage Lifestyle Prediction
**Contribution:** PhaBERT_CNN model (BERT + CNN hybrid architecture)
**Domain:** Bioinformatics, Genomics, Deep Learning

**Author:** Vũ Quang Sơn
**Institution:** VNU Hanoi - University of Engineering and Technology
**Supervisors:** Dr. Diep Thi Hoang
**Year:** 2025

**Source:** Research paper at `document/phabert_cnn.tex` (LaTeX source)

## Essential Commands

**Quick compile:**
```bash
pdflatex thesis.tex
```

**Full compile with bibliography:**
```bash
pdflatex thesis.tex && bibtex thesis && pdflatex thesis.tex && pdflatex thesis.tex
```

**Clean auxiliary files:**
```bash
rm -f *.aux *.log *.out *.toc *.lof *.lot *.bbl *.blg *.synctex.gz
```

**Other documents:**
```bash
pdflatex cover.tex      # Cover pages
pdflatex slide.tex      # Presentation slides
```

## Project Structure

**Main files:**
- `thesis.tex` - Main document
- `cover.tex` - Three cover pages (VN, VN+author, EN)
- `references.bib` - Bibliography database
- `slide.tex` - Beamer presentation

**Chapters:** `chapters/c1/` through `chapters/c5/`
- c1: Introduction (Giới thiệu)
  - Background, problem statement, objectives, contributions, scope, organization
- c2: Theoretical Background (Cơ sở lý thuyết)
  - Bacteriophage biology, metagenomics, ML/DL fundamentals
  - CNN, Transformer, BERT, DNABERT, DNABERT-2
  - Transfer learning, related work
- c3: Proposed Method - PhaBERT_CNN (Phương pháp đề xuất)
  - Section 3.1: Overview (motivation, pipeline, advantages)
  - Section 3.2: Data collection & preprocessing (sources, sliding window, augmentation, class imbalance)
  - Section 3.3: Architecture (DNABERT-2 backbone, multi-scale CNN, attention pooling, classification head)
  - Section 3.4: Training strategy (two-phase fine-tuning, discriminative learning rates, regularization)
- c4: Experiments and Evaluation (Thực nghiệm)
  - Dataset construction, hardware/software setup, baseline methods
  - Results on 4 contig length groups (100-400, 400-800, 800-1200, 1200-1800 bp)
  - Performance comparison, analysis, ablation study
- c5: Conclusion (Kết luận)
  - Summary, main results, contributions, limitations, future work

**Supporting:**
- `imgs/` - Figures and diagrams (PhaBERT-CNN architecture, results)
- `snipet/` - Python code examples
- `implementation/` - Python implementation of models
  - `phabert_cnn_model.py` - `Dnabert2CnnModel` (PhaBERT-CNN) and `Dnabert2DenseModel` (baseline)
- `document/phabert_cnn.tex` - Source research paper (LaTeX)

## LaTeX Configuration

- Document class: `report`, A4, 13pt
- Margins: left=3cm, right=2cm, top=2.5cm, bottom=3cm
- Line spacing: 1.3
- Vietnamese: `\usepackage[utf8]{vietnam}` + `\usepackage[utf8]{inputenc}`
- Bibliography: `natbib` with `unsrt` style, numbers, sort&compress

## Critical Rules

1. **NEVER commit sensitive files** (.env, credentials)
2. **Always run full compile** when adding citations or modifying references.bib
3. **UTF-8 encoding required** for Vietnamese characters
4. **Cross-reference everything** - all figures, tables, equations must have \label{} and be referenced
5. **Consistent terminology** - use Vietnamese ↔ English mapping from `.claude/rules/vietnamese-terms.md`
6. **Vietnamese language requirement** - Write the entire thesis in Vietnamese. Only use English for:
   - Technical terms that have no Vietnamese equivalent (e.g., "BPE tokenization", "attention pooling", "embedding")
   - Model/algorithm names (e.g., "DNABERT-2", "PhaBERT-CNN", "Random Forest")
   - Citations and references
   - Mathematical notation and variable names
   - Code snippets and technical specifications
   - Proper nouns (e.g., "SentencePiece framework", "ALiBi")

## Mandatory Writing Workflow

**Every time you write or expand thesis content, follow all 3 steps in order. Do not skip any step.**

### Step 1 — Plan

Before writing any LaTeX, create a plan file at `plans/<chapter>_<section>_plan.md`.

The plan must include:
1. **Outline** — numbered sections and subsections (I, II, III / 1, 2, 3)
2. **Paragraph descriptions** — for each paragraph: one sentence describing what it argues or explains
3. **Required citations** — list every citation key you intend to use, with a short note on why
4. **Numbers to verify** — list every number that will appear (accuracy, F1, dataset sizes, parameter counts)

Do not proceed to Step 2 until the plan file is saved.

### Step 2 — Write

Write LaTeX content following the plan exactly.
- Write entirely in Vietnamese (see Critical Rule #6 for exceptions)
- Use terminology from `.claude/rules/vietnamese-terms.md`
- Every figure, table, and equation must have `\label{}` and be referenced in text
- Every claim with a number must have `\cite{}`

### Step 3 — Verify

After writing, verify before presenting output:
1. **Citation keys** — confirm every `\cite{key}` exists in `references.bib`
2. **Claim verification** — use WebFetch to retrieve cited papers and confirm claims are accurate
3. **Number verification** — cross-check every number against `document/phabert_cnn.tex` (this work's results) or the cited paper (other works' results)
4. **Vietnamese terminology** — check every technical term against `.claude/rules/vietnamese-terms.md`

Report verification results. Fix all failures before finalizing output.

---

## Paper to Thesis Notes

**Chapter 3 Structure:**
- Based on Material and Methods section from `document/phabert_cnn.tex`
- Expanded with detailed explanations, rationale, and mathematical formulations
- Four main sections:
  1. Overview: Motivation, pipeline, advantages
  2. Data preprocessing: Sources, sliding window algorithm, augmentation, class imbalance handling
  3. Architecture: DNABERT-2 backbone, dual parallel branches (multi-scale CNN + attention pooling), classification head
  4. Training strategy: Two-phase fine-tuning with discriminative learning rates
- All content written directly in `chapters/c3/chapter_3.tex` (single file, not split into subsections)
- Includes algorithms, equations, tables for parameters and hyperparameters

## Detailed Guidance

For detailed instructions, see `.claude/rules/`:
- `bioinformatics-content.md` - Genomic sequences, model diagrams, metrics tables
- `python-code.md` - Code integration with listings package
- `bibliography.md` - Bibliography management and citation
- `figures-tables.md` - Adding and formatting figures/tables
- `vietnamese-terms.md` - Technical terminology mapping
- `latex-commands.md` - Common LaTeX commands for this thesis
- `troubleshooting.md` - Common issues and solutions

## Multi-Agent Workflows

Specialized agents available via slash commands:
- `/compile` - Compile thesis and debug errors
- `/review` - Review content consistency, structure, citations, and terminology
- `/paper2thesis` - Convert paper content to thesis format (uses 3-step workflow)
- `/plagiarism` - Check self-plagiarism and paraphrasing
- `/write-content` - Write new thesis content (uses 3-step workflow)
- `/terminology` - Manage terminology and abbreviations (add terms, check consistency, verify abbreviation expansion)

See `.claude/commands/` for agent details.

## Git Workflow

- Main branch: `master`
- LaTeX auxiliary files gitignored
- PDF tracked in repository
