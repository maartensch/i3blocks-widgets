import json
import sys

if len(sys.argv) != 2:
    print("Usage: python netflower_reader.py [json]")
    exit()

with open(sys.argv[1],'r') as f:
    content = f.read()
    i = json.loads(content)
    print(i['Total'])
