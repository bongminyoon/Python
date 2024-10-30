import time

#ITX 역 리스트
itx_stations = ["남춘천","강촌","가평","청평","마석","평내호평","사릉","퇴계원","청량리","왕십리","옥수","용산","상봉"]
itx_stations = [
    ("남춘천", 5),
    ("강촌", 10),
    ("가평", 3),
    ("청평", 1),
    ("마석", 2),
    ("평내호평", 3),
    ("사릉", 1),
    ("퇴계원", 1),
    ("청량리", ),
    ("왕십리", ),
    ("옥수", ),
    ("용산", ),
    ("상봉", ), 
]

def notify_station(station, interval):
    print(f"알림: {station}에 도착했습니다.")
    time.sleep(interval)

def main():
    while True:
        user_input = input("시작을 입력하세요: ")
        if user_input.strip().lower() == "시작":
            for station, interval in itx_stations:
                notify_station(station, interval)
            break
        else:
            print("시작을 입력하세요.")

if __name__ == "__main__":
    main()
