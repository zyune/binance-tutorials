
from binance.client import Client
import config
import numpy as np
proxies = {
    'http': 'http://127.0.0.1:1087',
    'https': 'http://127.0.0.1:1087'
}

# in the Client instantiation
client = Client(config.API_KEY,config.API_SECRET, {'proxies': proxies})
# info = client.get_account()
# balances=info['balances']
exchange_info = client.get_exchange_info();
subols = exchange_info['symbols']
# np.savetxt("data.txt",subols)
f = open('test.txt','w')

f.write(subols)

f.close()
print(subols)
