#!/usr/bin/python
import json,datetime
from os.path import dirname,abspath

dataPath = dirname(abspath(__file__)) + "/data"

with open(dataPath + '/dates.json','r') as f:
    text = f.read()
    data = json.loads(text)

dates = []
now = datetime.datetime.now()
nowweek = now.isocalendar()[1]
nowyear = now.year
for key,item in data.items():
    d = data[key]
    date = datetime.datetime.strptime(d,'%Y-%m-%d')
    week = date.isocalendar()[1]
    diff = nowweek - week
    if date.year == nowyear and diff < 3 and diff > -3:
        dates.append(date.day)

if len(dates) != 0:
    dates.sort()
    print("<span weight=\"bold\">%s</span>" % ",".join(map(str,dates)))
