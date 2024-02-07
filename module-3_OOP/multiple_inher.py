class bhavin:
    bid=0
    btech=" "

    def b_getdata(self):
        self.bid=input("Enter bhavin's ID:")
        self.btech=input("Enter bhavin's Technology:")

class janvi:
    jid=0
    jtech=" "

    def j_getdata(self):
        self.jid=input("Enter janvi's ID:")
        self.jtech=input("Enter janvi's Technology:")

class dhruvi:
    did=0
    dtech=" "

    def d_getdata(self):
        self.did=input("Enter dhruvi's ID:")
        self.dtech=input("Enter dhruvi's Technology:")

class tops(bhavin,janvi,dhruvi):
    def printdata(self):
        print("--------bhavin's data--------")
        print("Bhavin's ID:",self.bid)
        print("Bhavin's Technology:",self.btech)
        print("--------janvi's Data----------")
        print("janvi's ID:",self.jid)
        print("janvi's Technology:",self.jtech)
        print("--------dhruvi's Data--------")
        print("Dhruvi's ID:",self.did)
        print("Dhruvi's Technology:",self.dtech)

tp=tops()
tp.b_getdata()
tp.j_getdata()
tp.d_getdata()
tp.printdata()

        