from sklearn.model_selection import KFold
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix
import pandas as pd

# Read data
wineWhite = pd.read_csv("winequality-white.csv", delimiter=";", quotechar='"')

# Use KFold to split data
# Devide data into 100 parts and make a shuffle on data
kf = KFold(n_splits=100, shuffle=True)

X = wineWhite.iloc[:, 0:11]
y = wineWhite.iloc[:, 11:12]

model = GaussianNB()
# Phan chia du lieu
for train_index, test_index in kf.split(wineWhite):
	print("TRAIN:", train_index, "TEST:", test_index)
 	X_train, X_test = X.iloc[train_index, ], X.iloc[test_index, ]
    y_train, y_test = y.iloc[train_index], y.iloc[test_index]
    # huan luyen mo hinh
	model.fit(X_train, y_train)
	# du doan
	prediction = model.predict(X_test)
	last_result_Matrix = confusion_matrix(y_test, )

# Xay dung va huan luyen mo hinh


# Du bao
reality = y_test
prediction = model.predict(X_test)
reality
prediction

# Danh gia giai thuat
cnf_matrix_gnb = confusion_matrix(reality, prediction)
cnf_matrix_gnb
### Result
array([[ 1,  0,  0,  1,  0],
       [ 2,  8,  3,  0,  0],
       [ 0,  8,  5, 10,  0],
       [ 0,  0,  1,  5,  0],
       [ 1,  1,  1,  1,  0]])

# Cau 4
