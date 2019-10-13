###########  Bai 1  ##############
import sklearn
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
