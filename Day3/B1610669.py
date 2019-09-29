from sklearn.model_selection import KFold
import pandas as pd

wineWhite = pd.read_csv("winequality-white.csv", delimiter=";", quotechar='"')

# Use KFold to split data
# Devide data into 100 parts and make a shuffle on data
kf = KFold(n_splits=100, shuffle=True)

X = wineWhite.iloc[:, 0:11]
y = wineWhite.iloc[:, 11:12]

# SPecific kind of data
for train_index, test_index in kf.split(wineWhite):
	print("TRAIN:", train_index, "TEST:", test_index)
 	X_train, X_test = X.iloc[train_index, ], X.iloc[test_index, ]
    y_train, y_test = y.iloc[train_index], y.iloc[test_index]

# Create and train model
from sklearn.naive_bayes import GaussianNB

model = GaussianNB()
model.fit(X_train, y_train)
print(model)

# Predict
reality = y_test
prediction = model.predict(X_test)
reality
prediction


