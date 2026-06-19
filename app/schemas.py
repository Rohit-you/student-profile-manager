from pydantic import BaseModel
from typing import List


class MatchRequest(BaseModel):
    student_id: int
    job_id: int


class MatchResponse(BaseModel):
    student_id: int
    student_name: str
    job_id: int
    company: str
    match_score: float
    status: str
    reason: List[str]


class RankRequest(BaseModel):
    job_id: int


class Candidate(BaseModel):
    rank: int
    student_id: int
    student_name: str
    match_score: float
    status: str