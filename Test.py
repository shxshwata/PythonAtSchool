string2 = input("Enter a string: ")
length = len(string2)
i=0
for a in range (-1, (-length-1), -1):
    print (string2[i], "\t", string2[a])
    i+=1