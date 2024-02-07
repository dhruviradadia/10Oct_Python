class Student:
    def getdata(self,id,name):
        print("ID",id)
        print("Nmae:",name)


st=Student()

#ST.GETDATA(13,'dhruvi') #static
stid=input("Enter ID:")
stnm=input("Enter Name:")
    
st.getdata(stid,stnm) 