#!/usr/bin/python
import requests
import json
from os.path import dirname,abspath

response = requests.get('https://api.coinmarketcap.com/v1/ticker/ark/?convert=EUR&limit=10')
data = json.loads(response.text)[0]

d = dirname(abspath(__file__))
with open(d + "/data/crypto_balance.json","r") as f:
    mybalance = json.loads("".join(f.readlines()))["ark"]

priceInEuro = float(data['price_eur'])
print('%s' % round(priceInEuro,2))
