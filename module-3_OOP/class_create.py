class student:
    stid=12
    stnm="dhruvi"

    def getdata(self):
        print("this is getdata!")

    def getsum(self,a,b):
        print("Sum:",a+b)


    #object of class
        st=student()
        print("ID:",st.stid)
        print("Name:",st.stnm)
        st.getdata()
        st.getsum(20,45)           
        