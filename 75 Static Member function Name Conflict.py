class Base:
    def __init__(self):
        self.a=10
    @staticmethod
    def f1():
        print("Base f1")
class Derived(Base):
    def __init__(self):
        super().__init__()
        self.a=20
    @staticmethod
    def f1():
        print("Derived f1")
        #super().f1()
        Base.f1()
Derived.f1()

#it will show output as derived f1
#if we write super().f1() which i have commented then it will throw run time error because
#we know that if we do that it will implicitly pass the current object, but here f1
#is static and no such object is created. so if we want to call the parent class also then
#we will have to write Base.f1
#Now if we change the number of argument then it will work with the same principle of hiding

class Base:
    def __init__(self):
        self.a=10
    @staticmethod
    def f1(x):
        print("Base f1")
class Derived(Base):
    def __init__(self):
        super().__init__()
        self.a=20
    @staticmethod
    def f1():
        print("Derived f1")
        #super().f1()
        Base.f1()
Derived.f1(3)
