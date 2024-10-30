# street_name = "동산면 영서로 1290-31"
# print(street_name[4] + street_name[9])
# print(num[0] + num[1])

# a = input("2자리의 숫자 : ")
# b = int (a[0]) 
# c = int (a[1])
# print(b + c)


# a = "58"
# b = int (a[0]) 
# c = int (a[1])
# print(b + c)

# height = input("당신의 키는 몇 m : ")
# weight = input("당신의 몸무게는 몇 kg : ")

# bmi = int(weight) / float(height)**2
# bmi_as_int = int(bmi)
# print(bmi_as_int)

# print(int(8 / 3))
# print(round(8 / 3))
# print(round(8 / 3, 2))
# print(round(0.145676747234, 2))
# print(8//3)

# score = 0
# score +=1
# print(score)

# age = input("당신의 나이는 몇살일까요?")

# age_as_int = int(age)

# years_remaining = 90 - age_as_int
# days_remaining = years_remaining * 365
# week_remaining = years_remaining * 52
# months_remaining = years_remaining * 12

# print(months_remaining)

# message = f"당신의 남은{days_remaining} 날, {week_remaining} 주, {months_remaining} 월)"

# print(message)

# print("팁 계산기!")

# order = float(input("총 얼마를 주문했을까?"))
# tip = int(input ("팁을 얼마나 주면 좋을까? 10, 12, or, 15 ?"))
# people = int(input("몇명이서 나눠서 낼까?"))

# tip_as_percent = tip / 100
# total_tip = order * tip_as_percent
# total_bill = total_tip + order
# bill_per_person = total_bill / people

# final_bill = round(bill_per_person, 2)
# print(f"팁 포함해서 각자 내야하는 금액은: {final_bill} $")

print("롤러코스터를 타러 오셨군요!")
height = int(input("키카 몇 cm 입니까?"))

if height >= 120:
    print("롤러코스터를 탈 수 있습니다!")
    age = int(input("당신은 몇살입니까?"))
    if age < 12:
        print("무료입니다!")
    elif age <=18:
        print("7천원입니다")
    else:
        print("만2천원입니다")
else: 
    print("죄송하지만 롤러코스터를 탈수 없어요.")