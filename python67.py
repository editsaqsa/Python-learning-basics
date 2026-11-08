# finally keyword in python is used to define a block of code that will always be executed
def risk_code():
     print(10/10)

def handle_error(e):
    print(f"error pakra gya hai: {e}")

def cleanup():
    print("cleanup code ho raha hy ...")

try:
        risk_code()
except Exception as e:
     handle_error(e)
finally:
     cleanup()
     

    