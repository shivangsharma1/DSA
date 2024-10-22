import torch
import torch.nn as nn
import torch.nn.functional as F

def weighted_cross_entropy(targets, preds, weights):
    preds = F.softmax(preds, dim = 1)
    #one hot encodeing target
    oh_target = F.one_hot(targets, num_classes = preds.shape[1])
    #log probs 
    log_pred = torch.log(preds)
    #cross_entropy
    cross_entropy = -torch.sum(oh_target * log_pred * torch.tensor(weights), dim=1)

    return cross_entropy.mean()

if __name__ =='__main__':
    batch_size = 10
    classes = 4
    weights = [1, 2, 3, 1]
    preds = torch.rand(batch_size, classes) # 10, 4
    labels = torch.randint(0, classes, (batch_size, )) # 1, 10

    print(weighted_cross_entropy(labels, preds, weights))