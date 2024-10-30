
msg = '안녕하세요'
print(msg)#str...문자열


msg = '100'
print(msg)#str...문자열


val = (100,200)
print('va = ', val, type(val))
msg = '%d,%d'%val
print(msg)

#%%
a = 123
b = 456
c = 789

msg = f'{a} {b} {c}'%(123,123,123)
print(msg)
print('%d %5d %05d'%(123,123,123))
print('{0:d} {1:5d} {2:05d}'.format(123,456,789))
print('{0:d}\n {1:5d}\n {2:05d}'.format(123,456,789))
#%%

a = 123
b = 456
c = 789
msg = '{a} {b} {c}'
print(msg)


msg = f'{a:d} {b:5d} {c:05d}'
print(msg)

msg = f'{a}\n{b}\n{c}'
print(msg)
