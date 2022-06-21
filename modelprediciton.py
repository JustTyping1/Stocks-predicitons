from sklearn.tree import *
from sklearn.linear_model import *
import pandas as pd

class Predict():
    def __init__(self, open, high, low):
        self.open = open
        self.high = high
        self.low = low
    def predictdow(self):
        data = pd.read_csv('HistoricalPrices.csv')

        X = data.drop(columns=['Date'])
        del X[' Close']

        Y = data[' Close']

        model = DecisionTreeClassifier()
        model.fit(X, Y)
        predictions = model.predict([ [self.open, self.high, self.low] ])
        return predictions

newModel = Predict(20000, 30000, 20000)

print(newModel.predictdow)