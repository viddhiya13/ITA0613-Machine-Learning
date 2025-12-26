import pandas as pd
from sklearn.ensemble import RandomForestClassifier

data = pd.read_csv("credit_data.csv")   # income, age, loan, score
X = data.drop("score", axis=1)
y = data["score"]

model = RandomForestClassifier(random_state=42)
model.fit(X, y)

print("Accuracy:", model.score(X, y))
