import json
file1 = open("text.txt","r")
dict1={}
for i in file1:
    #splitting the data into keys and values and storing them in dictionary
    keys,values = i.split(None,1)
    dict1[keys]=values.strip()
print(dict1)
json_file = open("json_file.json","w")
json.dump(dict1,json_file)
json_file.close()
file1.close()
