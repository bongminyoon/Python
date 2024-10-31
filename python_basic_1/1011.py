import pandas as pd

dict_data = {'c0':[1,2,3,4,5], 'c1':[6,7,8,9,10]}

df1 = pd.DataFrame(dict_data)
print(type(df1), "\n")
print(df1, "\n")

df2 = pd.DataFrame(dict_data, index=['r0', 'r1', 'r2', 'r3', 'r4'])
print(df2, "\n")

list_of_list_data = [[1,2,3,4,5], [6,7,8,9,10]]
df3 = pd.DataFrame(list_of_list_data)
print(df3, "\n")

df4 = pd.DataFrame(list_of_list_data,
                   index=['r0','r1'],
                   columns=['c0','c1','c2','c3','c4'])
print(df4, "\n")

print(df2.shape)
print(df.shape)
