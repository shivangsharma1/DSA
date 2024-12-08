import torch
import torch.nn as nn
import torch.nn.functional as F


def cross_entropy(target, preds, weights = None):
    #target shape  = (n, 1)
    preds = torch.softmax(preds, dim = -1)
    # print(preds.shape)

    #one hot target
    targets = F.one_hot(target, num_classes=preds.shape[-1])

    if weights:
        weights = torch.tensor(weights)
        scores = -torch.sum(targets * weights * torch.log(preds))
    else:
        scores = -torch.sum(targets * torch.log(preds))
    print(scores)



if __name__ == '__main__':
    batch = 10
    classes = 5
    preds  = torch.rand(batch, classes)
    target = torch.randint(low = 0, high = classes, size = (batch, ))
    weights = [5, 2, 9, 10, 11]
    
    cross_entropy(target, preds, weights)