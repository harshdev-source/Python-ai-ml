import json

pydata = {
    "Name":"Harsh",
    "city":"Mumbai",
    "age":69,
    "Salary":"none"
}


#-----------------------------------------Reading a Json file-----------------------------------------
# with open("data2.json","r") as f:
#     py_object = json.load(f)

#     print(f"{py_object}\n ,{type(py_object)},")


# -----------------------------------------Overwritng a Json file-----------------------------------------
with open("data2.json", "w") as f:
    json.dump(pydata,f, indent =3 , sort_keys =True) 