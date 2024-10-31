import sklearn.datasets
import sklearn.svm
import PIL.Image
import numpy as np

def imagetoData(filename):
    grayImage=PIL.Image.open(filename).convert("L")
    grayImage=grayImage.resize((8,8))

    numImage=np.asarray(grayImage, dtype=float)
    numImage = np.floor(16-16*(numImage/256))
    numImage = numImage.flatten()
    return numImage

def prediction(data):
    digits=sklearn.datasets.load_digits()
    clf=sklearn.svm.SVC(gamma=0.001)
    clf.fit(digits.data, digits.target)
    n = clf.predict([data])
    print("예측", n)

data = imagetoData("C:\\Users\\user\\Downloads\\숫자이미지\\숫자(9).png")
prediction((data))