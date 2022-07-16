rev=0
def pal(n):
    global rev
    if n>0:
        r=n%10
        rev=(rev*10)+r
        pal(int(n/10))
    return rev
n=int(input("Enter the number: "))
n1=pal(n)
if n1==n:
    print("Palindrome")
else:
    print("Not palindrome")
