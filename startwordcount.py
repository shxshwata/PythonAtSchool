f=open("ABC.txt","w")
f.write("thermometer like no other")
f.close()
f=open("ABC.txt",'r')
s=f.read()
cw=0
for i in s:
    if i.startswith("the"):
        cw+=1
    if i.startswith("like")==True:
        cw+=1
    if i.startswith("their")==True:
        cw+=1
    if i.startswith("they")==True:
        cw+=1
print (cw)
        

