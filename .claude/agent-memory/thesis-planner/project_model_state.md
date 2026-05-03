---
name: Project Model State
<<<<<<< HEAD
description: Current state of PhaBERT-CNN model architecture — attention pooling removed in favor of masked mean pooling; abstract rewrite needed
=======
description: Current state of PhaBERT model naming, ablation study configuration, and architecture — as of 2026-05-02 revision request
>>>>>>> f8fa44d37b854687ffda96e5b79eee039d4ce47f
type: project
---

## Model Naming (as of 2026-05-02)

The proposed model has been renamed: **PhaBERT-CNN → PhaBERT**.

All chapters (c1–c5), abstracts, and glossary need updating. A detailed plan exists at `plans/c4_ablation_phabert_revision_plan.md`.

## New Ablation Study (4 Configurations)

<<<<<<< HEAD
**How to apply:** A detailed revision plan exists at `plans/c3_mkca_revision_plan.md`. Chapter 3 changes required:
1. Intro paragraph (line 4): remove "lớp gộp chú ý"
2. sec:overview (line 15): replace "Attention Pooling\cite{lin2017structured}" → "masked mean pooling"
3. MKCA subsec intro (line 116): update two-branch description
4. Delete entire subsubsec "Nhánh Attention Pooling toàn cục" (lines 139–163), removing eq:attn_hidden through eq:attn_proj and \cite{lin2017structured}
5. Add new subsubsec "Nhánh Masked Mean Pooling toàn cục" with eq:mean_pooling and eq:global_proj
6. eq:feature_fusion: change f_attn → f_global, update explanation (line 174)
7. Regularization sentence (line 213): "attention pooling" → "global pooling"
8. Conclusion (line 246): update MKCA description

## Abstract rewrite needed (as of 2026-04-15)

Both `chapters/abtract_vi.tex` and `chapters/abtract_en.tex` contain stale numbers from
the PhaBERT-CNN-AP ablation variant. A rewrite plan exists at `plans/abstract_rewrite_plan.md`.

Correct PhaBERT-CNN numbers (from `chapters/c4/chapter_4.tex` tab:main_results):
- Accuracy: 82.26%, 87.38%, 90.01%, 91.34% (Groups A–D)
- Sensitivity: 82.54%–92.31%
- Specificity: 81.30%–87.71%
- Improvement vs. state-of-the-art: 0.32–6.61%
- MKC over DNABERT-2 baseline: 0.74–4.09%

Wrong numbers currently in abstract (DO NOT USE):
- Accuracy: 81.59%, 87.91%, 90.01%, 90.69% — these are PhaBERT-CNN-AP numbers
- Sensitivity: 82.00%–91.12% — PhaBERT-CNN-AP
- Specificity: 80.15%–90.95% — PhaBERT-CNN-AP
- Improvement: 0.91–5.98% — computed from wrong baseline
=======
The ablation study now has **4 configurations** instead of the previous 3:

1. **DNABERT-2** — baseline, linear classifier head only
2. **PhaBERT** — proposed full model (DNABERT-2 + CNN + global branch)
3. **DNABERT-2-CNN** — ablation: CNN branch only, no global branch
4. **DNABERT-2-AP** — ablation: Attention Pooling branch only, no CNN

The old configurations ("PhaBERT-CNN-AP" and "PhaBERT-CNN") are no longer used.

## Architecture Ambiguity (UNRESOLVED — needs user confirmation)

It is unclear whether the full **PhaBERT** model uses **Attention Pooling** or **Masked Mean Pooling** as its global branch. Chapter 3 currently describes masked mean pooling. The 4-config ablation structure implies AP might be in the full model. User confirmation required before implementing Chapter 3 changes.

## New Ablation Data (Sn / Sp / Acc in %)

| Model | Group A | Group B | Group C | Group D |
|---|---|---|---|---|
| DNABERT-2 | 83,68 / 73,25 / 81,52 | 87,24 / 79,27 / 85,56 | 87,68 / 85,75 / 87,25 | 87,68 / 85,75 / 87,25 |
| PhaBERT | 82,68 / 80,44 / 82,18 | 88,11 / 84,63 / 87,36 | 91,21 / 86,25 / 90,16 | 91,75 / 88,58 / 91,07 |
| DNABERT-2-CNN | 83,33 / 79,77 / 82,56 | 88,50 / 84,33 / 87,59 | 90,60 / 87,96 / 90,04 | 92,38 / **47,88** / 91,34 |
| DNABERT-2-AP | 85,12 / 77,65 / 83,54 | 89,04 / 84,49 / 87,63 | 90,84 / 86,30 / 89,88 | 91,72 / 88,74 / 91,08 |

**Flags requiring user confirmation:**
- DNABERT-2-CNN Group D Sp = 47,88% — likely typo (87,88%?)
- DNABERT-2 Group C and Group D are identical — is this correct?

## Main Results (tab:main_results) — PhaBERT New Numbers

| Metric | Group A | Group B | Group C | Group D |
|---|---|---|---|---|
| Sn | 82,68 | 88,11 | 91,21 | 91,75 |
| Sp | 80,44 | 84,63 | 86,25 | 88,58 |
| Acc | 82,18 | 87,36 | 90,16 | 91,07 |

Old PhaBERT-CNN numbers (now obsolete): Acc = 82,26 / 87,38 / 90,01 / 91,34

**Why:** User provided new experimental results with a restructured ablation study and model rename as part of thesis revision in May 2026.

**How to apply:** Before writing any section referencing model performance, use the new PhaBERT numbers above. Do not use the old PhaBERT-CNN numbers. Always check this memory before citing accuracy figures.
>>>>>>> f8fa44d37b854687ffda96e5b79eee039d4ce47f
