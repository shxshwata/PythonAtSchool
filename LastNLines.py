f=open("DATA2.txt")
n=int(input("Enter the number of lines from the end you want to print: "))
l=f.readlines()
l=l[-n:]
for i in l:
    print(i)
f.close()
