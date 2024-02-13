import numpy as np

x1 = np.empty([4,3], dtype=int)
x2 = np.array(range(30))
x3 = np.arange(30) # 与x2相同
x4 = np.zeros([4,3], dtype=np.int8)
x5 = np.ones([4,4], dtype=float)

print(x1)
print(x2)
print(x3)
print(x4)
print(x5)
dt = np.dtype([('age',np.int8)])
print(dt)