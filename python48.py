#Recursion case
def count_down(number):
    " " " count down numbers " " "
    if number == 0:
      print("time up")
      return
    print(number)
    count_down(number-1)
    print("olti counting start")
    count_down(5)



