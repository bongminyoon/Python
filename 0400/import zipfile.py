import requests
def currency_converter(amount, from_currency, to_currency):
  
  url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
  
  response = requests.get(url)
  data = response.json()
  
 
  exchange_rate = data['rates'][to_currency]
  result = round(amount * exchange_rate, 2)
  

  return result
print("환율 변환기")
print("============")

while True:
  try:
  
    amount = float(input("변환하려는 금액을 입력하세요: "))
    
    from_currency = input("어떤 화폐에서 변환하시겠습니까? (예: USD, KRW): ").upper()
    to_currency = input("어떤 화폐로 변환하시겠습니까? (예: USD, KRW): ").upper()
    
  
    result = currency_converter(amount, from_currency, to_currency)
    
    
    print(f"{amount} {from_currency}은(는) {result} {to_currency}입니다.")
  
  
    choice = input("계속 변환하시겠습니까? (Y/N): ").upper()
    if choice != "Y":
      break
    
  except:
     print("올바른 값을 입력해주세요.")