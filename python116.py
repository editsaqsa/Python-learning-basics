#Multilevel inheritance in python
class LivingBeing:
    def __init__(self,category):
        self.category = category


    def show_category(self):
        print(f"Category: {self.category}")


class Animal(LivingBeing):
    def __init__(self,category,species):
        super().__init__(category)
        self.species = species


    def show_species(self):
        print(f"species: {self.species}")


class Cat(Animal):
    def __init__(self,category,species, name):
        super().__init__(category, species)
        self.name = name


    def show_details(self):
        self.show_category()
        self.show_species()
        print(f"Cat Name: {self.name}")


my_cat = Cat("Mammal", "Felidae", "Mimi")
my_cat.show_details()
