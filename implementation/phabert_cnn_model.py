import warnings

import torch
import torch.nn as nn
from transformers import AutoModel, PreTrainedModel, AutoConfig

warnings.filterwarnings('ignore')


def create_custom_config():
    """
    Tạo config cho custom model
    """
    config = AutoConfig.from_pretrained("zhihan1996/DNABERT-2-117M", trust_remote_code=True)
    config.num_labels = 2
    config.classifier_dropout = 0.1
    config.problem_type = "single_label_classification"
    return config


class Dnabert2CnnModelNoAttention(PreTrainedModel):
    """
    Ablation variant: PhaBERT-CNN without attention-based pooling.
    Attention pooling is replaced by masked mean pooling for global
    transformer feature aggregation.
    """

    def __init__(self, config, dropout_rate=0.1, num_classes=2):
        super(Dnabert2CnnModelNoAttention, self).__init__(config)

        # Load DNABERT-2 pre-trained model
        self.dnabert = AutoModel.from_pretrained(
            "zhihan1996/DNABERT-2-117M",
            trust_remote_code=True,
            add_pooling_layer=False
        )

        for param in self.dnabert.parameters():
            param.requires_grad = False

        self.cnn_branches = nn.ModuleList([
            # Branch 1: Small receptive field for local motifs
            nn.Sequential(
                nn.Conv1d(768, 256, kernel_size=3, padding=1),
                nn.BatchNorm1d(256),
                nn.ReLU(),
                nn.Conv1d(256, 128, kernel_size=3, padding=1),
                nn.BatchNorm1d(128),
                nn.ReLU(),
                nn.AdaptiveMaxPool1d(1)
            ),
            # Branch 2: Medium receptive field
            nn.Sequential(
                nn.Conv1d(768, 256, kernel_size=5, padding=2),
                nn.BatchNorm1d(256),
                nn.ReLU(),
                nn.Conv1d(256, 128, kernel_size=5, padding=2),
                nn.BatchNorm1d(128),
                nn.ReLU(),
                nn.AdaptiveMaxPool1d(1)
            ),
            # Branch 3: Large receptive field for longer patterns
            nn.Sequential(
                nn.Conv1d(768, 256, kernel_size=7, padding=3),
                nn.BatchNorm1d(256),
                nn.ReLU(),
                nn.Conv1d(256, 128, kernel_size=7, padding=3),
                nn.BatchNorm1d(128),
                nn.ReLU(),
                nn.AdaptiveMaxPool1d(1)
            )
        ])

        # Global pooling for transformer features (NO attention pooling)
        # Mean-pooled features are projected through this layer
        self.global_pooling = nn.Sequential(
            nn.Linear(768, 128),
            nn.ReLU(),
            nn.Dropout(0.1)
        )

        # NOTE: self.attention_pooling is REMOVED in this ablation variant.
        # Instead, masked mean pooling is used directly in forward().

        # Final classifier (same architecture as full model)
        total_features = 128 * 3 + 128  # CNN features + global features
        classifier_dropout = getattr(config, 'classifier_dropout', 0.1)

        self.classifier = nn.Sequential(
            nn.Linear(total_features, 256),
            nn.LayerNorm(256),
            nn.ReLU(),
            nn.Dropout(classifier_dropout),
            nn.Linear(256, 64),
            nn.ReLU(),
            nn.Dropout(classifier_dropout),
            nn.Linear(64, config.num_labels)
        )

    def freeze_dnabert(self):
        for param in self.dnabert.parameters():
            param.requires_grad = False

    def unfreeze_dnabert(self):
        for param in self.dnabert.parameters():
            param.requires_grad = True

    def forward(self, input_ids, attention_mask=None, labels=None):
        # Extract features từ DNABERT-2
        with torch.set_grad_enabled(self.dnabert.training and any(p.requires_grad for p in self.dnabert.parameters())):
            outputs = self.dnabert(input_ids=input_ids, attention_mask=attention_mask)
            if hasattr(outputs, 'last_hidden_state'):
                hidden_states = outputs.last_hidden_state
            elif isinstance(outputs, tuple):
                hidden_states = outputs[0]
            else:
                hidden_states = outputs['last_hidden_state']

        # ============================================================
        # ABLATION: Masked mean pooling (replaces attention pooling)
        # ============================================================
        if attention_mask is not None:
            # Expand mask: [batch_size, seq_len] -> [batch_size, seq_len, 1]
            mask_expanded = attention_mask.unsqueeze(-1).float()
            # Sum of hidden states weighted by mask
            sum_hidden = torch.sum(hidden_states * mask_expanded, dim=1)  # [batch_size, 768]
            # Count of non-padding tokens
            count = torch.clamp(mask_expanded.sum(dim=1), min=1e-9)  # [batch_size, 1]
            global_features = sum_hidden / count  # [batch_size, 768]
        else:
            # Fallback: simple mean pooling without mask
            global_features = torch.mean(hidden_states, dim=1)  # [batch_size, 768]

        global_features = self.global_pooling(global_features)  # [batch_size, 128]

        # CNN features (same as full model)
        cnn_input = hidden_states.transpose(1, 2)  # [batch_size, 768, seq_len]

        cnn_features = []
        for branch in self.cnn_branches:
            branch_output = branch(cnn_input)  # [batch_size, 128, 1]
            cnn_features.append(branch_output.squeeze(2))  # [batch_size, 128]

        # Combine all features
        combined_features = torch.cat([global_features] + cnn_features, dim=1)

        # Classification
        logits = self.classifier(combined_features)

        return logits