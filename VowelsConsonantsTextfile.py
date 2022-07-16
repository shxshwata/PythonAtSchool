f=open("MYFILE.txt","r")
c=0
v=0
s=f.read()
word=s.split()
for i in word:
    if len(i)==4:
        c+=1
print("There are ",c," four letter words.")
s=s.upper()
for i in s:
    if i in 'AEIOU':
        v+=1
print("There are ",v," vowels.")
        
