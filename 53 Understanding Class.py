class Employee:
    def __init__(self,first, last, pay):
        self.first=first  #we can give any name as self.fname=first 
        self.last=last
        self.pay=pay
        self.email=first+'.'+last+'@company.com'
    def fname(self):
        return'{} {}'.format(self.first,self.last)
emp_1=Employee('corey','schafer',50000)  #init method wil run automatically
emp_2=Employee('Test','User',60000)  #so emp_1 & emp_2 will be passed as self
#and then it will set all the attributes
'''when we create method within a class,
they receive the instance as first argument automatically'''
'''Now within our init method we are going to set the instance variables '''
'''when we create an instance of employee class which is emp_1 and emp_2
we can now pass the values that we specified in our init method.
Now the init method takes the instance which we call self and the first, last
and pay as arguments.'''
##print(emp_1)
##print(emp_2)

'''so now that we have init method in place we can delete the manual assignments
as shown below which i wrote at the beginning, here i will comment the codes written below'''

##emp_1.first='Corey'
##emp_1.last='Schafer'
##emp_1.='corey.schafer@company.com'
##emp_1.pay=50000
##
##emp_2.first='Test'
##emp_2.last='User'
##emp_2.email='Test.User@company.com'
##emp_2.pay=60000

print(emp_2.fname())
print(emp_1.fname())

