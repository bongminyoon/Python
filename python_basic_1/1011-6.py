import pandas as pd
import matplotlib as plt

df = pd.read_csv('D:/bong/data/bok_statistics_CD_2.csv', header=0, index_col=0)
print(df.head())
print('\n')

df.plot(kind='bar')
plt.pyplot.show()

df['CD_rate'].plot(kind='bar')
plt.pyplot.show()

df['change'].plot(kind='bar')
plt.pyplot.show()
