class student:
    stid=1
    stnm='dhruvi'

    def getdata(self):
        print("ID:",self.stid)
        print("Name:",self.stnm)

#object of class
"""st=student()
st.getdata()
st.stid=13
st.stnm='bhavin'
st.getdata()"""        

#instance

student().getdata()
student().stid=13
student().stnm='Bhavin'
student().getdata()