def unique_list(l):
    x=[]
    for a in l:
        if a not in x:
            x.append(a)

        return x
    

print(unique_list([2,3,4,5,6,7,8]))