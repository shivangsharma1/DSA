import torch
import torch.nn as nn
import torch.nn.functional as F

def contrastive_loss(emb1, emb2, preds, epsilon = 1.0):
    
    distance = F.pairwise_distance(emb1, emb2)
    #for similiar samples
    similar = (1 - preds) * torch.pow(distance, 2)

    #for dissimiliar samples
    dissimilar = preds * torch.pow(F.relu(epsilon - distance), 2)

    loss = 0.5 * (similar + dissimilar).mean()

    return loss


if __name__ == '__main__':
    batch, emb_dim = 5, 10
    
    emb1, emb2 = torch.rand(batch, emb_dim), torch.rand(batch, emb_dim)
    preds= torch.randint(1, (batch,))
    print(preds)
    print(contrastive_loss(emb1, emb2, preds))