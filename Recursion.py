def sum(n):
    if n==1:
        return 1
    elif n==0:
        return 0
    else:
        return (n+sum(n-1))
n=int(input("Enter a number: "))
print("Sum of the first ",n," natural numbers is ",sum(n))
