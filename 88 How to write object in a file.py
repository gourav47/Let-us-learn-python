class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
students_list=[Student('Amit',19),Student('Rahul',20),Student('Romesh',18),Student('Ajay',19)]
def saveStudents():
    import pickle
    f1=open('C:\Users\Dell\Desktop\python\Let-us-learn-python-master\file3.obj','wb')
    for s in students_list:
        pickle.dump(s,f1)
    f1.close()
def viewAllStudents():
    import pickle
    f2=open('C:\Users\Dell\Desktop\python\Let-us-learn-python-master\file3.obj','rb')
    s_list=[]
    while True:
        try:
            s_list+=[pickle.load(f2)]
        except EOFError:
            break
    return s_list
