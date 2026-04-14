---
name: johnson2017deep verification
description: Verification record for Johnson & Zhang 2017 DPCNN paper — what the paper does/does not claim, and both usages in the thesis
type: reference
---

## Paper Identity
- Key: johnson2017deep
- Title: Deep Pyramid Convolutional Neural Networks for Text Categorization
- Authors: Rie Johnson, Tong Zhang
- Venue: ACL 2017, pages 562–570
- URL: https://aclanthology.org/P17-1052/
- Domain: NLP / text categorization (NOT genomics)

## What the paper actually claims
- Core contribution: low-complexity word-level deep CNN architecture for text categorization
- Key quoted claim: "efficiently represent long-range associations in text"
- Pyramid structure purpose: increase network depth without large computational cost (via downsampling blocks)
- The paper does NOT claim: "longer sequences benefit more from multi-scale convolutions"
- The paper does NOT mention: local pattern extraction at multiple spatial scales as a function of sequence length
- The paper does NOT address: phage genomes, DNA motifs, or biological sequences

## Thesis usages

### Usage 1 — chapter_4.tex line 59 (MISMATCH)
Claim: "when sequences are longer, characteristic functional motifs of phage genomes become more complete
and richer, allowing convolutional filters at multiple spatial scales to more effectively exploit local patterns"
Verdict: MISMATCH — paper makes no such claim about longer sequences benefiting multi-scale filters.
The trend (longer contig → higher PhaBERT-CNN gain) is an empirical finding from the thesis's own experiments,
not something supported by the DPCNN paper.
Fix: Remove `\cite{johnson2017deep}` from this sentence. The observation is self-reported experimental
evidence — cite `document/phabert_cnn.tex` (own work) or use no citation.

### Usage 2 — chapter_3.tex line 120 (PARTIAL MATCH — closer but still imprecise)
Claim: "adding a second stacked Conv1d layer per sub-branch to enhance hierarchical feature extraction
[cite johnson2017deep]"
Verdict: Closer — DPCNN does use stacked conv blocks (pooling-conv-conv repeated blocks) to build depth.
The idea of stacking convolutional layers for richer feature extraction IS present in the paper.
However, DPCNN's stacking is motivated by depth/global context, not "hierarchical local feature extraction."
This usage is a reasonable (if imprecise) analogical citation; not a clear factual mismatch.

### Usage 3 — chapter_2.tex line 81 (MISMATCH)
Claim: "Using multiple filters with different kernel sizes allows simultaneous multi-scale feature extraction,
from short patterns of a few nucleotides to long patterns of tens of nucleotides [cite johnson2017deep]"
Verdict: MISMATCH — DPCNN uses a single kernel size per layer; it does NOT use parallel multi-kernel branches.
Multi-kernel parallel CNN is the TextCNN design (kim2014convolutional), not DPCNN.
Fix: Replace `\cite{johnson2017deep}` with `\cite{kim2014convolutional}` here.
