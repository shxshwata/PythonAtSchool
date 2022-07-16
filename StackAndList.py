stack=[]
def getChoice():
    print("Menu\n1. Push\n2. Pop\n3. Display\n4. Exit")
    choice=int(input("Enter your choice"))
    return choice
def pushitem(item):
    stack.append(item)
def popitem():
    global stack
    item=stack[-1]
    del stack[-1]
    return item
def display():
    print("Elements of the stack are: ",stack)
choice=getChoice()
while choice!=4:
    if choice==1:
        item=int(input("Enter value to push: "))
        pushitem(item)
    elif choice==2:
        if (len(stack))!=0:
            item=popitem()
            print("Popped item: ",item)
        else:
            print("Stack Underflow")
    elif choice==3:
        if (len(stack))!=0:
            display()
        else:
            print("Stack Underflow")
    else:
        print("Wrong Choice")
    choice=getChoice()
print("Finished")

