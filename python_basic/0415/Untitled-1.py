'''
자료형
a = 1 #정수형
a = '12345' #문자열
a = 1.123 #실수형
#컨테이너 형태
#박스형태의 집합 구조를 가지는 데이터 형
a = [1,2,3,4,5,1.123,2.123,3.123] #list 자료형
a = (1,2,3,4,5,1.123,2.123,3.123) #tuple 자료형
a = {'a':123, 'b':456, 'c':789} # dictionary 자료형
'''
a = [] #list 선언

a = [1,2,3] #list 선언과 초기화

a[0] = 10
a[1] = 20
a[2] = 30 #list 데이터변경
a.append(10)
a.append(20)
a.append(30)
a1 = a[0:1]
a2 = a[0:2]
a3 = a[0:3] #list 데이터를 가져오기 ..slice

#%%

a,b,c,d = 0,0,0,0

sum = 0
a = input('1번째 숫자를 입력하시오 : ') #문자열 -> 정수형
a = int(a)
b = input('2번째 숫자를 입력하시오 : ')
b = int(b)
c = input('3번째 숫자를 입력하시오 : ')
c = int(c)
d = input('4번째 숫자를 입력하시오 : ')
d = int(d)

#sum = a+b+c+d
print('총합은', sum, '입니다.')
print('총합은 %d 입니다.' % sum)
print(f'총합은 {sum} 입니다.')

위의 코드 a,b,c,d를  list append를 이용한 for 문
# %%
a,b,c,d = []
a,b,c,d = [0]

# %%
#strval = input('값을 입력하시오(정수) : ')
#val = int(strval)
#for _ in range(0, n):  for문 다양한 
#for i in range(0, n):
#for i in range(0, n ,1):

n = 10

val = []
for _ in range(n):
    #tmp = int(input('값을 입력하시오(정수) :'))
    #val.append(tmp)
    val.append(int(input('값을 입력하시오(정수) : ')))

print(f'val = {val}')


tot = sum(val)
print(f'총합은 {tot} 입니다.')  






# %%
#구구단 2단을 two_dan []리스트에 넣어서
#그결과를 출력하시오 (no input fuction, use for)

res = []

for i in range(1, 10, 1):
     two_dan=2*i
     print(two_dan)

# %

dan = 2
two_dan = [x for x in range(dan,dan*10,dan)]
print(two_dan)
tot = sum(two_dan)
print(tot)

# %%



print(f'val = {val}')

# %%
gugudan = []
for d in range(2,10):
    dan = []
    for x in range(1,10):
        dan.append(d*x)
    gugudan.append(dan)
print(gugudan[][])


     
    


# %%
#구구단을 가로로 출력하시오
dan_start = 5
dan_finish = 8
step_start = 3
step_finish = 7


for step in range(step_start-1, step_finish-1+1):
    line = ''
    for dan in range(dan_start-2, dan_finish-2+1):
        line = line + f'{dan}' * {step} = {gugudan[dan-2][step-1]}
        line = line +'\t'
    lines += line
    lines += line +'\t'
    print(line)
   
# %%
