def postTaxPrice(price):
    ans= price*1.1
    return ans

def sayhello(name):
    print("안녕하세요?", name, "님")


print(postTaxPrice(1000), "원")
print(postTaxPrice(2000), "원")
print(postTaxPrice(3000), "원")

sayhello("윤봉민")