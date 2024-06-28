import requests

# 발급받은 API 키
API_KEY = '2930ea83429d44989e3f21341ea700b4'  # 여기에는 실제 API 키를 입력해야 합니다.

# 특정 팀의 선수 목록을 가져오는 함수
def get_team_players(team_name):
    # API URL
    url = "http://api.football-data.org/v2/teams"

    # 요청 헤더에 API 키를 포함
    headers = {
        'X-Auth-Token': API_KEY
    }

    # API 요청
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print("API 요청에 실패했습니다.")
        return
    
    teams = response.json()['teams']
    
    # 팀 이름으로 팀을 찾기
    team = next((team for team in teams if team['name'] == team_name), None)
    if not team:
        print(f"{team_name} 팀을 찾을 수 없습니다.")
        return
    
    # 팀 ID로 선수 목록 가져오기
    team_id = team['id']
    team_url = f"http://api.football-data.org/v2/teams/{team_id}"
    team_response = requests.get(team_url, headers=headers)
    if team_response.status_code != 200:
        print("팀 정보를 가져오는데 실패했습니다.")
        return
    
    players = team_response.json()['squad']
    
    print(f"{team_name}의 선수 목록:")
    for player in players:
        print(player['name'])

if __name__ == "__main__":
    team_name = input("구단 이름을 입력하세요: ")
    get_team_players(team_name)
