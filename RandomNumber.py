#Program to random access any name
#First name will be at position 0, second will be at 20 and so on
size_of_rec=20
num=int(input("Enter record number: "))
with open('Names.dat','rb') as f:
    f.seek(size_of_rec*(num-1))
    str=f.read(size_of_rec)
    if (len(str)==0):
        print("Incorrect position")
    else:
        print(str.decode())
