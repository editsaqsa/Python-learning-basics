# hybrid and Hierarchical
class Device:
    def __init__(self,brand):
        self.brand = brand



    def power_on(self):
        print(f"{self.brand} device is turning on ...")


class laptop(Device):
    def run_code(self):
        print(f"Running python code on {self.brand} laptop...")



print("---Hierarchical inheritance---")
p = phone("Realme")
l = laptop("Dell")
p.power_on()
p.make_call("o300-1234567")
l.power_on()
l.run_code()



class person:
    def __init__(self,name):
        self.name = name



    def introduce(self):
        print(f"Hi, I am {self.name}")



class Learner(person):
    def study(self):
        print(f"{self.name} is practing python and ML...")



class Mentor:
    def guide(self):
        print(f"{self.name}is helping other with code...")


class CodingBuddy(Learner,Mentor):
    def share_notes(self):
        print(f"{self.name} is sharing diary and code with Github")


print("\n--- Hybrid inheritance---")
buddy = CodingBuddy("Aqsa")
buddy . introduce()
buddy . study()
buddy .guide()
buddy .share_notes()
print("\nMRO for codingBuddy:", [cls.__name__ for cls in CodingBuddy.__mro__])