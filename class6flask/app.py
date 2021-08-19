from flask import Flask, render_template, url_for
from binance.client import Client
import config
from binance.enums import *
app = Flask(__name__)
proxies = {
    'http': 'http://127.0.0.1:1087',
    'https': 'http://127.0.0.1:1087'
}

# in the Client instantiation
client = Client(config.API_KEY,config.API_SECRET, {'proxies': proxies})


@app.route('/')
def index():
    title = "coinviewYYY"
    info = client.get_account()
    exchange_info = client.get_exchange_info()
    symbols = exchange_info['symbols']
    
    # print(exchange_info)
    balances = info['balances']
    return render_template('iiindex.html', title=title,my_balances=balances, symbols=symbols) 
@app.route('/buy', methods = ['POST'])
def buy():
    order = client.create_order(
    symbol='BNBBTC',
    side=SIDE_BUY,
    type=ORDER_TYPE_LIMIT,
    timeInForce=TIME_IN_FORCE_GTC,
    quantity=100,
    price='0.00001')
    return
