# DAY 13 PROJECT - Smart Data Processor
# 14th May 2026

def process_numbers(numbers):
    print("=" * 45)
    print("        NUMBER PROCESSOR")
    print("=" * 45)
    print(f"  Original    : {numbers}")

    evens = list(filter(lambda x: x % 2 == 0,
                        numbers))
    odds = list(filter(lambda x: x % 2 != 0,
                       numbers))
    squares = list(map(lambda x: x**2, numbers))
    doubled = list(map(lambda x: x*2, numbers))
    greater_10 = [x for x in numbers if x > 10]
    even_squares = [x**2 for x in numbers
                    if x % 2 == 0]

    print(f"  Evens       : {evens}")
    print(f"  Odds        : {odds}")
    print(f"  Squares     : {squares}")
    print(f"  Doubled     : {doubled}")
    print(f"  Greater 10  : {greater_10}")
    print(f"  Even squares: {even_squares}")
    print(f"  Sum         : {sum(numbers)}")
    print(f"  Average     : {sum(numbers)/len(numbers):.1f}")
    print(f"  Maximum     : {max(numbers)}")
    print(f"  Minimum     : {min(numbers)}")
    print("=" * 45)

def process_words(words):
    print("=" * 45)
    print("         WORD PROCESSOR")
    print("=" * 45)
    print(f"  Original  : {words}")

    upper = list(map(lambda w: w.upper(), words))
    lengths = list(map(lambda w: len(w), words))
    long_words = list(filter(lambda w: len(w) > 4,
                             words))
    short_words = list(filter(lambda w: len(w) <= 4,
                              words))
    sorted_words = sorted(words)
    reversed_words = sorted(words, reverse=True)

    print(f"  Uppercase : {upper}")
    print(f"  Lengths   : {lengths}")
    print(f"  Long words: {long_words}")
    print(f"  Short words:{short_words}")
    print(f"  Sorted    : {sorted_words}")
    print(f"  Reversed  : {reversed_words}")
    print("=" * 45)

def student_processor():
    students = [
        {"name": "Meshiyat", "marks": 95},
        {"name": "Sara", "marks": 72},
        {"name": "Ahmed", "marks": 88},
        {"name": "Bilal", "marks": 61},
        {"name": "Ayesha", "marks": 79},
        {"name": "Zara", "marks": 55}
    ]

    print("=" * 45)
    print("       STUDENT PROCESSOR")
    print("=" * 45)

    passed = list(filter(
        lambda s: s["marks"] >= 60, students))
    failed = list(filter(
        lambda s: s["marks"] < 60, students))
    top_students = list(filter(
        lambda s: s["marks"] >= 80, students))

    sorted_students = sorted(
        students, key=lambda s: s["marks"],
        reverse=True)

    print("  All students (ranked):")
    for i, s in enumerate(sorted_students, 1):
        status = "✓" if s["marks"] >= 60 else "✗"
        print(f"  {i}. {s['name']:<12}"
              f"Marks: {s['marks']} {status}")

    print(f"\n  Passed  : {len(passed)}")
    print(f"  Failed  : {len(failed)}")
    print(f"  Top (80+): {len(top_students)}")
    avg = sum(s["marks"] for s in students) / len(students)
    print(f"  Average : {avg:.1f}")
    print("=" * 45)

# Main program
print("=" * 45)
print("      SMART DATA PROCESSOR")
print("=" * 45)

while True:
    print("\n1 - Process numbers")
    print("2 - Process words")
    print("3 - Process student data")
    print("4 - Quit")

    choice = input("\nEnter choice (1/2/3/4): ")

    if choice == "1":
        nums = [3, 7, 2, 15, 8, 12, 5,
                19, 4, 11, 6, 18]
        process_numbers(nums)

    elif choice == "2":
        words = ["python", "AI", "google",
                 "germany", "code", "learn",
                 "engineering", "data"]
        process_words(words)

    elif choice == "3":
        student_processor()

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")
