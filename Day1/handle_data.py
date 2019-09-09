import matplotlib.pyplot as plt
import scipy as sp

# Doc du lieu tu file web_traffic.tsv vao bien data
data = sp.genfromtxt("web_traffic.tsv", delimiter="\t")

# print shape
print(data.shape)

# lay du lieu cot thu nhat gan cho bien x
x = data[:, 0]

# lay du lieu cot thu hai gan cho bien y
y = data[:, 1]

# dem so hang khong co du lieu trong cot y
print(sp.isnan(y))

# loai bo cac dong khong co du lieu trong ca 2 cot
x = x[~sp.isnan(y)]
y = y[~sp.isnan(y)]


plt.scatter(x, y)
plt.title("Web tracfic over last month")
plt.xlabel("Time")
plt.ylabel("Hits/hour")
plt.xticks([w*7*24 for w in range(10)],
           ['week %i' % w for w in range(10)])
plt.autoscale(tight=True)
plt.grid()
plt.show()
