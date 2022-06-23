from indecies.__dow__ import dow
from indecies.__sp500__ import sp500
from indecies.__xetra__ import xetra
import tkinter as tk

portalwindow = tk.Tk()
portalwindow.title("STOCK PREDICTOR")

def opendow():
    dow()
def opensp():
    sp500()
def openxetra():
    xetra()

dowbutton = tk.Button(text="DOW JONES", command=opendow, height=20, width=20)
dowbutton.pack(side=tk.LEFT)

spbutton = tk.Button(text="S&P 500", command=opensp, height=20, width=20)
spbutton.pack(side=tk.LEFT)

xetrabutton = tk.Button(text="XETRA DAX", command=openxetra, height=20, width=20)
xetrabutton.pack(side=tk.LEFT)

portalwindow.mainloop()
