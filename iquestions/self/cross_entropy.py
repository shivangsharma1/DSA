import torch
import torch.nn as nn

def cross_entropy(labels, preds, weights=None):
    if len(labels.shape) == 1:
        labels = nn.functional.one_hot(labels, num_classes = preds.shape[1])

    if weights is not None:
        weights = torch.tensor(weights)
        print("in if")
        loss = -torch.sum(labels * weights * torch.log(preds), dim=-1)
    else:
        print("else")
        loss = -torch.sum(labels * torch.log(preds), dim=-1)
    
    return torch.mean(loss)



if __name__ =='__main__':
    batch_size = 10
    classes = 4
    weights = [1, 2, 3, 1]
    preds = torch.rand(batch_size, classes) # 10, 4
    labels = torch.randint(0, classes, (batch_size, )) # 1, 10

    print(cross_entropy(labels, preds))
