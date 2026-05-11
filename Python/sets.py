s = {1,2,2,4}
empty_set = set()

print(type(empty_set))  
print(s)

#Set Methods

s.add(5)
s.remove(4)
# s.clear()

s.pop()
new=s.union({20,30,40})
new_in=s.intersection({1,2,30})

print(s)
print(new)
print(new_in)