import numpy as np


class LogisticRegression:
    def __init__(self, lr=0.001, n_iters=100):
        self.lr = lr
        self.n_iters = n_iters

    def fit(self, X, y):
        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features)
        self.bias = 0

        for _ in range(self.n_iters):
            #get prediction
            y_pred = self.sigmoid(np.dot(X, self.weights) + self.bias)

            #calculate differentials
            dw = (1/n_samples)  * np.dot(X.T, (y-y_pred))
            db = (1/n_samples)  * np.sum(y-y_pred)

            #update weight
            self.weights -= self.lr * dw 
            self.bias -= self.lr * db

    def sigmoid(self, z):
        return (1/(1+np.exp(-z)))

    def predict(self, X_test): 
        y_preds = [self.sigmoid(np.dot(x, self.weights) + self.bias) for x in X_test]
        labels = [1 if preds>0.5 else 0 for preds in y_preds]
        return labels


# Example usage:
if __name__ == "__main__":
    # Example dataset
    X_train = np.array([[1, ], [2], [3], [4], [5]])
    y_train = np.array([0, 0, 1, 1, 1])

    # Initialize and fit the model
    model = LogisticRegression()
    model.fit(X_train, y_train)

    # Make predictions
    X_test = np.array([[6], [7]])
    predictions = model.predict(X_test)
    print(predictions)