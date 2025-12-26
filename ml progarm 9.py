import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

X = np.array([[1],[2],[3],[4],[5]])
y = np.array([1,4,9,16,25])

poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)

lin = LinearRegression()
lin.fit(X, y)

poly_reg = LinearRegression()
poly_reg.fit(X_poly, y)

print("Linear Prediction for 6:", lin.predict([[6]]))
print("Polynomial Prediction for 6:", poly_reg.predict(poly.transform([[6]])))
