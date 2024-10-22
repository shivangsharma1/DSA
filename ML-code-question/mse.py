import torch 
import torch.nn as nn
import torch.nn.functional as F

def MSE(labels, pred):
    mse = torch.pow(labels - pred, 2)
    return torch.mean(mse)

if __name__ =='__main__':
    batch, samples = 10, 4
    labels = torch.rand(batch, samples)
    pred = torch.rand(batch, samples)
    print(MSE(labels, pred))