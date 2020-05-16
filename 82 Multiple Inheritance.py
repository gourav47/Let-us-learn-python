class Person:
    def __init__(self,n,a):
        self.name=n
        self.age=a
class Student(Person):
    def __init__(self,n,a,r):
        self.rollno=r
        Person.__init__(self,n,a)
class Teacher(Person):
    def __init__(self,n,a,s,sub):
        self.salary=s
        self.subject=sub
        Person.__init__(self,n,a)
class BrightStudent(Student,Teacher):
    def __init__(self,n,a,r,s,sub,p):
        self.points=p
        Student.__init__(self,n,a,r)
        Teacher.__init__(self,n,a,s,sub)
obj=BrightStudent("Rahul",18,100,2000,"Physics",7)
print(obj.__dict__)
