import numpy as np

class KNN:
    def __init__(self, k = 3) :
        self.k = k

    def fit(self, X, y):
        self.X_train = X
        self.y_train = y

    def predict(self, X):
        predictions = [self._predict(x) for x in X]
        return predictions
    
    def euclidean_distance(self, x1, x2):
        distance =  np.sqrt(np.sum((x1-x2)**2))
        return distance

    def _predict(self, x):
        #compute distance
        distances = [self.euclidean_distance(x, train_x) for train_x in self.X_train]
        indexes = np.argsort(distances)[:self.k]
        top_labels = [self.y_train[i] for i in indexes]
        output = np.argmax(np.bincount(top_labels))
        return output
