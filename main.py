import pandas as pd
from sklearn.tree import *
from sklearn.linear_model import *
import matplotlib as plt

def predict(open, high, low):

    data = pd.read_csv('HistoricalPrices.csv')

    X = data.drop(columns=['Date'])
    del X[' Close']

    Y = data[' Close']

    model = DecisionTreeClassifier()
    model.fit(X, Y)
    predictions = model.predict([ [open, high, low] ])
    print(predictions)

predict(20000, 30000, 20000)
        