# Writing Plan: Section 4.4.4 - Ý nghĩa thực tiễn của cải thiện hiệu suất

## Metadata
- **Target file**: `chapters/c4/chapter_4.tex`
- **Position**: After Section 4.4.3 "So sánh chiến lược biểu diễn chuỗi" (line ~133)
- **Target length**: 350-500 từ (~0.7-1 trang LaTeX)
- **Created**: 2026-04-15

## Purpose
Giải thích tại sao sự cải thiện 1-5% về độ chính xác có ý nghĩa quan trọng trong bài toán phân loại lối sống thực khuẩn thể, đặc biệt trong bối cảnh liệu pháp phage và quy mô dữ liệu metagenomic.

## Structure

### 4.4.4. Ý nghĩa thực tiễn của cải thiện hiệu suất
**Label**: `\subsection{Ý nghĩa thực tiễn của cải thiện hiệu suất}` + `\label{sec:practical_significance}`

#### Paragraph 1: Bối cảnh an toàn lâm sàng (~150-200 từ)
- Liệu pháp phage yêu cầu phage "strictly lytic" (FDA/EMA guidelines)
- Rủi ro của phân loại sai phage ôn hòa → độc lực:
  - Lysogenic conversion: phage ôn hòa tích hợp vào hệ gen vi khuẩn
  - Chuyển gen độc lực đã được ghi nhận: độc tố tả, độc tố Shiga, độc tố bạch hầu
  - Kháng kháng sinh lan truyền qua HGT
- Rủi ro ngược: phage độc lực bị phân loại sai → mất ứng viên điều trị
- **Citations**: `\cite{brussow2004phages}`, `\cite{feiner2015new}`, `\cite{azimi2019phage}`

#### Paragraph 2: Tác động ở quy mô metagenomic (~100-150 từ)
- Quy mô cơ sở dữ liệu hiện tại: IMG/VR >15 triệu genome virus
- Tính toán cụ thể: cải thiện 1% trên 1 triệu contig = 10,000 lỗi giảm
- Ở quy mô IMG/VR: 1% = ~150,000 phân loại sai được khắc phục
- Liên hệ với kết quả PhaBERT-CNN: cải thiện 0.32-6.61% → hàng chục nghìn contig được phân loại đúng hơn
- **Citations**: Không cần citation mới (tính toán logic)

#### Paragraph 3: So sánh với lĩnh vực an toàn quan trọng khác (~100-150 từ)
- Chẩn đoán y tế AI: 1% cải thiện được coi là có ý nghĩa lâm sàng
- Dự đoán đích thuốc: 1-3% AUROC được công bố như cải tiến đáng kể
- Phage lifestyle prediction đáp ứng tiêu chí an toàn tương tự:
  - Ảnh hưởng trực tiếp đến an toàn bệnh nhân
  - Quy mô dữ liệu lớn khuếch đại tác động
- Kết luận: cải thiện của PhaBERT-CNN có ý nghĩa thực tiễn rõ ràng
- **Citations**: Không cần citation mới (so sánh định tính)

## Citations to use (verified in references.bib)
| Key | Purpose |
|-----|---------|
| `brussow2004phages` | Lysogenic conversion, evolution of bacterial pathogens |
| `feiner2015new` | Prophages as regulatory switches, virulence gene transfer |
| `azimi2019phage` | Phage therapy requirements, safety considerations |
| `howard2017lysogeny` | (backup) Lysogeny mechanisms in nature |

## Vietnamese terminology (from vietnamese-terms.md)
| Vietnamese | English |
|------------|---------|
| Liệu pháp phage | Phage therapy |
| Biến đổi tiềm tan | Lysogenic conversion |
| Chuyển gen ngang | Horizontal gene transfer |
| Gen đánh dấu | Marker gene |
| Thực khuẩn thể ôn hòa | Temperate phage |
| Thực khuẩn thể độc lực | Virulent phage |

## Style notes
- Maintain formal Vietnamese academic tone consistent with existing Chapter 4
- Use `\textit{}` for English technical terms on first use
- Keep sentences concise, avoid repetition
- Connect logically to preceding sections (4.4.1-4.4.3)

## Validation checklist
- [ ] All `\cite{}` keys exist in references.bib
- [ ] Vietnamese terminology consistent with vietnamese-terms.md
- [ ] LaTeX compiles without errors
- [ ] Section fits naturally after 4.4.3 and before 4.5 (Kết luận)
