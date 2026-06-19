import pandas as pd

# Load datasets
students = pd.read_csv("data/students.csv")
jobs = pd.read_csv("data/jobs.csv")

# Select only skill columns
student_features = students[
    ["python", "java", "sql", "react", "machine_learning"]
]

job_features = jobs[
    ["python", "java", "sql", "react", "machine_learning"]
]

print("===== Student Feature Matrix =====")
print(student_features)

print("\n===== Job Feature Matrix =====")
print(job_features)