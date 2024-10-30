import requests
url = "https://kauth.kakao.com/oauth/token"
data = {
  "grant_type" : "authorization_code",
  "client_id" : "bcd1767799cac8fdbd5b1efcda5d3fc4",
  "redirect_uri" : "https://localhost.com",
  "code" : "BdTHFEdDaKtsnzrS8iibh0Rzb0uqVQQXEMFVWXrhYsFBt4EJKCWw9gAAAAQKKwzTAAABkA_y136m1x-HnlkNwQ"
}
response = requests.post(url, data=data)
# 요청에 실패했다면,
if response.status_code != 200:
  print("error! because ", response.json())
else: # 성공했다면,
  tokens = response.json()
  print(tokens)
