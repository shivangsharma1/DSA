import numpy as np
import matplotlib.pyplot as plt

# preds = [0.8, 0.2, 0.7, 0.3, 0.1, 0.2, 0.9, 0.8, 0.7]
# actuals = [1, 1, 1, 0, 1, 0, 0, 1, 0]

actuals  = [1, 0, 1, 0]
preds  = [0.8, 0.6, 0.4, 0.2]

n = len(actuals)
P = sum(actuals)
N = n-P
FPR = []
TPR = []

thresholds = np.arange(0, 1.01, 0.1)

for thr in thresholds:
    FP = 0
    TP = 0
    for i in range(n):
        if preds[i]>=np.round(thr, 2):
            if actuals[i]==1:
                TP = TP+1
            else:
                FP=FP+1
    TPR.append(TP/P)
    FPR.append(FP/N)

print("TPR", TPR)
print("FPR", FPR)

plt.plot(FPR, TPR, linestyle='--', marker='o', color='darkorange', lw = 2, label='ROC curve', clip_on=False)
plt.plot([0, 1], [0, 1], color='navy', linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.0])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
# plt.title('ROC curve, AUC = %.2f'%auc)
plt.legend(loc="lower right")
# plt.savefig('AUC_example.png')
plt.show()