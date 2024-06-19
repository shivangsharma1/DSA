import numpy as np

class DecisionTree:
    def fit(self, X, y):
        self.X = X
        self.y = y
        self.n_classes = len(np.unique(y))
        self.n_features = X.shape[1]

    def _entropy(self, y):
        _, counts = np.unique(y, return_counts=True)
        probabilities = counts / len(y)
        entropy = -np.sum(probabilities * np.log2(probabilities + 1e-10))
        return entropy

    def _information_gain(self, feature, threshold):
        parent_entropy = self._entropy(self.y)
        left_idxs = np.where(self.X[:, feature] <= threshold)[0]
        right_idxs = np.where(self.X[:, feature] > threshold)[0]

        if len(left_idxs) == 0 or len(right_idxs) == 0:
            return 0

        n = len(self.y)
        n_left = len(left_idxs)
        n_right = len(right_idxs)
        entropy_left = self._entropy(self.y[left_idxs])
        entropy_right = self._entropy(self.y[right_idxs])

        child_entropy = (n_left / n) * entropy_left + (n_right / n) * entropy_right

        return parent_entropy - child_entropy

    def _find_best_split(self):
        best_gain = 0
        best_feature = None
        best_threshold = None

        for feature in range(self.n_features):
            thresholds = np.unique(self.X[:, feature])
            for threshold in thresholds:
                gain = self._information_gain(feature, threshold)
                if gain > best_gain:
                    best_gain = gain
                    best_feature = feature
                    best_threshold = threshold

        return best_feature, best_threshold

    def _split(self, X, y, feature, threshold):
        left_idxs = np.where(X[:, feature] <= threshold)[0]
        right_idxs = np.where(X[:, feature] > threshold)[0]
        left_X, left_y = X[left_idxs], y[left_idxs]
        right_X, right_y = X[right_idxs], y[right_idxs]
        return left_X, left_y, right_X, right_y

    def _build_tree(self, X, y):
        if len(np.unique(y)) == 1:
            return {'class': y[0]}
        if len(X) == 0:
            return {'class': np.argmax(np.bincount(self.y))}
        
        best_feature, best_threshold = self._find_best_split()
        if best_feature is None:
            return {'class': np.argmax(np.bincount(y))}

        left_X, left_y, right_X, right_y = self._split(X, y, best_feature, best_threshold)
        return {'feature': best_feature,
                'threshold': best_threshold,
                'left': self._build_tree(left_X, left_y),
                'right': self._build_tree(right_X, right_y)}

    def fit_model(self):
        self.tree_ = self._build_tree(self.X, self.y)

    def predict(self, X):
        predictions = []
        for x in X:
            node = self.tree_
            while 'class' not in node:
                if x[node['feature']] <= node['threshold']:
                    node = node['left']
                else:
                    node = node['right']
            predictions.append(node['class'])
        return predictions

# Example usage:
X_train = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y_train = np.array([0, 1, 1, 0])

tree = DecisionTree()
tree.fit(X_train, y_train)
tree.fit_model()

X_test = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
predictions = tree.predict(X_test)

print("Predictions:", predictions)
