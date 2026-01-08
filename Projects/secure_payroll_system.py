class Employee:
    def __init__(self,name,employee_id,salary):
        self.__name = name
        self.__employee_id = employee_id
        self.__salary = salary

    def get_name_EMP_id(self):
        print(f"Name:{self.__name} EMP[ID]:{self.__employee_id}")

    def View_salary(self,Role):
        if Role != "HR":
            print("Only HR can view salary")
        else:
            print(f"{self.__name}:${self.__salary}") 

    def Set_salary(self,new_salary):
        if new_salary > 0:
            self.__salary = new_salary
        else:
            print("Salary cannot be negative!")

Employee1 = Employee("Alice", 101, 5000)  
Employee1.Set_salary(-2000)

Employee2 = Employee("Bob",102,7000)
Employee2.View_salary("HR")

employee3 = Employee("Charlie",103,6000)
employee3.View_salary("Manager")




 