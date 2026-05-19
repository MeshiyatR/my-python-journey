# DAY 18 PROJECT - Personal Progress Dashboard
# 19th May 2026

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime
import os

def create_learning_data():
    data = {
        "Day": list(range(1, 19)),
        "Topic": [
            "Variables", "Strings",
            "Conditions", "Loops",
            "Lists", "Dictionaries",
            "Functions", "File Handling",
            "Error Handling", "OOP Basics",
            "Inheritance", "Modules",
            "Comprehensions", "Decorators",
            "APIs", "JSON",
            "Pandas", "NumPy"
        ],
        "Hours_Studied": [
            3, 3, 3, 3, 3, 3, 3,
            3, 3, 3, 3, 3, 3, 3,
            3, 3, 3, 3
        ],
        "Difficulty": [
            3, 3, 4, 4, 3, 4, 5,
            4, 5, 6, 7, 5, 6, 8,
            7, 6, 7, 7
        ],
        "Confidence": [
            5, 6, 6, 7, 7, 7, 8,
            7, 8, 6, 7, 8, 8, 7,
            8, 8, 8, 8
        ]
    }
    return pd.DataFrame(data)

def plot_learning_journey(df):
    fig, axes = plt.subplots(2, 2,
                              figsize=(14, 10))
    fig.suptitle(
        "Meshiyat's Python Learning Journey\n"
        "Day 1 to Day 18",
        fontsize=16,
        fontweight="bold"
    )

    # Chart 1: Hours studied per day
    axes[0, 0].bar(df["Day"],
                   df["Hours_Studied"],
                   color="#4ECDC4",
                   alpha=0.8)
    axes[0, 0].set_title(
        "Hours Studied Per Day")
    axes[0, 0].set_xlabel("Day")
    axes[0, 0].set_ylabel("Hours")
    axes[0, 0].set_ylim(0, 6)
    axes[0, 0].grid(True, alpha=0.3)

    # Chart 2: Difficulty progression
    axes[0, 1].plot(df["Day"],
                    df["Difficulty"],
                    color="#FF6B6B",
                    marker="o",
                    linewidth=2,
                    markersize=6)
    axes[0, 1].fill_between(
        df["Day"],
        df["Difficulty"],
        alpha=0.3,
        color="#FF6B6B"
    )
    axes[0, 1].set_title(
        "Topic Difficulty Progression")
    axes[0, 1].set_xlabel("Day")
    axes[0, 1].set_ylabel(
        "Difficulty (1-10)")
    axes[0, 1].grid(True, alpha=0.3)

    # Chart 3: Confidence growth
    axes[1, 0].plot(df["Day"],
                    df["Confidence"],
                    color="#45B7D1",
                    marker="s",
                    linewidth=2,
                    markersize=6)
    axes[1, 0].fill_between(
        df["Day"],
        df["Confidence"],
        alpha=0.3,
        color="#45B7D1"
    )
    axes[1, 0].set_title(
        "Confidence Growth Over Time")
    axes[1, 0].set_xlabel("Day")
    axes[1, 0].set_ylabel(
        "Confidence (1-10)")
    axes[1, 0].grid(True, alpha=0.3)

    # Chart 4: Topics covered pie chart
    categories = {
        "Basics": 4,
        "Data Structures": 3,
        "OOP": 3,
        "Advanced Python": 3,
        "Libraries": 5
    }
    colors = ["#FF6B6B", "#4ECDC4",
              "#45B7D1", "#96CEB4",
              "#FFEAA7"]
    axes[1, 1].pie(
        categories.values(),
        labels=categories.keys(),
        colors=colors,
        autopct="%1.0f%%",
        startangle=90
    )
    axes[1, 1].set_title(
        "Topics Covered by Category")

    plt.tight_layout()
    plt.savefig("learning_dashboard.png",
                dpi=150,
                bbox_inches="tight")
    plt.show()
    print("\nDashboard saved as "
          "learning_dashboard.png!")

def show_statistics(df):
    print("\n" + "=" * 45)
    print("      LEARNING STATISTICS")
    print("=" * 45)
    total_hours = df["Hours_Studied"].sum()
    avg_hours = df["Hours_Studied"].mean()
    total_days = len(df)
    avg_difficulty = df["Difficulty"].mean()
    avg_confidence = df["Confidence"].mean()
    max_confidence = df["Confidence"].max()

    print(f"  Total days     : {total_days}")
    print(f"  Total hours    : {total_hours}")
    print(f"  Daily average  : {avg_hours:.1f}h")
    print(f"  Avg difficulty : "
          f"{avg_difficulty:.1f}/10")
    print(f"  Avg confidence : "
          f"{avg_confidence:.1f}/10")
    print(f"  Peak confidence: "
          f"{max_confidence}/10")

    first_conf = df["Confidence"].iloc[0]
    last_conf = df["Confidence"].iloc[-1]
    growth = last_conf - first_conf
    print(f"  Confidence growth: "
          f"+{growth} points")
    print("=" * 45)

def weekly_summary(df):
    print("\n" + "=" * 45)
    print("        WEEKLY SUMMARY")
    print("=" * 45)
    df["Week"] = ((df["Day"] - 1) // 7) + 1

    for week in df["Week"].unique():
        week_data = df[df["Week"] == week]
        print(f"\n  Week {week}:")
        print(f"  Days    : {len(week_data)}")
        print(f"  Hours   : "
              f"{week_data['Hours_Studied'].sum()}")
        print(f"  Topics  : "
              f"{', '.join(week_data['Topic'].tolist()[:3])}...")
        print(f"  Avg Conf: "
              f"{week_data['Confidence'].mean():.1f}")
    print("=" * 45)

def numpy_analysis(df):
    print("\n" + "=" * 45)
    print("       NUMPY ANALYSIS")
    print("=" * 45)

    hours = np.array(df["Hours_Studied"])
    difficulty = np.array(df["Difficulty"])
    confidence = np.array(df["Confidence"])

    print(f"  Hours array: {hours}")
    print(f"\n  Difficulty stats:")
    print(f"  Mean : {difficulty.mean():.2f}")
    print(f"  Std  : {difficulty.std():.2f}")
    print(f"  Min  : {difficulty.min()}")
    print(f"  Max  : {difficulty.max()}")

    print(f"\n  Confidence stats:")
    print(f"  Mean : {confidence.mean():.2f}")
    print(f"  Std  : {confidence.std():.2f}")
    print(f"  Growth: "
          f"{confidence[-1] - confidence[0]}")

    correlation = np.corrcoef(
        difficulty, confidence)[0, 1]
    print(f"\n  Difficulty-Confidence")
    print(f"  Correlation: {correlation:.2f}")
    if correlation > 0:
        print(f"  Harder topics = "
              f"more confidence!")
    print("=" * 45)

# Main program
print("=" * 45)
print("   PERSONAL PROGRESS DASHBOARD")
print("   NumPy + Matplotlib + Pandas")
print("=" * 45)

df = create_learning_data()

while True:
    print("\n1 - Generate learning dashboard")
    print("2 - Show statistics")
    print("3 - Weekly summary")
    print("4 - NumPy analysis")
    print("5 - Quit")

    choice = input("\nEnter choice: ")

    if choice == "1":
        plot_learning_journey(df)
    elif choice == "2":
        show_statistics(df)
    elif choice == "3":
        weekly_summary(df)
    elif choice == "4":
        numpy_analysis(df)
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice!")
