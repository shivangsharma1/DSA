from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt

# Load the iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Train a decision tree classifier
clf = DecisionTreeClassifier(random_state=42)
clf.fit(X, y)

# Visualize the original decision tree
plt.figure(figsize=(10, 6))
plot_tree(clf, filled=True, rounded=True, class_names=iris.target_names)
plt.show()

# Cost complexity pruning
path = clf.cost_complexity_pruning_path(X, y)
ccp_alphas, impurities = path.ccp_alphas, path.impurities

# Train decision trees with different values of ccp_alpha
clfs = []
for ccp_alpha in ccp_alphas:
    clf = DecisionTreeClassifier(random_state=42, ccp_alpha=ccp_alpha)
    clf.fit(X, y)
    clfs.append(clf)

# Remove the last classifier (fully grown tree)
clfs = clfs[:-1]
ccp_alphas = ccp_alphas[:-1]

# Visualize the pruned decision trees
plt.figure(figsize=(20, 10))
for i, clf in enumerate(clfs):
    plt.subplot(2, len(clfs)//2, i+1)
    plot_tree(clf, filled=True, rounded=True, class_names=iris.target_names)
    plt.title("Decision Tree with ccp_alpha={:.3f}".format(ccp_alphas[i]))
plt.show()
