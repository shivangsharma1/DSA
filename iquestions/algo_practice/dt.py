import numpy as np

class Node:
    def __init__(self, feature=None, threshold=None, left=None, right=None, value=None):
        self.feature = feature
        self.threshold = threshold
        self.left=left
        self.right = right
        self.value=value

    def ischild_node(self):
        return self.value is not None
        
class DecisionTree:
    def __init__(self, max_depth=5, min_samples_split=5, n_features=None):
        self.max_depth = max_depth
        self.min_samples_split = min_samples_split
        self.n_features = n_features
        self.root = None

    def fit(self, X, y):
        self.n_features = X.shape[1] if self.n_features is None else min(self.n_features, X.shape[1])
        self.root_node = self._grow_tree(X, y, depth = 0)

    def _leaf_value(self, y):
        value = np.argmax(np.bincount(y))
        return value
    
    def _split(self, X_column, thr):
        left_idx = np.argwhere(X_column<=thr).flatten()
        right_idx = np.argwhere(X_column>thr).flatten()

        return left_idx, right_idx
    
    def _entropy(self, y):
        l = len(y)
        c = np.bincount(y)
        probs = c/l
        return -np.sum([prob * np.log(prob) for prob in probs])
    
    def _information_gain(self, X, y, thr):
        parent_entropy = self._entropy(y)

        left_idx, right_idx = self._split(X, thr)
        n = len(y)
        l_w = len(left_idx)/n
        r_w = len(right_idx)/n
        e_l, e_r = self._entropy(y[left_idx]), self._entropy(y[right_idx])

        child_entropy = ((l_w * e_l) + (r_w * e_r))
        info_gain = parent_entropy - child_entropy

        return info_gain



    def _best_split(self, X, y, feat_idxs):
        best_threshold, best_feature = None, None
        best_gain = -1
        
        for feat in feat_idxs:
            X_column = X[:, feat]
            thresholds = np.unique(X_column)

            for thr in thresholds:
                gain = self._information_gain(X_column, y, thr)

                if gain > best_gain:
                    best_gain = gain
                    best_feature = feat
                    best_threshold = thr


        return best_threshold, best_feature


    def _grow_tree(self, X, y, depth=0):
        n_samples, n_features = X.shape
        labels = np.unique(y)

        #stopping criteria
        if depth>=self.max_depth or n_samples <= self.min_samples_split or len(labels) == 1:
            value = self._leaf_value(y)
            return Node(value=value)


        #finding the best split
        feat_idxs = np.random.choice(n_features, self.n_features, replace=False)
        best_thresh, best_feature = self._best_split(X, y, feat_idxs)

        #creating child nodes
        left_idx, right_idx = self._split(X[:,best_feature], best_thresh)
        left_child = self._grow_tree(X[left_idx, :], y[left_idx], depth+1)
        right_child = self._grow_tree(X[right_idx, :], y[right_idx], depth+1)
        

        #finally returning the root node
        return Node(best_feature, best_thresh, left_child, right_child)

    def predict(self, X):
        prediction  = [self._predict(x, self.root_node) for x in X]
        return prediction

    def _predict(self, x, node):

        if node.is_leaf_node():
            return node.value

        if x[node.feature] <= node.threshold:
            return self._predict(x, node.left)
        else:
            return self._predict(x, node.right)
