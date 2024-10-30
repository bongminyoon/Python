from gtts import gTTS
import os
import time


itx_stations = ["남춘천","강촌","가평","청평","마석","평내호평","사릉","퇴계원","청량리","왕십리","옥수","용산","상봉"]

itx_stations = [
    ("남춘천", 10),
    ("강촌", 10),
    ("가평", 10),
    ("청평", 10),
    ("마석", 10),
    ("평내호평", 10),
    ("사릉", 10),
    ("퇴계원", 10),
    ("청량리", 10),
    ("왕십리", 10),
    ("옥수", 10),
    ("용산", 10),
    ("상봉", 10), 
]

door_open_time = 10
door_close_time = 10

def read_station_names():
    for i, (station, _) in enumerate(itx_stations):
        tts = gTTS(text=station, lang='ko')
        tts.save(f"station_{i}.mp3")  # 역 이름을 음성 파일로 저장
        os.system(f"start station_{i}.mp3")  # 음성 파일 실행
        time.sleep(door_open_time)  # 문이 열리는 시간
        time.sleep(door_close_time)  # 문이 닫히는 시간

def main():
    while True:
        user_input = input("출발을 입력하세요: ")
        if user_input.strip().lower() == "출발":
            read_station_names()  # 역 이름을 읽어주는 함수 호출
            break
        else:
            print("출발을 입력하세요.")

if __name__ == "__main__":
    main()