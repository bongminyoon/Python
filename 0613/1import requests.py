import requests
#이미지가 있는 url 주소
url = "https://search.pstatic.net/common?type=b&size=3000&quality=100&direct=true&src=http%3A%2F%2Fsstatic.naver.net%2Fpeople%2FprofileImg%2F65cbbaa5-e760-4883-91e8-4cff335dac77.jpg"
#해당 url로 서버에게 요청
img_response = requests.get(url)
#요청에 성공했다면
if img_response.status_code == 200:
#print(img_response.content)
  print("=====[이미지저장]=====")
  with open("test.jpg","wb") as fp:
    fp.write(img_response.content)
