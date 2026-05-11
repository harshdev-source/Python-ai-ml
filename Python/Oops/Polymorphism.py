# print(1+2, "Hello"+" World

class Employee:
    def get_designation(self):
        print("Your designation = Employee")

class Teacher(Employee):
    def get_designation(self):
        print("Your designation = Teacher")

t1 = Teacher()
t1.get_designation()
