n=int(input("Enter any number :"))
temp=n
rev=0
while (n>0):
    digit=n%10
    rev=rev*10+digit
    n=n//10
if (temp==rev):
    print("The entered number is a palindrome.")
else:
    print ("The entered number is not a palindrome.")