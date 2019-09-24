import json
from pprint import pprint

with open('apple.json') as f:
    data = json.load(f)

#pprint(data)
print(type(data))

i = iter(data)
b = dict(zip(i, i))
print(b)