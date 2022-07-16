n=eval(input("Enter the numbers: "))
def sum(l):
    if l>0:
        return (n[l-1]+sum(l-1))
    else:
        return 0
print(sum(len(n)))
