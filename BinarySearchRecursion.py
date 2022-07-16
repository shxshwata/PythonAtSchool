def binary(l,low,high,n):
    if low<=high:
        mid=(low+high)//2
        if l[mid]==n:
            return mid
        elif l[mid]>n:
            return binary(l,low,(mid-1),n)
        else:
            return binary(l,(mid+1),high,n)
l=eval(input("Enter a list of numbers:"))
n=int(input("Enter the element to be searched: "))
k=binary(l,0,(len(l)-1),n)
print("Element present at index:",(k+1))

