# DAY 17 PROJECT - Student Performance Analyzer
# 18th May 2026

import pandas as pd
import json
import os
from datetime import datetime

def create_sample_data():
    data = {
        "Name": ["Meshiyat", "Sara", "Ahmed",
                 "Bilal", "Ayesha", "Zara",
                 "Hassan", "Fatima", "Ali",
                 "Sana"],
        "Math": [95, 72, 88, 61, 79,
                 55, 90, 83, 67, 94],
        "Python": [98, 85, 92, 70, 75,
                   60, 95, 88, 72, 91],
        "English": [80, 90, 75, 65, 88,
                    70, 78, 92, 80, 85],
        "Science": [88, 76, 85, 58, 82,
                    65, 91, 79, 74, 89],
        "AI": [92, 68, 87, 55, 77,
               50, 93, 81, 69, 96]
    }
    return pd.DataFrame(data)

def calculate_results(df):
    df["Total"] = df[["Math", "Python",
                       "English", "Science",
                       "AI"]].sum(axis=1)
    df["Average"] = df["Total"] / 5

    def get_grade(avg):
        if avg >= 90: return "A+"
        elif avg >= 80: return "A"
        elif avg >= 70: return "B"
        elif avg >= 60: return "C"
        else: return "F"

    def get_status(avg):
        return "PASS" if avg >= 60 else "FAIL"

    df["Grade"] = df["Average"].apply(get_grade)
    df["Status"] = df["Average"].apply(get_status)
    df["Rank"] = df["Average"].rank(
        ascending=False).astype(int)
    return df

def show_full_results(df):
    print("\n" + "=" * 65)
    print("              COMPLETE RESULTS")
    print("=" * 65)
    display = df[["Rank", "Name", "Total",
                  "Average", "Grade",
                  "Status"]].sort_values("Rank")
    for _, row in display.iterrows():
        status_icon = "✅" if row[
            "Status"] == "PASS" else "❌"
        print(f"  {int(row['Rank']):<4}"
              f"{row['Name']:<12}"
              f"Total: {row['Total']:<6}"
              f"Avg: {row['Average']:.1f:<8}"
              f"Grade: {row['Grade']:<4}"
              f"{status_icon}")
    print("=" * 65)

def show_class_statistics(df):
    print("\n" + "=" * 45)
    print("         CLASS STATISTICS")
    print("=" * 45)
    print(f"  Total Students : {len(df)}")
    print(f"  Passed         : "
          f"{len(df[df['Status']=='PASS'])}")
    print(f"  Failed         : "
          f"{len(df[df['Status']=='FAIL'])}")
    print(f"  Class Average  : "
          f"{df['Average'].mean():.1f}")
    print(f"  Highest Average: "
          f"{df['Average'].max():.1f}")
    print(f"  Lowest Average : "
          f"{df['Average'].min():.1f}")
    print("\n  Subject Averages:")
    subjects = ["Math", "Python", "English",
                "Science", "AI"]
    for subject in subjects:
        avg = df[subject].mean()
        print(f"  {subject:<10}: {avg:.1f}")
    print("=" * 45)

def show_top_students(df):
    print("\n" + "=" * 45)
    print("           TOP 3 STUDENTS")
    print("=" * 45)
    top3 = df.nlargest(3, "Average")
    medals = ["🥇", "🥈", "🥉"]
    for i, (_, row) in enumerate(
            top3.iterrows()):
        print(f"  {medals[i]} {row['Name']:<12}"
              f"Average: {row['Average']:.1f}"
              f"  Grade: {row['Grade']}")
    print("=" * 45)

def search_student(df):
    name = input("\nEnter student name: ")
    student = df[df["Name"].str.lower() ==
                 name.lower()]
    if student.empty:
        print(f"Student '{name}' not found!")
        return
    row = student.iloc[0]
    print("\n" + "=" * 45)
    print("         STUDENT REPORT")
    print("=" * 45)
    print(f"  Name   : {row['Name']}")
    print(f"  Rank   : {int(row['Rank'])}"
          f" out of {len(df)}")
    print("\n  Subject Marks:")
    subjects = ["Math", "Python", "English",
                "Science", "AI"]
    for subject in subjects:
        mark = row[subject]
        bar = "█" * int(mark / 10)
        print(f"  {subject:<10}: "
              f"{mark:<5} {bar}")
    print(f"\n  Total  : {row['Total']}")
    print(f"  Average: {row['Average']:.1f}")
    print(f"  Grade  : {row['Grade']}")
    print(f"  Status : {row['Status']}")
    print("=" * 45)

def subject_analysis(df):
    print("\n" + "=" * 45)
    print("        SUBJECT ANALYSIS")
    print("=" * 45)
    subjects = ["Math", "Python", "English",
                "Science", "AI"]
    for subject in subjects:
        avg = df[subject].mean()
        highest = df[subject].max()
        lowest = df[subject].min()
        top_student = df.loc[
            df[subject].idxmax(), "Name"]
        print(f"  {subject}:")
        print(f"    Average : {avg:.1f}")
        print(f"    Highest : {highest}"
              f" ({top_student})")
        print(f"    Lowest  : {lowest}")
        print()
    print("=" * 45)

def save_results(df):
    filename = f"results_{datetime.now().strftime('%d%m%Y')}.csv"
    df.to_csv(filename, index=False)
    print(f"\nResults saved to {filename}!")

# Main program
print("=" * 45)
print("    STUDENT PERFORMANCE ANALYZER")
print("    Powered by Python Pandas 🐼")
print("=" * 45)

df = create_sample_data()
df = calculate_results(df)

while True:
    print("\n1 - View all results")
    print("2 - Class statistics")
    print("3 - Top 3 students")
    print("4 - Search student")
    print("5 - Subject analysis")
    print("6 - Save results to CSV")
    print("7 - Quit")

    choice = input("\nEnter choice: ")

    if choice == "1":
        show_full_results(df)
    elif choice == "2":
        show_class_statistics(df)
    elif choice == "3":
        show_top_students(df)
    elif choice == "4":
        search_student(df)
    elif choice == "5":
        subject_analysis(df)
    elif choice == "6":
        save_results(df)
    elif choice == "7":
        print("Goodbye!")
        break
    else:
        print("Invalid choice!")
