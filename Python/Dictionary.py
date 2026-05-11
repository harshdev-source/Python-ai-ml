info = {
    "name" : "harsh",
    "cgpa" : 9.3,
    "Subjects" : ["Maths", "Science"],
    3.14 : "PI"
}

print(type(info))
print(info["name"])

# dictionary methods

print(info.keys())
print(info.values())
print(info.items())
print(info.get(9.3))

info.update({
    "city" : "Ranchi"
})

print(info)
