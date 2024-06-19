import numpy as np
    
class Dropout:
    def __init__(self, ratio):
        self.ratio = ratio

    def forward(self, x):
        self.mask = np.random.binomial(1, self.ratio, x.shape)
        x = x*self.mask
        x /= self.ratio

        return x

    def backward(self, dY):
        dY *= self.ratio
        dY *= self.mask * dY

        return dY



x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(Dropout(x, 0.5))




