import json
data = { "name": "David",
     "class":"I",
     "age": 6  }
# print(type(data))
json_data = json.dumps(data)
print(json_data)
