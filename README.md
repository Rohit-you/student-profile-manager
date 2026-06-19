# AI Job Matching System

## 📌 Project Overview

The AI Job Matching System is an AI/ML-based recruitment application that recommends suitable jobs for students based on their technical skills, communication skills, academic performance, and experience. The system uses the Cosine Similarity algorithm to calculate the similarity between student profiles and job requirements.

The application is developed using FastAPI, Pandas, and Scikit-learn, providing REST APIs for job matching and candidate ranking.

---

# 🎯 Objectives

* Match students with suitable job opportunities.
* Recommend jobs based on skill similarity.
* Rank candidates for a specific job.
* Provide explainable AI recommendations.
* Demonstrate AI/ML concepts using FastAPI.

---

# ✨ Features

* Student and Job Dataset Management
* AI-based Job Recommendation
* Candidate Ranking System
* Cosine Similarity Matching
* Explainable AI Recommendations
* FastAPI REST APIs
* Swagger API Documentation
* Error Handling
* JSON Response Format

---

# 🛠️ Technologies Used

| Technology   | Purpose               |
| ------------ | --------------------- |
| Python 3.9+  | Programming Language  |
| FastAPI      | Backend API Framework |
| Pandas       | Data Processing       |
| NumPy        | Numerical Computation |
| Scikit-learn | Cosine Similarity     |
| Uvicorn      | FastAPI Server        |
| VS Code      | Code Editor           |

---

# 📂 Project Structure

```
AI-Job-Matching-System
│
├── app
│   ├── main.py
│   ├── services.py
│   ├── schemas.py
│   ├── matching.py
│   ├── feature_engineering.py
│   └── test.py
│
├── data
│   ├── students.csv
│   └── jobs.csv
│
├── model
├── notebooks
├── requirements.txt
├── README.md
└── venv
```

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/your-username/AI-Job-Matching-System.git
```

## Open Project

```bash
cd AI-Job-Matching-System
```

## Create Virtual Environment

```bash
python -m venv venv
```

## Activate Virtual Environment

Windows

```bash
venv\Scripts\activate
```

Linux / Mac

```bash
source venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run FastAPI Server

```bash
uvicorn app.main:app --reload
```

---

# 🌐 API Documentation

After starting the server, open:

```
http://127.0.0.1:8000/docs
```

Swagger UI will automatically open.

---

# 📡 API Endpoints

## Home

**GET /**

Returns API status.

---

## Match Student with Job

**POST /match**

Request

```json
{
    "student_id": 1,
    "job_id": 104
}
```

Response

```json
{
    "student_id": 1,
    "student_name": "Amar",
    "job_id": 104,
    "company": "Google",
    "match_score": 99.61,
    "status": "⭐⭐ Highly Recommended",
    "reason": [
        "Python matched",
        "Java matched",
        "SQL matched",
        "React matched",
        "Machine Learning matched"
    ]
}
```

---

## Rank Candidates

**POST /rank-candidates**

Request

```json
{
    "job_id": 104
}
```

Response

```json
[
    {
        "rank": 1,
        "student_id": 3,
        "student_name": "Priya",
        "match_score": 99.85,
        "status": "⭐⭐ Highly Recommended"
    }
]
```

---

# 🤖 AI Algorithm

The project uses the **Cosine Similarity** algorithm from the Scikit-learn library.

The algorithm compares the feature vectors of students and job requirements to calculate the similarity score.

The similarity score is converted into a percentage to determine how well a student matches a job.

---

# 📊 Dataset

### Student Dataset

The student dataset contains:

* Student ID
* Name
* Python
* Java
* SQL
* React
* Machine Learning
* Communication
* Experience
* CGPA

### Job Dataset

The job dataset contains:

* Job ID
* Company
* Required Skills
* Communication Requirement
* Experience Requirement

---

# 📈 Recommendation Levels

| Match Score   | Recommendation        |
| ------------- | --------------------- |
| 90% and above | ⭐⭐ Highly Recommended |
| 75% - 89%     | ✅ Recommended         |
| 60% - 74%     | ⚠ Average Match       |
| Below 60%     | ❌ Not Recommended     |

---

# 🚀 Future Enhancements

* Resume Upload
* Resume Skill Extraction using NLP
* Machine Learning Classification Models
* Database Integration (MySQL/PostgreSQL)
* Authentication and Authorization
* Web Frontend using React
* Cloud Deployment

---

# 👨‍💻 Author

**Amar Jaiswal**

AI/ML Developer

---

# 📄 License

This project is licensed under the MIT License.
