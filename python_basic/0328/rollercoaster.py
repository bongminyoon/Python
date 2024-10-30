print("롤러코스터에 오신것을 환엽합니다!")
height = int(input("키가 몇cm 입니까? "))
bill = 0

if height >= 120:
    print("롤러코스터를 타실 수 있습니다.")
    age = int(input("나이가 몇살입니까?"))
    if age < 12:
        bill = 0
        print("무료입니다!")
    elif age <= 18:
        bill = 7000
        print("청소년은 7천원입니다!")
    else:
        bill = 12000
        print("성인은 만2천원 입니다!")

    wants_photo = input("사진을 찍기를 원합니까? Yes(Y) or No(N).")
    if wants_photo == "Y" :
        bill += 1000
        print(f"지불하실 총 급액은{bill}")

else:
    print("죄송합니다. 롤러코스터를 타실수 없습니다.")