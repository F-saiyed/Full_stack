# Creating a tuple
my_tuple = (1, "hello", 3.14)

# Accessing elements
print(my_tuple[0])  # Output: 1
print(my_tuple[1])  # Output: hello

# Tuples can be used to return multiple values from a function
def get_coordinates():
    return (10, 20)

x, y = get_coordinates()
print("X:", x)  # Output: X: 10
print("Y:", y)  # Output: Y: 20
