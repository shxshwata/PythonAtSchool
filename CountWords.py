file=open("DATA.txt","r")
s=file.read().split()
arr=["the","my","he","they"]
count=0
for i in s:
    for j in arr:
        if i.startswith(j) or i.endswith(j):
            count=count+1
print(count)
