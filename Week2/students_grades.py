class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)
        print(f"Grade {grade} added for student {self.name}.")

    def print_grades(self):
        print(f"Grades for {self.name}: {self.grades}")

class School:
    def __init__(self):
        self.students = {}

    def add_student(self, name):
        if name not in self.students:
            self.students[name] = Student(name)
            print(f"Student {name} added.")
        else:
            print(f"Student {name} already exists.")

    def add_grade(self, name, grade):
        if name in self.students:
            self.students[name].add_grade(grade)
        else:
            print(f"Student {name} does not exist.")

    def print_grades(self, name):
        if name in self.students:
            self.students[name].print_grades()
        else:
            print(f"Student {name} does not exist.")

def main():
    school = School()
    while True:
        print("\nOptions:")
        print("1. Add student")
        print("2. Add grade")
        print("3. Search for student's grades")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter student name: ")
            school.add_student(name)
        elif choice == '2':
            name = input("Enter student name: ")
            grade = float(input("Enter grade: "))
            school.add_grade(name, grade)
        elif choice == '3':
            name = input("Enter student name: ")
            school.print_grades(name)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
