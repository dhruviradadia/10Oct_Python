"""data=set()

n=int(input("enter numberof student:"))

for i in range(n):
    x=input("enter your name:")
    data.add(x)


print(data)"""

#---------------------------------------------#

data=[]

n=int(input("enter number of elements:"))

for i in range(n):
    x=input("enter your element:")
    data.append(x)

print(set(data))    
