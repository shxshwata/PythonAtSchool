def hyphenSequence(w):
    for i in range(len(w)+1):
        for j in range(len(w)-1):
            if (w[j][0]>w[j+1][0]):
                w[j],w[j+1]=w[j+1],w[j]
    ns=("-").join(w)
    print("Result: ",ns)
s1=input("Enter input: ")
s2=s1.split("-")
hyphenSequence(s2)
