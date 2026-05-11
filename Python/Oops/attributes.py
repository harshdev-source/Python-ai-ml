class student:
    college_name = "ABC College" #Class Attribute

    def __init__(self, name, cgpa):
        self.name = name #Instance Attribute 
        self.cgpa = cgpa


stud= student("Rahul",4.4)

print(stud.name)
print(stud.cgpa)
print(student.college_name)