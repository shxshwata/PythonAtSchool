from functools import lru_cache
@lru_cache()
def fibo(n):
    if (n==1):
        return 0
    elif (n==2 or n==3):
        return 1
    elif (n>3):
        return fibo(n-1)+fibo(n-2)
for n in range(1,101):
    print(n,":",fibo(n))
