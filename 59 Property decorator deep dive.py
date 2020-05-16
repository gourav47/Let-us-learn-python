class student:
    def __init__(self,name,grade):
        self.name=name
        self.grade=grade
    @property
    def msg(self):
        return self.name +" got grade"+ self.grade
    @msg.setter
    def msg(self,msg):
        sent=msg.split(" ")
        self.name=sent[0]
        self.grade=sent[-1]

stud1=student("Nia","B")
stud1.msg="amulya got grade A"
print(stud1.name)
print(stud1.grade)
print(stud1.msg)
