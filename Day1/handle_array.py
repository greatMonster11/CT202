import numpy as np

a=np.array([0,1,2,3,4,5])

print(a)

#Hien thi so chieu cua a o dang ma tran
print(a.ndim)

print(a.shape)

#Hien thi phan tu lon hon 3
print(a[a>3])

#Thay doi gia tri
a[a>3] = 10

b=a.reshape((3,2))

print(b)

print(b[2][1])

c=b*2

print(c)
