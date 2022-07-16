def hcf(a,b):
    for i in range(min([a,b])+1,0,-1):
        if a%i==0 and b%i==0:
            print('HCF=', i)
            break
def trimorphic(n):
    if str(n**3).endswith(str(n)):
        print('Trimorphic')
    else:
        print('Not trimorphic')
def palindrome(m,n):
    if m<=n:
        print('Palindrome numbers: ')
        for i in range(m,n+1):
            if str(i)==(str(i))[::-1]:
                print(i)
c=int(input('Enter 1 for HCF, 2 for TRIMOPRHIC NUMBER and 3 for PALINDROME NUMBER: '))
x=int(input('Enter a number: '))
y=int(input('Enter a number: '))
l=min([x,y])
u=max([x,y])
if c==1:
    hcf(1,u)
elif c==2:
    trimorphic(1,u)
elif c==3:
    palindrome(1,u)
else:
    print('Invalid input')
