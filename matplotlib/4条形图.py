from matplotlib import pyplot as plt

x = ['DNA', 'RNA', 'Protein', 'Sugar', 'Oxygen']
x_2 = [i+0.3 for i in range(5)]
y = [55, 25, 65, 16, 5]
y_2 = [66, 34, 64, 12, 2]
colors=["#4CAF50","red","hotpink","#556B2F"]
colors2 = ['#bfa', 'hotpink', '#4CAF50', 'green']

plt.bar(x, y, width=0.3, align='center', color=colors)
# 想在一个图展示多个数据，需要对x轴进行变换
plt.bar(x_2,y_2, width=0.3, align='center', color=colors2)

plt.xlabel('elements')
plt.ylabel('presents')
plt.title('elements various after HIV infection in 48h')
plt.grid(alpha=0.3, linestyle='-.', axis='y')

# plt.legend(loc='upper left')

plt.show()