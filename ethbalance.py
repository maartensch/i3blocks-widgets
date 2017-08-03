#!/usr/bin/python
import requests
import json

response = requests.get('https://api.coinmarketcap.com/v1/ticker/ethereum/?convert=EUR&limit=10')
data = json.loads(response.text)[0]
with open("data/crypto_balance.json","r") as f:
    mybalance = json.loads("".join(f.readlines()))["eth"]

print('E%s' % int(float(data['price_eur']) * mybalance))
