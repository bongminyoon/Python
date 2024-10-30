import pyupbit

price = pyupbit.get_current_price("KRW-BTC")

print("현재 BTC?KRW의 가격은", price, "원입니다")