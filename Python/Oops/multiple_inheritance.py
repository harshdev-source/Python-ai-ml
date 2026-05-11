class Teacher: 
    def __init__(self,salary):
        self.salary = salary
    
class Student:
    def __init__(self,gpa):
        self.gpa = gpa

class TA(Teacher, Student):
    def __init__(self, salary, gpa, name):
        super().__init__(salary)
        Student.__init__(self, gpa)
        self.name = name

def get_name(self):
    print(self.name, self.salary, self.gpa)

Ta1 = TA(50_000, 9.9, "Aparijita")

get_name(Ta1)

