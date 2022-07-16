#factorial.py
def fac(n):
    s=0
    while n!=0:
        d=1
        k=n%10
        for i in range(1,k+1):
            d=d*i
        s=s+d
        n=n//10
    return s
n=120
print(s)
