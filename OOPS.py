class Student:
    #default constructor
    def __int__(self):
        pass
    #parameterized constructor
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
       # print("Adding new student to Database...")

s0 = Student("Karan", 97)
print(s0.name, s0.marks)

s1 = Student("Arjun", 98)
print(s1.name, s1.marks)
