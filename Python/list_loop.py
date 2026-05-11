nums = [1,2,63,14,5,19,10]

x=5
idx = 0

# Linear Search
for i in nums:
    if(i == x):
        print(f"{x} found at index = {idx}")
        break
    else:
        idx += 1

