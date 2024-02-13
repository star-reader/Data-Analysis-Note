import numpy as np

a = np.array([0,30,45,60,90])
# 通过乘 pi/180 转化为弧度
print (np.sin(a*np.pi/180))
print (np.cos(a*np.pi/180))
print (np.tan(a*np.pi/180))

b = np.array([[3,7,5],[8,4,3],[2,4,9]])
print(np.amin(b))
print(np.amax(b))
print(np.ptp(b))
print(np.ptp(b,axis=1))
print(np.mean(b))