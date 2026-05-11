data = True
line = 1
word = "Python"

with open("five.txt","r") as f:
    
    while data:
        data = f.readline()
        if("python" in data):
            print(f"{word} found at line number {line}")
            break

        line += 1
    
