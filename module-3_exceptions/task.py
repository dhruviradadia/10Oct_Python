
try:
    
    def getdata(id,name,city,number):
    
    print("ID:",id)
    print("Name:",name)
    print("City:",city)
    print("Number:",number)

n=int(input("Enter number of student:"))

for i in range(n):
    stid=input("Enter ID:")
    stnm=input("Enter Name:")
    stcity=input("Enter City:")
    number=input("Enter number:")


getdata(stid,stnm,stcity)

except:

print("error!")