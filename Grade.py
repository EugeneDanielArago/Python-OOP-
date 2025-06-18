class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        if 0 <= grade <= 100:
            self.grades.append(grade)
        else:
            print("Invalid grade! Please enter a value between 0 and 100.")

    def get_average(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def __str__(self):
        return f"{self.name} - Grades: {self.grades}\n Average: {self.get_average():.2f}"


class GradeTracker:
    def __init__(self):
        self.students = []

    def find_student(self, name):
        for student in self.students:
            if student.name.lower() == name.lower():
                return student
        return None

    def add_student(self, name):
        if self.find_student(name):
            print(f"Student '{name}' already exists.")
        else:
            new_student = Student(name)
            self.students.append(new_student)
            print(f"Added student '{name}'.")

    def add_grade(self, name, grade):
        student = self.find_student(name)
        if student:
            student.add_grade(grade)
        else:
            print(f"Student '{name}' not found.")

    def view_students(self):
        if not self.students:
            print("No students in the tracker.")
        else:
            print("\n--- All Students ---")
            for student in self.students:
                print(student)

    def view_grades(self, name):
        student = self.find_student(name)
        if student:
            print(f"\n{name}'s Grades: {student.grades}")
        else:
            print(f"Student '{name}' not found.")


tracker = GradeTracker()

while True:
    print("\n------------------------")
    print("  Student Grade Tracker")
    print("------------------------")
    print("1. Add Student")
    print("2. Add Grade")
    print("3. View Student Grades")
    print("4. Calculate Average")
    print("5. Exit")

    choice_input = input("Enter your choice (1-5): ")
    if not choice_input.isdigit():
        print("Invalid input. Please enter a number from 1 to 5.")
        continue

    choice = int(choice_input)

    if choice == 1:
        name = input("Enter Student Name to add: ")
        tracker.add_student(name)

    elif choice == 2:
        name = input("Enter student's name: ")
        grade_input = input("Enter grade (0-100): ")

        try_float = grade_input.replace('.', '', 1).isdigit() and grade_input.count('.') <= 1
        if try_float:
            grade = float(grade_input)
            tracker.add_grade(name, grade)
            print("Grade Added!")
        else:
            print("Please enter a valid number for the grade.")

    elif choice == 3:
        name = input("Enter student's name: ")
        tracker.view_grades(name)

    elif choice == 4:
        tracker.view_students()

    elif choice == 5:
        print("Exiting Grade Tracker. Goodbye!")
        break

    else:
        print("Invalid choice. Please select from 1 to 5.")
