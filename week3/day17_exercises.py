# DAY 17 EXERCISES - 18th May 2026
# Topic: Pandas Data Analysis

import pandas as pd

# Exercise 1: Creating DataFrames
data = {
    "Name": ["Meshiyat", "Sara", "Ahmed",
             "Bilal", "Ayesha"],
    "Age": [28, 22, 25, 30, 24],
    "City": ["Gilgit", "Lahore", "Karachi",
             "Islamabad", "Peshawar"],
    "Salary": [50000, 35000, 45000,
               60000, 40000]
}

df = pd.DataFrame(data)
print("Complete DataFrame:")
print(df)
print(f"\nShape: {df.shape}")
print(f"Columns: {list(df.columns)}")
print(f"Total rows: {len(df)}")

# Exercise 2: Accessing data
print("\nFirst 3 rows:")
print(df.head(3))

print("\nLast 2 rows:")
print(df.tail(2))

print("\nName column:")
print(df["Name"])

print("\nName and Salary:")
print(df[["Name", "Salary"]])

print("\nFirst row:")
print(df.iloc[0])

# Exercise 3: Filtering data
print("\nAge greater than 24:")
print(df[df["Age"] > 24])

print("\nSalary greater than 40000:")
print(df[df["Salary"] > 40000])

print("\nFrom Lahore or Karachi:")
print(df[df["City"].isin(["Lahore", "Karachi"])])

# Exercise 4: Basic statistics
print("\nBasic Statistics:")
print(df.describe())

print(f"\nAverage age: {df['Age'].mean():.1f}")
print(f"Max salary: {df['Salary'].max()}")
print(f"Min salary: {df['Salary'].min()}")
print(f"Total salary: {df['Salary'].sum()}")

# Exercise 5: Adding and sorting
df["Experience"] = [5, 2, 3, 8, 4]
df["Bonus"] = df["Salary"] * 0.10
print("\nWith new columns:")
print(df)

sorted_df = df.sort_values("Salary",
                            ascending=False)
print("\nSorted by salary (highest first):")
print(sorted_df[["Name", "Salary", "Bonus"]])
