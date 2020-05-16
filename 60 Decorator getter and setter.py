class student:
    def __init__(self,marks):
        self.__marks=marks
    def per(self):
        return (self.__marks/600)*100
    @property
    def marks(self):
        print("getting value:",end=" ")
        return self.__marks
    @marks.setter
    def setter(self,value):
        if value<0 or value>600:
            print("Invalid marks!!")
        else:    
            print("setting value:",value)
            self.__marks=value
    
        
        

s=student(400)
s.marks=500
#s.setter(500)
print(s.marks)
#print(s.getter())
print(s.per(),"%")
