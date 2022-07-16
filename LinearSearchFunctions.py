def linearSearch(a,s):
    k=[]
    for i in range(len(a)):
        if s==a[i]:
            k.append(i+1)
    if len(k)==0:
        print("Element not found")
    else:
        print("Index: ",k)
a=eval(input("Enter the elements: "))
s=int(input("Enter search element: "))
linearSearch(a,s)
