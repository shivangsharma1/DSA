import numpy as np
np.random.seed(1)
class KMeans:
    def __init__(self, n_clusters=2, n_iterations=10):
        self.n_cluster = n_clusters
        self.n_iterations = n_iterations

    def fit(self, X):
        n_samples, n_cols = X.shape
        choice = np.random.choice(n_samples, self.n_cluster, replace=False)
        print(choice)
        print("type of choice", type(choice))
        self.centroid = X[choice]
        for _ in range(self.n_iterations):
            labels = self._assign_label(X)
            old_centroid = self.centroid
            self._update_centroids(X, labels)
            if np.allclose(self.centroid, old_centroid):
                break
        return labels

    def _assign_label(self, X):
        labels = []
        for sample in X:
            label = [np.linalg.norm(sample - centroid) for centroid in self.centroid]
            out = np.argmin(label)
            labels.append(out)
        return np.array(labels)

    def _update_centroids(self, X, labels):
        for i in range(self.n_cluster):
            sample = X[labels==i]
            if len(sample)>0:
                self.centroid[i] = np.mean(sample)


if __name__ == '__main__':
    X = np.array([[1, 2], [1, 3], [2, 2], [5, 6], [6, 5], [7, 6], [10, 11]])

    model = KMeans()
    labels = model.fit(X)
    print("Centroids: ", model.centroid)
    print("labels: ",labels)
