import cv2
import time
count = 0
maxFrames = 60

cap = cv2.VideoCapture(0)

while count < maxFrames:
    ret, frame = cap.read()
    if not ret:
        break
    
    frame = cv2.resize(frame, (640, 480))
    cv2.imshow("test window", frame)
    cv2.imwrite(f"D:bong{count}.jpg", frame)
    time.sleep(1)
    count += 1
    
    if cv2.waitKey(1) & 0xFF == 27:
        break