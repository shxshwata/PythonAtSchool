def hyphenSequence(w):
    for i in range(len(w)):
        minimum=i
        for j in range(i+1,len(w)):
            if (w[minimum]>w[j]):
                minimum=j
    w[i],w[minimum]=w[minimum],w[i]
    for i in range(len(w)):
        print(w[i])
    ns=("-").join(w)
    print("Result: ",ns)
s1=(input("Enter input: "))
s2=s1.split("-")
hyphenSequence(s2)
