class student:
    def inputstudent(self):
        self.rollno=int(input("Enter roll number"))
        self.name=input("Enter student's name:")
        self.semester=int(input("Enter semester as integer"))
        self.branch=input("Enter branch")
    def showstudent(self):
        print("Roll No:",self.rollno)
        print("Name:",self.name)
        print("Semester:",self.semester)
        print("Branch:",self.branch)
        
    
