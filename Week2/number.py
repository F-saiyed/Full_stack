numbers = []
while True:
    num = input("Enter a number (or 'S' to exit): ")
    if num.lower() == "s":
        break
    try:
        num = int(num)
        numbers.append(num)
    except ValueError:
        print("Invalid input. Please enter a valid number.")

total = sum(numbers)
print("The sum of the numbers is:",total)