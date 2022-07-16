l1=eval(input("Enter list 1:"))
l2=eval(input("Enter list 2:"))
c=[]
d=[]
for i in l1:
    f=0
    for j in l2:
        if i==j:
            c.append(i)
            f=1
    if f==0:
        d.append(i)
print("Intersection: ",c)
print("List L1-L2: ",d)
