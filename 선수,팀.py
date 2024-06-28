import requests

# 발급받은 API 키
API_KEY = '2930ea83429d44989e3f21341ea700b4'

# 선수 이름을 입력하면 해당 선수의 소속 구단을 출력하는 함수
def get_player_team(player_name):
    # API URL
    url = "http://api.football-data.org/v2/players"

    # 요청 헤더에 API 키를 포함
    headers = {
        'X-Auth-Token': API_KEY
    }

    # API 요청
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print("API 요청에 실패했습니다.")
        return
    
    players = response.json()['players']
    
    # 선수 이름으로 선수를 찾기
    player = next((player for player in players if player['name'].lower() == player_name.lower()), None)
    if not player:
        print(f"{player_name} 선수를 찾을 수 없습니다.")
        return
    
    # 선수의 소속 구단 출력
    team_name = player['team']['name']
    print(f"{player_name} 선수는 {team_name} 소속입니다.")

# 구단 이름을 입력하면 해당 구단의 전체 선수 목록을 출력하는 함수
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
    team = next((team for team in teams if team['name'].lower() == team_name.lower()), None)
    if not team:
        print(f"{team_name} 팀을 찾을 수 없습니다.")
        return
    
    # 팀 ID로 선수 목록 가져오기
    team_id = team['id']
    squad_url = f"http://api.football-data.org/v2/teams/{team_id}"
    squad_response = requests.get(squad_url, headers=headers)
    if squad_response.status_code != 200:
        print("팀 정보를 가져오는데 실패했습니다.")
        return
    
    players = squad_response.json()['squad']
    
    print(f"{team_name} 소속 선수 목록:")
    for player in players:
        print(player['name'])

if __name__ == "__main__":
    user_input = input("선수 이름 또는 구단 이름을 입력하세요: ")
    if user_input.lower() == 'exit':
        print("프로그램을 종료합니다.")
    elif user_input.lower() == 'team':
        team_name = input("구단 이름을 입력하세요: ")
        get_team_players(team_name)
    else:
        get_player_team(user_input)
