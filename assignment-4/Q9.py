t=open("myfile.txt","r")
d=dict()
for i in t:
    i=i.strip()
    i=i.lower()
    w=i.split(" ")
    for wo in w:
        if wo in d:
            d[wo]=d[wo]+1
        else:
            d[wo]=1
for key in list (d.keys()):
    print(key,":",d[key])
