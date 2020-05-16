class A:
    def f1(self):
        print("A-f1")
class B:
    def f1(self):
        print("B-f1")
obj=A()
obj.f1()
obj=B()
obj.f1()

#as python is dynamically typed, it will run both the functions, in run time it resolves
#the object that which object is referring to which function.
#let us understand the polymorphic behaviour more specifically in the below pprogram

class Animal:
    def __init__(self,name):
        self.name=name
    def talk(self):         #this function's coding should not happen as per the Animal Class
        raise NotImplementedError("Derived class must implement this function")
class Cat(Animal):
    def talk(self):
        return "Meow"
class Dog(Animal):
    def talk(self):
        return "woof"
animals=[Cat("Rekha"),Cat("Soniya"),Dog("Moti"),Cat("Rupa"),Dog("Gabbar")]

for animal in animals:
    print(animal.name,"-",animal.talk())
