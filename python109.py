#super keyword in python
class parentClass:
    def __init__(self,name,id):
        self.name = name
        self,id = id


    def parent_method(self):
        print("yeh parentClass ka method hai")

class ChildClass(parentClass):
    def __init__(self,name,id,lang):
        super().__init__(name,id)
        self.lang = lang


    def parent_method(self):
        print("yeh childclass ka method hy")
        super().parent_method()


    def child_method(self):
        print(f"{self.name} (ID: {self.id}) {self,self.lang}seekh rahi hy.")
        super().parent_method()



c = ChildClass("Aqsa",102, "python")
c.child_method()
print("---")
c.parent_method()