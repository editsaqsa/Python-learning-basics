# Generator in python
def make_squares_list(n):
    result = [ ]
    for i in range(1, n+1):
        result.append(i * i)
    return result


def generate_squares(n):
    for i in range(1, n+1):
        print(f"Generating square for {i}.....")
        yield i * i


gen = generate_squares(4)

print("First value:", next(gen))
print("Second value:", next(gen))


print("\nBaaqe values 'for' loop se:")
for val in gen:
    print("Got:" , val)

even_gen = (num for num in range(10)if num % 2 == 0)
print("\nEven numbers from generator expression:", list(even_gen))

        