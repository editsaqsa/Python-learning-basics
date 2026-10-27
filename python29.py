def add_all(*args):
    total = 0
    for num in args:
        total += num
    print("variable-length argument total:", total)
    
add_all(1, 2, 3, 4, 5)
add_all(10, 20, 30)
