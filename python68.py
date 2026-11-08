def risk_code():
    print(20/20)

def handle_error(e):
    print(f"error pakra gya hai: {e}")

def cleanup():
    print("cleanup code ho raha hy ...")

try:
    number = [1, 2, 3]
    print(number[1])
except IndexError as e:
    print("finally index ka error pakra gya hai")
finally:
    print("asa code jo har hal ma run hoga without errror ")
    
