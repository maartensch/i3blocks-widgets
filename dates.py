#!/usr/bin/python
import json,datetime
from os.path import dirname,abspath

dataPath = dirname(abspath(__file__)) + "/data"

with open(dataPath + '/dates.json','r') as f:
    text = f.read()
    data = json.loads(text)


weeks_until = 1
dates = []
now = datetime.datetime.now()
nowweek = now.isocalendar()[1]
nowyear = now.year
for key in data.iterkeys():
    #print(key,data[key])
    date = datetime.datetime.strptime(key,'%Y-%m-%d')
    week = date.isocalendar()[1]
    diff = nowweek - week
    if date.year == nowyear and diff < weeks_until and diff > -weeks_until:
        dates.append(date.day)

if len(dates) != 0:
    dates.sort()
    print "<span weight=\"bold\" color=\"#ff6600\">%s</span>" % ",".join(map(str,dates))
