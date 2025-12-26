import pandas as pd
from sklearn.linear_model import LinearRegression

data = pd.read_csv("car_data.csv")

X = data[['year', 'km_driven']]
y = data['price']

model = LinearRegression()
model.fit(X, y)

print("Predicted Price:", model.predict([[2020, 20000]]))
