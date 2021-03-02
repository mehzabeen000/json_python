import json
json_data =  '{ "Name":"David", "Class":"I", "Age":6 }'
python_obj = json.loads(json_data)
print("JSON data:")
print(python_obj)
print("\nName: ",python_obj["Name"])
print("Class: ",python_obj["Class"])
print("Age: ",python_obj["Age"]) 