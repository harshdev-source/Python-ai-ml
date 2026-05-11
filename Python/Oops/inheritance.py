class Employee:
    start_time = "10am"
    end_time = "6pm"

class teacher(Employee):
    def __init__(self, subj):
        self.subj = subj

class adminstaff(Employee):
    def __init__(self, role):
        self.role = role

t1 = teacher("Math")
staff1 = adminstaff("Manager")

print(staff1.start_time, staff1.end_time, staff1.role)
print(t1.subj, t1.start_time, t1.end_time)  