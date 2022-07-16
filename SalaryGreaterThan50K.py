import pickle
e1={'Empno':"EO1",'Name':"Ayush",'City':"Delhi",'Salary':65000}
e2={'Empno':"EO2",'Name':"Shreya",'City':"Mumbai",'Salary':54000}
e3={'Empno':"EO3",'Name':"Rahul",'City':"Delhi",'Salary':76000}
e4={'Empno':"EO4",'Name':"Kavya",'City':"Kolkata",'Salary':43000}
l={}
found=False
f=open("Emp.dat","wb")
pickle.dump(e1,f)
pickle.dump(e2,f)
pickle.dump(e3,f)
pickle.dump(e4,f)
f.close()
with open("Emp.dat","rb") as f:
    l=pickle.load(f)
    if l['Salary']>50000:
        if l['City']=="Delhi":
            print (l)
        found=True
if found==False:
    print("No records found.")
else:
    print("Search successful.")
