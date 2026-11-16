#static method in python
class Math:
    def __init__(self,num):
        self.num = num


    def addtoNum(self,n):
        self.num += n

    @staticmethod
    def add(a,b):
        return a + b


a = Math(5)
a.addtoNum(6)
print("Update num:", a.num)


sum_result = Math.add(7,3)
print("sum using statice method:", sum_result)
