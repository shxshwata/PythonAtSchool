def decBin(n):
    if n>1:
        decBin(n//2)
    print(n%2,end="")

def decOct(n):
    if n>0:
        decOct(int(n/8))
        print(n%8, end="")
        
n=int(input("Enter the decimal number: "))
decBin(n)
decOct(n)




