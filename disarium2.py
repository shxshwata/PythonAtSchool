import math
def disarium(n):
    count=len(str(n))
    s=0
    copy=n
    while (copy!=0):
        d=copy%10
        s=(int)(s+math.pow(d,count))
        count+=1
        d=d/10
    if (s==n):
        return 1
    else:
        return 0
n=int(input("Enter the number: "))
if (disarium(n)==1):
    print("Yes, it is a Disarium number.")
else:
    print("No, it is NOT a Disarium number.")
