def display():
    f=open("DATA.txt","r")
    f1=f.readlines()
    for i in f1:
        word=i.split()
        for j in word:
            if len(j)<4:
                print(j)
    f.close()
display()
