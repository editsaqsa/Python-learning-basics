#instance variable vs class variable
class Employee:
    company_name = "Tech solution"
    no_of_employee = 0


    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        Employee.no_of_employee += 1



    def show_details(self):
        print(
            f"Employee name: {self.name}, salary: {self.salary},company:{Employee.company_name}"
        )



emp1 = Employee("Aqsa", 50000)
emp2 = Employee("Ayesha",60000)



emp1.show_details()
emp2.show_details()

print(f"Total Employee: {Employee.no_of_employees}")
