import torch
import torch.nn as nn


class Contrastive_loss(nn.Module):
    def __init__(self, margin=1.0):
        super().__init__()
        self.margin - margin

    def forward(self, out1, out2, label):

        # calcualting the euclidean distance
        edist = nn.functional.pairwise_distance(out1, out2)

        # calculate loss
        contrastive_loss = torch.mean(
            (1 - label) * torch.pow(edist, 2) + 
            (label * (torch.pow(torch.clamp(self.margin - edist, min=0.0), 2)))
        )

        return contrastive_loss


