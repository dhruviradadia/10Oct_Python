class bank:
    def account(self):
        self.accno=int(input("Enter the account no:"))
        self.name=input("Enter the account holder name:")
        self.type=input("Enter the type of account [c\s]:")

    def amount(self):
        self.deposit=int(input("enter the initial amount:"))

        

    def withdrawn(self):
        amount=int(input("enter amount to be withdrew:"))
        if self.balance >= amount:
           self.balance -= amount
           print("you withdrawn:",amount)
        else:
            print("insufficient balance:")

s=bank()
s.account()
s.amount()
s.withdrawn()

