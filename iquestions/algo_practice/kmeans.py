import numpy as np

class KMeans:
    def __init__(self, n_cluster=2, n_iteration=100):
        self.n_cluster = n_cluster
        self.n_iteration = n_iteration

    def fit(self, X):
        n_samples, n_features = X.shape
        choice = np.random.choice(n_samples, self.n_cluster, replace=False)
        self.centroid = X[choice]

        for _ in range(self.n_iteration):
            label = self._assign_labels(X)

            old_centroids = self.centroid.copy()
            self.update_centroid(X, label)

            if np.allclose(self.centroid, old_centroids):
                break

            return label
        
    def _assign_labels(self, X):
        labels = []
        for sample in X:
            distance = [np.linalg.norm(sample - centroid) for centroid in self.centroid]
            print("Sample", sample)
            print("Sample", distance)
            cluster = np.argmin(distance)
            print("cluster", cluster)
            labels.append(cluster)

        return np.array(labels)
    
    def update_centroid(self, X, label):
        for i in range(self.n_cluster):
            sub_data = X[label==i]
            if len(sub_data)>1:
                self.centroid[i] = np.mean(sub_data)




if __name__ == '__main__':

    X = np.array([[1, 2], [1, 3], [2, 2], [5, 6], [6, 5], [7, 6], [10, 11]])

    #initialize the model
    model = KMeans(n_cluster = 2)
    labels = model.fit(X)
    print("Centroids: ", model.centroid)
    print("labels: ",labels)