# Plan: Chapter 1 — Rewrite (based on phabert_cnn paper)

## Goal
Rewrite Chapter 1 as flowing prose, fewer subsections, no bullet lists.
Match the writing style of Chapters 3–5: dense paragraphs, minimal sub-headings.
Source: paper Introduction + Related Work sections.

## Structure

### Chapter intro sentence
One sentence: Chapter 1 presents background, problem, objectives, contributions, scope, and organization.

### Section 1.1 — Bối cảnh nghiên cứu
**Para 1:** Phage biology — what phages are, abundance ($10^{31}$), ecological roles (regulating bacteria, HGT).
**Para 2:** Two lifestyle categories — virulent (lytic cycle) vs temperate (lysogenic cycle, prophage, induction).
**Para 3:** Importance of lifestyle classification — microbiome research, phage therapy (only virulent suitable), lysogenic conversion risk.
**Para 4:** Limitations of experimental methods → need for computational approaches. Metagenomics context: contigs from NGS, length variation, fragmentation challenge.

### Section 1.2 — Vấn đề nghiên cứu
**Para 1:** Four challenges (prose, not bullets): data limitations, no universal marker gene, short fragments, sequence similarity with host.
**Para 2:** Formal problem statement (binary classification equation).
**Para 3:** Limitations of existing methods — ML methods (PHACTS, PhageAI, BACPHLIP) fail on contigs; DeePhage lacks pre-trained knowledge; PhaTYP depends on Prodigal (fails on short contigs); DeepPL/ProkBERT have k-mer information leakage.

### Section 1.3 — Mục tiêu và đóng góp
**Para 1:** Main objective: develop PhaBERT-CNN — hybrid DNABERT-2 + multi-scale CNN + attention pooling.
**Para 2:** Key contributions (prose): (1) architecture, (2) two-phase training, (3) comprehensive evaluation on 4 length groups, (4) analysis of advantages/limitations.

### Section 1.4 — Phạm vi nghiên cứu
One paragraph: binary classification, 4 contig length groups (100–1800 bp), dataset from DeePhage+DeepPL (2,241 genomes), DNABERT-2 as backbone, 5-fold CV, metrics sn/sp/acc.

### Section 1.5 — Bố cục luận văn
One paragraph describing the 5 chapters briefly.

## Citation list
| Key | Reason |
|-----|--------|
| suttle2007marine | Phage abundance $10^{31}$ |
| koskella2014bacteria | Phage ecological roles, HGT |
| wu2021deephage | Virulent/temperate definition; DeePhage method |
| mcnair2012phacts | Lytic cycle description; PHACTS method |
| howard2017lysogeny | Lysogenic cycle |
| feiner2015new | Prophage induction |
| shang2023phatyp | Importance of classification; PhaTYP |
| gorski2016phage | Phage therapy |
| azimi2019phage | Phage therapy alternative to antibiotics |
| cobian2016viruses | Lysogenic conversion risk |
| hayes2017metagenomic | Data limitations |
| mokili2012metagenomics | No universal marker gene |
| jiang2017ensvmb | Short fragment challenge |
| rozov2017recycler | Sequence similarity with host |
| setubal2021metagenome | Contigs from metagenomics |
| ghurye2016metagenomic | Metagenomic assembly |
| hyatt2010prodigal | Prodigal dependency of PhaTYP |
| trimble2012short | Prodigal fails on short contigs |
| zhou2023dnabert | DNABERT-2 |
| ligeti2024prokbert | ProkBERT k-mer leakage |
| zhang2024deeppl | DeepPL |
| tynecki2020phageai | PhageAI |
| hockenberry2021bacphlip | BACPHLIP |

## Numbers to verify
- Phage abundance: $10^{31}$ — from suttle2007marine ✓
- 2,241 genomes (707 temperate, 1,534 virulent) — from Chapter 3 ✓
- 4 contig groups: 100–400, 400–800, 800–1200, 1200–1800 bp ✓
- PhaBERT-CNN acc: 81.59%–90.01% (Groups A–C) ✓
