s=input("Enter a sentence: ")
l=s.split()
c,m=0,0
for i in l:
    t=""
    for k in i:
        t=k+t
    if i == t:
        c+=1
    if len(i) > m:
        m = len(i)
print("There is/are ",c, "Palindrome word(s)")
print ("Longest Word(s)")
for i in l:
    if len(i)==m:
        print (i)

