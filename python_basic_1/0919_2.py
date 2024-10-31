import numpy as np
import matplotlib as plt

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense


x = np.array([[2, 0], [4, 4], [6, 2], [8, 3]])
y = np.array([84,93,91,97])

model = Sequential()

model.add(Dense(1, input_dim=2, activation='linear'))
model.compile(optimizer='sgd', loss='mse')

model.fit(x,y, epochs=2000)
hour = 0
private_class = 0
prediction = model.predict([np.array([[hour, private_class]])])

print("%.f 시간을 공부하고 %.f 시간외 과외를 받을경우, 예상 점수는 %.02f점입니다." % (hour, private_class, prediction))
