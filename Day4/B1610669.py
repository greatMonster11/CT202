###########  Bai 1  ##############
import sklearn
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

# read data from csv file
dt = pd.read_csv("Housing_2019.csv", index_col=0)
X = dt.iloc[:, [1, 2, 4, 10]]
Y = dt.price

# using hold-out
X_train, X_test, y_train, y_test = train_test_split(
    X, Y, test_size=1/3.0, random_state=123)

# train model
model = linear_model.LinearRegression()
model.fit(X_train, y_train)

# predict
y_pred = model.predict(X_test)


# The coefficients
print('Coefficients: \n', model.coef_)
# MSE and RMSE
err = mean_squared_error(y_test, y_pred)
err
rmse_err = np.sqrt(err)
round(rmse_err, 3)


############# Bai 2 #################

X = np.arra([1, 2, 4]).T
Y = np.array([2, 3, 6]).T

plt.axis([0, 5, 0, 8])  # Dinh hinh chieu cao va chieu rong cho bieu do
plt.plot(X, Y, "ro", color="blue")  # "ro" hinh la cua diem(tron)
plt.xlabel("Gia tri thuoc tinh X")
plt.ylabel("Gia tri du doan Y")
plt.show()

# define a function that gonna calulate the linear gradient


def LR2(X, Y, eta, lanlap, theta0, theta1):
    m = len(Y)
    theta00 = theta0
    theta11 = theta1
    for i in range(0, lanlap):
        print("Lan lap: ", i)
        for j in range(0, m):
            # theta0
            h = theta0 + theta11*X[j]
            theta0 = theta0 + eta*(Y[j] - h)*1
            print("Phan tu ", j, "y= ", Y[j],
                  "h= ", h, "gia tri theta0= ", theta0)

            # theta1
            h = theta00 + theta1*X[j]
            theta1 = theta1 + eta*(Y[j] - h)*X[j]
            print("Pha tu: ", j, "gia tri theta1 = ", theta1)
            theta00 = theta0
            theta11 = theta1
        print("theta00 = ", theta00)
        print("theta11 = ", theta11)
    return [theta0, theta1]


theta = LR2(X, Y, 0.2, 1, 0, 1)  # theta 1 buoc
X1 = np.array([1, 6])
Y1 = theta[0] + theta[1]*X1

theta2 = LR2(X, Y, 0.2, 2, 0, 1)  # theta 2 buoc lap
X2 = np.array([1, 6])
Y2 = theta2[0] + theta2[1]*X2

### Ve duong hoi quy ###
plt.axis([0, 7, 0, 10])  # dinh khung cho bieu do
plt.plot(X, Y, "ro", color="blue")

plt.plot(X1, Y1, color="violet")
plt.plot(X2, Y2, color="green")

plt.xlabel("Gia tri thuoc tinh X")
plt.ylabel("Gia tri thuoc tinh Y")
plt.show()

#### Du bao cho phan tu moi toi ####
XX = [0, 3, 5]
for i int range(0, 3):
    YY = theta[0] + theta[1]*XX[i]
    print(round(YY, 3))
