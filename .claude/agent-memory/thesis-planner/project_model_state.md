---
name: Project Model State
description: Current state of PhaBERT-CNN model architecture — attention pooling removed in favor of masked mean pooling; abstract rewrite needed
type: project
---

The model in `implementation/phabert_cnn_model.py` has been revised (as of 2026-04-13). The class is now `Dnabert2CnnModelNoAttention`.

Key architectural change: **Attention pooling (nhánh Attention Pooling) has been removed.** It is replaced by **masked mean pooling** for global transformer feature aggregation.

Architecture now:
- DNABERT-2 backbone (frozen in warmup, unfrozen in fine-tuning)
- 3 parallel CNN branches with kernels {3, 5, 7}: 768→256→128 channels, AdaptiveMaxPool1d → f_CNN ∈ R^384
- Global pooling via masked mean pooling → Linear(768→128) → ReLU → Dropout(0.1) → f_global ∈ R^128
- Combined features: [f_global; f_CNN] ∈ R^512
- Classifier: 512→256→64→2 (LayerNorm after first layer)

**Why:** The attention pooling was removed as part of an ablation study variant. The masked mean pooling is simpler and deterministic.

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
