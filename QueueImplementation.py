q=[]
def getChoice():
    print("MENU\n 1. INSERT\n 2. DELETE\n 3. DISPLAY\n 4. EXIT")
    choice=int(input("Enter your choice: "))
    return choice
def insertitem(item):
    q.append(item)
def deleteitem():
    global q
    item=q[0]
    q=q[1:len(q)]
    return item
def display():
    print("Elements of Queue are: ",q)
print("Program starts")
choice=getChoice()
while choice!=4:
    if choice==1:
        item=int(input("Enter value to insert: "))
        insertitem(item)
    elif choice==2:
        if (len(q)!=0):
            item=deleteitem()
            print("Delete item=",item)
        else:
            print("Queue Underflow")
    elif choice==3:
        if (len(q)!=0):
            display()
        else:
            print("Queue Underflow")
    else:
        print("Wrong choice")
    choice=getChoice()
print("Queue operations are over")
