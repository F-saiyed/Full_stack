# Function to check if a number is positive, negative, or zero
def check_number(num):
    if num > 0:
        return "Positive number"
    else:
        if num < 0:
            return "Negative number"
        else:
            return "Zero"

# Test the function
number = float(input("Enter a number: "))
result = check_number(number)
print(result)
