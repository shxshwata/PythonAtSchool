source=open("source.txt","r")
target=open("target.txt","w")
f=source.readlines()
for i in f:
    if i[0]!="@":
        target.write(i)
source.close()
target.close()
    
