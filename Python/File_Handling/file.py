f = open("one.txt","r")  
# -----------------------------------File Reading-----------------------------------

# data = f.read()
# print(data)

dataline = f.readline()
print(dataline)

dataline = f.readline()
print(dataline)


f.close()