from matplotlib import pyplot as plt
from random import randint

x = range(0,24,2)
y = [randint(15,26) for _ in range(12)]
z = [randint(15,26) for _ in range(12)]

# figure设置大小
fig = plt.figure(figsize=(15,8), dpi=80)

plt.plot(x,y, label='data 1', linestyle='--', marker='o', color='c', linewidth=1.4)
plt.plot(x,z, label='data 2', linestyle='--', marker='*', color='m', linewidth=1.4)
# plt.savefig保存图片
# 修改x/y的刻度值
plt.xticks(x)
y_ticks_label = [i for i in range(15,27)]
plt.yticks(y_ticks_label)
# 修改x/y的显示文字
plt.xlabel('time')
plt.ylabel('data')
plt.title('chart')
# 绘制网格
plt.grid(axis='y', linestyle='-.', color='r', linewidth=0.4)

# 添加图例
plt.legend(loc='upper left')

plt.show()