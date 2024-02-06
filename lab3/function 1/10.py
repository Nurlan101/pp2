def uniq(a):
    v = [] 
    for i in a:
        if(i in v): #if element i in the v we will skip 
            continue
        else:
            v.append(i) # if there is no we will add
    return v

a = [1,2,3,2,1]
a = uniq(a)
print(a) 