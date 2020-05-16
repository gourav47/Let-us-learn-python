class Base:
    def __init__(self):
        self.a=10
    def f1(self):
        print("Base f1")
class Derived(Base):
    def __init__(self):
        super().__init__()
        self.a=20
    def f1(self):
        print("Derived f1")
        super().f1()    #it will call the f1 of parent class
obj=Derived()
obj.f1()  #here f1 is getting overridden

#here as child class object is called it will run f1 of child
#outout will be Derived  f1 without super().f1()
#however if we put the super().f1 in child class function it will
#call the f1 of parent class, that is the process to do
#so now if we execute the program with super().f1() it will call base f1
#if we write the code without super().f1() it will call f1 of base
#even if we dont define f1 in derived class then also it will run the
#f1 of parent class because of inheritance.
#so overriding is used when we want both parent and child class function to execute
