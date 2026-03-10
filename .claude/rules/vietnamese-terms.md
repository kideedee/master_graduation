# Vietnamese Terminology

This file contains Vietnamese ↔ English technical terminology mapping for the thesis.

## Language Notes

- The thesis uses UTF-8 encoding with Vietnamese language support
- Chapter titles, figure/table captions, and algorithm names are in Vietnamese
- Maintain consistent Vietnamese terminology throughout

## Key Technical Terms

| Vietnamese | English |
|---|---|
| Thực khuẩn / Phage | Bacteriophage |
| Phân loại | Classification |
| Học sâu | Deep Learning |
| Mô hình | Model |
| Huấn luyện | Training |
| Tiền huấn luyện | Pre-training |
| Tinh chỉnh | Fine-tuning |
| Học chuyển giao | Transfer Learning |
| Đánh giá | Evaluation |
| Độ chính xác | Accuracy |
| Hệ gen | Genome |
| Chuỗi DNA | DNA Sequence |
| Kiến trúc | Architecture |
| Thực nghiệm | Experiment |
| Kết quả | Result |
| Phương pháp | Method |
| Dữ liệu | Data |
| Tập dữ liệu | Dataset |
| Contig | Contig (DNA fragment) |
| Metagenomic | Metagenomic |
| Rò rỉ thông tin | Information leakage |
| Mã hóa cặp byte (BPE) | Byte Pair Encoding |
| Embedding ngữ cảnh | Contextualized embeddings |
| Nhánh song song kép | Dual parallel branches |
| Đa tỷ lệ | Multi-scale |
| Mạng nơ-ron tích chập | Convolutional Neural Network (CNN) |
| Cơ chế chú ý | Attention mechanism |
| Lối sống | Lifestyle (temperate/virulent) |
| Chuỗi DNA thô | Raw DNA sequence |
| Đầu phân loại | Classification head |
| Kích thước ẩn | Hidden size |
| Trọng số | Weight |
| Lớp tuyến tính | Linear layer |
| Kích thước cửa sổ tích chập | Kernel |

## Usage Guidelines

- Write the entire thesis in Vietnamese (see CLAUDE.md rule #6)
- Keep English only for: technical terms with no Vietnamese equivalent, model/algorithm names, citations, math notation, code
- When introducing a new technical term, provide both Vietnamese and English: "thực khuẩn (bacteriophage)"
- In figure/table captions, use Vietnamese
- In code comments within LaTeX listings, use English

## Forbidden Substitutions (Keep in English)

The following terms **must stay in English** — do not translate or substitute. When checking terminology (Step 3), do not flag these as errors:

| Keep as-is (English) | Reason |
|---|---|
| embedding | No standard Vietnamese equivalent |
| fine-tuning | Specific technical name |
| pre-training | Specific technical name |
| attention | In context of "attention mechanism" / "attention pooling" |
| tokenization | Specific technical name |
| token | Specific technical unit |
| batch | In context of "batch size", "mini-batch" |
| dropout | Specific technical name |
| pooling | In context of "max pooling", "attention pooling" |
| backbone | In context of model architecture |
| benchmark | Specific technical name |
| pipeline | In context of processing workflow |
| BPE | Byte Pair Encoding — technical abbreviation |
| ALiBi | Specific technical name |
| k-mer | Bioinformatics term |
| contig | Bioinformatics term |
| metagenomic | Bioinformatics term |
| DNABERT-2, PhaBERT-CNN, BERT, CNN, SVM, Random Forest | Model/algorithm names |

