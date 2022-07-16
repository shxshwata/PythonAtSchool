m=int(input("m = "))
n=int(input("n = "))
if m < n and 99 < m < 10000 and 99 < n < 10000:
    c=0
    print("THE FASCINATING NUMBERS ARE: ")
    for i in range (m,n+1):
        x=str(i)+str(i*2)+str(i*3)
        for j in range (1,10):
            if x.count(str(j))!=1:
                break
        else:
            print(i, end=" ")
            c+=1
    if c == 0:
        print("NIL", end = " ")
    print("\nFREQUENCY OF FASCINATING NUMBERS IS: ",c)
