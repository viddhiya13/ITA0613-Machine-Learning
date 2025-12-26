from sklearn.datasets import fetch_california_housing
from sklearn.linear_model import LinearRegression

X, y = fetch_california_housing(return_X_y=True)
model = LinearRegression()
model.fit(X, y)

print("House Price:", model.predict([X[0]]))
