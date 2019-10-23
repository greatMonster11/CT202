import pandas as pd

# Read data
data = pd.read_csv("housing_RT.csv", index_col=0)
data.iloc[1:5,]

#Using hold-out to percific data trained
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(data.iloc[:,1:5], data.iloc[:,0],
test_size = 1/3.0, random_state=100)
X_train[1:5]
X_test[1:5]

# Building model for training
from sklearn.tree import DecisionTreeRegressor
regressor = DecisionTreeRegressor(random_state = 0)
regressor.fit(X_train, y_train)

# Predict and judge the model
y_pred = regressor.predict(X_test)
y_test[1:5]
y_pred[1:5]

# Chi so MSE
from sklearn.metrics import mean_squared_error
err = mean_squared_error(y_test, y_pred)
err

# Chi so RMSE
