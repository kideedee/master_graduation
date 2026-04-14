---
name: writing-style-guide
description: >
  Academic writing style guidelines for Vietnamese master's thesis.
  Injected into thesis-planner and thesis-writer agents as reference knowledge.
  NOT user-invocable — this is a knowledge skill, not a workflow.
user-invocable: false
disable-model-invocation: true
---

# Hướng dẫn văn phong luận văn thạc sĩ

## 1. Tham chiếu chéo (Cross-references)

**KHÔNG làm:**
- `(xem Mục~\ref{subsec:X} để biết thêm chi tiết)` — máy móc, làm gián đoạn mạch đọc
- `Chi tiết được trình bày tại Mục~\ref{sec:Y}.` — câu không mang thông tin

**NÊN làm:**
- Lồng cross-reference vào nội dung tự nhiên: `Như đã phân tích tại Mục~\ref{subsec:comparison_gaps}, các phương pháp hiện có...`
- Chỉ dùng `\ref{}` khi tham chiếu phục vụ mạch lập luận, không phải ghi chú phụ
- Trong phần **Bố cục luận văn**: tham chiếu `\ref{}` là hợp lý vì đó là roadmap
- Trong phần nội dung: ưu tiên viết đủ ý tại chỗ, chỉ cross-ref khi cần tham chiếu số liệu/bảng/hình cụ thể ở chương khác

**Nguyên tắc:** Cross-reference phải trả lời câu hỏi "đọc Mục X để hiểu gì?", không phải "xem Mục X cho đầy đủ".

## 2. Cấu trúc và chuyển tiếp giữa các mục

**Mỗi section phải nối logic với section tiếp theo:**
- Cuối "Đặt vấn đề" → dẫn vào "Thách thức": tóm tắt nhu cầu → chỉ ra khó khăn
- Cuối "Thách thức" → dẫn vào "Mục tiêu": thách thức → cách giải quyết
- Cuối "Mục tiêu" → dẫn vào "Đóng góp": mục tiêu → kết quả đạt được
- Cuối "Đóng góp" → dẫn vào "Phạm vi": kết quả → giới hạn áp dụng
- Cuối "Phạm vi" → dẫn vào "Bố cục": scope → cách trình bày

**KHÔNG để section bắt đầu đột ngột** mà không có câu nối từ section trước.

## 3. Phần Đóng góp (Contributions)

**NÊN làm:**
- Liệt kê 3-4 đóng góp cụ thể, mỗi mục bắt đầu bằng **bold** chủ đề
- Mỗi đóng góp chỉ cần 1 con số tiêu đề (headline number): "đạt 82,26--91,34%"
- Nêu tính mới (novelty) rõ ràng: PhaBERT-CNN khác gì phương pháp hiện có

**KHÔNG làm:**
- Không đưa bảng kết quả đầy đủ vào Introduction — để Chương 4
- Không dùng cross-reference máy móc: `(chi tiết tại Chương~\ref{chap:X})`
- Không lặp lại toàn bộ số liệu — chỉ con số ấn tượng nhất

## 4. Phần Phạm vi và Hạn chế (Scope & Limitations)

**NÊN làm:**
- Viết bằng prose liền mạch (1-2 đoạn), giọng tự tin phân tích
- Nêu phạm vi trước (in-scope), sau đó giải thích cái loại trừ và lý do
- Dùng cấu trúc: "Luận văn tập trung vào X vì Y" thay vì "Luận văn không xem xét Z"

**KHÔNG làm:**
- Không liệt kê kiểu "Thứ nhất... Thứ hai... Thứ ba... Thứ tư..." — giọng phòng thủ
- Không liệt kê quá nhiều hạn chế ở Introduction — hạn chế chi tiết để Chương 5
- Không viết giọng xin lỗi: "luận văn còn hạn chế là..."

## 5. Phần Bố cục luận văn (Thesis Organization)

**NÊN làm:**
- Viết thành 1 đoạn narrative liền mạch, cho thấy mạch logic: lý thuyết → phương pháp → thực nghiệm → kết luận
- Mô tả mỗi chương bằng vai trò/câu hỏi nó giải quyết, không chỉ nội dung
- Dùng `\ref{}` tự nhiên trong đoạn văn

**KHÔNG làm:**
- Không bold **Chương X** mỗi dòng riêng biệt — tạo danh sách thay vì đoạn văn
- Không viết kiểu "Chương 1 giới thiệu... Chương 2 trình bày... Chương 3 đề xuất..." một cách máy móc

## 6. Câu và đoạn văn

**Độ dài câu:**
- Câu tiếng Việt học thuật nên từ 20-40 từ. Trên 50 từ → chia thành 2 câu
- Ưu tiên cấu trúc: chủ ngữ → vị ngữ → bổ ngữ. Tránh mệnh đề phụ quá dài

**Đoạn văn:**
- Mỗi đoạn có 1 ý chính (topic sentence), thường ở đầu đoạn
- 3-6 câu/đoạn là phù hợp cho văn phong học thuật tiếng Việt
- Đoạn nào dài quá 8 câu → xem xét chia

**Tránh lặp ý:**
- Không nói cùng một ý ở 2 mục khác nhau trong Chapter 1
- Nếu ý đã nói ở "Đặt vấn đề", không lặp lại ở "Thách thức"

## 7. Giọng văn học thuật

- Dùng thể bị động hoặc ngôi thứ ba: "luận văn đề xuất", "học viên thực hiện" — KHÔNG dùng "tôi", "chúng tôi"
- Tránh ngôn ngữ không chính thức: "khá tốt", "rất hay", "thú vị"
- Dùng thuật ngữ chính xác: "cải thiện 4,09%" thay vì "cải thiện đáng kể"
- Tránh hedging quá mức: "có thể cho thấy rằng có lẽ..." → "kết quả cho thấy..."