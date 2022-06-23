from cProfile import label
from turtle import color
from click import command
import pandas as pd
from sklearn.tree import *
from sklearn.linear_model import *
import tkinter as tk
def xetra():

    window4 = tk.Tk()

    def xetrapredict():

        data = pd.read_csv('data/xetrahistoricalprices.csv')

        X = data.drop(columns=['Date'])
        del X[' Close']
        del X[' High']
        del X[' Low']

        Y = data[' Close']

        model = LinearRegression()
        model.fit(X, Y)
        predictions = model.predict([[ round(int(xetraentry.get()), 2) ], [ round(int(xetraentry.get()), 2)]])
        ansxetra = tk.Label(window4, text = "I PREDICT... \n" + str(predictions[1]))
        ansxetra.pack()

    intro = tk.Label(window4, text = "ENTER OPEN PRICE >")
    intro.pack()
    global xetraentry
    xetraentry = tk.Entry(window4)
    xetrapredictbutton = tk.Button(window4, text = "Predict!", command = xetrapredict)
    xetraentry.pack()
    xetrapredictbutton.pack()

    window4.mainloop()