---
name: thesis-reviewing
description: >
  Review thesis chapters for consistency, structure, citations, and terminology.
  Use when user says "review", "check chapter", "kiểm tra", "đánh giá",
  "verify consistency", or before submitting a chapter.
  Covers: structure, terminology, labels/refs, citation accuracy, and writing quality.
---

# Thesis Review

Comprehensive review of a chapter or file covering 5 dimensions.

## Review Dimensions

### 1. Structure & Flow
- Section/subsection hierarchy is logical
- Paragraphs flow with transitions
- No orphan sections (subsection without parent)
- Chapter length is proportionate to importance
- **Chapter introduction consistency**: The introductory paragraph of each chapter must accurately describe ALL sections/subsections that follow. If new content was added (e.g., a new Discussion section), verify the chapter intro mentions it. Flag any mismatch between promised content and actual sections.

### 2. Vietnamese Terminology
- Read `.claude/rules/vietnamese-terms.md` FIRST
- Every VN technical term matches the canonical mapping
- Same EN concept → same VN translation everywhere
- "Forbidden Substitutions" terms kept in English
- First occurrence of abbreviation: "Full Vietnamese (English, ABBR)" format

### 3. Figures, Tables, Equations
- Every `\begin{figure}`, `\begin{table}`, `\begin{equation}` has `\label{}`
- Every `\label{}` has at least one `\ref{}` in text
- Captions are in Vietnamese
- Tables use `booktabs` style (`\toprule`, `\midrule`, `\bottomrule`)

### 4. Citations (delegate to `/citation-verifying` for deep check)
- Quick check: all `\cite{key}` exist in references.bib
- Claims with numbers have citations
- No uncited claims about other works

### 5. Writing Quality
- Academic tone maintained
- No informal language
- Sentences not too long (Vietnamese academic style)
- Technical depth appropriate for master's thesis

## Workflow

1. Read the target chapter/file
2. Read `.claude/rules/vietnamese-terms.md`
3. Run checks for all 5 dimensions
4. For citation issues: suggest running `/citation-verifying` for deep verification
5. Report findings with specific line numbers and fix suggestions

## Output Format

```
**Reviewing:** [file/chapter]

**1. Structure:** [✓ OK / issues found]
**2. Terminology:** [✓ OK / N issues]
**3. Labels/Refs:** [✓ OK / N missing]
**4. Citations:** [✓ OK / N issues — run /citation-verifying for deep check]
**5. Writing:** [✓ OK / N suggestions]

**Issues (by priority):**
1. [CRITICAL] ...
2. [WARNING] ...
3. [SUGGESTION] ...
```

## Gotchas
- Do NOT report "Forbidden Substitution" terms as terminology errors (embedding, fine-tuning, attention, tokenization, dropout, pooling, backbone, benchmark, pipeline, BPE, k-mer, contig, metagenomic, etc.)
- Vietnamese metric terms: use "do nhay" (sensitivity), "do dac hieu" (specificity) in Vietnamese text, not English equivalents
- Don't flag standard LaTeX macros as undefined — check the preamble first
- Cross-chapter term check: same English term must map to same Vietnamese translation everywhere
- Do NOT suggest adding citations for common knowledge claims (e.g., "DNA consists of four nucleotides")
