def myfunc():
    print("this is function:")

def myfunc(a,b):
    print("Mul:",a*b) 

def getdata(id,name,city):
    print("ID:",id)
    print("Name:",name)
    print("City:",city)

    #calling a function
    myfunc()
    getmul(45,67)
    getdata(56,'dhruvi','rajkot') #static

id=input("enter ID:")
name=input("Enter Name:")
city=input("Enter City:")

getdata(id,name,city)
