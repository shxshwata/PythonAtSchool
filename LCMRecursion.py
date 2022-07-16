def hcf(n1,n2):
    if (n1==0):
        return n2 
    else:
        return hcf(n2%n1,n1)
def lcm(n1,n2):
    return (n1/(hcf(n1,n2)))*n2

n1=int(input("Enter a number:"))
n2=int(input("Enter a number:"))
print(lcm(n1,n2))
