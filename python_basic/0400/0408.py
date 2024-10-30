'''
i, hap = 0,0

for i in range(1, 1001, 1):

    if hap == i*2:
        
        hap = hap + i
     
print("1과1000사이에 있는 짝수의 합계 : %d" %hap)
    
'''

   


hap = 0

for i in range(1, 1001, 1):
    if i % 2 == 0:  
        hap = hap + i
    
        

    else: 

        print(" 짝수의 합: %d" % hap)
        print("홀수 의 합: %d" % hap)        




