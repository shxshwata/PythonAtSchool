import math
def largestprimefac(n):
    a=-1
    for i in range (2,n//2+1):
        while n%i == 0:
            a=i
            n=n//i
    return int(a)

n= int (input("Enter the number: "))
print (largestprimefac(n))
