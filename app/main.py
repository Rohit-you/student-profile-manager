from typing import List

from fastapi import FastAPI, HTTPException

from app.schemas import (
    MatchRequest,
    MatchResponse,
    RankRequest,
    Candidate
)

from app.services import (
    get_match,
    rank_candidates
)

app = FastAPI(
    title="AI Job Matching API",
    description="AI/ML based Student Job Recommendation System using Cosine Similarity.",
    version="1.0.0",
    contact={
        "name": "Amar Jaiswal",
        "email": "amar@example.com"
    },
    license_info={
        "name": "MIT License"
    }
)


# -------------------------------
# Home API
# -------------------------------
@app.get("/")
def home():
    return {
        "message": "AI Job Matching API Running Successfully"
    }


# -------------------------------
# Match Student with Job
# -------------------------------
@app.post("/match", response_model=MatchResponse)
def match(request: MatchRequest):

    try:
        return get_match(
            request.student_id,
            request.job_id
        )

    except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e)
        )


# -------------------------------
# Rank Candidates for a Job
# -------------------------------
@app.post("/rank-candidates", response_model=List[Candidate])
def rank(request: RankRequest):

    try:
        return rank_candidates(request.job_id)

    except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e)
        )