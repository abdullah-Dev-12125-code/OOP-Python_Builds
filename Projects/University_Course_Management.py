class Course:
    def __init__(self,Course_Name,Course_code,Max_student):
        self.Course_Name = Course_Name
        self.Course_code = Course_code
        self.Max_student = Max_student
        self.students = []

    def Enroll(self,Student_Name):
        if len(self.students) < self.Max_student:
            self.students.append(Student_Name)
        else:
            print("No spaces left!!")

    def drop(self,Student_Name):
        if Student_Name in self.students:
            self.students.remove(Student_Name)
        else:
            print("No student with that Name!!")

    def info(self):
        print("="*40)
        print(f"Course: {self.Course_Name} ({self.Course_code})")
        if self.students:
            for i, student in enumerate(self.students, 1):
                print(f"{i}. {student}")
        else:
            print("No students enrolled yet.")
        print("="*40, "\n")



python_course = Course("Python Programming", "CSE101", 3)
data_stracture_course = Course("Data Structures", "CSE202", 2)

python_course.Enroll("Alice")
python_course.Enroll("Bob")

data_stracture_course.Enroll("Charlie")
data_stracture_course.Enroll("David")

data_stracture_course.Enroll("Eve")

python_course.drop("Alice")

python_course.Enroll("Eve")

python_course.info()
data_stracture_course.info()





