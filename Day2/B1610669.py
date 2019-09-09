########################### Bai 1 #####################
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
df = pd.read_csv("winequality-white.csv", delimiter=";", quotechar='"')

len(df)  # so luong phan tu
df.columns  # so nhan
df['quality'].unique()

data = df.iloc[:, 0:11]
target = df.iloc[:, 11:12]

X_train, X_test, y_train, y_test = train_test_split(
    data, target, test_size=0.2, random_state=123)

clf_entropy = DecisionTreeClassifier(
    criterion="entropy", random_state=100, max_depth=3, min_samples_leaf=5)
clf_entropy.fit(X_train, y_train)
clf_entropy

# du doan
y_pred = clf_entropy.predict(X_test)
y_test

# tinh do chinh xac
print("Accuracy is", accuracy_score(y_test, y_pred)*100)


print("Accuracy is", accuracy_score(y_test[0:6], y_pred[0:6])*100)

########################### Bai 2 #####################
X = [[180, 15, 0],
     [167, 42, 1],
     [136, 35, 1],
     [174, 15, 0],
     [141, 28, 1]]
Y = ['Nam', 'Nu', 'Nu', 'Nam', 'Nu']

clf_entropy = DecisionTreeClassifier(criterion="entropy")
clf_entropy.fit(X, Y)
clf_entropy

# du doan
clf_entropy.predict([[135, 39, 1]])
