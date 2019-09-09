# Lay file iris truc tiep tu sklearn
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
iris_dt = load_iris()
iris_dt.data[1:5]  # thuoc tinh tap cua iris_dt
iris_dt.target[1:5]  # gia tri cua nhan / class

X_train, X_test, y_train, y_test = train_test_split(
    iris_dt.data, iris_dt.target, test_size=1/3.0, random_state=123)

X_train[1:6]
X_train[1:6, 1:3]
y_train[1:6]
X_test[6:10]
y_test[6:10]

# Xay dung mo hinh cay quyet dinh du tren chi so Gini
clf_gini = DecisionTreeClassifier(
    criterion="entropy", random_state=100, max_depth=5, min_samples_leaf=None)
clf_gini.fit(X_train, y_train)

# du doan
y_pred = clf_gini.predict(X_test)
y_test
clf_gini.predict([[4, 4, 3, 3]])

# tinh do chinh xac
print("Accuracy is", accuracy_score(y_test, y_pred)*100)

confusion_matrix(y_test, y_pred, labels=[2, 0, 1])
