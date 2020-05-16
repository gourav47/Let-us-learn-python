class Base:
    x=11
    def __init__(self):
        self.a=10
        Base.x=13
    def showBase(self):
        print("Base a:",self.a)
class derived(Base):
    x=12
    def __init__(self):
        self.a=20
        super().__init__()
    def show():
        print(Base.x,derived.x)
    def showDerived(self):
        print("Derived a:",self.a)
print(derived.x)


#output will be 12
#we need to understand that if two x variables are created!! so we will print it via dict
obj=derived()
print(derived.__dict__)
print(Base.x)
print(derived.x)
derived.show()


#here unlike instancevariable 2 copies gets create one w.rt base and other w.r.t derived
#base class variable is accessed if called for base and child class variable is accessed if called for child.
