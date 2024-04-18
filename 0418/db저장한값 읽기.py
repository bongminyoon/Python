import sqlite3

        
conn = sqlite3.connect(r'D:\bong\목\0418\upbit.db')
cur = conn.cursor()

cur.execute("SELECT * FROM BTC_KRW")
rows = cur.fetchall()

for row in rows:
    print(row)

conn.close()