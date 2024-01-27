a=[]
n=int(input("enter number of element:"))

for i in range (0,n):
    b=input('enter your element:'+ str(i+1))

    a.append(b)
c=len(a[0])
d=a[0]

for j in a:
    if(len(j)>c):
        c=len(j)
        d=j

print("the longest word is:",d)       
    

