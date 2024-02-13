import numpy as np

a = np.arange(24).reshape([2,3,4])
for i in a.flat:
    print(i, end=',')

b = a.flatten(order='C')

print(a.T)
print(a.shape)
print(a.T.shape)
print('======')
c = np.array([[1], [2], [3]])
d = np.array([4, 5, 6])
e = np.broadcast(c,d)
print(e.shape) # (3,3)
r, c = e.iters
print (next(r), next(c))
print (next(r), next(c))
print ('\n')


y = np.expand_dims(c, axis = 1)
print(y)