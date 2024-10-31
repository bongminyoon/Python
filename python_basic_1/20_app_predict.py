import tkinter as tk
import tkinter.filedialog as fd
import PIL.Image
import PIL.ImageTk

import sklearn.datasets
import sklearn.svm
import numpy as np


def imagetoData(filename):
    # 이미지를 흑백으로 변환하고 8x8로 리사이즈
    grayImage = PIL.Image.open(filename).convert("L")
    grayImage = grayImage.resize((8, 8))

    # 표시할 이미지를 300x300으로 리사이즈
    dispImage = PIL.ImageTk.PhotoImage(grayImage.resize((300, 300)))
    imageLabel.configure(image=dispImage)
    imageLabel.image = dispImage  # 가비지 컬렉션 방지

    # 이미지를 16단계로 변환하여 숫자 데이터로 변경
    numImage = np.asarray(grayImage, dtype=float)
    numImage = np.floor(16 - 16 * (numImage / 256))
    numImage = numImage.flatten()
    return numImage


def prediction(data):
    # 숫자 데이터셋 불러오기 및 SVM 모델 학습
    digits = sklearn.datasets.load_digits()
    clf = sklearn.svm.SVC(gamma=0.001)
    clf.fit(digits.data, digits.target)

    # 이미지 데이터에 대한 예측
    n = clf.predict([data])

    # 예측 결과를 레이블에 표시
    resultLabel.config(text=f"예측 결과: {n[0]}")


def openFile():
    # 파일 열기 대화상자
    fpath = fd.askopenfilename()
    if fpath:
        data = imagetoData(fpath)  # 이미지 데이터 변환
        prediction(data)  # 예측 수행


# Tkinter 윈도우 생성
root = tk.Tk()
root.geometry("400x400")

# 버튼, 이미지, 결과 레이블 생성
btn = tk.Button(root, text="파일 열기", command=openFile)
imageLabel = tk.Label(root)
resultLabel = tk.Label(root, text="예측 결과: ")

# 위젯 배치
btn.pack()
imageLabel.pack()
resultLabel.pack()

# Tkinter 이벤트 루프 실행
tk.mainloop()
