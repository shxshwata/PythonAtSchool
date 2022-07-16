def factorial(n):
    if n<2:
        return 1
    return n*factorial(n-1)
#__main__
n=int(input("Enter a number(>0):"))
print("Factorial of ",n,"is ",factorial(n))
