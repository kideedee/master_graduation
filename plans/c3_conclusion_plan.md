# Plan: Chapter 3 — Kết luận chương

## Goal
Replace the current verbose conclusion with a concise summary of what Chapter 3 achieved.
No new citations, no new numbers, no re-explaining details already in the body.

## Outline

**Paragraph 1 — Overview sentence**
One sentence: Chapter 3 presented the PhaBERT-CNN method across four main sections.

**Paragraph 2 — Data preprocessing**
One sentence summarizing: 2,241 complete phage genomes → sliding window contig generation (4 groups A–D) → reverse complement augmentation → Random Undersampling for class balance.

**Paragraph 3 — Architecture**
One sentence: DNABERT-2 backbone + Modified TextCNN (multi-scale CNN branches k∈{3,5,7} + attention pooling) → 512-dim combined representation → 3-layer classification head.

**Paragraph 4 — Training strategy**
One sentence: Two-phase fine-tuning — warm-up (frozen backbone) then full fine-tuning with discriminative learning rates.

**Closing sentence**
Transition to Chapter 4 (experiments and evaluation).

## Citation list
None — conclusion section does not introduce new claims.

## Numbers to verify
None — no new numbers introduced; all numbers already verified in body.