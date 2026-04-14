# Python Code Integration

This file contains guidance for integrating Python code into the thesis.

## Inline Code Snippets

```latex
\begin{lstlisting}[language=Python, caption={PhaBERT\_CNN model architecture}]
import torch
import torch.nn as nn
from transformers import BertModel

class PhaBERT_CNN(nn.Module):
    def __init__(self, num_classes):
        super().__init__()
        self.bert = BertModel.from_pretrained('bert-base-uncased')
        self.cnn = nn.Sequential(
            nn.Conv1d(768, 256, kernel_size=3),
            nn.ReLU(),
            nn.MaxPool1d(2),
            nn.Conv1d(256, 128, kernel_size=3),
            nn.ReLU(),
            nn.AdaptiveAvgPool1d(1)
        )
        self.classifier = nn.Linear(128, num_classes)

    def forward(self, input_ids, attention_mask):
        bert_output = self.bert(input_ids, attention_mask)
        sequence_output = bert_output.last_hidden_state
        # Transpose for CNN: (batch, seq_len, hidden) -> (batch, hidden, seq_len)
        cnn_input = sequence_output.transpose(1, 2)
        cnn_output = self.cnn(cnn_input).squeeze(-1)
        logits = self.classifier(cnn_output)
        return logits
\end{lstlisting}
```

## Including External Python Files

```latex
% Include complete model file
\lstinputlisting[language=Python, caption={Complete model implementation}]{snipet/phabert_model.py}
```

## Configure listings Package

Add to thesis preamble for better Python formatting:

```latex
\lstset{
    language=Python,
    basicstyle=\ttfamily\small,
    keywordstyle=\color{blue},
    commentstyle=\color{gray},
    stringstyle=\color{red},
    numbers=left,
    numberstyle=\tiny,
    breaklines=true,
    frame=single
}
```
