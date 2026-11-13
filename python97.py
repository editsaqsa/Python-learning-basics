# constructor in python
class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        print(f"constructor called Employee '{self.name}' ban gya hai.")



    def show_details(self):
        print(f"name: {self.name}, salary: {self.salary}")



emp1 = Employee("aqsa", 50000)
emp2 = Employee("smaira",60000)



emp1.show_details()
emp2.show_details()
