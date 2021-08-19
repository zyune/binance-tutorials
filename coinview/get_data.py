import config, csv
from binance.client import Client

client = Client(config.API_KEY, config.API_SECRET)
proxies = {
    'http': 'http://127.0.0.1:1087',
    'https': 'http://127.0.0.1:1087'
}
# prices = client.get_all_tickers()

# for price in prices:
#     print(price)

csvfile = open('2021_15min_519_817.csv', 'w', newline='') 
candlestick_writer = csv.writer(csvfile, delimiter=',')

#candlesticks = client.get_historical_klines("DOGEUSDT", Client.KLINE_INTERVAL_15MINUTE, "1 Jan, 2021", "17 Aug, 2021")
candlesticks = client.get_historical_klines("DOGEUSDT", Client.KLINE_INTERVAL_1DAY, "19 May, 2021", "17 Aug, 2021")
#candlesticks = client.get_historical_klines("DOGEUSDT", Client.KLINE_INTERVAL_1DAY, "1 Jan, 2017", "12 Jul, 2020")

for candlestick in  candlesticks:
    candlestick[0] = candlestick[0] / 1000
    candlestick_writer.writerow(candlestick)

csvfile.close()
