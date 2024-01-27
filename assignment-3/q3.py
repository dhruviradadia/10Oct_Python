list=[]
n=int(input("enter number of element:"))

for i in range(1,n+1):
    a=int(input("enter nembers:"))
    list.append(a)

print("list items=",list)
z=[]

for i in list:
    if i not in z:
        z.append(i)

print("list items after removing duplicates=",z)        