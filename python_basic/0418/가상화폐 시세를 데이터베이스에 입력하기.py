import pyupbit
import sqlite3
import datetime

conn = sqlite3.connect(r'D:\bong\목\0418\upbit.db')
cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS BTC_KRW(time TEXT, price INTEGER)")

price = pyupbit.get_current_price("KRW-BTC")
now = datetime.datetime.now()

print(now, price)

cur.execute("INSERT INTO BTC_KRW (time, price) VALUES (?, ?)", (now, price))
conn.commit()

conn.close()