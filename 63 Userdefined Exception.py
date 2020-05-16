##class InsufficientBalance(ZeroDivisionError):
##    def __init__(self,arg):
##        self.msg=arg
##balance=5000
##w=int(input("enter amount to withdraw"))
##if w>balance:
##    raise InsufficientBalance("Insufficient balance in the account")
##balance=balance-w
##print("Current Balance is:",balance)

class InsufficientBalance(ZeroDivisionError):
    def __init__(self,arg):
        self.msg=arg
balance=5000
w=int(input("enter amount to withdraw"))
try:
    if w>balance:
        raise InsufficientBalance("Insufficient balance in the account")
    balance=balance-w
except InsufficientBalance as i:
    print("Exception",i.msg)
else:
    print("Withdraw amount",w,"Successfully")
finally:
    print("Current Balance is:",balance)
