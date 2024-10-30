#%%
for i in range(1,5+1,1):
    print(i, '*'*i)

digits_max = 5
for i in range(digits_max,0,-1):
    msg_empty = f' '*(i-1)
    msg_star = f'*'*(digits_max-i+1)
    print(i, msg_empty+msg_star)
# %%

lines_max = 9
star  = ['    *    ']
star += ['   * *   ']
star += ['  * * *  ']
star += [' * * * * ']
star += ['* * * * *']
star += [' * * * * ']
star += ['  * * *  ']
star += ['   * *   ']
star += ['    *    ']

print(type(star))
print(star)
for i in range(0,len(star),1):
    print(i, star[i])
# %%
