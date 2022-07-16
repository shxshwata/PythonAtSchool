def sumDigits(n):
    s=0
    while (n>0):
        s+=n%10
        n=n//10
    return s
def sortingArray(arr,n):
    k=[]
    for i in range(n):
        k.append(sumDigits(arr[i],arr[i]))
    k.sort()
    for i in range(len(k)):
        print(k[i][1],end=" ")
arr=input("Enter the list of elements: ")
n=len(arr)
print(sortingArray(arr,n))
