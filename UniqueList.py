def uniqueList(l):
    k=[]
    for i in l:
        if i not in k:
            k.append(i)
    return k
l=eval(input("Enter the elements: "))
print(uniqueList(l))
