# Dictionary to store student names and their grades
students = {}

# Function to add a new student
def add_student(name):
    if name not in students:
        students[name] = []
        print(f"Student {name} added.")
    else:
        print(f"Student {name} already exists.")

# Function to add grades for an existing student
def add_grade(name, grade):
    if name in students:
        students[name].append(grade)
        print(f"Grade {grade} added for student {name}.")
    else:
        print(f"Student {name} does not exist.")

# Function to print all grades for a specific student
def print_grades(name):
    if name in students:
        print(f"Grades for {name}: {students[name]}")
    else:
        print(f"Student {name} does not exist.")

# Example usage
add_student("Alice")
add_student("Bob")
add_grade("Alice", 90)
add_grade("Alice", 85)
add_grade("Bob", 78)
print_grades("Alice")
print_grades("Bob")
print_grades("Charlie")  # This will show that Charlie does not exist
