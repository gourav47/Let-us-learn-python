class Base:
    def __init__(self):
        self.x=20
    @staticmethod
    def f1():
        print("Static f1")
    def f1(self):
        print("instance f1")
obj=Base()
obj.f1()


#There is no concept of function overloading in Python
#so even if we try to call the static function f1 by class name, it will throw error
#it will always access the instance function if both static function and instance function name is same
#lets see what happens if we give two instance function with same name (without inheritance)
class Base:
    def __init__(self):
        self.x=20
        print("First init")
    def __init__(self,x):
        self.x=30
        print("Second init")
    @staticmethod
    def f1():
        print("Static f1")
    def f1(self):
        print("instance f1")
obj=Base()
obj.f1(3)


