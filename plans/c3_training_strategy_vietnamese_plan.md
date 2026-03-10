# Plan: Rewrite Section 3.5 with Vietnamese Terminology

## Context

Section 3.5 "Chiến lược huấn luyện và tinh chỉnh" currently contains many English technical terms that should be converted to Vietnamese according to the thesis language requirements. The section describes the two-phase training strategy (warm-up + full fine-tuning) with discriminative learning rates, loss function, and regularization techniques.

## Current Issues

The section contains English terms that should be converted to Vietnamese:
- "fine-tune" → should use "tinh chỉnh" consistently
- "task-specific" → "đặc thù cho tác vụ" or "chuyên biệt cho tác vụ"
- "warm-up" → "khởi động" or "làm nóng"
- "discriminative learning rates" → "tốc độ học phân biệt"
- "gradient" → "gradient" (keep, but consider "độ dốc")
- "overfitting" → "quá khớp"
- "early stopping" → "dừng sớm"
- "weight decay" → "suy giảm trọng số"
- "learning rate" → "tốc độ học"
- "batch size" → keep as "batch size" (forbidden substitution)
- "dropout" → keep as "dropout" (forbidden substitution)
- "backbone" → keep as "backbone" (forbidden substitution)
- "checkpoint" → "điểm kiểm tra" or keep as "checkpoint"

## Outline

### I. Section Introduction (1 paragraph)
Explains the problem of fine-tuning pre-trained models with randomly initialized task-specific layers and introduces the two-phase progressive fine-tuning strategy.

### II. Subsection 3.5.1: Giai Đoạn 1: Khởi Động (1 paragraph)
Describes the warm-up phase where DNABERT-2 is frozen and only Modified TextCNN layers are trained for 1 epoch, including optimizer settings (AdamW, learning rate, weight decay, momentum coefficients, one-cycle schedule).

### III. Subsection 3.5.2: Giai Đoạn 2: Tinh Chỉnh Đầy Đủ (1 paragraph)
Describes the full fine-tuning phase with discriminative learning rates (1×10⁻⁵ for DNABERT-2, 1×10⁻⁴ for task-specific layers), training for up to 10 epochs with one-cycle schedule and early stopping (patience 3).

### IV. Subsection 3.5.3: Hàm Mất Mát và Kỹ Thuật Regularization (2 paragraphs)
1. Binary cross-entropy loss function with equation
2. Regularization techniques: weight decay, dropout, layer normalization, early stopping, AMP, gradient accumulation

## Paragraph Descriptions

1. **Section intro**: Explains that fine-tuning pre-trained models with randomly initialized task-specific layers can cause training instability due to gradient incompatibility, and introduces the two-phase progressive fine-tuning strategy (warm-up + full fine-tuning with discriminative learning rates).

2. **Warm-up phase**: Describes freezing DNABERT-2 (117M parameters) and training only Modified TextCNN layers for 1 epoch to allow randomly initialized layers to learn appropriate parameter configurations before updating pre-trained weights, using AdamW optimizer with specific hyperparameters and one-cycle schedule.

3. **Full fine-tuning phase**: Describes unlocking the entire architecture and optimizing with discriminative learning rates (low rate 1×10⁻⁵ for DNABERT-2 to preserve genomic patterns, high rate 1×10⁻⁴ for task-specific layers for aggressive optimization), training for up to 10 epochs with one-cycle schedule and early stopping.

4. **Loss function**: Presents binary cross-entropy loss as the optimization objective for binary classification with equation.

5. **Regularization techniques**: Lists multiple regularization techniques to prevent overfitting: weight decay via AdamW, dropout (rate=0.1), layer normalization, early stopping (patience 3), AMP for memory reduction, and gradient accumulation (4 steps, physical batch size 8, effective batch size 32).

## Citation List

- `loshchilov2017decoupled` - AdamW optimizer
- `smith2019super` - One-cycle learning rate schedule
- `howard2018universal` - Discriminative learning rates / Universal Language Model Fine-tuning (ULMFiT)

## Numbers to Verify

From current section (no need to verify, these are our implementation details):
- DNABERT-2: 117M parameters
- Warm-up: 1 epoch
- Warm-up learning rate: 2×10⁻³
- Warm-up weight decay: 1×10⁻⁴
- Momentum: β₁=0.9, β₂=0.999
- Warm-up one-cycle: 30% warm-up period, initial division factor 5, final division factor 10
- Full fine-tuning DNABERT-2 learning rate: 1×10⁻⁵
- Full fine-tuning DNABERT-2 weight decay: 1×10⁻⁵
- Full fine-tuning task-specific learning rate: 1×10⁻⁴ (10× higher)
- Full fine-tuning task-specific weight decay: 1×10⁻⁴
- AdamW epsilon: 10⁻⁶
- Full fine-tuning: max 10 epochs
- Full fine-tuning one-cycle: 10% warm-up period, initial division factor 5, final division factor 50
- Early stopping patience: 3 epochs
- Dropout rate: 0.1
- Gradient accumulation: 4 steps
- Physical batch size: 8 samples/GPU
- Effective batch size: 32

## Vietnamese Terminology Mapping

| Current (English) | Replacement (Vietnamese) | Notes |
|---|---|---|
| fine-tune | tinh chỉnh | Already in terminology list |
| task-specific | đặc thù cho tác vụ | New term |
| warm-up | khởi động | New term |
| discriminative learning rates | tốc độ học phân biệt | New term |
| gradient | gradient | Keep English (technical term) |
| overfitting | quá khớp | New term |
| early stopping | dừng sớm | New term |
| weight decay | suy giảm trọng số | New term |
| learning rate | tốc độ học | New term |
| batch size | batch size | Keep (forbidden substitution) |
| dropout | dropout | Keep (forbidden substitution) |
| backbone | backbone | Keep (forbidden substitution) |
| checkpoint | checkpoint | Keep English |
| momentum | momentum | Keep English (technical term) |
| regularization | regularization | Keep English (technical term) |
| layer normalization | layer normalization | Keep English (technical term) |
| mixed precision | mixed precision | Keep English (technical term) |
| gradient accumulation | tích lũy gradient | New term |

## Changes to Make

1. **Line 173**: "fine-tune" → "tinh chỉnh"
2. **Line 173**: "task-specific" → "đặc thù cho tác vụ"
3. **Line 173**: "two-phase progressive fine-tuning" → "tinh chỉnh tiến triển hai giai đoạn"
4. **Line 173**: "warm-up" → "khởi động"
5. **Line 173**: "fine-tuning" → "tinh chỉnh"
6. **Line 173**: "discriminative learning rates" → "tốc độ học phân biệt"
7. **Line 175**: "Warm-up" → "Khởi Động"
8. **Line 177**: "warm-up" → "khởi động"
9. **Line 177**: "learning rate" → "tốc độ học"
10. **Line 177**: "weight decay" → "suy giảm trọng số"
11. **Line 179**: "Fine-tuning Đầy Đủ" → keep as is
12. **Line 181**: "warm-up" → "khởi động"
13. **Line 181**: "discriminative learning rates" → "tốc độ học phân biệt"
14. **Line 181**: "learning rate" → "tốc độ học"
15. **Line 181**: "weight decay" → "suy giảm trọng số"
16. **Line 181**: "early stopping" → "dừng sớm"
17. **Line 181**: "overfitting" → "quá khớp"
18. **Line 181**: "checkpoint" → keep as "checkpoint"
19. **Line 192**: "overfitting" → "quá khớp"
20. **Line 192**: "Early Stopping" → "Dừng Sớm"
21. **Line 192**: "gradient accumulation" → "tích lũy gradient"
22. **Line 192**: "batch size" → keep as "batch size"

## Verification Steps

1. **Citation keys**: Verify loshchilov2017decoupled, smith2019super, howard2018universal exist in references.bib
2. **Terminology**: Check all Vietnamese terms against vietnamese-terms.md
3. **Consistency**: Ensure all instances of the same English term are translated consistently
4. **Forbidden terms**: Verify that batch, dropout, backbone, attention, pooling remain in English