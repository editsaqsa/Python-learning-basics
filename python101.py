#Accessor modifier in python
class student:
    def __init__(self,name,age,roll_no):
        self.name = name
        self.__roll_no = roll_no



    def get_roll_no(self):
        return self.__roll_no



s1 = student("Aqsa",18,105)

print("name (publice):", s1.name)

print("age (protected):",s1._age)

print(s1.__roll_no)

print("roll no (private accessd via method)",s1.get_roll_no())