def bsearch(arr,x):
    a=0
    b=len(arr)-1
    c=0

    while a<=b:
        c=(a+b)//2
        if arr[c]<x:
            a=b+1
        elif arr[c]>x:
            b=a-1
        else:
            return c
    return -1
arr=[]
n=int(input("Enter the number of elements: "))
for i in range(0,n):
    num=int(input("Enter the element: "))
    arr.append(num)
x=int(input("Enter the number whose index you want to search: "))
s=bsearch(arr,x)
if s!=-1:
    print("Index: ",str(s))
else:
    print("Not present")
            
