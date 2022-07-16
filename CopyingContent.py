file=open("DATA2.txt","r")
c=file.read().split()
c=[]
for i in file:
    c.append(i)
print(c)
