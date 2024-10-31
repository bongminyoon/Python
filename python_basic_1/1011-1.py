import pandas as pd

csv_file = 'D:/bong/data/bok_statistics_CD.csv'

df1 = pd.read_csv(csv_file)
print(df1)
print('\n')

df2 = pd.read_csv(csv_file, header=None)
print(df2)
print('\n')

df3 = pd.read_csv(csv_file, index_col=0)
print(df3)
print('\n')


df4 = pd.read_csv(csv_file, index_col=0, header=None)
print(df4)
print('\n')

excel_file = 'D:/bong/data/report_Key100Stat.xlsx'

df5 = pd.read_excel(excel_file, engine="openpyxl")
print(df5)
