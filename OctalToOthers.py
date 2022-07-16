def oct2others(n):
    print("Entered octal number: ",n)
    ns=str(n)
    dec=int(ns,8)
    print("Number in decimal: ",dec)
    print("Number in binary: ",bin(dec))
    print("Number in hexadecimal: ",hex(dec))
num=int(input("Enter an octal number: "))
oct2others(num)
