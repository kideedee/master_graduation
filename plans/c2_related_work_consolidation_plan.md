# Plan: Consolidation of Sections 2.4.1, 2.4.2, 2.4.3

## Task
Merge sections 2.4.1 (tokenization methods), 2.4.2 (traditional ML methods), and 2.4.3 (deep learning methods) into a single cohesive section that presents each method comprehensively (algorithm, data, tokenization, etc.) rather than fragmenting information across subsections.

## Outline

### I. Introduction paragraph
Brief overview of computational approaches for phage lifestyle classification, organized by methodology evolution (traditional ML → deep learning → foundation models)

### II. Traditional Machine Learning Methods (PHACTS, PhageAI, BACPHLIP)

#### 1. PHACTS
- Algorithm: Random Forest
- Data source: Complete phage genomes
- Tokenization/encoding: Protein similarity vectors via FASTA35
- Performance: High on complete genomes (~90%), poor on contigs (~50%)
- Limitations: Requires complete protein-coding regions

#### 2. PhageAI
- Algorithm: Support Vector Machine (SVM) with RFECV
- Data source: Complete phage genomes
- Tokenization: k-mer → Word2Vec embeddings
- Performance: High on complete genomes
- Limitations: Insufficient context signal on short contigs

#### 3. BACPHLIP
- Algorithm: Random Forest
- Data source: Complete phage genomes
- Tokenization/encoding: Binary feature vectors of conserved protein domains (via HMMER3)
- Performance: Competitive on complete genomes
- Limitations: Returns errors on fragmented contigs; limited conserved protein data

### III. Deep Learning Methods (DeePhage, PhaTYP, DeepPL, ProkBERT)

#### 1. DeePhage
- Algorithm: Convolutional Neural Network (CNN)
- Data source: Metagenomic contigs (100-1800 bp, 4 groups A-D)
- Tokenization: One-hot encoding (direct DNA sequence)
- Pre-training: No (trained from scratch)
- Performance: 89% accuracy on contigs; 30% improvement over PHACTS; 810× faster
- Limitations: No pre-trained knowledge; sparse representation

#### 2. PhaTYP
- Algorithm: BERT (Transformer encoder)
- Data source: Complete genomes and contigs
- Tokenization: Protein clusters (requires Prodigal for ORF prediction)
- Pre-training: Yes (self-supervised on protein sequences)
- Performance: Strong on long contigs (Group D: 91.02% accuracy)
- Limitations: Depends on gene prediction; Prodigal fails on <200 bp fragments

#### 3. DeepPL
- Algorithm: DNABERT (BERT with k-mer tokenization)
- Data source: Contigs
- Tokenization: Overlapping k-mer (k=6)
- Pre-training: Yes (DNABERT on human genome)
- Performance: Not evaluated on full benchmark
- Limitations: 512-token limit (~500 bp); information leakage from overlapping k-mers; excluded from comparison

#### 4. ProkBERT
- Algorithm: BERT with Local Context-Aware (LCA) tokenization
- Data source: Microbial genomes
- Tokenization: LCA k-mer (adjustable stride overlapping k-mer)
- Pre-training: Yes (multi-species microbial genomes)
- Performance: Moderate (80.68%-85.35% accuracy); stagnates on longer contigs
- Limitations: Information leakage from overlapping k-mers; performance plateau

### IV. Foundation Models for Genomics (DNABERT, DNABERT-2)

#### 1. DNABERT
- Algorithm: BERT (Transformer encoder)
- Data source: Human genome
- Tokenization: Overlapping k-mer (typically k=6)
- Pre-training: Yes (masked language modeling on human genome)
- Limitations: Information leakage; computational inefficiency (~L tokens); 512-token hard limit

#### 2. DNABERT-2
- Algorithm: BERT with architectural improvements
- Data source: Multi-species genome corpus
- Tokenization: Byte Pair Encoding (BPE) via SentencePiece (4,096 vocab, ~5× compression)
- Pre-training: Yes (masked language modeling, avg 700 bp sequences)
- Architectural innovations:
  - BPE tokenization: eliminates information leakage, 5× sequence compression, span prediction
  - ALiBi positional encoding: arbitrary sequence length support
  - Flash Attention: 3× efficiency, 1/3 FLOPs
- Performance: Comparable to 2.5B-parameter Nucleotide Transformer with 21× fewer parameters, 92× less GPU time
- Advantages: No gene prediction dependency, no length limit, no information leakage

### V. Comprehensive Comparison Table
Replace the tokenization-only table with a comprehensive table including:
- Method name
- Data source (complete genomes / contigs / metagenomics)
- Tokenization method
- Algorithm/model architecture
- Pre-training (Yes/No)
- Performance on short contigs (Strong/Moderate/Weak)
- Key limitations

### VI. Research Gap and Motivation
Synthesize four key gaps:
1. Gene prediction dependency (PhaTYP)
2. Information leakage from overlapping k-mers (DNABERT, DeepPL, ProkBERT)
3. Sequence length limits (DeepPL)
4. Lack of pre-trained knowledge (DeePhage)

PhaBERT-CNN addresses all four gaps by combining DNABERT-2 (BPE + ALiBi + pre-training) with multi-scale CNN architecture.

## Paragraph Descriptions

1. **Introduction**: Overview of computational phage classification evolution from traditional ML to deep learning to foundation models
2. **PHACTS**: Random Forest on protein similarity vectors; high accuracy on complete genomes but fails on contigs due to incomplete protein regions
3. **PhageAI**: SVM with Word2Vec k-mer embeddings; applies NLP techniques to genomics but limited by insufficient context on short contigs
4. **BACPHLIP**: Random Forest on conserved protein domain features; competitive on complete genomes but returns errors on fragmented contigs
5. **DeePhage**: First deep learning method for metagenomic contigs; CNN with one-hot encoding; no gene prediction dependency; 89% accuracy but trained from scratch without pre-trained knowledge
6. **PhaTYP**: First BERT application to phage classification; protein-level tokenization; strong on long contigs but depends on Prodigal gene prediction which fails on short fragments
7. **DeepPL**: DNABERT-based approach; operates on DNA sequences but inherits DNABERT limitations (overlapping k-mer, 512-token limit); excluded from benchmark
8. **ProkBERT**: BERT with LCA tokenization; moderate performance with stagnation on longer contigs; still suffers from information leakage
9. **DNABERT**: First genomic BERT; overlapping k-mer tokenization causes information leakage, computational inefficiency, and length limits
10. **DNABERT-2**: Next-generation genomic foundation model; BPE tokenization eliminates leakage; ALiBi enables arbitrary length; Flash Attention improves efficiency; multi-species pre-training
11. **Comparison table**: Comprehensive comparison of all methods across data source, tokenization, algorithm, pre-training, and performance dimensions
12. **Research gap**: Synthesize four key limitations of existing methods and explain how PhaBERT-CNN addresses them

## Citation List

All citations from existing sections:
- mcnair2012phacts: PHACTS method
- tynecki2020phageai: PhageAI method
- hockenberry2021bacphlip: BACPHLIP method
- wu2021deephage: DeePhage method, benchmark dataset
- shang2023phatyp: PhaTYP method
- zhang2024deeppl: DeepPL method
- ligeti2024prokbert: ProkBERT method
- ji2021dnabert: DNABERT method
- zhou2023dnabert: DNABERT-2 method
- hyatt2010prodigal: Prodigal gene prediction tool
- trimble2012short: Gene prediction performance on short fragments
- sennrich2015neural: BPE tokenization
- kudo2018sentencepiece: SentencePiece framework
- press2021train: ALiBi positional encoding
- dao2022flashattention: Flash Attention
- raffel2020exploring: Span prediction effectiveness
- dalla2025nucleotide: Nucleotide Transformer comparison
- kim2014convolutional: TextCNN
- szegedy2015going: Inception architecture

## Numbers to Verify

From PHACTS:
- ~90% accuracy on complete genomes
- ~50% accuracy on contigs (100-1800 bp)

From PhageAI:
- (No specific numbers in current text)

From BACPHLIP:
- (No specific numbers in current text)

From DeePhage:
- 89% accuracy (cross-validation)
- 30% improvement over PHACTS
- 10% improvement over PhagePred
- 810× faster than PHACTS

From PhaTYP:
- Group D: 92.29% sensitivity, 89.75% specificity, 91.02% accuracy
- Prodigal fails on <200 bp

From DeepPL:
- 512-token limit
- ~500 bp with k=6

From ProkBERT:
- 80.68%-85.35% accuracy range
- Peak at 85.35% in Group B

From DNABERT:
- k=6 typical
- 512-token limit

From DNABERT-2:
- 4,096 vocabulary size
- ~5× sequence compression
- ~700 bp average pre-training sequence length
- 21× fewer parameters than Nucleotide Transformer
- 92× less GPU time than Nucleotide Transformer
- 3× efficiency improvement over DNABERT
- 1/3 FLOPs compared to DNABERT
- 30% more parameters than DNABERT
- 23/28 datasets outperform DNABERT on GUE benchmark
