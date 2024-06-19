import numpy as np

class KMeans:
    def __init__(self, n_clusters, max_iter=300):
        self.n_clusters = n_clusters
        self.max_iter = max_iter

    def fit(self, X):
        self.centroids = X[np.random.choice(X.shape[0], self.n_clusters, replace=False)]
        
        for _ in range(self.max_iter):
            # Assign each data point to the nearest centroid
            labels = self._assign_clusters(X)

            # Update centroids based on the mean of the data points assigned to each cluster
            new_centroids = self._update_centroids(X, labels)

            # Check for convergence
            if np.allclose(self.centroids, new_centroids):
                break

            self.centroids = new_centroids

    def _assign_clusters(self, X):
        distances = np.sqrt(((X - self.centroids[:, np.newaxis])**2).sum(axis=2))
        return np.argmin(distances, axis=0)

    def _update_centroids(self, X, labels):
        new_centroids = np.zeros_like(self.centroids)
        for i in range(self.n_clusters):
            if np.sum(labels == i) > 0:
                new_centroids[i] = np.mean(X[labels == i], axis=0)
            else:
                new_centroids[i] = self.centroids[i]
        return new_centroids

# Example usage:
X = np.array([[1, 2], [1.5, 1.8], [5, 8], [8, 8], [1, 0.6], [9, 11]])

kmeans = KMeans(n_clusters=2)
kmeans.fit(X)

print("Cluster centroids:")
print(kmeans.centroids)

# Predict clusters for new data points
new_data = np.array([[0, 0], [10, 10]])
predictions = kmeans._assign_clusters(new_data)
print("Predictions for new data points:")
print(predictions)
