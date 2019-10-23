from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
import pandas as pd

# Read data
wineWhite = pd.read_csv("winequality-white.csv", delimiter=";", quotechar='"')
X = wineWhite.iloc[:, 0:11]
y = wineWhite.iloc[:, 11:12]

from sklearn.model_selection import KFold
# Use KFold to split data
# Devide data into 100 parts and make a shuffle on data
kf = KFold(n_splits=100, shuffle=True)

from sklearn.naive_bayes import GaussianNB
model = GaussianNB()

loop_counter = 1
sum_accuracy = 0

# Phan chia du lieu 
for train_index, test_index in kf.split(wineWhite):
	#print("TRAIN:", train_index, "TEST:", test_index)
    X_train, X_test = X.iloc[train_index, ], X.iloc[test_index, ]
    y_train, y_test = y.iloc[train_index], y.iloc[test_index]

    # train model        
    model.fit(X_train, y_train)

    # prediction
    y_pred = model.predict(X_test)
    last_result_Matrix = confusion_matrix(y_test, y_pred)
    loop_counter += 1

    # Cau 4
    # do chinh xac cua tung lan lap
    # print("Do chinh xac cua lan lap thu", loop_counter, "la: ", accuracy_score(y_test, y_pred)*100)
    # Do chinh xac cua lan lap thu 100 la:  43.75

    # do chinh xac tong the cua cac lan lap
    sum_accuracy += accuracy_score(y_test, y_pred)

# Cau 5
print("Do chinh xac trung binh tong the la", sum_accuracy / loop_counter)
# Do chinh xac trung binh tong the la 0.4424883814912101

# Cau 6
# Do chinh xac cua navie-bayes thap hon decision-tree

