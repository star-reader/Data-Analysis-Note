import pandas as pd

a = pd.Series([1,2,3], ['a','b','c'])
print(a)

#也可以使用key-value格式
b = {1:'a', 2:'b', 3:'c'}
c = pd.Series(b)
print(b)

print(b[1])

data = [['Google', 10], ['Runoob', 12], ['Wiki', 13]]

# 创建DataFrame
df = pd.DataFrame(data, columns=['Site', 'Age'])

# 使用astype方法设置每列的数据类型
df['Site'] = df['Site'].astype(str)
df['Age'] = df['Age'].astype(float)

print(df)

data = {'Site':['Google', 'Runoob', 'Wiki'], 'Age':[10, 12, 13]}

df = pd.DataFrame(data)

print (df)