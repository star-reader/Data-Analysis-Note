import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
colors = ["#d5695d", "#5d8ca8", "#65a479", "#a564c9"]

plt.pie(y,labels=['A','B','C','D'],colors=colors, labeldistance=0.7)
plt.title("Pie chart")
plt.show()