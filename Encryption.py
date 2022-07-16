s=input("Enter a string: ")
t='@$'.join(s)
print("Encrypted string: ",t,"\nDecrypted String: ",end=' ')
for i in t.split('@$'):
    print(i, end='',sep='')
