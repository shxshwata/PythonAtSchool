n=int(input("Enter the value of n: "))
for r in range(n):
    a=r+1
    b=n-1
    for c in range(r+1):
        print ((a), end=" ")
        a=a+b
        b=b-1

    print()
