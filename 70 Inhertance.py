class Person:
    def __init__(self,n,a):
        self.name=n
        self.age=a
    def showName(self):
        print("Name:",self.name)
    def showAge(self):
        print("Age:",self.age)

class Student(Person):
    def __init__(self,r):
        self.rollno=r
        Person.__init__(self,"Rahul",16)
    def showRollno(self):
        print("Roll Number:",self.rollno)

s1=Student(100)
s1.showRollno()
s1.showName()
s1.showAge()    

#or


class Person1:
    def __init__(self,n,a):
        self.name=n
        self.age=a
    def showName(self):
        print("Name:",self.name)
    def showAge(self):
        print("Age",self.age)

class Student1(Person1):
    def __init__(self,r,n,a):
        super().__init__(n,a)
        self.rollno=r
    def showRollno(self):
        print("Roll number",self.rollno)
s2=Student1(100,"Rahul",15)
s2.showRollno()
s2.showName()
s2.showAge()
