import pandas as pd

df = pd.read_csv('D:/bong/data/bok_statistics_CD.csv', header=None)

print(df.head())
print('\n')
print(df.head(3))
print('\n')
print(df.tail())
print('\n')
print(df.tail(3))
