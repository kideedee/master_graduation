# Plan: Chapter 3 — Rewrite "Nhánh CNN Đa kernel" subsection

## Context
User renamed the module to "Modified TextCNN" with the CNN multi-kernel branch as a named subcomponent.
The current subsection `\subsubsection{Nhánh CNN Đa kernel}` (line 127) needs to be rewritten
to reflect this naming and align with the actual implementation in `phabert_cnn_model.py`.

## Key facts from implementation (phabert_cnn_model.py)
- `self.cnn_branches`: ModuleList of 3 branches, kernel sizes 3, 5, 7
- Each branch: Conv1d(768→256, k) → BatchNorm1d → ReLU → Conv1d(256→128, k) → BatchNorm1d → ReLU → AdaptiveMaxPool1d(1)
- Padding: kernel 3 → padding=1, kernel 5 → padding=2, kernel 7 → padding=3 (same-padding)
- Output per branch: [batch, 128] after squeeze
- `self.attention_pooling`: Linear(768→64) → Tanh → Linear(64→1) → Softmax(dim=1)
- `self.global_pooling`: Linear(768→128) → ReLU → Dropout(0.1)
- Combined: [global_features(128)] + [cnn_features(128×3)] = 512 total

## What to rewrite
Only the `\subsubsection{Nhánh CNN Đa kernel}` block (lines 127–142).
The section intro at line 125 and the attention pooling subsubsection remain unchanged.

## Outline for rewritten subsection

**Paragraph 1 — Motivation and origin:**
Describe that this branch is adapted from TextCNN (Kim 2014), originally for text classification.
Explain the adaptation: instead of word embeddings, operates on 768-dim DNABERT-2 contextual representations;
adds a second stacked Conv1d layer for hierarchical feature extraction (not in original TextCNN).

**Paragraph 2 — Architecture (with equations):**
Three parallel pathways with kernel sizes k ∈ {3, 5, 7}.
Each pathway: two stacked Conv1d layers with channel reduction 768→256→128, BatchNorm+ReLU after each,
same-padding to preserve sequence length, AdaptiveMaxPool1d(1) to get fixed 128-dim vector.
Equations for the two conv layers and pooling (reuse existing eq labels).

**Paragraph 3 — Multi-scale rationale:**
Explain what each kernel size captures biologically:
- k=3: fine-grained local motifs (~6-12 bp after BPE compression)
- k=5: intermediate patterns (~10-20 bp)
- k=7: broader functional domains (~20-30 bp)
Concatenation to form 384-dim CNN feature vector.

## Citation list
| Key | Reason |
|-----|--------|
| kim2014convolutional | TextCNN origin |
| szegedy2015going | Inception-style multi-scale parallel branches |
| johnson2017deep | CNN on pre-trained embeddings for NLP |

## Numbers to verify
- Channel sizes: 768→256→128 ✓ (from code lines 38-43)
- Kernel sizes: 3, 5, 7 ✓ (from code lines 38, 48, 58)
- Padding: 1, 2, 3 (same-padding) ✓ (from code)
- Output per branch: 128-dim ✓
- Concatenated CNN output: 384-dim ✓ (128×3)
