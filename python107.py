# class method as Alternative constructor
class Employee:

    def __init__(self,name,salary):
        self.name = name
        self.salary = salary


    def show_details(self):
        print(f"Employee name: {self.name}, salary:{self.salary}")



    @classmethod
    def from_str(cls, string_data):
        name, salary = string_data.splite("_")
        return cls(name, int(salary))


emp1 = Employee("Aqsa",50000)
emp1.show_details()
string_input = "Smaira-60000"
emp2 = Employee.from_str(string_input)
emp2.show_details()