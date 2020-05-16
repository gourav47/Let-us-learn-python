class Base:
    x=11
    def __init__(self):
        self.a=10
    @staticmethod
    def basefunction():
        print("Base Static function x=",Base.x)
class Derived(Base):
    def __init__(self):
        super().__init__()
    def f1(self):
        self.basefunction()
        #derived.basefunction()
obj=Derived()
obj.f1()


#instance member function can call both static member and instance member.
#what if we define static function in derived class, lets see that in below code:

class Base:
    x=11
    def __init__(self):
        self.a=10
    @staticmethod
    def basefunction():
        print("Base Static function x=",Base.x)
class Derived(Base):
    def __init__(self):
        super().__init__()
    @staticmethod
    def f1():
        Base.basefunction()
        #derived.basefunction()
obj=Derived()
obj.f1()

#we cannot access the static member function of base class by applying super in derived class
#because super represents an object and there is no object as such
#we cannot use self also as that represents instance and there is no instance in it.
#we will use the class name, either base or derived
