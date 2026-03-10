# Plan: Tokenization Methods in Related Works (Chapter 2)

## Context
Adding a new subsection to Chapter 2, Section 2.6 (Các công trình liên quan) about tokenization methods used in related works for phage genome analysis.

## Placement
Insert as subsection 2.6.3 "Các phương pháp phân tách token trong phân tích hệ gen" after subsection 2.6.2 (Các phương pháp học sâu) and before subsection 2.6.4 (Tổng hợp và khoảng trống nghiên cứu).

## Outline

### I. Introduction paragraph
- Explain the importance of tokenization in genomic sequence analysis
- State that different tokenization methods affect model performance and efficiency
- Preview the four main tokenization approaches discussed

### II. One-hot encoding (Mã hóa one-hot)
1. Definition and mechanism
2. Used by DeePhage
3. Advantages: simple, no information loss, direct representation
4. Disadvantages: high dimensionality, no semantic information, sparse representation

### III. Overlapping k-mer tokenization (Phân tách k-mer có chồng lấn)
1. Definition and mechanism (with example)
2. Used by DNABERT, DeepPL, ProkBERT (LCA variant)
3. Advantages: captures local context, fixed vocabulary size
4. Disadvantages: information leakage, computational inefficiency, redundancy

### IV. Word2Vec on k-mer (Word2Vec trên k-mer)
1. Definition and mechanism
2. Used by PhageAI
3. Advantages: captures semantic relationships between k-mers, dense embeddings
4. Disadvantages: requires separate training, still uses k-mer with fixed k

### V. Byte Pair Encoding (BPE) (Mã hóa cặp byte)
1. Definition and mechanism
2. Used by DNABERT-2, PhaBERT-CNN
3. Advantages: no information leakage, variable-length tokens, efficient compression, span prediction
4. Comparison with overlapping k-mer

### VI. Comparison table
- Table comparing all four methods across key dimensions:
  - Information leakage
  - Sequence length reduction
  - Vocabulary size
  - Semantic information
  - Computational efficiency
  - Representative tools

### VII. Conclusion paragraph
- Summarize the evolution from simple (one-hot) to sophisticated (BPE) tokenization
- Emphasize why BPE is chosen for PhaBERT-CNN
- Transition to next subsection (research gap)

## Citations to Use

### Existing citations in references.bib:
- `ji2021dnabert` - DNABERT (overlapping k-mer)
- `zhou2023dnabert` - DNABERT-2 (BPE, information leakage discussion)
- `wu2021deephage` - DeePhage (one-hot encoding)
- `tynecki2020phageai` - PhageAI (Word2Vec on k-mer)
- `ligeti2024prokbert` - ProkBERT (LCA k-mer)
- `sennrich2015neural` - BPE original paper
- `kudo2018sentencepiece` - SentencePiece framework
- `zhang2024deeppl` - DeepPL (DNABERT k-mer)

### Need to verify:
- Check if DeePhage paper explicitly mentions one-hot encoding
- Verify PhageAI's exact Word2Vec approach
- Confirm ProkBERT's LCA tokenization details

## Numbers to Verify

From zhou2023dnabert (DNABERT-2 paper):
- DNABERT-2 vocabulary size: 4,096 tokens
- Average token length: ~5 nucleotides
- Sequence length reduction: ~5× compared to DNABERT
- DNABERT k value: typically k=6
- DNABERT max sequence length: 512 tokens

From ji2021dnabert (DNABERT paper):
- k-mer values used: k=3, 4, 5, 6
- Overlapping pattern: adjacent tokens share k-1 nucleotides

From wu2021deephage (DeePhage paper):
- Verify if one-hot encoding is explicitly mentioned
- Input representation dimensions

From tynecki2020phageai (PhageAI paper):
- k-mer size used for Word2Vec
- Word2Vec embedding dimensions

## Terminology Mapping

| Vietnamese | English |
|---|---|
| Phân tách token | Tokenization |
| Mã hóa one-hot | One-hot encoding |
| k-mer có chồng lấn | Overlapping k-mer |
| Mã hóa cặp byte | Byte Pair Encoding (BPE) |
| Rò rỉ thông tin | Information leakage |
| Từ điển | Vocabulary |
| Biểu diễn thưa | Sparse representation |
| Biểu diễn dày đặc | Dense representation |
| Ngữ nghĩa | Semantic |
| Hiệu quả tính toán | Computational efficiency |
| Độ dài token thay đổi | Variable-length tokens |
| Nén chuỗi | Sequence compression |
| Dự đoán đoạn | Span prediction |

## Key Technical Terms to Keep in English
- BPE (Byte Pair Encoding)
- one-hot
- k-mer
- Word2Vec
- token
- tokenization (when used as technical term)
- embedding
- SentencePiece
