#parent class
class Employee:
    def __init__(self,name,id):
        self.name = name
        self.id = id


    def show_details(self):
        print(f"Employee name: {self.name},id: {self.id}")



class programmer(Employee):
    def show_language(self):
        print(f"{self.name}python programming par kam")



emp = programmer("Aqsa", 101)

emp.show_details()
emp.show_language()
