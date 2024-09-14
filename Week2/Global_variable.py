# Global variable
x = "global"

def my_function():
    # Local variable
    x = "local"
    print("Inside the function, x is:", x)

my_function()
print("Outside the function, x is:", x)

# Modifying global variable inside a function
def modify_global():
    global x
    x = "modified global"
    print("Inside modify_global, x is:", x)

modify_global()
print("After modify_global, x is:", x)
