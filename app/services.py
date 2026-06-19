import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# ============================================
# Load Datasets
# ============================================

students = pd.read_csv("data/students.csv")
jobs = pd.read_csv("data/jobs.csv")

# ============================================
# Feature Columns
# ============================================

SKILL_COLUMNS = [
    "python",
    "java",
    "sql",
    "react",
    "machine_learning",
    "communication"
]

# ============================================
# Feature Matrices
# ============================================

student_features = students[SKILL_COLUMNS]
job_features = jobs[SKILL_COLUMNS]

# ============================================
# Cosine Similarity Matrix
# ============================================

similarity_matrix = cosine_similarity(student_features, job_features)


# ============================================
# Match Function
# ============================================

def get_match(student_id: int, job_id: int):

    # ----------------------------------------
    # Find Student
    # ----------------------------------------
    student_df = students[students["student_id"] == student_id]

    if student_df.empty:
        raise ValueError("Student Not Found")

    # ----------------------------------------
    # Find Job
    # ----------------------------------------
    job_df = jobs[jobs["job_id"] == job_id]

    if job_df.empty:
        raise ValueError("Job Not Found")

    student = student_df.iloc[0]
    job = job_df.iloc[0]

    student_index = student_df.index[0]
    job_index = job_df.index[0]

    # ----------------------------------------
    # Calculate Match Score
    # ----------------------------------------
    score = round(similarity_matrix[student_index][job_index] * 100, 2)

    # ----------------------------------------
    # Recommendation Status
    # ----------------------------------------
    if score >= 90:
        status = "⭐⭐ Highly Recommended"
    elif score >= 75:
        status = "✅ Recommended"
    elif score >= 60:
        status = "⚠ Average Match"
    else:
        status = "❌ Not Recommended"

    # ----------------------------------------
    # Explainable AI
    # ----------------------------------------
    reasons = []

    # Skill Matching
    for skill in SKILL_COLUMNS:

        if job[skill] == 1:

            if student[skill] >= 70:
                reasons.append(f"{skill.replace('_', ' ').title()} matched")
            else:
                reasons.append(f"{skill.replace('_', ' ').title()} needs improvement")

    # Experience Check
    if student["experience"] >= job["experience"]:
        reasons.append("Experience requirement satisfied")
    else:
        reasons.append("Experience below requirement")

    # Academic Performance
    if student["cgpa"] >= 8.5:
        reasons.append("Excellent academic performance")
    elif student["cgpa"] >= 7.5:
        reasons.append("Good academic performance")
    else:
        reasons.append("Academic performance needs improvement")

    # Communication Skills
    if student["communication"] >= 85:
        reasons.append("Excellent communication skills")
    elif student["communication"] >= 70:
        reasons.append("Good communication skills")
    else:
        reasons.append("Communication skills need improvement")

    # Overall Recommendation
    if score >= 90:
        reasons.append("Strong overall fit for this job")
    elif score >= 75:
        reasons.append("Suitable candidate with minor improvements needed")
    else:
        reasons.append("Candidate requires additional skill development")

    # ----------------------------------------
    # API Response
    # ----------------------------------------
    return {
        "student_id": int(student["student_id"]),
        "student_name": student["name"],
        "job_id": int(job["job_id"]),
        "company": job["company"],
        "match_score": score,
        "status": status,
        "reason": reasons
    }

def rank_candidates(job_id: int):

    job_df = jobs[jobs["job_id"] == job_id]

    if job_df.empty:
        raise ValueError("Job Not Found")

    job_index = job_df.index[0]

    rankings = []

    for index, student in students.iterrows():

        score = round(similarity_matrix[index][job_index] * 100, 2)

        if score >= 90:
            status = "⭐⭐ Highly Recommended"

        elif score >= 75:
            status = "✅ Recommended"

        elif score >= 60:
            status = "⚠ Average Match"

        else:
            status = "❌ Not Recommended"

        rankings.append({

            "student_id": int(student["student_id"]),

            "student_name": student["name"],

            "match_score": score,

            "status": status

        })

    rankings = sorted(

        rankings,

        key=lambda x: x["match_score"],

        reverse=True

    )

    for i, candidate in enumerate(rankings, start=1):

        candidate["rank"] = i

    return rankings