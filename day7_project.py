# DAY 7 PROJECT - Student Grade Calculator
# 8th May 2026

def get_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    else:
        return "F"

def get_status(grade):
    if grade == "F":
        return "FAIL"
    else:
        return "PASS"

def calculate_average(marks_list):
    total = sum(marks_list)
    average = total / len(marks_list)
    return average

def print_report(name, marks_list):
    print("=" * 45)
    print("        STUDENT GRADE REPORT")
    print("=" * 45)
    print(f"  Student Name : {name}")
    print("-" * 45)

    subjects = ["Math", "Science", "English",
                "Computer", "Urdu"]

    for i in range(len(subjects)):
        grade = get_grade(marks_list[i])
        print(f"  {subjects[i]:<10}: {marks_list[i]}  Grade: {grade}")

    average = calculate_average(marks_list)
    final_grade = get_grade(average)
    status = get_status(final_grade)

    print("-" * 45)
    print(f"  Average      : {average:.1f}")
    print(f"  Final Grade  : {final_grade}")
    print(f"  Status       : {status}")
    print("=" * 45)

# Main program
print("=" * 45)
print("     STUDENT GRADE CALCULATOR")
print("=" * 45)

name = input("Enter student name: ")
marks = []

subjects = ["Math", "Science", "English",
            "Computer", "Urdu"]

for subject in subjects:
    mark = int(input(f"Enter {subject} marks (0-100): "))
    marks.append(mark)

print_report(name, marks)