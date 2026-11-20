# Operator overloding in python
class Vector:
    def __init__(self, i, j, k):
        self.i = i
        self.j = j
        self.k = k



    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"


    def __sub__(self,other):
        return Vector(self.i + other.i, self.j + other.j, self.k + other.k)


    def __sub__(self,other):
        return Vector(self.i - other.i, self.j - other.j , self.k - other.k)


v1 = Vector(3,5,6)
v2 = Vector(1,2,9)


print("Vector1:",v1)
print("Vector2:",v2)


print("\nSum (v1 + v2):", v_Sum)
print("Difference (v1 - v2):", v_diff)

