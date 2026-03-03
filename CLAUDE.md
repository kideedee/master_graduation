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
- c2: Theoretical Background (Cơ sở lý thuyết)
- c3: Proposed Method - PhaBERT_CNN (Phương pháp đề xuất)
- c4: Experiments and Evaluation (Thực nghiệm)
- c5: Conclusion (Kết luận)

**Supporting:**
- `imgs/` - Figures and diagrams (PhaBERT-CNN architecture, results)
- `snipet/` - Python code examples
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

## Paper to Thesis Workflow

1. Extract sections from paper → expand for thesis chapters
2. Chapter 2 should be 2-3x longer than paper's related work
3. Add implementation details, design decisions, ablation studies
4. Maintain terminology consistency
5. Ensure all citations in references.bib

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
- `/citation-check` - Validate citations and cross-references
- `/compile` - Compile thesis and debug errors
- `/review` - Review content consistency and structure
- `/figures` - Manage figures and images
- `/vietnamese` - Validate Vietnamese language
- `/paper2thesis` - Convert paper content to thesis format
- `/plagiarism` - Check self-plagiarism and paraphrasing
- `/write-content` - Write new thesis content

See `.claude/commands/` for agent details.

## Git Workflow

- Main branch: `master`
- Development: `develop` (current)
- LaTeX auxiliary files gitignored
- PDF tracked in repository
