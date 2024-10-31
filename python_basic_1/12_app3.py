import tkinter as tk
import random

def displabel():
    list_unse= ["대길", "중길", "소길", "흉"]
    lbl.configure(text=random.choice(list_unse))

root= tk.Tk()
root.geometry("500x500")

lbl=tk.Label(text="LABEL",foreground="red",background="blue")
btn=tk.Button(text="PUSH", command=displabel)

lbl.pack()
btn.pack()
tk.mainloop()




