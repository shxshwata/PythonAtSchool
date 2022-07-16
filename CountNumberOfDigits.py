f=open("DIGIT.txt","w")
f.write("FC Barcelona: Leo Messi 2000-2021")
f.close()
f=open("DIGIT.txt","r")
s=f.read()
cd=0
for i in s:
    if i.isdigit():
        cd+=1
print("Number of digits: ",cd)
