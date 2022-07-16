s=''
def hex(n):
    global s
    if n//2>0:
        if n%2<10:
            s=str(n%2)+s
        hex(n//2)
    elif n<2:
        s=str(n)+s
    return s
if hex(int(input('Enter a number: '))).count('1')%2==0:
    print('Evil Number')
else:
    print('Odious Number')
