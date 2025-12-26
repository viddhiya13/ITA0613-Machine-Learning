from sklearn.neural_network import MLPClassifier
from sklearn.datasets import load_iris

X, y = load_iris(return_X_y=True)
model = MLPClassifier(hidden_layer_sizes=(10,), max_iter=1000)
model.fit(X, y)

print("Accuracy:", model.score(X, y))
