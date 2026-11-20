#Method Override
class shape:
    def __init__(self,x,y):
        self.x = x
        self.y = y



    def area(self):
        return self.x * self.y



class Circle(shape):
    def __init__(self,radius):
        self.radius = radius
        super(). __init__(radius,radius)



    def area(self):
        return 3.14 * super().area()



rect = shape(4,5)
print("shape (4*5) area:", rect.area())
C = Circle(5)
print("Circle (radius 5) area:", C.area())
