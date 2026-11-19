# dir_dict_and help method in python
class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age



    def info(self):
        print(f"mera name {self.name}hai our meri age {self.age} years ha.")

p = person("Aqsa",18)
print("___dir()output___")
print(dir(p))
print("\n--- ___dict__output---")
print("\n---help()output---")
help(person)
