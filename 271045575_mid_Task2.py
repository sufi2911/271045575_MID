# Task 2
class School():
    def __init__(self,name,age,id):
        self.name = name
        self.age = age
        self.id = id
    
    def displayinfo(self):
        print(f"\nName:{self.name}\nAge: {self.age}\nID: {self.id}")

    
class Student(School):
    def __init__(self,name,age,id,grade,classes):
        super().__init__(name,age,id)
        self.grade = grade
        self.classes = classes
    def display_std_info(self):
        print(f"\nName:{self.name}\nAge: {self.age}\nID: {self.id}\nGrade:{self.grade}\nClasses:{self.classes}")

class Teacher(School):
    def __init__(self,name,age,id,subject,course):
        super().__init__(name,age,id)
        self.subject = subject
        self.course = course
    def display_tea_info(self):
        print(f"\nName:{self.name}\nAge: {self.age}\nID: {self.id}\nSubjects teachs:{self.subject}\nManages Class:{self.course}")
    
class Admin(School):
    def __init__(self,name,age,id,manage,emps):
        super().__init__(name,age,id)
        self.manage = manage
        self.emps = emps
    def display_adm_info(self):
        print(f"\nName:{self.name}\nAge: {self.age}\nID: {self.id}\nDepartment:{self.manage}\nEmployess Manages:{self.emps}")   


students = Student("SUFYAN",19,276104435,"A",["maths","stats"])
students.display_std_info()

teacher = Teacher("Muzammil",45,231045564,["Maths","Computer","Stats"],["STAT101","MATHS111","COMP113"])
teacher.display_tea_info()

admin = Admin("Mushtaq",56,145564,"Computer Science Department",["Ali","Ahmed","sarfarz"])
admin.display_adm_info()
