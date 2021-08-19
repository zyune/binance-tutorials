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
#https://www.backtrader.com/blog/posts/2015-08-04-generic-csv-datafeed/generic-csv-datafeed/
# fromdate = datetime.datetime.strptime('2021-01-01', '%Y-%m-%d')
# todate = datetime.datetime.strptime('2020-08-17', '%Y-%m-%d')

#data = bt.feeds.GenericCSVData(dataname='doge_data/2021_15minutes.csv', dtformat=2, compression=15, timeframe=bt.TimeFrame.Minutes, fromdate=fromdate, todate=todate)
data = bt.feeds.GenericCSVData(dataname='doge_data/2021_15min_519_817.csv', dtformat=2, compression=15,)
cerebro.adddata(data)

cerebro.addstrategy(RSIStrategy)

cerebro.run()

cerebro.plot()