fin=open("F1.txt","r")
s=fin.read().split()
uc=lc=dc=0

for x in s:
    if (x[0].isupper()):
        uc+=1
    elif(x[0].islower()):
        lc+=1
    elif(x[0].isdigit()):
        dc+=1

print("uc= ",uc,"lc= ",lc,"dc= ",dc)
fin.close()
