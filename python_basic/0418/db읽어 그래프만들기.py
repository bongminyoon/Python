import sqlite3
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

conn = sqlite3.connect(r'D:\bong\목\0418\upbit.db')

query = 'SELECT * FROM BTC_KRW'

cur = conn.cursor()
cur.execute(query)
rows = cur.fetchall()

dates = [row[0] for row in rows]
amounts = [row[1] for row in rows]

fig, ax = plt.subplots()
ax.plot_date(dates, amounts, '-')
ax.set_xlabel('Date')
ax.set_ylabel('Amount')
ax.set_title('Upbit Date')
plt.show()

conn.close()
              