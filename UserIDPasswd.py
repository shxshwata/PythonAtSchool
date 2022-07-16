import csv
a=[["userid1","passwd1"],
   ["userid2","passwd2"],
   ["userid3","passwd3"],
   ["userid4","passwd4"],
   ["userid5","passwd5"]]
u=input("Enter your User ID: ")
f=open("userinfo.csv","w+")
f1=csv.writer(f)
f1.writerows(a)
f.seek(0)
f2=open("userinfo.csv","r")
r=csv.reader(f2)
for i in r:
    if i[0]==u:
        print("Your password is: ",i[1])
f.close()
