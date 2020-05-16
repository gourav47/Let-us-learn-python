class Base:
    x=10
    def __init__(self):
        self.x=20
class Derived(Base):
    def __init__(self):
        super().__init__()
obj=Derived()
print(obj.x,Base.x,Derived.x)

#if we want both the values to be displayed then
#we need to access static variable by the class name and instance variable by object name

class Base:
    x=10
    def __init__(self):
        self.a=20
class Derived(Base):
    def __init__(self):
        super().__init__()
obj=Derived()
print(obj.x)

#if the names are different then obj.x will take the static member value

class Base:
    x=10
    def __init__(self):
        self.x=20
class Derived(Base):
    def __init__(self):
        super().__init__()
obj=Derived()
print(obj.x)

#if the names are same then obj.x will take the instance member value

class Base:
    x=10
    def __init__(self):
        self.x=20
class Derived(Base):
    def __init__(self):
        super().__init__()
obj=Derived()
print(Derived.x)
