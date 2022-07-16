def largestFreq(l):
    c=0
    n=l[0]
    for i in l:
        c1=l.count(i)
        if (c1>c):
            c=c1
            n=i
    return n
l=eval(input("Enter the elements: "))
print(largestFreq(l))
