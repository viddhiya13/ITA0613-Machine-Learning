from sklearn.mixture import GaussianMixture
from sklearn.datasets import load_iris

X, _ = load_iris(return_X_y=True)
gmm = GaussianMixture(n_components=3)
gmm.fit(X)

print("Cluster Labels:", gmm.predict(X)[:10])
