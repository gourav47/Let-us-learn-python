class test:
    a=10   #static variable
    def __init__(self):
        self.x=1   #instance variable
        test.b=20  #static variable
    def f1(self):  #instance member function
        self.x=2   #instance variable
        test.c=30  #static variable
    @staticmethod    
    def f2(m,n):      #static method
        test.d=40  #static variable
    @classmethod
    def f3(cls):
        cls.e=50    #static variable
        test.f=60   #static variable
test.g=70           #static variable
t1=test()
t1.f1()
test.f2(3,4)
test.f3()
print(test.__dict__)
