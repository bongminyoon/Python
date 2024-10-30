#%%
print(5)
print(5+3*1)
print('윤봉민')
print('윤봉민'*3)
print(4 > 60)
print(50 > 1)
print(True)
print('True')

#%%

animal = '강아지'
name = '단풍'
age = 12
hobby = 'sleep'
is_adult = age > 5

print("우리집 강아지의 이름은 연탄이에요")
print("연탄이는 4살이며, 산책을 아주 좋아해요")
print("연탄이는 어른일까요? True")

print('우리집'+ animal + '이름은' + name + '이에요')
print(name + '는' + str(age) + ' 살 이며,' + hobby + '을(를) 아주 좋아해요')
print(age)
print(age, "살입니다")

#%%
station = '사당'



print(station + '행 열차가 들어오고 있습니다.')
station = '신도림'
print(station + '행 열차가 들어오고 있습니다.')
station = '인천공항'
print(station + '행 열차가 들어오고 있습니다.')

#%%

print(1+1)
print(2-1)
print(3*1)
print(5/2) #소수점 몫 
print(5//2) #몫
print(5%2) #나머지

print(1 != 3)
#%%
print(abs(-22))
print(min(2,1))
print(max(2,1))
print(pow(2,3))
print(round(4.1234))

#%%

from random import *

print(random()) #0.0 ~ 1.0까지 임의
print(int(random()*10)) #0 ~ 10 까지 임의
  
print(randrange(1,45+1))  

#%%
import random

  
x = randint(3,28)
print('오프라인 스터디 모임 날짜는 매월' + str(x) + '일로 선정되었습니다')
#%%

str = '나는 바보입니다'
print(str)
str2 = "나는 천재입니다"
print(str2)

#%%

jm = '991127-1234567' 
print("성별 : " + jm[7])
print('지역번호: ' + jm[8:13])
print('생일 : ' + jm[0:6])
print('주민등록번호 : ' + jm[:13])
print('뒷자리 : ' + jm[-7:])
#%%
python = 'python is amazing'
python
print(python.upper())
python.upper()
print(len(python))

# %%
#문자열 포맷
print('나는 %d살입니다, 동생은 %d살입니다' %(20, 12))
print('나는 %s을 좋아해요' %"파이썬" )

print('나는 {}살입니다,동생은 {}살입니다'.format(20, 12))


age1 = 20
age2 = 12
color = 'blue'
print(f'나는 {age1}살입니다, 동생은 {age2}살입니다')


# %%
print('나는 "윤봉민" 입니다')
print("나는 \"윤봉민\" 입니다")

 

# %%
a = "http:///naver.com"
b = a[8:-4]  #b = naver
c = b[0:3] #c = nav 
d = len(b)   #d = 5
e = b.find('e') # e = 1

print(f'{c}{d}{e}!')



#b #naver
#c = len(b)
#c 
#print(b + c + '!')

# %%
url = "http:///naver.com"
my_str = url.replace("http://", "")
my_str = my_str[:my_str.index(".")]
password = my_str[:3] +str(len(my_str)) + str(my_str.count("e"))

# %%
 