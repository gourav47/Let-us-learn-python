class Base:
    def __init__(self):
        self.a=10
class Derived(Base):
    def __init__(self):
        super().__init__()
    def f1(self):
        print(self.a)
obj=Derived()
print(obj.a)

#we can access the instance member variables of base class only by applying self.a in child class
