f = open("four.txt", "r+" ) #Starting ke texts ko replace krdega
f = open("four.txt", "a+" ) #End mei texts add karega

f.write("123")
print(f.read())

f.close()
