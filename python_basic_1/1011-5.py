import pandas as pd

dict_data = {'c0':[1,2,3], 'c1':[4,5,6]}
df = pd.DataFrame(dict_data, index=['r0', 'r1', 'r2'])
print(df,"\n")

df.to_csv("D:/bong/data/df.csv")
df.to_excel("D:/bong/data/df.xlsx")
