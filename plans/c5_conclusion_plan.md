# Plan: Chapter 5 — Rewrite (incorporating Section 4.3)

## Context
- Current Chapter 5 is bullet-point heavy, uses English phrases, and lacks prose style
- Section 4.3 (Phân tích và thảo luận) from Chapter 4 contains: ưu điểm, hạn chế, đánh giá đóng góp kiến trúc
- These analysis/discussion paragraphs belong in Chapter 5 (Kết luận), not Chapter 4
- Chapter 4 should only present results; Chapter 5 synthesizes and concludes

## Structure

### Intro paragraph
One sentence: Chapter 5 summarizes contributions, analyzes results, discusses limitations, and proposes future directions.

### Section 5.1 — Tóm tắt đóng góp
Prose paragraph: What PhaBERT-CNN is and what it achieves — hybrid DNABERT-2 + Modified TextCNN, operates on raw DNA, no gene prediction dependency, evaluated on 4 contig length groups.

### Section 5.2 — Phân tích kết quả
Moved from Section 4.3. Three prose paragraphs:
1. Ưu điểm: 3 factors (BPE/no Prodigal, pre-trained knowledge, dual-branch architecture)
2. Đánh giá đóng góp kiến trúc: DNABERT-2 baseline vs PhaBERT-CNN comparison, improvement trend by length
3. Hạn chế: Group D gap vs PhaTYP, undersampling info loss, inference cost

### Section 5.3 — Hướng nghiên cứu tương lai
Prose (not bullet list). Three directions:
1. Cải thiện xử lý class imbalance (focal loss, class weighting)
2. Kết hợp protein features theo kiến trúc multi-modal
3. Mở rộng ứng dụng (real metagenomic data, host prediction, interpretability)

### Closing paragraph
One paragraph: significance of PhaBERT-CNN as a paradigm for combining genomic foundation models with task-specific architectures.

## Citation list
| Key | Reason |
|-----|--------|
| hyatt2010prodigal | PhaTYP's dependency on Prodigal |
| trimble2012short | Prodigal fails on short contigs |

## Numbers to verify (all from Chapter 4 results)
- Group A acc: 81.59% ✓
- Group B acc: 87.91% ✓
- Group C acc: 90.01% ✓
- Group D acc: 90.69% ✓
- PhaTYP Group D acc: 91.02% ✓
- Improvement range A–C: 0.91–5.98% ✓
- Accuracy improvement trend: 0.07% (A) → 3.43% (D) over DNABERT-2 baseline ✓
- Specificity improvement Group A: 6.90% ✓