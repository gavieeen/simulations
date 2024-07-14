import numpy as np
from datetime import datetime
import backtrader as bt
import yfinance as yf

class LinearRegression:
    def __init__(self):
        self.slope = None
        self.intercept = None

    def fit(self, X, y):
        """
        Fit the linear regression model to the data.

        Parameters:
        - X: Independent variable (features)
        - y: Dependent variable (target)
        """
        x_mean = np.mean(X)
        y_mean = np.mean(y)

        numerator = 0
        denominator = 0

        for i in range(len(X)):
            numerator += (X[i] - x_mean) * (y[i] - y_mean)
            denominator += (X[i] - x_mean) ** 2

        self.slope = numerator / denominator
        self.intercept = y_mean - (self.slope * x_mean)

    def predict(self, X):
        """
        Predict the target variable for new data points.

        Parameters:
        - X: New data points (features)

        Returns:
        - Predicted target variable
        """
        return self.slope * X + self.intercept

class LinearRegressionStrategy(bt.Strategy):
    params = (
        ("lookback_period", 30),
    )

    def __init__(self):
        self.lr = LinearRegression()
        self.data_close = self.datas[0].close
        self.data_high = self.datas[0].high
        self.data_low = self.datas[0].low
        self.data_open = self.datas[0].open
        self.data_volume = self.datas[0].volume

    def next(self):
        if len(self.data_close) > self.params.lookback_period:
            X = np.arange(0, self.params.lookback_period)
            y = np.array(self.data_close.get(size=self.params.lookback_period))

            self.lr.fit(X, y)
            predicted_price = self.lr.predict(self.params.lookback_period)

            current_price = self.data_close[0]

            if predicted_price > current_price:
                self.buy()
            elif predicted_price < current_price:
                self.sell()

if __name__ == '__main__':
    cerebro = bt.Cerebro()

    # Add your custom strategy here
    cerebro.addstrategy(LinearRegressionStrategy)
    
    # Download data from Yahoo Finance
    nvda_data = yf.download("NVDA", start="2018-01-01", end="2018-12-31")

    # Convert data to PandasData for backtrader
    data = bt.feeds.PandasData(dataname=nvda_data)
    cerebro.adddata(data)
    cerebro.broker.setcash(1000.0)
    # cerebro.addobserver(bt.observers.BuySell)
    cerebro.addobserver(bt.observers.Value)

    print(f'Starting Portfolio Value: {cerebro.broker.getvalue():.2f}')
    cerebro.run()
    print(f'Final Portfolio Value: {cerebro.broker.getvalue():.2f}')
    cerebro.plot(iplot=True, volume=False)
