# Bioinformatics Content Formatting

This file contains guidance for formatting bioinformatics-specific content in the thesis.

## Formatting Genomic Sequences

**Short sequences inline:**
```latex
The sequence \texttt{ATCGATCGTAGC} shows...
```

**Longer sequences in listings:**
```latex
\begin{lstlisting}[caption={Phage genome fragment}]
ATCGATCGTAGCTAGCTAGCTAGCTAGCTAGC
GCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTA
\end{lstlisting}
```

## Model Architecture Diagrams

- Create diagrams using TikZ or include images from Python (matplotlib, seaborn)
- Place in `imgs/` directory with descriptive names like `phabert_cnn_architecture.png`
- Use consistent styling across all architecture diagrams

## Performance Metrics Tables

```latex
\begin{table}[h]
\centering
\caption{Classification performance comparison}
\label{tab:performance}
\begin{tabular}{lccc}
\toprule
Model & Accuracy & Precision & F1-Score \\
\midrule
Baseline & 85.2\% & 83.1\% & 84.0\% \\
PhaBERT & 92.5\% & 91.8\% & 92.1\% \\
\textbf{PhaBERT\_CNN} & \textbf{95.3\%} & \textbf{94.7\%} & \textbf{95.0\%} \\
\bottomrule
\end{tabular}
\end{table}
```

**Dataset statistics table:**
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

## Mathematical Notation

```latex
% Loss function
\mathcal{L} = -\sum_{i=1}^{N} y_i \log(\hat{y}_i)

% Model notation
\text{PhaBERT\_CNN}(x) = \text{CNN}(\text{BERT}(x))

% Softmax
\sigma(z_i) = \frac{e^{z_i}}{\sum_{j=1}^{K} e^{z_j}}

% Accuracy formula
\text{Accuracy} = \frac{TP + TN}{TP + TN + FP + FN}
```
