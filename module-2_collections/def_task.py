def getdata(id,name,city):
    print("Id:",id)
    print("Name:",name)
    print("City:",city)

n=int(input("enter numebr of students:"))   

for i in range(n):
    stid=input("Enter ID:")
    stnm=input("Enter Name:")
    stcity=input("Enter City:")

    getdata(stid,stnm,stcity)
    

