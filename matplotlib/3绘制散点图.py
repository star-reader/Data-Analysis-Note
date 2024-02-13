from matplotlib import pyplot as plt
from random import randint

x = [randint(0, 30) for _ in range(40)]
y = [randint(4, 26) for _ in range(40)]
colors = range(40)
sizes = [randint(16, 360) for _ in range(40)]

plt.figure(figsize=(15,8), dpi=80)

plt.scatter(x, y, c=colors,s=sizes, cmap='rainbow')

# 配置与plot均一样
plt.xlabel('x factor')
plt.ylabel('y factor')
plt.xticks(range(41))
plt.yticks(range(28))
plt.grid(linewidth=0.35, linestyle='-.')

# 显示颜色条
plt.colorbar()

plt.show()