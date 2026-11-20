#Multiple Inheritance in python 
class coder:
    def __init__(self,language):
        self.language = language


    def skill(self):
        print(f"Coding skill: {self.language}")



class Designer:
    def __init__(self,tool):
        self.tool = tool


    def design_skill(self):
        print(f"Design tool: {self.tool}")


class FullStackCreator(coder, Designer):


    def __init__(self,name,language,tool):
        self.name = name
        coder.__init__(self,language)
        Designer.__init__(self,tool)


    def show_profile(self):
        print(f"Name: {self.name}")
        self.skill()
        self.design_skill()


creator = FullStackCreator("Aqsa", "Python", "Figma")
creator.show_profile()
print("\nMRO Order:", [cls.__name__ for cls in FullStackCreator.__mro__])
