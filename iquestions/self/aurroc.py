import matplotlib.pyplot as plt
import numpy as np

# labels = [1,0,0,1,1,0]
# preds = [0.8, 0.6, 0.4, 0.2, 0.3, 0.6]``


labels  = [1, 0, 1, 0]
preds  = [0.8, 0.6, 0.4, 0.2]

P = sum(labels)
N = len(labels) - P

FPR = []
TPR = []


thresholds = np.arange(0, 1.01, 0.1)

for thr in thresholds:
    FP = 0
    TP = 0
    for i in range(len(labels)):
        if preds[i]>np.round(thr, 2):
            if labels[i] == 1:
                TP+=1
            else:
                FP+=1
    TPR.append(TP/P)
    FPR.append(FP/N)


print(FPR)
print(TPR)

plt.plot(FPR, TPR, linestyle="--")
plt.plot([0, 1], [1, 0])
plt.show()