import pandas as pd
data = pd.read_csv("play_tennis.csv", delimiter=",")
data.head(5)
data.tail(5)
data.ix[3:7] # hang thu 4 den 8
data.ix[:,0:1] # cot dau tien
data.ix[:,0:5] #tu cot dau tien den cot thu 5
data.ix[:,2:3] # cot thu 3
data.ix[3:4,2:3] # gia tri hang 4-5, cot 3
data.outlook # gia tri cot outlook
len(data)

###############################
from sklearn.datasets import load_iris
iris_dt = load_iris()
iris_dt.data[1:5]
iris_dt.target[1:6]
