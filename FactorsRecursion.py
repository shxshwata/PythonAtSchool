i=1
def factors(n,i):
    if (i<=n):
        if ((n%i)==0):
            print(i)
        factors(n,(i+1))
n=int(input("Enter the number: "))
factors(n,i)
