class Base:
    def __init__(self):
        self.a=10
    def showBase(self):
        print("Base a:",self.a)
class derived(Base):
    def __init__(self):
        self.a=20
        super().__init__()
    def showDerived(self):
        print("Derived a:",self.a)
obj=derived()
obj.showBase()
obj.showDerived()


#in the output it will show both the value as 10
#because no new object a will be created and it will overwrite the derived value of a with base value of a
#what if we write the super line before self.a=20?

class Base:
    def __init__(self):
        self.a=10
    def showBase(self):
        print("Base a:",self.a)
class derived(Base):
    def __init__(self):
        super().__init__()
        self.a=20
    def showDerived(self):
        print("Derived a:",self.a)
obj=derived()
obj.showBase()
obj.showDerived()

#in these output will be 20 as a is created initially and then self.a is running
