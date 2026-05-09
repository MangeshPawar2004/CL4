import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# -----------------------------
# 1. Dataset
# -----------------------------
X = np.array([
    [1, 2],
    [1, 4],
    [1, 0],
    [10, 2],
    [10, 4],
    [10, 0]
])

print("Input Data:")
print(X)

# -----------------------------
# 2. Apply K-Means
# -----------------------------
kmeans = KMeans(n_clusters=2, random_state=42, n_init=10)
kmeans.fit(X)

labels = kmeans.labels_
centroids = kmeans.cluster_centers_

print("\nCluster Labels:")
print(labels)

print("\nCentroids:")
print(centroids)

# -----------------------------
# 3. Visualize clusters
# -----------------------------
plt.figure(figsize=(7, 5))

plt.scatter(X[:, 0], X[:, 1], c=labels, s=100, cmap='viridis', label='Data Points')
plt.scatter(
    centroids[:, 0],
    centroids[:, 1],
    c='red',
    s=200,
    marker='X',
    label='Centroids'
)

for i, point in enumerate(X):
    plt.text(point[0] + 0.1, point[1] + 0.1, f"P{i+1}")

plt.title("K-Means Clustering")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()