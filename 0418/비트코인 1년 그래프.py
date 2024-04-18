import pyupbit
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

to_date = datetime.now()
from_date = to_date - timedelta(days=365)

df = pyupbit.get_ohlcv("KRW-BTC", interval="day", to=to_date, count=365)

x_values = pd.date_range(start=from_date, end=to_date - timedelta(days=1), freq='D')

plt.plot(x_values, df['close'])

plt.title('Bitcoin Price in KRW (1 year)')
plt.xlabel('Date')
plt.ylabel('Price (KRW)')

plt.xticks(rotation=45)

plt.show()