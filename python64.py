# for loops with else statment
for i in range(1,4):
    print(f"loop ka chakar number: {i}")
else:
    print("loop kamyabi sa pora ho gya")
    for i in range(1,6):
        if i == 3:
            print("yaha pr break hogya")
            break
        print(f"number: {i}")
    else:
        print("loop pora nahi hua")
        
