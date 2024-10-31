import tkinter as tk

def displabel():
    lbl.configure(text="안녕하세요")

root=tk.Tk()
root.geometry("1000x500")

lbl=tk.Label(text="레이블", foreground="red",background="blue")
btn=tk.Button(text="누르기", command=displabel)



lbl.pack()
btn.pack()
tk.mainloop()