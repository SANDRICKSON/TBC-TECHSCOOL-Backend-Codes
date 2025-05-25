class Student:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def get_info(self):
        print(f"{self.name} {self.surname}")

class School:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.students = []  

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, index):
        if 0 <= index < len(self.students):
            removed = self.students.pop(index)
            print(f"Removed student: {removed.name} {removed.surname}")
        else:
            print("Invalid index!")

    def show_students(self):
        print(f"\nStudents in {self.name}:")
        for student in self.students:
            student.get_info()

my_school = School("5th Public School", "12 Gogebashvili str")

student1 = Student("Sandro", "Qatamadze", 15)
student2 = Student("Eka", "Tsereteli", 16)
student3 = Student("Medea", "Tsereteli", 14)


my_school.add_student(student1)
my_school.add_student(student2)
my_school.add_student(student3)

my_school.show_students()

my_school.remove_student(1)

my_school.show_students()



