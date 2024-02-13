from matplotlib import pyplot as plt
import numpy as np

data = np.random.randn(10000) #正态分布

plt.hist(data, bins=80, color='skyblue', alpha=0.8)

plt.show()

