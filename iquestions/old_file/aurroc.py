import numpy as np
import matplotlib.pyplot as plt



y  = [1, 0, 1, 0]
preds  = [0.8, 0.6, 0.4, 0.2]

FPR = []
TPR = []

P = sum(y)
N = len(y) - P
threshold = np.arange(0, 1.01, 0.1)

for thresh in threshold:
    FP = 0
    TP = 0

    for i in range(len(y)):
        if preds[i]>=round(thresh, 2):
            if y[i] == 1:
                TP = TP + 1
        
            if y[i] == 0:
                FP = FP + 1
    FPR.append(FP/N)
    TPR.append(TP/P)
print("FPR", FPR)
print("TPR", TPR)

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