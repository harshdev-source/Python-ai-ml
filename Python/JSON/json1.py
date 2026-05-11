import json

py_obj = {
    "name":"Harsh",
    "isTeacher":True,
    "salary":"null"
}

json_string = json.dumps(py_obj)
print(f"{type(json_string)},\n {json_string}")



json_str =  '{"name":"Harsh", "isTeacher":true}'  #its in json string
py_object = json.loads(json_str)

print(type(json_str))
print(f"{type(py_object)},\n{py_object}")