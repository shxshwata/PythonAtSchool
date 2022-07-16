import pickle
emp={}
found=False
fin=open("emp1.dat","rb+")
fin.seek(0)
try:
    while True:
        pos=fin.tell()
        emp=pickle.load(fin)
        if emp['Empno']=='1251':
            emp['Salary']+=2000
            fin.seek(pos)
            pickle.dump(emp,fin)
            print(emp)
            found=True
except EOFError:
    if found==False:
        print("Sorry, no matching record found.")
    else:
        print("Records succesfully updated.")
    fin.close()
