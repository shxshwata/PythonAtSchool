import math
def randomNumGen(a,b):
    c=random.randrange(a,b)
    return int(c)
a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
print(randomNumGen(a,b))
