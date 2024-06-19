import numpy as np

class LinearRegression:
    def __init__(self, lr = 0.01, n_iteration=100):
        self.lr =lr
        self.n_iteration = n_iteration

    def fit(self, X_train, y_train):
        n_samples, n_features = X_train.shape
        self.weights = np.random.rand(n_features)
        self.bias = 0

        for _ in range(self.n_iteration):

            preds = [(np.dot(sample, self.weights) + self.bias) for sample in X_train]

            dw = (1/n_samples) * np.dot(X_train.T, (y_train-preds))
            db = (1/n_samples) * np.sum(y_train-preds)

            self.weights -= self.lr * dw
            self.bias -= self.lr * db

    def predict(self, X_test):
        preds = [(np.dot(sample, self.weights) + self.bias) for sample in X_test]
        return preds




# Example usage:
if __name__ == "__main__":
    # Example dataset
    X_train = np.array([[1, 10], [2, 11], [3, 12], [4, 12], [5, 15]])
    y_train = np.array([10, 20, 21, 31, 61])

    # Initialize and fit the model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Make predictions
    X_test = np.array([[6, 10], [7, 11]])
    predictions = model.predict(X_test)
    print(predictions)