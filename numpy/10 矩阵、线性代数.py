import numpy as np

a = np.arange(12).reshape(4,3)
print (a)
print (a.T)

print (np.eye(n =  2, M =  5,k = 0, dtype =  int))
print (np.inner(np.array([1,2,3]),np.array([0,1,0])))

a = np.arange(8).reshape(2,2,2)
b = np.arange(4).reshape(2,2)
print (np.matmul(a,b))

x = np.array([[1,2],[3,4]])
y = np.linalg.inv(x)
print (np.dot(x,y))