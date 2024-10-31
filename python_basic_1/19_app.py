import tkinter as tk
import tkinter.filedialog as fd
import PIL.Image
import PIL.ImageTk

import sklearn.datasets
import sklearn.svm
import numpy as np

def imagetoData(filename):
    grayImage=PIL.Image.open(filename).convert("L")
    grayImage=grayImage.resize((8,8))

    dispImage=PIL.ImageTk.PhotoImage(grayImage.resize((300,300)))
    imageLabel.configure(image=dispImage)
    imageLabel.image=dispImage

    numImage = np.asarray(grayImage, dtype=float)
    numImage = np.floor(16 - 16 * (numImage / 256))
    numImage = numImage.flatten()
    return numImage



def prediction(data):
    digits=sklearn.datasets.load_digits()
    clf=sklearn.svm.SVC(gamma=0.001)
    clf.fit(digits.data, digits.target)
    n = clf.predict([data])
    textLabel.configure(text = " 이 그림은 " +str(n)+"입니다.")


def openFile():
    fpath=fd.askopenfilename()
    if fpath:
        data = imagetoData(fpath)
        prediction(data)


root = tk.Tk()
root.geometry("400x350")

btn = tk.Button(root, text="파일열기", command=openFile)
imageLabel =tk.Label()

btn.pack()

imageLabel.pack()

textLabel = tk.Label(text="손글씨 숫자를 인식합니다")
textLabel.pack()

tk.mainloop()
