import json
data = {"name": "David", "class": 7, "age": 6}
end = json.dumps(data)
print(end)
print(type(end))