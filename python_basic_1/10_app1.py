import tkinter as tk

root = tk.Tk()
root.geometry("200x100")

lbl = tk.Label(text="LABEL")
btn = tk.Button(text="PUSh")

lbl.pack()
btn.pack()
tk.mainloop()