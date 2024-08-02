import torch
import torch.nn as nn


class Contrastive_loss(nn.Module):
    def __init__(self, margin=1.0):
        super().__init__()
        self.margin = margin

    def forward(self, out1, out2, label):

        # calcualting the euclidean distance
        edist = nn.functional.pairwise_distance(out1, out2)

        # calculate loss
        contrastive_loss = torch.mean((1 - label) * torch.pow(edist, 2)
            + 
            (label * (torch.pow(torch.clamp(self.margin - edist, min=0.0), 2)))
        )
        return contrastive_loss


if __name__ =='__main__':
    x1 = torch.rand(10, 512)
    x2 = torch.rand(10, 512)
    labels = torch.randint(0, 2, (10, ))

    print("x1", x1)
    print("x2", x1)
    print("labels", labels)
    contrastive_loss = Contrastive_loss()
    print(contrastive_loss(x1, x2, labels))