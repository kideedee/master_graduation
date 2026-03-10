# Plan: Reorganize DNABERT content into Related Works

## Current Structure

**Section 2.3: DNABERT và DNABERT-2** (standalone section)
- 2.3.1: DNABERT
- 2.3.2: DNABERT-2
- Table comparing DNABERT vs DNABERT-2

**Section 2.5: Các công trình liên quan**
- 2.5.1: Các phương pháp học máy truyền thống
- 2.5.2: Các phương pháp học sâu
- 2.5.3: Các phương pháp phân tách token trong phân tích hệ gen
- 2.5.4: Tổng hợp và khoảng trống nghiên cứu

## Proposed New Structure

**Remove Section 2.3 entirely**

**Section 2.4: Học chuyển giao trong tin sinh học** (renumber from 2.4)

**Section 2.5: Các công trình liên quan** (keep as 2.5)
- 2.5.1: Các phương pháp học máy truyền thống (unchanged)
- 2.5.2: Các phương pháp học sâu (unchanged)
- **2.5.3: DNABERT** (moved from 2.3.1)
- **2.5.4: DNABERT-2** (moved from 2.3.2)
- 2.5.5: Các phương pháp phân tách token trong phân tích hệ gen (renumber from 2.5.3)
- 2.5.6: Tổng hợp và khoảng trống nghiên cứu (renumber from 2.5.4)

## Rationale

1. DNABERT and DNABERT-2 are foundation models that PhaBERT-CNN builds upon, so they belong in "related works"
2. Tokenization methods remain as a separate subsection to maintain clear organization
3. This structure groups all related work together in one section
4. The flow is logical: traditional ML → deep learning → DNABERT → DNABERT-2 → tokenization methods → research gap

## Changes Required

1. Delete Section 2.3 heading and content (lines 116-160)
2. Add DNABERT content as subsection 2.5.3 in related works
3. Add DNABERT-2 content as subsection 2.5.4 in related works
4. Renumber existing subsections 2.5.3 → 2.5.5 and 2.5.4 → 2.5.6
5. Update all cross-references to Section 2.3 throughout the thesis
6. Update section numbering for Section 2.4 (Transfer Learning) if needed

## Content to Move

- Lines 116-160 from current chapter_2.tex
- Includes: DNABERT subsection, DNABERT-2 subsection, comparison table
- No content changes, only structural reorganization
