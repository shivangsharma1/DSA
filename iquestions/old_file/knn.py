import numpy as np

class KNN:
    def __init__(self, n_neighbors=5):
        self.n_neighbors = n_neighbors

    def fit(self, X, y):
        self.X_train = X
        self.y_train = y

    def _euclidean_distance(self, x1, x2):
        return np.sqrt(np.sum((x1 - x2)**2))

    def predict(self, X):
        predictions = []
        for x_test in X:
            distances = [self._euclidean_distance(x_test, x_train) for x_train in self.X_train]
            nearest_indices = np.argsort(distances)[:self.n_neighbors]
            nearest_labels = [self.y_train[i] for i in nearest_indices]
            most_common_label = max(set(nearest_labels), key=nearest_labels.count)
            predictions.append(most_common_label)
        return predictions

# Example usage:
X_train = np.array([[1, 2], [2, 3], [3, 4], [5, 6], [7, 8]])
y_train = np.array([0, 0, 1, 1, 1])

knn = KNN(n_neighbors=3)
knn.fit(X_train, y_train)

X_test = np.array([[4, 5], [6, 7]])
predictions = knn.predict(X_test)

print("Predictions for test data:")
print(predictions)
