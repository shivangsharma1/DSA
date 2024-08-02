import torch
import torch.nn as nn
import torch.nn.functional as F

class TripletLoss(nn.Module):
    def __init__(self, margin=1.0):
        super(TripletLoss, self).__init__()
        self.margin = margin

    def forward(self, anchor, positive, negative):
        distance_positive = F.pairwise_distance(anchor, positive, p=2)
        distance_negative = F.pairwise_distance(anchor, negative, p=2)
        
        losses = F.relu(distance_positive - distance_negative + self.margin)
        return losses.mean()

# Example usage
if __name__ == "__main__":
    # Dummy data
    anchor = torch.rand(10, 128, 512)   # Batch of 10 samples with 128-dimensional embeddings
    positive = torch.rand(10, 128, 512) # Batch of 10 samples with 128-dimensional embeddings
    negative = torch.rand(10, 128, 512) # Batch of 10 samples with 128-dimensional embeddings

    triplet_loss = TripletLoss(margin=2.0)
    loss = triplet_loss(anchor, positive, negative)
    print(f"Triplet Loss: {loss.item()}")
