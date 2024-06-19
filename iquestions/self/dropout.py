import torch
import torch.nn as nn
import numpy as np

class Dropout(nn.Module):
    def __init__(self, ratio=0.2):
        self.ratio = ratio

    def forward(self, x):
        mask = np.random.binomial(1, 1-0.2, 10)
        x = x * mask

        x/=self.ratio
        return x


if __name__ == '__main__':
    array = torch.rand(10)
    print(array)

    drop = Dropout()
    print(drop.forward(array))
