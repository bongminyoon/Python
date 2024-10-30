#%%
hap1 = 0
hap2 = 0

for i in range(1, 1001, 1):
    if i % 2 == 0:  
        hap1 = hap1 + i  
        
    else:  
        hap2 = hap2 + i  

print("짝수의 합:", hap1)
print("홀수의 합:", hap2)

#%%


hap = 0

for i in range(1,101,7):
        hap = hap + i    
print("7의배수의합 : %d" %hap)


# %%

flag_stop = False
i = 0
hap1 = 0
hap2 = 0
print('while start')
while(not flag_stop):
    if i > 1000:
        flag_stop = True
        break
    if i % 2 == 0:  
        hap1 = hap1 + i  
        
    else:  
        hap2 = hap2 + i  


    i = i + 1


print("짝수의 합:", hap1)
print("홀수의 합:", hap2)
print("while finish")


    




# %%
