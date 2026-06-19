import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# Load datasets
students = pd.read_csv("data/students.csv")
jobs = pd.read_csv("data/jobs.csv")

skills = ["python", "java", "sql", "react", "machine_learning"]

student_features = students[skills]
job_features = jobs[skills]

similarity = cosine_similarity(student_features, job_features)

print("\n========== AI Job Recommendation ==========\n")

for i, student in students.iterrows():

    best_job_index = similarity[i].argmax()

    best_job = jobs.iloc[best_job_index]

    best_score = similarity[i][best_job_index] * 100

    print(f"Student : {student['name']}")
    print(f"Recommended Company : {best_job['company']}")
    print(f"Match Score : {best_score:.2f}%")

    print("\nReason:")

    for skill in skills:

        if best_job[skill] == 1:
            print(f"✔ {skill.capitalize()} matched")

    print("-" * 50)