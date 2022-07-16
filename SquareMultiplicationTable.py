n=int(input("Enter the number of rows and columns: "))
for row in range(1,n):
    for col in range(1,n):
        prod=row*col
        if prod<10:
            print(" ",prod," ",end="")
        else:
            print(prod," ",end=" ")
    print()
