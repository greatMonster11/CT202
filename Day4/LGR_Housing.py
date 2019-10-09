import pandas as pd
import matplotlib.pyplot as plt

# read data
dt = pd.read_csv("Housing_2019.csv", index_col=0)
dt.iloc[2:4, 4]
X = dt.iloc[:, [1,2,3,4,10]]
X.iloc[1:5,]
Y = dt.price

plt.scatter(dt.lotsize, dt.price)
plt.show()

# train model
import sklearn
from sklearn import linear_model
lm = linear_model.LinearRegreesion()
lm.fit(X[0:520], Y[0:520])

print lm.intercept_
print lm.coef_

# predict for last 20 elements in data set
y = dt.price
y_test = y[-20:]
X_test = X[-20:]
y_pred = lm.predict(X_test)

# compare with real data and prediction data
y_pred
y_test

from sklearn.metrics import mean_squared_error
err = mean_squared_error(y_test, y_pred)
err
rmse_err = np.sqrt(err)
round(rmse_err, 3)
