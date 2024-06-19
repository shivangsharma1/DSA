import numpy as np

class KNN:
    def __init__(self, k):
        self.k = k

    def fit(self, X, y):
        self.X = X
        self.y = y

    def predict(self, X_test):
        preds = [self._predict(x) for x in X_test]
        return preds
    
    def euclidean(self, x, t):
        distance = np.sqrt(np.sum((x-t)**2))
        return distance

    def _predict(self, x):
        distances = [self.euclidean(x, t) for t in self.X_train]
        top_d = np.argsort(distances)[:self.k]
        top_labels = [self.y[i] for i in top_d]
        np.argmax(np.bincount(top_labels))