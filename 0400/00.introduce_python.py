
#%%
print('hello python world!!!')
print('KOPI'*3)


# %%
# python 기본 자료
# char a = 'a' c/c++
a = 'a2'
print(a, type(a))
# string a = 'abcdef' c/c++
a = 'abcdef'
print(a, type(a))
# int a = 1 c/c++
a = 1
print(a, type(a))
# float a = 123.456 c/c++
a = 123.456
print(a, type(a))
# %%
a = 123
print(a+123)
a = '123'
print(a+'123')

# %%
#calc
a = 1
b = 2
c = a+b
print(f"{a}+{b} = {c}")

b = 1000
c = a+b
print(f'{a}+{b} = {c}')



# %%
# type
# string / integer
# list  ... array/data/read+write
'''
a = [1,2,3,4,5]
'''
a = [1,2,3,4,5]
print(a, type(a))
# tuple ... array/data/read only
'''
a = (1,2,3,4,5)
'''
a = (1,2,3,4,5)
print(a, type(a))
# dict  ... 사전/serach/key:value/read+write
'''
a = {'a':1,'b':2,'c':3,'d':4,'e':5}
'''
a = {'a':1,'b':2,'c':3,'d':4,'e':5}
print(a, type(a))


# %%
#operator
# + - * / ... 4칙연산
# ** ..
  '''
    python = c/c++ ... result
    2*2    = 2^2 ... 4
    2**3   = 2^3 ...8
  '''
# //
  '''
    python = c/c++         ... result
    5/2    = float(5.0/2)  ... 2.5
    5//2   = 5/2           ... 2
  '''
  
#length ... sizeof .... c , c++ vector.size() / length()
#len(a)


#%%
print('this is calculation program 2024-03-18')
a = input('in a : ')
a = int(a)#type-casting : str to int
print(a, type(a))
b = input('in b : ')
b = int(b)#type-casting : str to int
print(b, type(b))
op = input('in op(+,-,*,/,//,**) : ')

## 제어문{조건문,반복문} ... if from python <-> if / switch from c/c++
#print(op == '+')
if (op == '+'):#만약에 True 조건이면
  c = a+b
elif (op == '-'):#만약에 True 조건이면
  c = a-b
elif (op == '*'):#만약에 True 조건이면
  c = a*b
elif (op == '/'):#만약에 True 조건이면
  c = a/b
elif (op == '//'):#만약에 True 조건이면
  c = a//b
elif (op == '**'):#만약에 True 조건이면
  c = a**b
else:#다 아니면 
  print('만족하는 Op가 없습니다.')
print(c, type(c))
print(f"{a}{op}{b} = {c}")

'''
switch (op)
 case '+'  
    c = a+b
 case '-'  
    c = a-b
 case '*'  
    c = a*b
'''



a = 1
a = 1.123
#type-casting .. 형 변환
# int() / str() / float()
# %%
# 조건문과 반복문 ... 구구단
#조건문 : if
a = 10
if a>= 10 :
  print('a는 10보다 크거나 같습니다.')
else:
  print('a는 10보다 작습니다.')

#반복문 : for 
for i in range(0, 9+1, 1): # for(int i=0; i<10; i++)
  print(i)

print(10*10)

for i in [1,2,3]:
  print(i)
for i in (1,2,3):
  print(i)



# %%
print('---'*20)
a1 = "10"*10
print(a1)

a2 = ''
for i in range(1, 10+1, 1): # for(int i=1; i<11; i++)
  print(i)
  a2+='10'
print(a2)
print(a1==a2)
print('---'*20)




# %%
# 조건문과 반복문 ... 구구단

#GUGUDAN
#Q1.GUGUDAN 출력하시오
# 2 * 1 = 2
# 2 * 2 = 4
# ...
# 9 * 8 = 72
# 9 * 9 = 81
Dan_Start = 2
Dan_Finish = 9
Step_Start = 1
Step_Finish = 9
for dan in range(Dan_Start, Dan_Finish+1, 1): # for(int i=1; i<11; i++)
  for step in range(Step_Start, Step_Finish+1, 1):
    result = dan*step
    msg = f'{dan} * {step} = {result}'
    print(msg)
# %%
#Q2.GUGUDAN 가로형태로 출력하시오
# 2 * 1 = 2  3 * 1 = 3  ... 9 * 1 = 9
# 2 * 2 = 4  3 * 2 = 6  ... 9 * 2 = 18

#input
print('input')
Dan_Start = 2
Dan_Finish = 9
Step_Start = 1
Step_Finish = 9
lines=''


#function
print('function')
#input -> function -> output
for step in range(Step_Start, Step_Finish+1, 1):
  msg=''
  for dan in range(Dan_Start, Dan_Finish+1, 1): 
    result = dan*step
    msg += f'{dan} * {step} = {result}'
    msg += '\t'
  lines += msg+'\n'



#output & display
print('output')
print(lines)

# %%
#Q3.GUGUDAN 형태로 출력하시오
# GuGuDan Start = 2 dan, Finish = 6 dan
# GuGuDan Step Start = 5, Finish = 8 step
# 2 * 5 = 10  2 * 6 = 12   ... 2 * 8 = 16
# 
# 6 * 5 = 30  6 * 6 = 36   ... 6 * 8 = 48
print('input')
Dan_Start = 2
Dan_Finish = 6
Step_Start = 5
Step_Finish = 8
lines=''
print('function')



#function
print('function1'*10)
#input -> function -> output
if True:
  for step in range(Step_Start, Step_Finish+1, 1):
    msg=''
    for dan in range(Dan_Start, Dan_Finish+1, 1): 
      
      result = dan*step
      msg += f'{dan} * {step} = {result}'
      msg += '\t'
    lines += msg+'\n'

print(lines)
lines=''




print('function2'*10)
for step in range(1, 9+1, 1):
  msg=''
  for dan in range(1, 9+1, 1):
    if step >= Step_Start and step <= Step_Finish and dan >= Dan_Start and dan <= Dan_Finish:
      result = dan*step
      msg += f'{dan} * {step} = {result}'
      msg += '\t'
  lines += msg+'\n'

#output & display
print('output')
print(lines)
# %%
