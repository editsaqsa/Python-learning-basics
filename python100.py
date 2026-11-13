#Getter and setter
class Myclass:
    def __init__(self,value):
        self._value = value


        @property
        def value(self):
            return self._value


    @value.setter
    def value(self,new value):
        if new_value < 0:
            print("value negative nahi ho sakta ")
        else:
            self._value = new_value


obj = Myclass(10)

print("current value:", obj.value)


obj.value = 25
print("update value:",obj.value)

obj.value = -5
