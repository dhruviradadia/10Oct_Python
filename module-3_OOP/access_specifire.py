class student:
    __stid=15
    __stnm='dhruvi'

    def __getdata(self):
        print("this is getdata!")
        print("ID:",self.__stid)
        print("Nmae:",self.__stnm)

    def printdata(self):
        self.___getdata()

st=student()        
"""print("ID",st.stid)
print("Name:",st.stnm)"""
st.getdata()