from __dow__ import dow
from __sp500__ import sp500
from __xetra__ import xetra
import tkinter as tk

portalwindow = tk.Tk()

def opendow():
    dow()
def opensp():
    sp500()
def openxetra():
    xetra()

dowbutton = tk.Button(text="DOW JONES", command=opendow, height=20, width=20)
dowbutton.pack()

spbutton = tk.Button(text="S&P 500", command=opensp, height=20, width=20)
spbutton.pack()

xetrabutton = tk.Button(text="XETRA DAX", command=openxetra, height=20, width=20)
xetrabutton.pack()

portalwindow.mainloop()
