def selectionSort(w):
    for i in range(len(w)):
        a,b=w[i],i
        for j in range(i+1,len(w)):
            if[j]<a:
                a,b=w[j],j
        w[i],w[b]=w[b],w[i]
    print("New List: ",w)
w=eval(input("Enter list: "))
selectionSort(w)
