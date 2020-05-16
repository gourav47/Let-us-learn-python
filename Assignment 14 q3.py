class employee:
    def inputemployee(self):
        self.empid=int(input("Enter the employee ID:"))
        self.name=input("Enter the name:")
        self.salary=input("Enter the salary:")
        return self
    def showemployee(self):
        print("Employee ID:",self.empid,end=' ')
        print("Name:",self.name,end=' ')
        print("salary:",self.salary)
    @staticmethod
    def sortbyname(emp_list):
        emp_list.sort(key=lambda e:e.name)
    @staticmethod
    def sortbysalary(emp_list):
        emp_list.sort(key=lambda e:e.salary, reverse=True)

l1=[employee().inputemployee()
    for i in range(int(input("How many employee data you want to enter")))]
employee.sortbyname(l1)
print("list of employee sorted by their names")
for e in l1:
    e.showemployee()
employee.sortbysalary(l1)
print("List of employees sorted by their salary in reverse")
for e in l1:
    e.showemployee()
