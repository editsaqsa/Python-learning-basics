# Single inheritance in python
class Employee:
    def __init__(self,name,emp_id):
        self.name = name
        self.emp_id = emp_id


    def show_info(self):
        print(f"Name: {self.name}, ID: {self.emp_id}")


class programmer(Employee):


    def __init(self,name,emp_id, Language):
        super().__init__(name,emp_id)
        self.Language = Language


    def show_Language(self):
        print(f"{self.name}uses {self.language} for coding.")


emp = Employee("Aqsa",101)
emp.show_info()

print("---")

dev = programmer("Aqsa", 102, "Python")
dev.show_info()
dev.show_language()