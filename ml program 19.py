import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import LabelEncoder

data = pd.read_csv("bank_loan.csv")

le = LabelEncoder()
data['loan'] = le.fit_transform(data['loan'])

X = data.drop("loan", axis=1)
y = data["loan"]

model = GaussianNB()
model.fit(X, y)

print("Accuracy:", model.score(X, y))

sample = pd.DataFrame([[30, 40000, 690]],
                      columns=["age", "income", "credit_score"])

prediction = model.predict(sample)
print("Loan Approved:", "Yes" if prediction[0] == 1 else "No")
