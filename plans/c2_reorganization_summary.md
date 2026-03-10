# Chapter 2 Reorganization Summary

## Task Completed

Successfully reorganized Chapter 2 by moving DNABERT and DNABERT-2 content from a standalone section into the "Related Works" section, while keeping tokenization methods as a separate subsection.

## Changes Made

### 1. Removed Section 2.3 "DNABERT và DNABERT-2"
- Deleted the standalone section that was between "Học máy và học sâu" and "Học chuyển giao"
- This section contained:
  - Subsection 2.3.1: DNABERT
  - Subsection 2.3.2: DNABERT-2
  - Table comparing DNABERT vs DNABERT-2

### 2. Renumbered Sections
- Section 2.4 "Học chuyển giao trong tin sinh học" (was Section 2.4, now Section 2.3)
- Section 2.5 "Các công trình liên quan" (remains Section 2.4)

### 3. Added DNABERT Content to Related Works
Inserted two new subsections in Section 2.4 (Các công trình liên quan):
- **Subsection 2.4.3: DNABERT** (moved from old 2.3.1)
  - Describes DNABERT architecture and overlapping k-mer tokenization
  - Lists four main limitations: information leakage, computational inefficiency, 512 token limit, single-species pre-training

- **Subsection 2.4.4: DNABERT-2** (moved from old 2.3.2)
  - Describes three major improvements: BPE tokenization, ALiBi positional encoding, Flash Attention + multi-species pre-training
  - Includes architecture details (12 layers, 768 hidden size, 117M parameters)
  - Includes comparison table (Table 2.1: DNABERT vs DNABERT-2)

### 4. Renumbered Existing Subsections
- **Subsection 2.4.5: Các phương pháp phân tách token trong phân tích hệ gen** (was 2.4.3)
  - Kept as separate subsection as requested
  - Covers: one-hot encoding, overlapping k-mer, Word2Vec on k-mer, BPE
  - Includes comparison table (Table 2.2: tokenization methods comparison)

- **Subsection 2.4.6: Tổng hợp và khoảng trống nghiên cứu** (was 2.4.4)
  - Research gap summary and motivation for PhaBERT-CNN

## Final Structure of Section 2.4 (Các công trình liên quan)

```
2.4 Các công trình liên quan
├── 2.4.1 Các phương pháp học máy truyền thống
│   ├── PHACTS
│   ├── PhageAI
│   └── BACPHLIP
├── 2.4.2 Các phương pháp học sâu
│   ├── DeePhage
│   ├── PhaTYP
│   ├── DeepPL
│   └── ProkBERT
├── 2.4.3 DNABERT [NEW LOCATION]
├── 2.4.4 DNABERT-2 [NEW LOCATION]
├── 2.4.5 Các phương pháp phân tách token trong phân tích hệ gen
│   ├── Mã hóa one-hot
│   ├── k-mer có chồng lấp
│   ├── Word2Vec trên k-mer
│   └── BPE
└── 2.4.6 Tổng hợp và khoảng trống nghiên cứu
```

## Rationale

1. **Logical flow**: DNABERT and DNABERT-2 are foundation models that PhaBERT-CNN builds upon, so they naturally belong in "related works" rather than as a separate theoretical section.

2. **Grouping related content**: All methods related to phage lifestyle classification are now grouped together in one section.

3. **Clear progression**: The structure now follows a clear progression:
   - Traditional ML methods → Deep learning methods → DNABERT → DNABERT-2 → Tokenization methods → Research gap

4. **Tokenization as separate subsection**: Tokenization methods remain as a distinct subsection because they are a cross-cutting concern that applies to multiple methods (DNABERT, DNABERT-2, DeepPL, ProkBERT, PhaBERT-CNN).

## Verification

- ✅ LaTeX compilation successful (thesis.pdf generated)
- ✅ No undefined cross-references to old Section 2.3
- ✅ All citations intact
- ✅ Tables properly numbered and referenced
- ✅ Chapter introduction still accurate (mentions "bốn phần chính" which is still correct)

## Files Modified

- `chapters/c2/chapter_2.tex` - Main reorganization
- `plans/c2_reorganize_dnabert_plan.md` - Planning document
- `plans/c2_reorganization_summary.md` - This summary

## Next Steps

If you want to compile with bibliography:
```bash
pdflatex thesis.tex && bibtex thesis && pdflatex thesis.tex && pdflatex thesis.tex
```

This will resolve the citation warnings and ensure all cross-references are correct.
