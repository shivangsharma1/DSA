import numpy as np

class LogisticRegression:
    def __init__(self, lr = 0.01, n_iters = 100):
        self.lr = lr
        self.n_iters = n_iters
        

    def fit(self, X_train, y_train):
        n_samples, n_features = X_train.shape
        self.weights = np.random.rand(n_features)
        self.bias = 0

        for _ in range(self.n_iters):
            y_preds = self.sigmoid(np.dot(X_train, self.weights) + self.bias)

            dw = (1/n_samples) * (np.dot(X_train.T, (y_train-y_preds)))
            db = (1/n_samples) * np.sum(y_train-y_preds)

            self.weights -= self.lr*dw
            self.bias -= self.lr * db

    def predict(self, X_test):
        pred = [self.sigmoid(np.dot(sample, self.weights) + self.bias) for sample in X_test]
        pred = [1 if prob>0.1 else 0 for prob in pred]
        return pred

    def sigmoid(self, X):
        return 1/(1+np.exp(-X))


if __name__ == '__main__':
    # Example dataset
    X_train = np.array([[1], [2], [3], [4], [5]])
    y_train = np.array([0, 0, 1, 1, 1])

    # Initialize and fit the model
    model = LogisticRegression()
    model.fit(X_train, y_train)

    # Make predictions
    X_test = np.array([[6], [7]])
    predictions = model.predict(X_test)
    print(predictions)