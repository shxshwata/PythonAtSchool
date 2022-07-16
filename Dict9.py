a = {'gfg' : 6, 'is' : 4, 'best' : 7} 
b = {'gfg' : 10, 'is' : 6, 'best' : 10} 

print("The original dictionary 1 : " +  str(a)) 
print("The original dictionary 2 : " +  str(b)) 

res = {key: b[key] - a.get(key, 0) 
    for key in b.keys()} 
print("The difference dictionary is : " + str(res)) 

