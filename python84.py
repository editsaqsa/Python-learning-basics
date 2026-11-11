# seek() , tell() , and other functions in python
with open("sample.txt", "r") as f:
    f.seek(5)
print("current position:", f.tell())
data = f.read(5)
print("data read hogya", data)

