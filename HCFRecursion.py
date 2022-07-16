n1=int(input("Enter number: "))
n2=int(input("Enter number: "))
def hcf(num):
    if (n1%n1==0) and (n2%n2==0):
        return num
    else:
        return (hcf(num-1))
if n1<n2:
    n1,n2=n2,n1
print(hcf(n2))
