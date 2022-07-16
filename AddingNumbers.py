n=int(input("Enter any number :"))
s=0
for i in range(n+1):
    for j in range(i):
        s=s+j
print ("The sum is: ", s)
