class Account:
##    def __init__(self,a,b):
##        self.accno=a
##        self.balance=b
    def f1(self,a,b):
        self.accno=a
        self.balance=b

acc1=Account()
acc1.accno=102
acc1.balance=6000
print(acc1.__dict__)
