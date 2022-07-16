def disarium(num):
    x=0
    while(num!=0):
        x=x+1
        num=num//10
    return x
n=int(input("Enter the number: "))
d=s=0
x=disarium(n)
copy=n
while(n>0):
    d=n%10
    s=s+int(d**x)
    n=n//10
    x=x-1
if (s==copy):
    print("Yes, this is a disarium number")
else:
    print("No, it is not a disarium number")
    
