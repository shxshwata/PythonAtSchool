s=input("Enter a sentence: ").upper()
t,x,c="",s.split(),0
i=0
for i in range(len(x)-i-1):
    for j in range(len(x)-i-1):
        if len(x[j])>len(x[j+1]):
            x[j],x[j+1]=x[j+1],x[j]
print(x)
for i in s.split():
    if "AEIOU".find(i[0])!=1:
        c=c+1
print("After Arranging: ",t)
print("Number of words: ",c)
    
