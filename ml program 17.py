import pandas as pd
from sklearn.ensemble import RandomForestClassifier

data = pd.read_csv("mobile_price.csv")

X = data.drop("price_range", axis=1)
y = data["price_range"]

model = RandomForestClassifier(random_state=42)
model.fit(X, y)

print("Accuracy:", model.score(X, y))
