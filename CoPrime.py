def factors(m,n):
    l=[]
    for i in range(1,min([m,n])+1):
        if m%i==0 and n%i==0:
            l.append(i)
        return (l)
def coprime (lst):
    if len(lst)==1:
        print("Coprime")
    else:
        print("Not Coprime")
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
coprime(factors(a,b))
