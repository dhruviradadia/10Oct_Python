with open("myfile.txt","r")as f:
    a=f.readlines()
print(a)
a=[x.strip() for x in a]
print(a)    