# DAY 10 PROJECT - Student Management System
# 11th May 2026

class Student:
    total_students = 0

    def __init__(self, name, age, subjects):
        self.name = name
        self.age = age
        self.subjects = subjects
        self.marks = {}
        Student.total_students += 1
        self.student_id = Student.total_students

    def add_marks(self, subject, mark):
        if subject in self.subjects:
            self.marks[subject] = mark
            print(f"Marks added for {subject}!")
        else:
            print(f"{subject} not in student's subjects!")

    def calculate_average(self):
        if len(self.marks) == 0:
            return 0
        return sum(self.marks.values()) / len(self.marks)

    def get_grade(self):
        avg = self.calculate_average()
        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        elif avg >= 60:
            return "D"
        else:
            return "F"

    def display_report(self):
        print("=" * 45)
        print("         STUDENT REPORT CARD")
        print("=" * 45)
        print(f"  ID      : {self.student_id}")
        print(f"  Name    : {self.name}")
        print(f"  Age     : {self.age}")
        print("-" * 45)
        print("  MARKS:")
        for subject, mark in self.marks.items():
            print(f"  {subject:<15}: {mark}")
        print("-" * 45)
        print(f"  Average : {self.calculate_average():.1f}")
        print(f"  Grade   : {self.get_grade()}")
        print("=" * 45)

class School:
    def __init__(self, name):
        self.name = name
        self.students = []

    def add_student(self, student):
        self.students.append(student)
        print(f"Student {student.name} added!")

    def find_student(self, name):
        for student in self.students:
            if student.name.lower() == name.lower():
                return student
        return None

    def display_all(self):
        print(f"\n{'=' * 45}")
        print(f"  {self.name} — All Students")
        print(f"{'=' * 45}")
        for student in self.students:
            avg = student.calculate_average()
            print(f"  {student.student_id}. {student.name:<15} Grade: {student.get_grade()} Avg: {avg:.1f}")
        print(f"  Total Students: {Student.total_students}")
        print(f"{'=' * 45}")

# Main program
school = School("Python Academy")

student1 = Student("Meshiyat", 28,
                   ["Math", "Python", "AI"])
student2 = Student("Sara", 22,
                   ["Math", "Python", "English"])
student3 = Student("Ahmed", 25,
                   ["Math", "Python", "AI"])

school.add_student(student1)
school.add_student(student2)
school.add_student(student3)

student1.add_marks("Math", 95)
student1.add_marks("Python", 98)
student1.add_marks("AI", 92)

student2.add_marks("Math", 78)
student2.add_marks("Python", 85)
student2.add_marks("English", 90)

student3.add_marks("Math", 88)
student3.add_marks("Python", 92)
student3.add_marks("AI", 95)

while True:
    print("\n1 - View all students")
    print("2 - Search student")
    print("3 - View student report")
    print("4 - Quit")

    choice = input("\nEnter choice (1/2/3/4): ")

    if choice == "1":
        school.display_all()

    elif choice == "2":
        name = input("Enter student name: ")
        student = school.find_student(name)
        if student:
            print(f"Found: {student.name}")
            student.display_report()
        else:
            print("Student not found!")

    elif choice == "3":
        name = input("Enter student name: ")
        student = school.find_student(name)
        if student:
            student.display_report()
        else:
            print("Student not found!")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")