class InvalidGradeException(Exception):
    pass
class UnauthorizedAccessException(Exception):
    pass


class Student:
    def __init__(self,student_name,student_ID,grade=None):
        self.__student_name = student_name
        self.__student_ID = student_ID
        self.__grade = grade
        
    
    def get_student_name(self):
        return self.__student_name

    def get_studentID(self):
        return self.__student_ID

    def get_grade(self,role):
         if role == "professor":
            print(f"Name:{self.__student_name} Grade:{self.__grade}")  
         else:
            raise UnauthorizedAccessException("You must be a professor to set grade")
    
    def set_grade(self,Newgrade,role=None):
        if role != "professor":
            raise UnauthorizedAccessException("You must be a professor to set grade")
            
        valid_grades = {"A", "B", "C", "D", "F"}

        if Newgrade not in valid_grades:
            raise InvalidGradeException("The grades can only be (A, B, C, D, F)")
        else:
            self.__grade = Newgrade


Student1 = Student("Alice",301)
Student2 = Student("Bob",302)

Student1.set_grade("A","professor")
# Student2.set_grade("Z","professor")


Student1.get_grade("professor")

# Student2.get_grade("Charlie")
