# Plan: Thay "backbone" bang "mang nen DNABERT-2" trong toan bo luan van

## Muc tieu

Thong nhat thuat ngu: thay vi dung tu tieng Anh "backbone", su dung "mang nen" (Vietnamese) hoac "mang nen DNABERT-2" tuy ngu canh. Chuong 2 da dung dung mau "mang nen (backbone)" -- cac chuong khac can theo.

## Nguyen tac thay the

- Lan dau xuat hien trong moi chuong: **mang nen (backbone)** de nguoi doc biet thuat ngu tieng Anh tuong ung
- Cac lan sau trong cung chuong: **mang nen** hoac **mang nen DNABERT-2**
- Trong bang (table): giu "backbone" trong ngoac don vi khong gian han che
- Tieu de subsection: doi thanh tieng Viet

## Danh sach thay doi cu the

### Chapter 1 (`chapters/c1/chapter_1.tex`)

| Dong | Hien tai | Thay thanh |
|------|----------|------------|
| 37 | "DNABERT-2 backbone va MKCA" | "mang nen DNABERT-2 va MKCA" |

### Chapter 2 (`chapters/c2/chapter_2.tex`)

| Dong | Hien tai | Thay thanh |
|------|----------|------------|
| 112 | Da dung "mang nen (backbone)" | **Khong can sua** |

### Chapter 3 (`chapters/c3/chapter_3.tex`)

| Dong | Hien tai | Thay thanh |
|------|----------|------------|
| 85 | "DNABERT-2 backbone dong vai tro" | "mang nen DNABERT-2 dong vai tro" |
| 94 | `\subsection{DNABERT-2 Backbone}` | `\subsection{Mang nen DNABERT-2}` |
| 96 | "backbone trich xuat dac trung" | "mang nen trich xuat dac trung" |
| 228 | "Toc do hoc (backbone)" | "Toc do hoc (mang nen)" |
| 230 | "Suy giam trong so (backbone)" | "Suy giam trong so (mang nen)" |

### Chapter 5 (`chapters/c5/chapter_5.tex`)

| Dong | Hien tai | Thay thanh |
|------|----------|------------|
| 7 | "ca backbone va cac thanh phan task-specific" | "ca mang nen va cac thanh phan task-specific" |
| 16 | "dong bang backbone de huan luyen" + "learning rate thap hon cho backbone" | "dong bang mang nen de huan luyen" + "learning rate thap hon cho mang nen" |

## Cap nhat vietnamese-terms.md

- Chuyen "backbone" tu bang "Forbidden Substitutions (Keep in English)" sang bang "Key Technical Terms"
- Them: `| Mang nen | Backbone |`

## Citations

Khong can them citation moi.

## Luu y

- Chuong 5 da dung "mo hinh nen tang genome" o mot so cho -- day la cach dich khac cua "foundation model", KHONG phai "backbone". Khong can sua nhung cho nay.
- Kiem tra sau khi sua: compile LaTeX dam bao khong loi.
