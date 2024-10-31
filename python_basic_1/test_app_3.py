import pytesseract
import cv2
import matplotlib.pyplot as plt
import re  # 정규 표현식 사용

# Tesseract 경로 설정
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\user\Desktop\ybm\tess\tesseract.exe'

# 이미지 파일 경로 수정
path = r"C:/Users/user/Desktop/ybm/OIP.jpg"

# 이미지 읽기
image = cv2.imread(path)

# 이미지가 정상적으로 읽혔는지 확인
if image is None:
    print("이미지를 열 수 없습니다. 경로를 확인하세요.")
else:
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # OCR로 텍스트 인식
    text = pytesseract.image_to_string(rgb_image, lang='kor')  # 한국어와 영어 인식
    text = text.strip()  # 공백 제거
    print("추출된 텍스트:\n", text)

    # 7자리 텍스트 확인
    if len(text) >= 8:
        # 4번째 자리를 강제로 한글로 설정
        fixed_text = text[:3] + '가' + text[4:7]  # 4번째 자리를 '가'로 설정

        print("수정된 텍스트:\n", fixed_text)

        # 4번째 자리가 한글인지 확인
        if re.search(r'[가-힣]', fixed_text[3]):
            print("4번째 자리가 한글로 설정되었습니다.")
        else:
            print("4번째 자리가 한글로 설정되지 않았습니다.")
    else:
        print("인식된 텍스트가 너무 짧습니다.")

    # 이미지 출력 (확인용)
    plt.imshow(rgb_image)
    plt.axis('off')  # 축 제거
    plt.show()
