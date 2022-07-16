def harshad(a,b):
    print("Harshad Numbers: ")
    for i in range(a,b+1):
        s,t=0,i
        while t>0:
            s,t=s+(t%10),t//10
        if i % s == 0:
            print(i, end="")
n1=int(input("Enter lower limit: "))
n2=int(input("Enter upper limit: "))
harshad(n1,n2)
