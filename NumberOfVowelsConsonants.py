w=input('Enter a word: ')
d,v,c={},0,0
w=w.upper()
for i in w:
    if i in 'AEIOU':
        v+=1
    else:
        c+=1
    d[i]=w.count(i)
for i in d:
    print(i,'-',d[i])
print('Number of vowels: ',v)
print('Number of consonants: ',c)
