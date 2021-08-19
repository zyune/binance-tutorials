import backtrader as bt
import datetime

class RSIStrategy(bt.Strategy):

    def __init__(self):
        self.rsi = bt.talib.RSI(self.data, period=14)

    def next(self):
        if self.rsi < 30 and not self.position:
            self.buy(size=1)
        
        if self.rsi > 70 and self.position:
            self.close()


cerebro = bt.Cerebro()

fromdate = datetime.datetime.strptime('2021-01-01', '%Y-%m-%d')
todate = datetime.datetime.strptime('2020-08-17', '%Y-%m-%d')

data = bt.feeds.GenericCSVData(dataname='doge_data/2020_1d.csv', dtformat=2, compression=15, timeframe=bt.TimeFrame.Minutes, fromdate=fromdate, todate=todate)

cerebro.adddata(data)

cerebro.addstrategy(RSIStrategy)

cerebro.run()

cerebro.plot()