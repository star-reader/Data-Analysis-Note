import numpy as np

a = np.arange(20).reshape([4,5])

for i in np.nditer(a):
    print(i)

for i in np.nditer(a.T, order='C'):
    print(i)

for i in np.nditer(a, order='F', op_flags=['readwrite']):
    i[...] = i*2
print(a)
