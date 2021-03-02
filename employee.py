import json
file1 = open("employee.txt","r")
dict1={}
l=1
for i in file1:
    info = list( i.strip().split(None, 4)) 
    print(info)
    auto_id = "emp"+str(l)
    dict2={}
    data = ["name","designation","age","salary"]
    i=0
    while i<len(data):
        dict2[data[i]]=info[i]
        i+=1
    dict1[auto_id]=dict2
    l+=1
print(dict1)
file1.close()
file2 = open("employee.json","w")
json.dump(dict1,file2)
file2.close()