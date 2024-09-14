# Predefined list of students with their grades
students_grades = {
    "Fehmida Saiyed": "A",
    "Uzair Saiyed": "B+",
    "Vibhu Puri": "A-",
    "Atyander Singh": "C"
}

# Taking student's first and last name as input
first_name = input("Enter the student's first name: ")
last_name = input("Enter the student's last name: ")

# Combining first and last name to form the full name
full_name = f"{first_name} {last_name}"

# Checking if the student's name is in the list and printing the grade
if full_name in students_grades:
    print(f"{full_name}'s grade is {students_grades[full_name]}.")
else:
    print(f"Error: {full_name} is not in the list.")
