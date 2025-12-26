from sklearn.naive_bayes import GaussianNB
from sklearn.datasets import load_iris

X, y = load_iris(return_X_y=True)
model = GaussianNB()
model.fit(X, y)

print(model.predict([[6.3,3.3,6.0,2.5]]))
