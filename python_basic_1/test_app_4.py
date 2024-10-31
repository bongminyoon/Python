import pytesseract
import cv2
import matplotlib.pyplot as plt

# Tesseract 경로 설정 (Windows에서 필요한 경우)
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\user\Desktop\ybm\tess\tesseract.exe'

# 이미지 파일 경로 수정
path = r"C:/Users/user/Desktop/ybm/123.png"
# 이미지 읽기
image = cv2.imread(path)

# 이미지가 정상적으로 읽혔는지 확인
if image is None:
    print("이미지를 열 수 없습니다. 경로를 확인하세요.")
else:
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # OCR로 텍스트 인식
    text = pytesseract.image_to_string(rgb_image, lang='kor')
    print("추출된 텍스트:\n", text)

    # 이미지 출력 (확인용)
    plt.imshow(rgb_image)
    plt.axis('off')  # 축 제거
    plt.show()
