def compare(a):
    ctr=0

    for word in a:
        if len(word)>2 and word[0]==word[-1]:
            ctr+=1
    return ctr        
a=['abc' , 'aba' , 'elmn' , 'dhruvi' , 'ucbu','lil']
for i in a:
    z=compare(a)


print(z)
