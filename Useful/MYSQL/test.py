import json

f = open("data.json",'r')
obj = json.load(f)
print(obj)
f.close()
