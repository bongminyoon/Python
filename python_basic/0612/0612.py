#%%
import pyupbit

price = pyupbit.get_current_price("KRW-BTC")
print("현재 BTC/KRW의 가격은", price, "원입니다")

tickers = pyupbit.get_tickers()

#%%
for ticker in tickers:
    try: 
        price = pyupbit.get_current_price(ticker)
        print(ticker, price)
    
    except:pass
# %%
import pyupbit
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

to_date = datetime.now()
from_date = to_date - timedelta(days=365)

df = pyupbit.get_ohlcv("KRW-BTC", interval="day", to=to_date, count=365)

x_values = pd.date_range(start=from_date, end=to_date - timedelta(days=1), freq='D')

plt.plot(x_values, df['close'])
plt.title('Bitcoin Price in KRW (1 years)')
plt.xlabel('Date')
plt.ylabel('Price (KRW)')

plt.xticks(rotation=45)

plt.show


# %%
import pyupbit
import sqlite3
import datetime

conn = sqlite3.connect(r'upbit.db')
cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS BTC_KRW (time TEXT, price INTEGER)")
price = pyupbit.get_current_price("KRW-BTC")
now = datetime.datetime.now()

print(now, price)

cur.execute("INSERT INTO BTC_KRW(time, price) VALUES (?, ?)", (now,price))
conn.commit()

conn.close()
#%%
import pyupbit
import sqlite3
import datetime
import time

conn = sqlite3.connect(r'upbit.db')
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS BTC_KRW (time TEXT, price INTEGER)")

while True:
    try: 
        price = pyupbit.get_current_price("KRW-BTC")
        now = datetime.datetime.now()
        
        print(now, price)
        cur.execute("INSERT INTO BTC_KRW (time, price) VALUES (?, ?)", (now, price))
        conn.commit()
        
        time.sleep(10)
    except Exception as e:
        print(e)
        time.sleep(1)
        
        
conn.close()
# %%
import sqlite3

conn = sqlite3.connect(r'25.가상화폐 데이터 획득하여 데이터베이스에 저장\upbit.db')
cur = conn.cursor()

cur.execute("SELECT * FROM BTC_KRW")
rows = cur.fetchall()

for row in rows:
    print(row)
    
conn.close()
#%%
