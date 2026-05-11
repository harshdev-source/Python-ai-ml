class student:
    # subj = "Python" #When we don't write init method python autmatically writes constructor for us and also runs it.
    def __init__(self,name,cgpa):
        print("Constructor was called")
        self.name = name
        self.cgpa = cgpa

    def get_cgpa(self):
        return self.cgpa

stud1 = student("Rahul",7.8)
stud2 = student("Aprajita",9.9)
stud3 = student("Harsh",10)
print(stud1.cgpa)
print(stud1.get_cgpa())