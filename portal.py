from __dow__ import dow
from __sp500__ import sp500
import tkinter as tk

portalwindow = tk.Tk()

def opendow():
    dow()
def opensp():
    sp500()

dowbutton = tk.Button(text="DOW JONES", command=opendow, height=20, width=20)
dowbutton.pack()

spbutton = tk.Button(text="S&P 500", command=opensp, height=20, width=20)
spbutton.pack()

portalwindow.mainloop()
