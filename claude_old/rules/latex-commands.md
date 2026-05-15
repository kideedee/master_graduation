# Common LaTeX Commands

This file contains commonly used LaTeX commands for this thesis.

## Model Names

```latex
\textbf{PhaBERT\_CNN}  % Bold for emphasis
PhaBERT\_CNN           % Regular text
```

## Performance Metrics

```latex
Accuracy: 95.3\%
F1-Score: 94.9\%
Precision: 94.7\%
Recall: 95.0\%
```

## Genomic Sequences

```latex
\texttt{ATCGATCG}      % Monospace font for sequences
```

## Mathematical Notation

```latex
% Loss function
\mathcal{L} = -\sum_{i=1}^{N} y_i \log(\hat{y}_i)

% Softmax
\sigma(z_i) = \frac{e^{z_i}}{\sum_{j=1}^{K} e^{z_j}}

% Accuracy
\text{Accuracy} = \frac{TP + TN}{TP + TN + FP + FN}

% Argmax
\argmax_{y} P(y|x)
```

## Cross-Referencing

```latex
% Define labels
\label{fig:architecture}
\label{tab:results}
\label{eq:loss}

% Reference them
Hình \ref{fig:architecture}
Bảng \ref{tab:results}
Phương trình \ref{eq:loss}
```

## Adding New Sections

```latex
% In chapters/c2/co_so_ly_thuyet.tex
\input{chapters/c2/bacteriophage_intro}
\input{chapters/c2/bert_architecture}
\input{chapters/c2/cnn_fundamentals}
\input{chapters/c2/related_work}
```
