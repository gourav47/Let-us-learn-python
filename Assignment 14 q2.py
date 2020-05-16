class employee:
    def __init__(self,empid,name,salary):
        self.empid=empid
        self.name=name
        self.salary=salary
    def showemployeedata(self):
        print("Empoyee ID:",self.empid)
        print("Name:",self.name)
        print("salary:",self.salary)
        
