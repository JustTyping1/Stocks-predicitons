from cProfile import label
from turtle import color
from click import command
import pandas as pd
from sklearn.tree import *
from sklearn.linear_model import *
import tkinter as tk
def dow():

    window = tk.Tk()
    window.title("DOW JONES IND. AVG.")

    def dowpredict():

        data = pd.read_csv('data/dowjoneshistoricalprices.csv')

        X = data.drop(columns=['Date'])
        del X[' Close']
        del X[' High']
        del X[' Low']

        Y = data[' Close']

        model = LinearRegression()
        model.fit(X, Y)
        predictions = model.predict([[ round(int(dowentry.get()), 2) ], [round(int(dowentry.get()), 2)]])
        ansdow = tk.Label(window, text = "I PREDICT... \n" + str(predictions[1]))
        ansdow.pack()

    intro = tk.Label(window, text = "ENTER OPEN PRICE >")
    intro.pack()
    global dowentry
    dowentry = tk.Entry(window)
    dowpredictbutton = tk.Button(window, text = "Predict!", command = dowpredict)
    dowentry.pack()
    dowpredictbutton.pack()

    window.mainloop()