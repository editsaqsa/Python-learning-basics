#cstom error
age = int(input("apni age 18 ya 60 ka darmyan likhnana"))
if age < 18 or age > 60:
    raise ValueError("age should be between 18 and 60")
print("age is valid")
