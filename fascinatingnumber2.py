n=int(input("Enter the number: "))
val=' '
val=(str(n)+str(n*2)+str(n*3))
c=0
for i in val:
    if val.count(i)!=1:
        c=1
        break

if c==0:
    print("Facinating number")
else:
    print("Not a fascinating number")
