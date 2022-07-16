t=int(input("Enter the number of terms: "))
def tribo(n):
    if n==0 or n==1:
        return 0
    elif n==2:
        return 1
    else:
        return(tribo(n-1)+tribo(n-2)+tribo(n-3))
for i in range(0,t):
    print(tribo(i),end=" ")
