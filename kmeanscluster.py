import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Data
X = np.array([
    [25,500],   #C1
    [30,700],   #C2
    [22,300],   #C3
    [35,1000],  #C4
    [40,1200],  #C5
    [20,200]    #C6
])

# Apply KMeans
kmeans = KMeans(n_clusters=2, random_state=0)
kmeans.fit(X)

# Output
print("Centroids: ", kmeans.cluster_centers_)
print("Labels: ", kmeans.labels_)

# Visualization
plt.scatter(X[:, 0], X[:, 1], c=kmeans.labels_, cmap='viridis', s=100)
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], 
            color='red', marker='X', s=200, label='Centroids')

plt.xlabel("Age")
plt.ylabel("Amount")
plt.title("K-Means Clustering")
plt.legend()
plt.grid(True)
plt.show()
