def pangram(s):
    a="abcdefghijklmnopqrstuvwxyz"
    b=s.lower()
    for i in a:
        if i not in b:
            return False
    return True
s=str(input("Enter the word/sentence: "))
if (pangram(s)==True):
    print("Pangram")
else:
    print("Not a pangram")
