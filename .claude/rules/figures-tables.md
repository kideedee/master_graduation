# Figures and Tables

This file contains guidance for adding and formatting figures and tables in the thesis.

## Adding Figures

### Place Images in imgs/ Directory

```bash
imgs/
├── phabert_cnn_architecture.png
├── training_curves.png
├── confusion_matrix.png
├── roc_curve.png
└── dataset_distribution.png
```

### Single Figure

```latex
\begin{figure}[h]
  \centering
  \includegraphics[width=0.8\textwidth]{imgs/phabert_cnn_architecture.png}
  \caption{Kiến trúc mô hình PhaBERT\_CNN}
  \label{fig:architecture}
\end{figure}

% Reference in text
Như thể hiện trong Hình \ref{fig:architecture}, ...
```

### Side-by-Side Figures

```latex
\begin{figure}[h]
  \centering
  \begin{subfigure}{0.45\textwidth}
    \includegraphics[width=\textwidth]{imgs/training_loss.png}
    \caption{Training loss}
    \label{fig:train_loss}
  \end{subfigure}
  \hfill
  \begin{subfigure}{0.45\textwidth}
    \includegraphics[width=\textwidth]{imgs/validation_loss.png}
    \caption{Validation loss}
    \label{fig:val_loss}
  \end{subfigure}
  \caption{Đường cong huấn luyện của mô hình}
  \label{fig:training_curves}
\end{figure}
```

## Adding Tables

### Performance Comparison Table

```latex
\begin{table}[h]
\centering
\caption{So sánh hiệu suất các mô hình phân loại}
\label{tab:comparison}
\begin{tabular}{lcccc}
\toprule
\textbf{Mô hình} & \textbf{Accuracy} & \textbf{Precision} & \textbf{Recall} & \textbf{F1-Score} \\
\midrule
Random Forest & 82.3\% & 80.5\% & 81.2\% & 80.8\% \\
SVM & 85.7\% & 84.3\% & 85.0\% & 84.6\% \\
CNN & 89.2\% & 88.5\% & 88.9\% & 88.7\% \\
BERT & 92.5\% & 91.8\% & 92.1\% & 92.0\% \\
\textbf{PhaBERT\_CNN} & \textbf{95.3\%} & \textbf{94.7\%} & \textbf{95.0\%} & \textbf{94.9\%} \\
\bottomrule
\end{tabular}
\end{table}
```

### Dataset Statistics Table

```latex
\begin{table}[h]
\centering
\caption{Thống kê dữ liệu huấn luyện}
\label{tab:dataset}
\begin{tabular}{lrrr}
\toprule
\textbf{Phage Family} & \textbf{Training} & \textbf{Validation} & \textbf{Test} \\
\midrule
Myoviridae & 1,250 & 312 & 313 \\
Siphoviridae & 980 & 245 & 245 \\
Podoviridae & 756 & 189 & 189 \\
Others & 423 & 106 & 106 \\
\midrule
\textbf{Total} & \textbf{3,409} & \textbf{852} & \textbf{853} \\
\bottomrule
\end{tabular}
\end{table}
```
