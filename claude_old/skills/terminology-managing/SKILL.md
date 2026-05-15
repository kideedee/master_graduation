---
name: terminology-managing
description: >
  Manage Vietnamese↔English terminology and abbreviations in the thesis.
  Use when user says "add term", "check abbreviations", "terminology",
  "thuật ngữ", "từ viết tắt", "glossary", "verify consistency",
  or when checking if terms are used consistently across chapters.
---

# Terminology & Abbreviation Manager

## Tasks

### Add New Term
Input: `/terminology-managing add "ABBR" "Full English" "Tiếng Việt"`

1. Read `chapters/glossary.tex` → find last STT number
2. Add new row: `N+1 & ABBR & Full English & Tiếng Việt \\    \hline`
3. Add to `.claude/rules/vietnamese-terms.md` if not present
4. Report what was added

### Check Abbreviation Expansion
Input: `/terminology-managing check-abbr chapters/cN/`

1. Scan .tex files for uppercase abbreviations (2-10 chars)
2. For each: find first occurrence
3. Verify first occurrence has format: "Thuật ngữ đầy đủ (Full English Term, ABBR)"
4. Report: ✓ expanded / ✗ needs expansion

### Verify Consistency
Input: `/terminology-managing verify`

1. Read `.claude/rules/vietnamese-terms.md` for canonical mappings
2. Scan all `chapters/**/*.tex`
3. For each English term: check all VN translations used
4. Flag inconsistencies (e.g., "classification" → "phân loại" in c2 but "phân lớp" in c3)

## Format Rules

**glossary.tex rows:**
```latex
N & ABBR & Full English Term & Thuật ngữ tiếng Việt \\    \hline
```
- STT must be sequential (no gaps)
- Add BEFORE `\end{longtable}`
- Keep 4 spaces before `\hline`

**Abbreviation first-use format:**
```latex
Mạng nơ-ron tích chập (Convolutional Neural Network, CNN)
```

**Terms that STAY in English** (from vietnamese-terms.md "Forbidden Substitutions"):
embedding, fine-tuning, pre-training, attention, tokenization, token, batch, dropout, pooling, backbone, benchmark, pipeline, BPE, ALiBi, k-mer, contig, metagenomic, and all model names.

## Output Format

```
**Action:** [add/check-abbr/verify]

**Results:**
- ✓ [what passed]
- ✗ [what failed + fix suggestion]

**Files modified:** [list, if any]
```
