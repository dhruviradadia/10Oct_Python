def unique_list(l):
    x=[]
    for a in l:
        if a not in x:
            x.append(a)
    return x

print(unique_list([1,2,3,4,4,5,7,7,23,34,]))        

