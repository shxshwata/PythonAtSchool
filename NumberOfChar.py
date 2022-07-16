file=open("Myfile.txt","r")
data=file.readlines()
for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] == "$":
            break
print("Number of characters upto '$' mark: ",i+j)
file.close()
