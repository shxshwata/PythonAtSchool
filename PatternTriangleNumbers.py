def pattern(n=5):
    i=1
    j=1
    k=1
    for i in range(n):
        for j in range(i+1):
            if (k%2==0):
                print("0", end="")
            else:
                print("1", end="")
            k=k+1

        print()

n=int(input("Enter the number of lines: "))
pattern(n)
pattern()

