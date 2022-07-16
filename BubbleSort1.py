list = [20,8,43,62,1,22,5]
print("Original list is: ", list)
n = len(list)
i=0
j=0
#Traverse through all the list elements
for i in range(n):
    #Last i elements are already in place
    for j in range (0, n-i-1):
        #traverse the list from 0 to n-i-1
        #swap if the element found is greater than the next element
        if list[j]>list[j+1]:
            list[j],list[j+1]=list[j+1],list[j]
print("List after sorting: ", list)
