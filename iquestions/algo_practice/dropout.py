import numpy as np

def Dropout(arr, ratio = 0.5):
    mask = np.random.binomial(1, 1-ratio, arr.shape)
    print("mask", mask)
    result = arr*mask
    return result




arr = np.array([1,2,3,4,5,6,7,8,9,10])
ratio = 0.5
print(Dropout(arr, ratio))