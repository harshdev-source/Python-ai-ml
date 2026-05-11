class Employee:
    start_time = "10am"
    end_time = "6pm"


class adminstaff(Employee):
    def __init__(self, role):
        self.role = role

# -------------------------Multilevel Inheritance-------------------------
class Accountant(adminstaff):
    def __init__(self,salary,role):
        super().__init__(role)  # Super keyword se parent class ke contructor ko call karte hai
        self.salary = salary

acc1 = Accountant(25_000,"CA")

print(acc1.role, acc1.salary)