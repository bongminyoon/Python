import pandas as pd
import matplotlib.pyplot as plt

# 데이터 읽기
df = pd.read_csv('D:/bong/data/bok_statistics_CD_2.csv', header=0, index_col=0)

# 박스 플롯 생성
boxplot = df.plot(kind='box')

# 플롯 저장 (먼저 호출)
plt.savefig('D:/bong/data/plot.png')

# 플롯 표시
plt.show()
