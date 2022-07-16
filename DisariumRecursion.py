num=int(input("Enter a number: "))
s=0
def dis(a,n):
    global s
    if a!=0:
        s+=(a%10)**n
        dis(a//10,n-1)
dis(num,len(str(num)))
if num==s:
    print("Disarium")
else:
    print("Not disarium")
