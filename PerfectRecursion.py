n=int(input("Enter a number:"))
copy=0
def perfect(n1):
    global copy
    if n1>0:
        if n%n1==0:
            copy+=n1
        perfect(n1-1)
perfect(n-1)
if n==copy:
    print("Perfect number")
else:
    print("Non perfect number")
            
    
