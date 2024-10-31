import pytesseract
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Tesseract 경로 설정 (Windows에서 필요한 경우)
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\user\Desktop\ybm\tess\tesseract.exe'

# 이미지 파일 경로 수정
path = r"C:\Users\user\Desktop\ybm\123.png"  # 자동차 이미지 경로
image = cv2.imread(path)

# 이미지가 정상적으로 읽혔는지 확인
if image is None:
    print("이미지를 열 수 없습니다. 경로를 확인하세요.")
else:
    # 이미지 전처리
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 그레이스케일 변환
    blur = cv2.GaussianBlur(gray, (5, 5), 0)  # 노이즈 제거를 위한 블러 적용
    ret, otsu = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)  # Otsu 이진화

    # 윤곽선 검출
    contours, hierarchy = cv2.findContours(otsu, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # 번호판 영역 검출
    plate_img = None
    for cnt in contours:
        x, y, width, height = cv2.boundingRect(cnt)
        aspect_ratio = width / float(height)  # 비율 계산
        if 2 < aspect_ratio < 5 and width > 100:  # 번호판 비율과 크기 필터링
            plate_img = image[y:y + height, x:x + width]  # 번호판 영역 추출
            cv2.rectangle(image, (x, y), (x + width, y + height), (0, 255, 0), 2)  # 원본 이미지에 사각형 그리기
            break  # 첫 번째 번호판만 처리

    # 번호판 이미지가 검출되었는지 확인
    if plate_img is not None:
        # 번호판에서 텍스트 추출
        plate_rgb = cv2.cvtColor(plate_img, cv2.COLOR_BGR2RGB)  # Tesseract는 RGB 이미지를 입력으로 받음
        text = pytesseract.image_to_string(plate_rgb, lang='kor+eng')  # OCR 처리
        print("번호판에서 추출된 텍스트:\n", text)

        # 번호판 이미지 출력
        plt.imshow(plate_rgb)
        plt.axis('off')
        plt.show()
    else:
        print("번호판을 찾을 수 없습니다.")

    # 결과 이미지 출력
    cv2.imshow('Detected Plate', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
