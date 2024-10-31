import tkinter as tk
import tkinter.filedialog as fd
import PIL.Image
import PIL.ImageTk

def dispPhoto(path):
    newImage = PIL.image.open(path).resize((300,300))
    imageData=PIL.ImageTk.PhotoImage(newImage)
    imageLabel.configure(Image=imageData)
    imageLabel.image=imageData

def openFile():
    fpath=fd.askopenfilename()
    if fpath:
        dispPhoto(fpath)



root = tk.Tk()
root.geometry("400x350")

btn = tk.Button(text="파일열기", command=openFile)
imageLabel =tk.Label()
btn.pack()
imageLabel.pack()
tk.mainloop()
