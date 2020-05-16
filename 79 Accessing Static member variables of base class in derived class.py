class Base:
    x=11  #static member variable
    def __init__(self):
        self.a=10
class Derived(Base):
    def __init__(self):
        super().__init__()
    @staticmethod
    def f1():
        print(x)
Derived.f1()
print(Derived.x)

#the above code will give error as if we cal f1 then it will search for the local variable x
#but we have not created x as a local variable, so to access the static variable,
#we will have to give the class name either Derived.x or Base.x as shown in the below program

class Base:
    x=11  #static member variable
    def __init__(self):
        self.a=10
class Derived(Base):
    def __init__(self):
        super().__init__()
    @staticmethod
    def f1():
        print(Base.x)
Derived.f1()
print(Derived.x)
