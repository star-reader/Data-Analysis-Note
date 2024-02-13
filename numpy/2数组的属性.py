import numpy as np

a = np.arange(24)
a = a.reshape([2,4,3])  # 2个大的元素（或者说块），每个大元素包含4行和3列
print(a)
# 矩阵的秩
print(a.ndim)

# 矩阵形状
print(a.shape)

# 矩阵大小
print(a.size)

# 每个元素的大小
print(a.itemsize)

# 内存信息
print(a.flags)