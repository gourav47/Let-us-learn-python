class Test:
    x=10 #static, visible from outside the class
    __h=20 #static, hidden variable
print(Test.x)
#print(Test.__h)

#it will print x as 10 but will give error for __h as it gets hidden because of the prefix.
#here what python actually does is, it change the hidden variable name internally
#it adds underscore classname in prefix as _Test__h
#however we can access the __h inside the class itself as shown in below code:
#also we will try to access __h outside the class by the new name which gets change internally
class Test:
    x=10 #static, visible from outside the class
    __h=20  #static, hidden variable
    @staticmethod
    def f1():
        print(Test.__h)
Test.f1()
print("outside class __h", Test._Test__h)

#technically we can say that there is nothing as private variable in python as we can access it somehow


############ Data Hiding for Insstance Variable   #########

class Test:
    x=10  #static, Visible from outside the class
    __h=20  #static, hidden variable
    def __init__(self):
        self.__a=100  #private Instance variable
    @staticmethod
    def f1():
        print(Test.__h)
obj=Test()
print(obj.__dict__)
print(obj._Test__a)

#Benifit of using double underscore is that we can use it in base class and derived class
#when we call the variable the it will not get conflict as it will appl the prefx of respective class name
            
