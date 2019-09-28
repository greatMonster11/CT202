from sklearn.model_selection import KFold
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.navie_bayes import MultinamialNB
from sklearn.navie_bayes import GaussianNB
from sklearn import datasets
iris = datasets.load_iris()
X = iris.data
Y = iris.target


# Phan chia du lieu thanh tap test va train
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=0)
# Xay dung mo hinh dua tren phan phoi xac suat tuan theo Gaussian
model = GaussianNB()
model.fit(X_train, y_train)
print(model)
# predict
thucte = y_test
dubao = model.predict(X_test)
thucte
dubao

# Danh gia giai thuat
cnf_matrix_gnb = confusion_matrix(thucte, dubao)
print(cnf_matrix_gnb)
[[16, 0, 0]
 [0, 18, 0]
 [0, 0, 11]]

# Su dung hold-out de phan chia du lieu voi hanm Kfold
kf = KFold(n_splits=15)

for train_index, test_index in kf.split(X):
    # print("TRAIN: ", train_index, "TEST: ", test_index)
    X_train, X_test = X.iloc[train_index, ], X.iloc[test_index, ]
    y_train, y_test = y.iloc[train_index, ], y.iloc[test_index, ]
    # print("X_train", "X_test") # In thuoc tinh cua du lieu can kiem tra
    print("+++++++++++")
