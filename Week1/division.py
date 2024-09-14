# Function to divide two numbers
def divide_numbers():
    try:
        # Taking input from the user
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        # Performing division
        result = num1 / num2
        
        # Printing the result
        print(f"The result of dividing {num1} by {num2} is: {result}")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except ValueError:
        print("Error: Please enter valid numbers.")

# Calling the function
divide_numbers()
