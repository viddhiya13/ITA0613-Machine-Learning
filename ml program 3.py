from sklearn.tree import DecisionTreeClassifier
from sklearn import datasets, tree

iris = datasets.load_iris()
X, y = iris.data, iris.target

model = DecisionTreeClassifier(criterion='entropy')
model.fit(X, y)

sample = [[5.1, 3.5, 1.4, 0.2]]
print("Predicted Class:", model.predict(sample))
