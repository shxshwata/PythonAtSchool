def DecToBin(n):
    if n > 1:
        DecToBin(n//2)
    print(n%2,end='')
num = int(input("Enter the Number: "))
DecToBin(num)
