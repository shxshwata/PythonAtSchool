file1=open("portal.txt","r")
file2=open("express.txt","w")
lst=file1.readLines()
for i in lst:
    word=i.split()
    file2.write(" ".join(word))
    file2.write("\n")
print("The edit has been made.")
