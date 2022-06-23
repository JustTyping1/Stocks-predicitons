from __dow__ import dow
import tkinter as tk

portalwindow = tk.Tk()

def opendow():
    dow()

dowbutton = tk.Button(text="DOW JONES", command=opendow, height=20, width=20)
dowbutton.pack()

portalwindow.mainloop()
