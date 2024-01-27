stdata={}

n=int(input("enter number of student:"))


for i in range(n):
    key=input("enter student id:")
    value=input("enter student name and city:")
    
    stdata[key]=value #adding


print(stdata)