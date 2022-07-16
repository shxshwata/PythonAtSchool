import pickle
e=[]
while True:
    empno=int(input("Enter employee's number: "))
    name=input("Enter employee's name: ")
    city=input("Enter employee's city: ")
    salary=int(input("Enter employee's salary: "))
    data=[empno,name,city,salary]
    e.append(data)
    c=input("If you don't want to continue, press 'N'")
    if c in 'N':
        break
f=open("Emp.dat","wb")
pickle.dump(e,f)
print("Records added.")
f.close()
f=open("Emp.dat","rb")
print("The entered records are: ")
while True:
    try:
        print(pickle.load(f))
    except EOFError:
        break
f.close()
    
    
