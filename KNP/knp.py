from scipy.spatial.distance import cdist
import numpy as np
import seaborn; seaborn.set()
import matplotlib.pyplot as plt

rand = np.random.RandomState(42)
X = rand.rand(10, 2)

plt.scatter(X[:, 0], X[:, 1], s=100)

dist_sq = np.sum((X[:,np.newaxis, :] - X[np.newaxis,:,:]) ** 2, axis=-1)
dist_sq.diagonal()

nearest = np.argsort(dist_sq, axis=1)
print(nearest)

K = 1
nearest_partition = np.argpartition(dist_sq, K+1, axis=1)
plt.scatter(X[:, 0], X[:, 1], s=100)

for i in range(X.shape[0]):
    for j in nearest_partition[i, :K+1]:
        plt.plot(*zip(X[j], X[i]), color='black')

plt.show()