from sklearn import datasets
iris = datasets.load_iris()
X = iris.data
Y = iris.target

from sklearn.navie_bayes import GaussianNB
from sklearn.navie_bayes import MultinamialNB

# Phan chia du lieu thanh tap test va train
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
# Xay dung mo hinh dua tren phan phoi xac suat tuan theo Gaussian
model = GaussianNB()
model.fit(X_train, y_train)
print(model)
# predict
thucte = y_test
dubao= model.predict(X_test)
thucte
dubao

# Danh gia giai thuat
from sklearn.metrics import confusion_matrix
cnf_matrix_gnb = confusion_matrix(thucte, dubao)
print(cnf_matrix_gnb)
[[16 0  0]
[0 18 0]
[0 0 11]]
