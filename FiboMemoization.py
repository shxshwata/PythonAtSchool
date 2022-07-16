fibo_cache = {}
def fibo(n):
    # if we have cached the value, then return it
    if n in fibo_cache:
        return fibo_cache[n]
    #compute the nth term
    if (n==1):
        value=0
    elif (n==2 or n==3):
        value=1
    elif (n>3):
        value=fibo(n-1)+fibo(n-2)
    # cache the value and return it
    fibo_cache[n]=value
    return value
for n in range(1,101):
    print(n,":",fibo(n))
