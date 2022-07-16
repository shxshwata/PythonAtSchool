def primeFac(n):
    f=[]
    if n>1:
        i=2
        while (n%i)!=0:
            i=i+1
        f.append(i)
        f.extend(primeFac(n/i))
    return f
n=int(input("Enter the number: "))
print(primeFac(n))
        
