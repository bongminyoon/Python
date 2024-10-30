'''
fruits = ["딸기","복숭아","배","천두복숭아","사과","포도","체리","블루베리"]
vegetable = ["시금치","케일","피망","강남콩"]

dirty_dozen = [fruits, vegetable]

print(dirty_dozen)
'''
'''
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
fruits[-1] = "Melons"
fruits.append("Lemons")
print(fruits)
'''

'''
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]

print(dirty_dozen[1][1])
'''

'''
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

img_hands = [rock, paper, scissors]

my_choice = int(input("무엇을 내겠습니까? 바위(0), 보(1), 가위(2): "))

if my_choice >= 3 or my_choice < 0:
    print("잘못된 숫자를 입력했습니다")
else:
    print("나의 선택은: ")
    print(img_hands[my_choice])

    computer_choice = random.randint(0, 2)
    print("컴퓨터의 선택은: ")
    print(img_hands[computer_choice])

    if computer_choice == 0 and my_choice == 2:
        print("컴퓨터가 이겼습니다.")
    elif my_choice == 0 and computer_choice == 2:
        print("당신이 이겼습니다!")
    elif computer_choice > my_choice:
        print("컴퓨터가 이겼습니다.")
    elif my_choice == computer_choice:
        print("비겼습니다!")
    elif my_choice > computer_choice:
        print("당신이 이겼습니다!")
'''
'''
import random
# 1부터 100까지 무작위 숫자 생성
number = random.randint(1, 100)
# 몇 회 시도했는지를 저장하는 변수
num_of_guesses = 0
# 무한 반복문
while True:
  # 사용자로부터 숫자 입력 받기
  guess = int(input("1부터 100까지의 숫자를 입력하세요: "))
  
  # 시도 횟수 증가
  num_of_guesses += 1
  
   # 추측한 숫자가 정답보다 큰 경우
  if guess > number:
    print("입력한 숫자가 너무 큽니다.")
    
  # 추측한 숫자가 정답보다 작은 경우
  elif guess < number:
    print("입력한 숫자가 너무 작습니다.")
    
 # 추측한 숫자가 정답인 경우
  else:
    print(f"축하합니다! {num_of_guesses}회 만에 숫자를 맞췄습니다.")
    break
''''''
import socket

hostname = socket.gethostname()

ip_address = socket.gethostbyname(hostname)

print("내부 IP: " + ip_address)
'''
'''import pyttsx3 

engine = pyttsx3.init()
engine.setProperty('rate', 150) 

def speak(text):
  engine.say(text)
  engine.runAndWait()

text = "나는 메이플랜덤디펜스 태초 오우너입니다."
speak(text)
from gtts import gTTS
from playsound import playsound
# 텍스트를 입력받습니다.
text = input('텍스트를 입력하세요: ')
# 한국어로 음성을 출력하도록 설정합니다.
tts = gTTS(text, lang='ko')
# 음성을 mp3 파일로 저장합니다.
tts.save('output.mp3')
# 저장한 mp3 파일을 재생합니다.ㅇ
playsound('output.mp3')'''