import tkinter as tk
import tkinter.filedialog as fd
import PIL.Image
import PIL.ImageTk
import sklearn.datasets
import sklearn.svm
import numpy


# Convert image to numerical data (grayscale)
def imageToData(filename):
    grayImage = PIL.Image.open(filename).convert("L")
    grayImage = grayImage.resize((8, 8))
    dispImage = PIL.ImageTk.PhotoImage(grayImage.resize((150, 150)))

    return grayImage, dispImage


# Load image in original color
def loadOriginalImage(filename):
    colorImage = PIL.Image.open(filename)
    colorImage = colorImage.resize((150, 150))
    dispImage = PIL.ImageTk.PhotoImage(colorImage)

    return dispImage


# Predict digit from the image data
def predictDigits(data):
    digits = sklearn.datasets.load_digits()
    clf = sklearn.svm.SVC(gamma=0.001)
    clf.fit(digits.data, digits.target)
    n = clf.predict([data])
    return n[0]


# Open two files and predict digits for one and display another in color
def openFiles():
    filepaths = fd.askopenfilenames(filetypes=[("Image files", "*.jpg *.jpeg *.png")], title="두개의 이미지를 선택해주세요",
                                    multiple=True)
    if len(filepaths) == 2:
        # Process first image (grayscale for digit prediction)
        grayImage1, dispImage1 = imageToData(filepaths[0])
        imageLabel1.configure(image=dispImage1)
        imageLabel1.image = dispImage1
        numImage1 = numpy.asarray(grayImage1, dtype=float)
        numImage1 = numpy.floor(16 - 16 * (numImage1 / 256))
        numImage1 = numImage1.flatten()
        prediction1 = predictDigits(numImage1)

        # Load second image in original color
        dispImage2 = loadOriginalImage(filepaths[1])
        imageLabel2.configure(image=dispImage2)
        imageLabel2.image = dispImage2

        textLabel.configure(text=f"첫 번째 이미지는: {prediction1}, 두 번째 이미지는 원본으로 표시됩니다.")
    else:
        textLabel.configure(text="Please select exactly two images.")


# GUI setup
root = tk.Tk()
root.geometry("600x600")

btn = tk.Button(root, text="Open Images", command=openFiles)
imageLabel1 = tk.Label(root)
imageLabel2 = tk.Label(root)
textLabel = tk.Label(root, text="This program recognizes handwritten digits.")

# Place widgets
btn.pack()
imageLabel1.pack()
imageLabel2.pack()
textLabel.pack()

tk.mainloop()
