a=int(input("Enter base number: "))
b=int(input("Enter exponent number: "))
def power(n):
    if n==0:
        return 1
    else:
        return(a*power(n-1))
print(power(b))
