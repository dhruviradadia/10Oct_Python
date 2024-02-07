class rectangle():
    def __init__(self,b,l):
        self.b=b
        self.l=l

    def area(self):
        return self.b*self.l

y=int(input("enter length of rectangle:"))
x=int(input("enter width of rectangle:"))
n=rectangle(y,x)
print("area of rectangle is:",n.area())        