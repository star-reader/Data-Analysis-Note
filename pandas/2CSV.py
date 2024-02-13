import pandas as pd

df = pd.read_csv('../assets/VOR.csv', encoding='GB2312')
print(df.head())
print(df.info())