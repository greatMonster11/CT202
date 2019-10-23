import pandas as pd
dt5 = pd.read_csv("iris_data.csv", delimiter=",")
dt5[1:5]
len(dt5)
dt5.petalLength[1:5]
