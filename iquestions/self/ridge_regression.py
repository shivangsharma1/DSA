import numpy as np

class RidgeRegression:
    def __init__(self, lr=0.01, n_iters=100, l2=1) -> None:
        self.lr = lr
        self.n_iters = n_iters
        self.l2 = l2


    def fit(self, X_train, y_train):
        n_sample, n_features = X_train.shape
        self.weights = np.zeros(n_features)
        self.bias = 0


        for _ in range(self.n_iters):
            preds = np.dot(X_train, self.weights) + self.bias
            
            dw = (1/n_sample) * ((np.dot(X_train.T, (y_train-preds))) + (self.l2 * self.weights))
            db = (1/n_sample) * np.sum(y_train-preds)

            self.weights -= (self.lr * dw)
            self.bias -= (self.lr * db)

    def predict(self, X_test):
        preds = np.dot(X_test, self.weights) + self.bias
        return preds


# dW = ( - ( 2 * ( self.X.T ).dot( self.Y - Y_pred ) ) + ( 2 * self.l2_penality * self.W ) ) / self.m 

# Example usage:
if __name__ == "__main__":
    # Example dataset
    X_train = np.array([[1, 10], [2, 11], [3, 12], [4, 12], [5, 15]])
    y_train = np.array([10, 20, 21, 31, 61])

    # Initialize and fit the model
    model = RidgeRegression()
    model.fit(X_train, y_train)

    # Make predictions
    X_test = np.array([[6, 10], [7, 11]])
    predictions = model.predict(X_test)
    print(predictions)