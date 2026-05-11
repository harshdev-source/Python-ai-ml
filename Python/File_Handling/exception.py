try:
    x = int(input("Enter x: "))
    answer = 10/x

except ZeroDivisionError:
    print(f"Divide by 0 is not allowed")

except ValueError:
    print(f"Invalid input")

else:
    print(f"Ans = {answer}")

finally:
    print("End of program")

#--------------------------LIST COMPREHENSIONS--------------------------
square = []

for i in range(6):
    square.append(i*i)

print(square)


sq = [i*i for i in range(6) if i%2!=0] #LIST COMPREHENSIONS 
print(sq)