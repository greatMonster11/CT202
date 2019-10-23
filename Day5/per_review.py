import numpy as np
import matplotlib.pyplot as plt

X = np.array([[0,0,1,1], [0,1,0,1]])
Y = np.array([0,0,0,1])
X
X = X.T # chuyen doi hang thanh cot

colormap = np.array(['red', 'green'])
plt.axis([0,1.2,0,1.2])
plt.scatter(X[:,0], X[:,1], c=colormap[Y], s=150)
plt.xlabel("Gia tri cua X1")
plt.ylabel("Gia tri cua X2")
plt.show()

# Install resolver
import random
import numpy as np

def my_perceptron(X, y, eta, lanlap):
    n = len(X[0,])
    m = len(X[:,0])
    print("m = ", m, "& n= ", n)
    # w0 = random.random() # khoi tao ngau nhien w0
    w = np.random.random(n) # khoi tao ngau nhien cac gia tri w
    w0 = -0.2 # Kiem tra ket qua
    w = (0.5, 0.5) # Kiem tra ket qua
    for t in range(0, lanlap):
        print("Lan lap ____", t)
        for i in range(0, m):
            gx = w0 + sum(X[i]*w)
            print("gx= ", gx)
            if (gx > 0):
                output = 1
            else:
                output = 0
            w0 = w0 + eta*(y[i] - output)
            w = w + eta*(y[i]-output)*X[i,]
            print("w0 = ", w0)
            print("w= ", w)
    return (w0, w)

my_perceptron(X,Y,0.15,2)
