c=0
def count(n):
    global c
    if(n > 0):
        c=c+1
        count(n//10)
    return c

Number = int(input("Enter any Number: "))
c = count(Number)
print(c)
