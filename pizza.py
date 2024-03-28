# 파이썬 피자에 오신것을 환영합니다!
# 원하는 피자 사이즈는 S , M , L  / 스몰은 만오천원, 중간은 2만원, 큰 피자는 3만원
# 페퍼로니 추가는 2천원
# 치즈 추가는 3천원
# 총 지불하실 금액은?

print("파이썬 피자에 오신것을 환영합니다!")
size = input("원하는 사이즈는 무엇입니까(S, M, L) > ")
price = 0


if(size == 'S'):
    price = 15000 
    print("만오천원 입니다!")
elif(size == 'M'):
    price = 20000
    print("이만원 입니다!")
else:
    price = 30000
    print("3만원 입니다!")

wants_topping = input("페페로니를 추가하시겠습니까? Yes(Y) or No(N).")
if wants_topping == "Y" :
    price += 2000

wants_cheese = input("치즈를 추가하시겠습니까? Yes(Y) or No(N).")
if wants_cheese == "Y" :
    price += 3000

wants_cola = input("콜라를 추가하시겠습니까? Yes(Y) or No(N).")
if wants_cola == "Y" :
    price += 3500
    
print(f"총 지불하실 금액은{price}원 입니다")



