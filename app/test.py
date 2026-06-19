import pandas as pd

# Read datasets
students = pd.read_csv("data/students.csv")
jobs = pd.read_csv("data/jobs.csv")

print("========== Students ==========")
print(students)

print("\n========== Jobs ==========")
print(jobs)