class Employee:
    def __init__(self,first, last, pay):
        self.first=first  
        self.last=last
        self.pay=pay
        self.email=first+'.'+last+'@company.com'
    def fname(self):
        return'{} {}'.format(self.first,self.last)
    def apply_raise(self):
        self.pay=int(self.pay * self.raise_amt)
    def __repr__(self):
        pass
emp_1=Employee('corey','schafer',50000)
emp_2=Employee('Test','User',60000) 


