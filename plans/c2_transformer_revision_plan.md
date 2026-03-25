# Plan: Chapter 2 - Rut gon muc "Kien truc Transformer va co che chu y"

## Boi canh

Muc `\subsection{Kien truc Transformer va co che chu y}` (dong 83-106, `chapters/c2/chapter_2.tex`) hien dang chua noi dung ve cac bien the ma hoa vi tri (learned positional embedding, ALiBi) tai dong 103. Noi dung nay khong phu hop voi pham vi cua muc --- chi nen trinh bay Transformer goc va co che tu chu y. Dac biet, ALiBi da duoc trinh bay day du trong muc DNABERT-2 (dong 123), gay trung lap.

## Pham vi thay doi

Chi sua **doan dong 103** (doan ve positional encoding). Cac doan khac giu nguyen.

## Noi dung hien tai cua dong 103

```latex
Do co che tu chu y khong co khai niem ve thu tu vi tri, Transformer can bo sung thong tin vi tri cho cac phan tu trong chuoi. Phuong phap ban dau su dung ma hoa vi tri dang ham sin (sinusoidal positional encoding)~\cite{vaswani2017attention}. Cac bien the sau nay bao gom bieu dien vi tri hoc duoc (learned positional embedding), trong do vector vi tri duoc huan luyen cung mo hinh nhung bi gioi han boi do dai toi da da dinh truoc, va ALiBi (Attention with Linear Biases)~\cite{press2021train}, phuong phap them do lech tuyen tinh vao diem chu y dua tren khoang cach giua cac vi tri, cho phep mo hinh xu ly chuoi co do dai tuy y ma khong can huan luyen lai.
```

## Noi dung de xuat thay the

```latex
Do co che tu chu y khong co khai niem ve thu tu vi tri, Transformer can bo sung thong tin vi tri cho cac phan tu trong chuoi. Phuong phap goc su dung ma hoa vi tri dang ham sin (sinusoidal positional encoding)~\cite{vaswani2017attention}, trong do vi tri cua moi phan tu duoc bieu dien bang to hop cac ham sin va cosin voi tan so khac nhau, cho phep mo hinh suy luan tuong doi ve khoang cach giua cac vi tri.
```

### Ly do thay doi

1. **Loai bo ALiBi va learned positional embedding**: Day la cac cai tien sau nay, khong thuoc Transformer goc (Vaswani et al., 2017). ALiBi da duoc trinh bay o muc DNABERT-2 (dong 123), khong can gioi thieu truoc.
2. **Bo sung giai thich ngan ve sinusoidal encoding**: Doan goc chi noi ten phuong phap ma khong giai thich, doan moi them mot cum mo ta ngan ("to hop cac ham sin va cosin voi tan so khac nhau") de nguoi doc hieu ban chat.
3. **Bo trich dan `\cite{press2021train}`**: Trich dan nay chi can xuat hien o muc DNABERT-2.

## Outline cua muc sau khi sua

Muc giu nguyen 5 doan nhu cu, chi doan 4 (ve positional encoding) duoc rut gon:

I. **Doan 1 (dong 86)**: Gioi thieu Transformer, so sanh voi RNN/LSTM, uu diem xu ly song song --- GIU NGUYEN
II. **Hinh (dong 88-93)**: Hinh kien truc Transformer --- GIU NGUYEN
III. **Doan 2 (dong 95-99)**: Co che tu chu y: Q, K, V, cong thuc scaled dot-product attention --- GIU NGUYEN
IV. **Doan 3 (dong 101)**: Co che chu y da dau (multi-head attention) --- GIU NGUYEN
V. **Doan 4 (dong 103)**: Ma hoa vi tri --- **SUA**: chi trinh bay sinusoidal positional encoding goc, bo ALiBi va learned positional embedding
VI. **Doan 5 (dong 105)**: Cau truc lop Transformer (FFN, layer norm, residual) --- GIU NGUYEN

## Trich dan

- `\cite{vaswani2017attention}` --- Transformer goc, sinusoidal positional encoding --- OK EXISTS (dong 1, references.bib)
- `\cite{press2021train}` --- **SE BI LOAI KHOI MUC NAY** --- van con duoc dung o muc DNABERT-2 (dong 123, 249 trong references.bib) nen khong mat trich dan

## So lieu can kiem tra

Khong co so lieu cu the trong doan bi sua.

## Thuat ngu tieng Viet

- Attention mechanism -> Co che chu y
- Self-attention -> Tu chu y / Co che tu chu y
- Multi-head attention -> Chu y da dau
- Positional encoding -> Ma hoa vi tri
- Sinusoidal positional encoding -> Ma hoa vi tri dang ham sin
- Residual connection -> Ket noi tat
- Layer normalization -> Chuan hoa lop
- Feed-forward network -> Mang truyen thang

## Hinh/Bang

Khong can thay doi hinh hay bang nao.

## Ghi chu

- Kiem tra lai muc DNABERT-2 (dong 116-126) sau khi sua de dam bao ALiBi van duoc gioi thieu day du o do --- **DA KIEM TRA**: dong 123 trinh bay ALiBi chi tiet, khong bi anh huong.
- Dong 103 hien tai cung nhac "learned positional embedding" --- cung se bi loai vi la cai tien sau Transformer goc, va khong lien quan truc tiep den DNABERT-2 (DNABERT-2 dung ALiBi, khong dung learned positional embedding).
