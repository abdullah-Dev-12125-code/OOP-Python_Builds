class StudentGrading:
    def __init__(self, Student_name, roll_number, student_grade):
        self.Student_name = Student_name
        self.roll_number = roll_number
        self._student_grade = student_grade

    def getter(self):
        return self._student_grade

    def setter(self, grade):
        self._student_grade = grade

    def view(self):
        print("╔" + "═" * 45 + "╗")
        print(f"║ {'STUDENT REPORT CARD':^43} ║")
        print("╠" + "═" * 45 + "╣")
        print(f"║ Name        : {self.Student_name:<28}  ║")
        print(f"║ Roll Number : {self.roll_number:<28}  ║")
        print(f"║ Grade       : {self._student_grade:<28}  ║")
        print("╚" + "═" * 45 + "╝\n")


print("\n\t\t Initial Grade")
student1 = StudentGrading('John', 101, 'B')
student1.getter()
student1.view()

student1.setter('A')
print("\n\t\t Final Grade")
student1.view()
