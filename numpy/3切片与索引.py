import numpy as np

# 使用slice内置函数
a = np.arange(10)
s = slice(1,5,2)
print(a[s])

# 冒号
b = a[1:5:2]
print(b)
print(b.ndim)

# 多维数组
c = np.arange(24)
c = c.reshape([4,2,3])  #多维数组
print(c)
d = c[1:3]
print(d)
print('=====')
# numpy高级索引
e = c[[0,1,2],  [0,0,1]]
print (e)
print('=========')
import numpy as np

x = np.arange(9)
print(x)
# 一维数组读取指定下标对应的元素
print("-------读取下标对应的元素-------")
x2 = x[[0, 6]] # 使用花式索引
print(x2)

print(x2[0])
print(x2[1])