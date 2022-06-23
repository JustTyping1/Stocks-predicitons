from cProfile import label
from turtle import color
from click import command
import pandas as pd
from sklearn.tree import *
from sklearn.linear_model import *
import tkinter as tk
def sp500():

    window3 = tk.Tk()

    def sppredict():

        data = pd.read_csv('data/sp500historicalprices.csv')

        X = data.drop(columns=['Date'])
        del X[' Close']
        del X[' High']
        del X[' Low']

        Y = data[' Close']

        model = LinearRegression()
        model.fit(X, Y)
        predictions = model.predict([[ round(int(spentry.get()), 2) ], [ round(int(spentry.get()), 2)]])
        anssp = tk.Label(window3, text = "I PREDICT... \n" + str(predictions[1]))
        anssp.pack()

    intro = tk.Label(window3, text = "ENTER OPEN PRICE >")
    intro.pack()
    global spentry
    spentry = tk.Entry(window3)
    sppredictbutton = tk.Button(window3, text = "Predict!", command = sppredict)
    spentry.pack()
    sppredictbutton.pack()

    window3.mainloop()