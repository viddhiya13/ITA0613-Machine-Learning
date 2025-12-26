from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_iris

X, y = load_iris(return_X_y=True)
model = KNeighborsClassifier(n_neighbors=5)
model.fit(X, y)

print(model.predict([[5.9,3.0,5.1,1.8]]))
