# class object in python
class student:
    def __init__(self,name,marks):

       self.name = name
       self.marks = marks


    def get_info(self):
        print(f"student name: {self.name},marks:{self.marks}")


student1 = student("aqsa",95)
student2 = student("smaira" ,88)


#method ko call krna
student1.get_info()
student2.get_info()