import matplotlib.pyplot as plt
import scipy as sp

data = sp.genfromtxt("baitap1.csv", delimiter=",")
print(data)

data[:, 2:3]  # Hien thi du lieu cot so 3
data[4:10]  # Hien thi du lieu tu dong 5 den 10
data[4:5, 0:2]  # Hien thi du lieu cot 1,2 dong 5

for x in range(50):
    if x % 2 == 0:
        print(x)

x = data[:, 1:2]  # du lieu cot 2
y = data[:, 2:3]  # du lieu cot 3


plt.scatter(x, y)
plt.show()
