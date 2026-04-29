def cal_fact(n):
    fact=1
    for i in range(1,n+1):
        fact *= i

    return fact

n = int(input("Enter your number: "))
print(cal_fact(n))