import os

with open("one.txt", "r") as f:
    print(f.read())

# --------------------------DELETE FILE--------------------------
os.remove("Sample2.txt")