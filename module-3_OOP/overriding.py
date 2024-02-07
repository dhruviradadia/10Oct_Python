class stud:
    def getdata(self,id,name):
        print("ID:",id)
        print("Name:",name)


class newstud(stud):
    def getdata(self, id, name):
        return super().getdata(id, name)(self,id,name)
    

st=stud()
ne=newstud()

st.getdata(1,'Bhavin')
ne.getdata(2,'Dhruvi')
        