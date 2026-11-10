# local vs global variables
a = 50
def test():
    a = 10
    print("inside",a)
    test()
    print("outside",a)
    