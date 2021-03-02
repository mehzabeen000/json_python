import json
shopping_list = {
    "shopping_list":
        { 
            "choco":"15",
            "Biscuits":"50",
            "ice_cream":"20",
            "Diary_milk":"30",
        } 
}
out_file = open("shopping_list.json","w")
json.dump(shopping_list,out_file)
# out_file.close()
item = input("enter any item : ")
quantity = int(input("enter the quantity : "))
mydict = {}
new_shopping_list = {}
mydict[item] = quantity
for i in shopping_list:
    for j in shopping_list[i]:
        for k in mydict:
            if j != k:
                new_shopping_list[j] = shopping_list[i][j]
                if k not in shopping_list[i]:
                    new_shopping_list[k]=mydict[k]
out_file = open("new_shopping_list.json","w")
json.dump(new_shopping_list,out_file)
out_file.close()


