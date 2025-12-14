# class definition
class Student():
    def __init__(self):
        self.name = ""
        self.age = 0
        self.gpa = ''

def main():
    # object creation based on the class
    student1 = Student()
    student2 = Student()
    student3 = Student()
    student1.name = "Dominic"
    student1.age = 19
    student1.gpa='4.0'
    student2.name = "Olivia"
    student2.age = 21
    student2.gpa='3.7'
    student3.name = "Adam"
    student3.age = 22
    student3.gpa = '3.4'
    print('LIST OF STUDENTS')
    print('================')
    print(f'{student1.name},GPA: {student1.gpa}, {student1.age} years old')
    print(f'{student2.name},GPA: {student2.gpa}, {student2.age} years old')
    print(f'{student3.name},GPA: {student3.gpa}, {student3.age} years old')
if __name__ == "__main__":
    main()