import pandas as pd
from sklearn.linear_model import LinearRegression

# Load data
data = pd.read_csv("sales.csv")

X = data[['month']]
y = data['sales']

# Train model
model = LinearRegression()
model.fit(X, y)

# Predict future sales (month 13)
future_data = pd.DataFrame({'month': [13]})
prediction = model.predict(future_data)

print("Future Sales:", prediction)
