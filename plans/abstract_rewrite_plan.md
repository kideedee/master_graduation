# Plan: Abstract Rewrite — Vietnamese and English

## Metadata

| Field | Value |
|---|---|
| Target files | `chapters/abtract_vi.tex`, `chapters/abtract_en.tex` |
| Position in document | Before Chapter 1, after title page |
| Target length | 250–300 words per abstract (VNU guideline: max 350) |
| Structure | IMRaD: Problem → Method → Results → Conclusion |
| Language | Vietnamese (abtract_vi.tex), English (abtract_en.tex) |

---

## Purpose

Rewrite both abstracts to accurately reflect the final PhaBERT-CNN model as described in
Chapters 3–5. The current abstracts contain four factual errors that must be corrected:

1. Accuracy numbers are from PhaBERT-CNN-AP (81.59%, 87.91%, 90.01%, 90.69%), not the
   final PhaBERT-CNN model (82.26%, 87.38%, 90.01%, 91.34%).
2. The architecture is described as using "attention pooling" — the final model uses masked
   mean pooling. Attention pooling is the discarded ablation variant (PhaBERT-CNN-AP).
3. Improvement over state-of-the-art is stated as 0.91–5.98%, but the correct range is
   0.32–6.61% (vs. best competitor per group across all four groups).
4. Sensitivity/specificity ranges cite PhaBERT-CNN-AP values, not PhaBERT-CNN values.

---

## Structure and Paragraph Descriptions

### Paragraph 1 — Problem (≈ 70 words)

**What it argues:** Establish why phage lifestyle classification matters for phage therapy,
why it is technically difficult, and what gap existing computational tools leave.

Key content to include:
- Phage therapy context: thực khuẩn thể (bacteriophage) as antibiotic alternative
- Safety constraint: only virulent phages (thực khuẩn thể độc lực) are safe; temperate
  phages (thực khuẩn thể ôn hòa) risk biến đổi tiềm tan (lysogenic conversion) and
  horizontal gene transfer of virulence genes
- Traditional methods: require lab cultivation, cannot scale to unculturable phages
- Computational tools (PhaTYP, DeePhage) limitation: depend on gene prediction tools
  (Prodigal), which fail on short contigs from metagenomic data; k-mer methods suffer
  from rò rỉ thông tin (information leakage)

### Paragraph 2 — Method (≈ 80 words)

**What it argues:** Describe PhaBERT-CNN's architecture and training strategy, correctly
naming the MKC module and masked mean pooling.

Key content to include:
- Proposal: PhaBERT-CNN, kiến trúc học sâu lai (hybrid deep learning architecture)
  combining DNABERT-2 (mô hình nền tảng hệ gen — genome foundation model) with MKC
  module (Multi-Kernel Convolutional)
- MKC module details: nhánh song song kép (dual parallel branches) — CNN branch with
  kernel sizes 3, 5, 7 for đặc trưng đa tỷ lệ (multi-scale features) + masked mean
  pooling branch for global representation
- Tokenization: BPE (mã hóa cặp byte) — no gene prediction dependency, operates
  directly on chuỗi DNA thô (raw DNA sequence)
- Training: chiến lược hai giai đoạn với tốc độ học phân biệt (two-stage training with
  discriminative learning rates)
- Dataset: 2,241 complete phage genomes (707 temperate, 1,534 virulent)

### Paragraph 3 — Results (≈ 80 words)

**What it argues:** Report the correct PhaBERT-CNN accuracy numbers, improvement range,
and sensitivity/specificity from the final model (not PhaBERT-CNN-AP).

Key content to include:
- Experimental setup: four contig length groups A–D (100–400 bp, 400–800 bp, 800–1,200
  bp, 1,200–1,800 bp) with 5-fold stratified cross-validation
- PhaBERT-CNN accuracy (CORRECT — from Table tab:main_results):
  82.26%, 87.38%, 90.01%, 91.34% (Groups A–D)
- Improvement over state-of-the-art: 0.32–6.61% vs. PhaTYP, DeePhage, ProkBERT
- Sensitivity range (PhaBERT-CNN, CORRECT): 82.54%–92.31%
- Specificity range (PhaBERT-CNN, CORRECT): 81.30%–87.71%
- MKC module contribution: 0.74–4.09% improvement over DNABERT-2 baseline

### Paragraph 4 — Conclusion (≈ 50 words)

**What it argues:** Synthesize the key takeaway — the hybrid paradigm works, and it has
broader implications for biological sequence analysis.

Key content to include:
- Direct operation on raw DNA without gene prediction dependency
- Effective combination of genome foundation model (mô hình nền tảng hệ gen) with
  task-specific architecture (MKC)
- Promising paradigm for biological sequence analysis tasks, especially metagenomic
  analysis with incomplete/fragmented sequences

---

## Outline

```
I.  Problem
    1. Phage therapy need; safety constraint (virulent only)
    2. Traditional methods insufficient (lab cultivation)
    3. Computational tools limited: gene prediction dependency + k-mer leakage

II. Method
    1. PhaBERT-CNN: DNABERT-2 + MKC module
    2. MKC: dual parallel branches (CNN kernels 3,5,7 + masked mean pooling)
    3. BPE tokenization — no gene prediction needed
    4. Two-stage training, discriminative learning rates
    5. Dataset: 2,241 phage genomes

III. Results
    1. 4 contig groups, 5-fold CV
    2. Accuracy: 82.26%, 87.38%, 90.01%, 91.34%
    3. Improvement: 0.32–6.61% vs. state-of-the-art
    4. Sn: 82.54%–92.31% / Sp: 81.30%–87.71%
    5. MKC contribution: 0.74–4.09% over baseline

IV. Conclusion
    1. Foundation model + task-specific architecture = effective combination
    2. Promising paradigm for biological sequence analysis
```

---

## Citations

No `\cite{}` commands appear in the current abstract files — this is standard practice
for Vietnamese master's thesis abstracts (citations belong in the main chapters).
Do not add citations to either abstract.

---

## Numbers to Verify

All numbers below are sourced from `chapters/c4/chapter_4.tex` (Table `tab:main_results`
and Table `tab:ablation_results`). They are authoritative ground truth — no external
verification needed.

| Number | Source location | Notes |
|---|---|---|
| 82.26% | tab:main_results, PhaBERT-CNN, Group A | Replaces wrong 81.59% |
| 87.38% | tab:main_results, PhaBERT-CNN, Group B | Replaces wrong 87.91% |
| 90.01% | tab:main_results, PhaBERT-CNN, Group C | Unchanged — same for both variants |
| 91.34% | tab:main_results, PhaBERT-CNN, Group D | Replaces wrong 90.69% |
| 0.32–6.61% | c4/chapter_4.tex §So sánh với các phương pháp tiên tiến | Replaces wrong 0.91–5.98% |
| 82.54%–92.31% | tab:main_results, Sn column, PhaBERT-CNN rows A–D | Replaces wrong 82.00%–91.12% |
| 81.30%–87.71% | tab:main_results, Sp column, PhaBERT-CNN rows A–D | Replaces wrong 80.15%–90.95% |
| 0.74–4.09% | tab:ablation_results + c4 ablation text | MKC contribution |
| 2,241 | c4/chapter_4.tex §Thiết lập thực nghiệm | Genome count |
| 707 temperate, 1,534 virulent | c4/chapter_4.tex §Thiết lập thực nghiệm | Dataset breakdown |

---

## Vietnamese Terminology

| English term | Vietnamese term (from vietnamese-terms.md) |
|---|---|
| Bacteriophage | Thực khuẩn thể (bacteriophage) — introduce both on first use |
| Phage therapy | Liệu pháp phage |
| Virulent phage | Thực khuẩn thể độc lực |
| Temperate phage | Thực khuẩn thể ôn hòa |
| Lysogenic conversion | Biến đổi tiềm tan |
| Deep learning | Học sâu |
| Genome foundation model | Mô hình nền tảng hệ gen |
| Hybrid architecture | Kiến trúc học sâu lai |
| Multi-scale features | Đặc trưng đa tỷ lệ |
| Dual parallel branches | Nhánh song song kép |
| Raw DNA sequence | Chuỗi DNA thô |
| Information leakage | Rò rỉ thông tin |
| Byte Pair Encoding | Mã hóa cặp byte (BPE) |
| Discriminative learning rate | Tốc độ học phân biệt |
| Accuracy | Độ chính xác |
| Dataset | Tập dữ liệu |
| Classification | Phân loại |
| Lifestyle (virulent/temperate) | Lối sống |
| Metagenomic | Metagenomic (keep in English per rules) |
| MKC module | MKC (keep in English per rules — specific module name) |
| DNABERT-2, PhaBERT-CNN | Keep in English — model names |
| BPE | Keep as BPE — technical abbreviation |
| contig | Keep as contig — bioinformatics term |
| kernel | Describe in context; "kernel sizes 3, 5, 7" stays in English |
| pooling | Keep as "masked mean pooling" — pooling stays in English per rules |
| cross-validation | Keep as cross-validation (alongside "kiểm định chéo") |
| baseline | Keep as baseline per rules |

---

## What NOT to include in the abstract

- No `\cite{}` commands — standard for thesis abstracts
- No equations or math notation — abstract must be plain prose
- No figure/table references
- No descriptions of related work comparisons beyond naming the methods
- No discussion of limitations (belongs in Chapter 5)
- Do not mention PhaBERT-CNN-AP — the abstract describes only the final model

---

## Figures/Tables Needed

None — abstracts contain no figures or tables.

---

## Validation Checklist

Before finalizing, verify each item:

- [ ] Accuracy numbers: 82.26%, 87.38%, 90.01%, 91.34% (NOT 81.59%, 87.91%, 90.01%, 90.69%)
- [ ] Architecture: "masked mean pooling" — NOT "attention pooling"
- [ ] Module name: "MKC" (Multi-Kernel Convolutional) — NOT "attention pooling mechanism"
- [ ] Improvement range: "0.32–6.61%" — NOT "0.91–5.98%"
- [ ] Sensitivity range: "82.54%–92.31%" — NOT "82.00%–91.12%"
- [ ] Specificity range: "81.30%–87.71%" — NOT "80.15%–90.95%"
- [ ] MKC improvement over DNABERT-2: "0.74–4.09%"
- [ ] Dataset size mentioned: 2,241 phage genomes
- [ ] No citations in abstract
- [ ] Vietnamese abstract: all technical terms match vietnamese-terms.md
- [ ] English abstract: terminology consistent with Vietnamese abstract
- [ ] Word count: 250–300 words each
- [ ] Keywords section preserved in both files (7 keywords each)
- [ ] LaTeX structure preserved: \begin{center}, \addcontentsline, \begin{small} blocks

---

## Current Abstract Problems (Summary for Writer Reference)

| Location in current text | Wrong value | Correct value | Source |
|---|---|---|---|
| Paragraph 3, accuracy list | 81.59%, 87.91%, 90.01%, 90.69% | 82.26%, 87.38%, 90.01%, 91.34% | tab:main_results |
| Paragraph 2, architecture | "attention pooling mechanism" | "masked mean pooling" (MKC module) | Chapter 3 + ablation |
| Paragraph 3, improvement | 0.91–5.98% | 0.32–6.61% | c4 §comparison section |
| Paragraph 3, sensitivity | 82.00%–91.12% | 82.54%–92.31% | tab:main_results |
| Paragraph 3, specificity | 80.15%–90.95% | 81.30%–87.71% | tab:main_results |
| Paragraph 2, module name | not named | MKC (Multi-Kernel Convolutional) | Chapter 3 |
