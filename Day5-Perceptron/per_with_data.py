import pandas as pd
from sklearn.linear_model import Perceptron
from sklearn.model_selection import train_test_split

# Read data 
dt = pd.read_csv("data_per.csv")
dt

X_train, X_test, y_train, y_test = train_test_split(dt.iloc[:,0:5], dt.iloc[:,5], test_size=1/3.0, random_state=100)

# Create model and train
net = Perceptron()
net.fit(X_train, y_train)
print(net)

# Predict model
y_pred = net.predict(X_test)
from sklearn.metrics import accuracy_score
accuracy_score(y_test, y_pred) # 0.3
