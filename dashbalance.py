#!/usr/bin/python
import requests
import json
from os.path import dirname,abspath

response = requests.get('https://api.coinmarketcap.com/v1/ticker/dash/?convert=EUR&limit=10')
data = json.loads(response.text)[0]
d = dirname(abspath(__file__))
with open(d+"/data/crypto_balance.json","r") as f:
    mybalance = json.loads("".join(f.readlines()))["dash"]

print('D%s' % int(float(data['price_eur']) * mybalance))
