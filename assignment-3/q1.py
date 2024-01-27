list=[]
n=int(input("enter total number of element:"))
for i in range(1,n+1):
    Value=int(input("enter value:"))
    list.append(Value)


print("the smallest number in list is:",min(list))
print("the largest number in list is:", max(list))
