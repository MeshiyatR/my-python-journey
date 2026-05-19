# DAY 18 EXERCISES - 19th May 2026
# Topic: NumPy and Matplotlib

import numpy as np
import matplotlib.pyplot as plt

# Exercise 1: NumPy basics
arr = np.array([1, 2, 3, 4, 5,
                6, 7, 8, 9, 10])
print("NumPy Array:")
print(arr)
print(f"Shape: {arr.shape}")
print(f"Type: {arr.dtype}")
print(f"Sum: {arr.sum()}")
print(f"Mean: {arr.mean()}")
print(f"Max: {arr.max()}")
print(f"Min: {arr.min()}")
print(f"Std: {arr.std():.2f}")

# Exercise 2: NumPy operations
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([10, 20, 30, 40, 50])

print("\nArray operations:")
print(f"Addition: {arr1 + arr2}")
print(f"Multiply: {arr1 * arr2}")
print(f"Divide: {arr2 / arr1}")
print(f"Power: {arr1 ** 2}")

# NumPy special arrays
zeros = np.zeros(5)
ones = np.ones(5)
range_arr = np.arange(0, 50, 5)
linspace = np.linspace(0, 1, 5)

print(f"\nZeros: {zeros}")
print(f"Ones: {ones}")
print(f"Range: {range_arr}")
print(f"Linspace: {linspace}")

# Exercise 3: Line chart
months = ["Jan", "Feb", "Mar", "Apr",
          "May", "Jun", "Jul", "Aug",
          "Sep", "Oct", "Nov", "Dec"]
sales = [12000, 15000, 13000, 18000,
         22000, 20000, 25000, 23000,
         28000, 26000, 30000, 35000]

plt.figure(figsize=(10, 5))
plt.plot(months, sales,
         color="blue",
         marker="o",
         linewidth=2,
         markersize=8)
plt.title("Monthly Sales 2026",
          fontsize=16)
plt.xlabel("Month")
plt.ylabel("Sales (PKR)")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("line_chart.png")
plt.show()
print("Line chart saved!")

# Exercise 4: Bar chart
subjects = ["Math", "Python", "English",
            "Science", "AI"]
scores = [95, 98, 80, 88, 92]
colors = ["#FF6B6B", "#4ECDC4", "#45B7D1",
          "#96CEB4", "#FFEAA7"]

plt.figure(figsize=(8, 5))
bars = plt.bar(subjects, scores,
               color=colors,
               width=0.6)
plt.title("My Subject Scores",
          fontsize=16)
plt.xlabel("Subject")
plt.ylabel("Score")
plt.ylim(0, 110)
for bar, score in zip(bars, scores):
    plt.text(bar.get_x() +
             bar.get_width() / 2,
             bar.get_height() + 1,
             str(score),
             ha="center",
             fontsize=12)
plt.tight_layout()
plt.savefig("bar_chart.png")
plt.show()
print("Bar chart saved!")

# Exercise 5: Pie chart
skills = ["Python", "Canva", "LinkedIn",
          "Communication", "Data Analysis"]
percentages = [35, 20, 15, 20, 10]
colors = ["#FF6B6B", "#4ECDC4", "#45B7D1",
          "#96CEB4", "#FFEAA7"]
explode = (0.1, 0, 0, 0, 0)

plt.figure(figsize=(8, 8))
plt.pie(percentages,
        labels=skills,
        colors=colors,
        explode=explode,
        autopct="%1.1f%%",
        startangle=90)
plt.title("My Skills Distribution",
          fontsize=16)
plt.tight_layout()
plt.savefig("pie_chart.png")
plt.show()
print("Pie chart saved!")
