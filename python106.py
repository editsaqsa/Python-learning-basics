# class method in python
class Employee:
    company = "Tech solutions"



    def __init__(self,name,salary):
        self.name = name
        self.salary = salary


    def show_details(self):
        print(
            f"Employee Name: {self.name}, salary: {self.salary}, company:{Employee.company}"
        )



    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company



emp1 = Employee("Aqsa",50000)
emp1.show_details()


Employee.change_company("Google Ai")
emp1.show_details()
print("Direct class se company check ki", Employee.company)
