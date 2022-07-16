s=input("Enter an expression: ")
l,k=[],0
for i in s:
    if i in '[{(':
        l.append(i)
    elif i==')':
        if l.pop()!='(':
            k=1
            break
    elif i=='}':
        if l.pop()!='{':
            k=1
            break
    elif i==']':
        if l.pop()!='[':
            k=1
            break
else:
    if len(l)==0:
        print("Valid")
    else:
        print("Invalid")
if k==1:
    print("Invalid")
