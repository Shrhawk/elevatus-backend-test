from pydantic import EmailStr

from models.base_model import BaseModel


class Candidate(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    uuid: str
    career_level: str
    job_major: str
    years_of_experience: int
    degree_type: str
    skills: list
    nationality: str
    city: str
    salary: float
    gender: str
