class Base:
    def __init__(self):
        self.a=10
    def f1(self):
        print("Base f1")
class Derived(Base):
    def __init__(self):
        super().__init__()
        self.a=20
    def f1(self,x):
        print("Derived f1")
        super().f1()    #it will call the f1 of parent class
obj=Derived()
obj.f1(3)

#as the object of derived class is called it will see the f1 in derived class only
#if the argument is passed as per the derived class f1 then it will execute both class
#suppose if we dont pass argument which is 3 in the above program then
#it will throw error, it will not go to parent class and search f1 as the obj is of derived class
