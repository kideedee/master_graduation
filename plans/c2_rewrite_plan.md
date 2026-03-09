# Plan: Chapter 2 — Rewrite (prose style, fewer subsections)

## Goal
Rewrite Chapter 2 as flowing prose with fewer subsections, matching Chapter 3 style.
All content consolidated into a single file `co_so_ly_thuyet.tex` (replacing the \input chain).
Related works section must introduce all methods mentioned in Chapter 3.

## Structure

### Chapter intro paragraph
One paragraph: Chapter 2 covers phage biology, metagenomics, deep learning foundations (CNN, Transformer, BERT), DNABERT → DNABERT-2, transfer learning, and related work.

### Section 2.1 — Thực khuẩn thể và phân loại lối sống
**Para 1:** Definition, abundance ($10^{31}$), ecological roles (kill-the-winner, HGT, nutrient cycling).
**Para 2:** Virulent phage — lytic cycle (5 steps: adsorption, injection, biosynthesis, assembly, lysis).
**Para 3:** Temperate phage — lysogenic cycle (integration, prophage state, induction by UV/stress). Decision factors.
**Para 4:** Importance of classification: microbiome research, phage therapy (only virulent suitable), lysogenic conversion risk.

### Section 2.2 — Metagenomics và dữ liệu contig
**Para 1:** Metagenomics definition, NGS platforms (Illumina short reads, PacBio/Nanopore long reads), why it matters for phage research.
**Para 2:** Metagenomic assembly pipeline → contigs. Challenges: uneven coverage, repeats, chimerism.
**Para 3:** Contig characteristics: variable length (100 bp – hundreds of kb), incomplete genes, quality variation. Short contigs (100–1200 bp) are especially challenging.
**Para 4:** Phage research applications: diversity discovery, phage-host interactions, prophage identification. Transition: need for computational tools.

### Section 2.3 — Nền tảng học sâu
**Para 1:** Deep learning vs traditional ML: automatic feature learning, hierarchical representations, end-to-end optimization. Relevance to genomics.
**Para 2:** CNN for sequences — 1D convolution formula, receptive field, pooling (max/adaptive). Multi-scale CNN (Inception-style, kernel sizes 3/5/7). TextCNN (Kim 2014) for sentence classification.
**Para 3:** Transformer architecture — self-attention (Q/K/V formula), multi-head attention, positional encoding. Advantages: parallelization, long-range dependencies.
**Para 4:** BERT — MLM objective (mask 15%, 80/10/10 strategy), bidirectional context, pre-training + fine-tuning paradigm. Application to genomics.
**Para 5:** Attention pooling — self-attentive sentence embedding (Lin 2017), dynamic weighting, interpretability advantage over max/avg pooling.
**Para 6:** AdamW optimizer, binary cross-entropy loss, regularization (dropout, layer norm, early stopping).

### Section 2.4 — DNABERT và DNABERT-2
**Para 1:** DNABERT (Ji 2021) — first BERT for DNA, overlapping k-mer tokenization, pre-trained on human genome. Three limitations: information leakage in MLM, computational inefficiency (token count ≈ sequence length), 512-token max length, single-species training.
**Para 2:** DNABERT-2 (Zhou 2023) — BPE tokenization via SentencePiece (vocab 4096, avg ~5 nt/token, ~5× length reduction, no leakage). Architecture: 12 layers, 768 hidden, 12 heads, ~117M params, GELU, LayerNorm.
**Para 3:** ALiBi positional encoding — formula $\mathbf{B}_{ij} = m \cdot (j-i)$, flexible sequence length, no retrain needed. Multi-species pre-training corpus. Three output types: token-level $\mathbf{H}$, [CLS], pooled.
**Para 4:** Comparison table DNABERT vs DNABERT-2 (keep `tab:dnabert_comparison`).

### Section 2.5 — Học chuyển giao trong sinh tin học
**Para 1:** Transfer learning paradigm: pre-training on large corpus → fine-tuning on target task. Benefits: data efficiency, faster convergence, better generalization.
**Para 2:** Fine-tuning strategies: full fine-tuning, feature extraction (frozen backbone), discriminative fine-tuning (different LRs per layer group). Catastrophic forgetting challenge.
**Para 3:** Two-phase strategy used in PhaBERT-CNN: warm-up (frozen backbone, LR $2\times10^{-3}$, 1 epoch) → full fine-tuning (discriminative LR: $1\times10^{-5}$ for DNABERT-2, $1\times10^{-4}$ for task-specific layers).

### Section 2.6 — Các công trình liên quan
**Para 1:** Traditional ML methods — PHACTS (RF + protein similarity, >90% on complete genomes, degrades on contigs), PhageAI (Word2Vec + SVM, no gene prediction needed but limited on short contigs), BACPHLIP (conserved domains + RF, requires complete domains). Common limitation: designed for complete genomes.
**Para 2:** DeePhage (CNN + one-hot, first DL method, no pre-training, limited receptive field). PhaTYP (BERT + Prodigal gene prediction, SOTA on long contigs, fails on short contigs <200 bp due to Prodigal limitation).
**Para 3:** DeepPL (DNABERT + k-mer, information leakage, 512 bp limit), ProkBERT (LCA tokenization, same k-mer leakage, performance stagnation on longer contigs).
**Para 4:** Comparison table `tab:method_comparison` (keep existing table).
**Para 5:** Positioning of PhaBERT-CNN: addresses all four limitations — no gene prediction dependency, BPE tokenization (no leakage), DNABERT-2 pre-trained knowledge, hybrid CNN+attention architecture.

## Citation list
| Key | Reason |
|-----|--------|
| `suttle2007marine` | Phage abundance $10^{31}$ |
| `koskella2014bacteria` | Kill-the-winner, HGT |
| `gorski2016phage` | Phage therapy |
| `azimi2019phage` | Phage therapy for antibiotic resistance |
| `cobian2016viruses` | Lysogenic conversion risk |
| `howard2017lysogeny` | Lysogenic cycle |
| `feiner2015new` | Prophage induction |
| `mokili2012metagenomics` | Metagenomics definition |
| `setubal2021metagenome` | Contigs from metagenomics |
| `ghurye2016metagenomic` | Metagenomic assembly |
| `hayes2017metagenomic` | Phage diversity via metagenomics |
| `szegedy2015going` | Inception multi-scale CNN |
| `kim2014convolutional` | TextCNN for sentence classification |
| `johnson2017deep` | Deep pyramid CNN |
| `vaswani2017attention` | Transformer architecture |
| `press2021train` | ALiBi positional encoding |
| `devlin2019bert` | BERT |
| `lin2017structured` | Self-attentive sentence embedding |
| `loshchilov2017decoupled` | AdamW optimizer |
| `ji2021dnabert` | DNABERT original |
| `zhou2023dnabert` | DNABERT-2 |
| `sennrich2015neural` | BPE tokenization |
| `kudo2018sentencepiece` | SentencePiece |
| `howard2018universal` | ULMFiT / discriminative fine-tuning |
| `smith2019super` | One-cycle LR schedule |
| `mcnair2012phacts` | PHACTS |
| `tynecki2020phageai` | PhageAI |
| `hockenberry2021bacphlip` | BACPHLIP |
| `wu2021deephage` | DeePhage |
| `shang2023phatyp` | PhaTYP |
| `hyatt2010prodigal` | Prodigal gene prediction |
| `trimble2012short` | Prodigal fails on short contigs |
| `zhang2024deeppl` | DeepPL |
| `ligeti2024prokbert` | ProkBERT |

## Numbers to verify
- Phage abundance: $10^{31}$ — suttle2007marine ✓
- DNABERT-2: 12 layers, 768 hidden, 12 heads, ~117M params — zhou2023dnabert ✓
- BPE vocab: 4,096 tokens — zhou2023dnabert ✓
- Average token length: ~5 nt — zhou2023dnabert ✓
- Sequence length reduction: ~5× — zhou2023dnabert ✓
- BERT masking: 15% tokens, 80/10/10 strategy — devlin2019bert ✓
- PHACTS accuracy >90% on complete genomes — mcnair2012phacts / wu2021deephage ✓
- Prodigal fails on fragments <200 bp — trimble2012short ✓
- Warm-up LR: $2\times10^{-3}$; DNABERT-2 LR: $1\times10^{-5}$; task LR: $1\times10^{-4}$ — chapter_3.tex ✓

## Implementation note
- Consolidate all content into `co_so_ly_thuyet.tex` (remove \input chain)
- Keep `tab:dnabert_comparison` and `tab:method_comparison` tables
- No bullet lists in prose paragraphs (use inline enumeration instead)
- Subsections only at section level (2.1, 2.2, ...) — no sub-subsections
