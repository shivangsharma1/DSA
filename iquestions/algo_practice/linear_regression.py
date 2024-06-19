import numpy as np

class LinearRegression:
    def __init__(self, lr=0.01, n_iters=100):
        self.lr = lr
        self.n_iters = n_iters
        self.weights = None
        self.bias = None

    def fit(self, X, y):
        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features, )
        self.bias = 0

        for _ in range(self.n_iters):
            y_pred = np.dot(X, self.weights) + self.bias

            dw = (1/n_samples) * np.dot(X.T, (y-y_pred))
            db = (1/n_samples) * np.sum(y-y_pred)

            self.weights -= self.lr * dw
            self.bias -= self.lr * db

    def predict(self, X):
        pred = np.dot(X, self.weights) + self.bias
        return pred
    

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