from cProfile import label
from turtle import color
from click import command
import pandas as pd
from sklearn.tree import *
from sklearn.linear_model import *
import tkinter as tk
def dow():

    window = tk.Tk()

    def dowpredict():

        data = pd.read_csv('HistoricalPrices.csv')

        X = data.drop(columns=['Date'])
        del X[' Close']
        del X[' High']
        del X[' Low']

        Y = data[' Close']

        model = LinearRegression()
        model.fit(X, Y)
        predictions = model.predict([[ int(dowentry.get()) ], [int(dowentry.get())]])
        ansdow = tk.Label(text = "I PREDICT... \n" + str(predictions[1]))
        ansdow.pack()

    intro = tk.Label(text = "ENTER OPEN PRICE >")
    intro.pack()
    global dowentry
    dowentry = tk.Entry()
    dowpredictbutton = tk.Button(text = "Predict!", command = dowpredict)
    dowentry.pack()
    dowpredictbutton.pack()

    window.mainloop()