class Base:
    def __init__(self):
        self.a=10
    def basefunction(self):
        print("Base Instance function a=",self.a)
class Derived(Base):
    def __init__(self):
        super().__init__()
    def f1(self):
        self.basefunction()
obj=Derived()
obj.f1()

#in python if we want to access instace member in class body the we will have to
#access it by using self.functionname as shown in self.basefunction() in above code
#we cannot define static function in Derived class and access instance member function
#as instance itself is not there so we cannot the instance member fucntion.
#insted of self.basefunction() we can write super().basefunction() as in both the cases
#we are calling the base function
