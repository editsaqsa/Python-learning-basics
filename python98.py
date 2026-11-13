# Decorators in python

def greet_decorator(fx):
    def mfx():

        print("good morning ")
        fx()
        print("thanks for using this funcion")


    return mfx


@greet_decorator
def hello():
    print("hello aqsa, python programing kasi ja rahi haa ")


hello()