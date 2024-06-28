import time
import tkinter as tk

def set_timer():
    try:
        timer_input = input("타이머를 설정할 시간(분:초)을 입력하세요 (예: 5:30): ")
        minutes, seconds = map(int, timer_input.split(':'))
        return minutes * 60 + seconds
    except ValueError:
        print("올바른 시간 형식을 입력하세요.")
        return None

def show_alarm(message):
    root = tk.Tk()
    root.title("알림")
    
    label = tk.Label(root, text=message, font=("Helvetica", 14))
    label.pack(padx=20, pady=20)

    button = tk.Button(root, text="확인", command=root.destroy)
    button.pack(pady=10)

    root.mainloop()

def main():
    print("타이머를 시작합니다.")
    timer_seconds = set_timer()
    if timer_seconds is None:
        return
    
    start_time = time.time()
    end_time = start_time + timer_seconds

    while time.time() < end_time:
        remaining_time = int(end_time - time.time())
        minutes, seconds = divmod(remaining_time, 60)
        print(f"남은 시간: {minutes:02d}:{seconds:02d}", end='\r')
        time.sleep(1)

    show_alarm("타이머 종료!")  # 원하는 메시지를 여기에 입력하세요.

if __name__ == "__main__":
    main()
