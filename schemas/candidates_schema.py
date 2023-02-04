import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel, EmailStr


class CarrerLevelEnum(str, Enum):
    junior = "Junior"
    senior = "Senior"
    mid_level = "Mid Level"


class DegreeTypeEnum(str, Enum):
    bachelor = "Bachelor"
    master = "Master"
    high_school = "High School"


class GenderEnum(str, Enum):
    male = "Male"
    female = "Female"
    not_specified = "Not Specified"


class CandidateRequestSchema(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    career_level: CarrerLevelEnum
    job_major: str
    years_of_experience: int
    degree_type: DegreeTypeEnum
    skills: list
    nationality: str
    city: str
    salary: float
    gender: GenderEnum


class CandidateResponseSchema(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    uuid: str
    career_level: CarrerLevelEnum
    job_major: str
    years_of_experience: int
    degree_type: DegreeTypeEnum
    skills: list
    nationality: str
    city: str
    salary: float
    gender: GenderEnum
    created_on: datetime.datetime
    updated_on: datetime.datetime


class CandidateUpdateRequestSchema(BaseModel):
    career_level: Optional[CarrerLevelEnum]
    job_major: Optional[str]
    years_of_experience: Optional[int]
    degree_type: Optional[DegreeTypeEnum]
    skills: Optional[list]
    nationality: Optional[str]
    city: Optional[str]
    salary: Optional[float]
    gender: Optional[GenderEnum]


class SearchKeySchema(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    email: Optional[EmailStr]
    uuid: Optional[str]
    career_level: Optional[CarrerLevelEnum]
    job_major: Optional[str]
    years_of_experience: Optional[int]
    degree_type: Optional[DegreeTypeEnum]
    skills: Optional[str]
    nationality: Optional[str]
    city: Optional[str]
    salary: Optional[float]
    gender: Optional[GenderEnum]


#
# class SearchKeyEnum(str, Enum):
#     career_level = "career_level"
#     job_major = "job_major"
#     years_of_experience = "years_of_experience"
#     degree_type = "degree_type"
#     skills = Optional[list]
#     nationality = Optional[str]
#     city = Optional[str]
#     salary = Optional[float]
#     gender = Optional[GenderEnum]
#     junior = 'Junior'
#     senior = 'Senior'
#     mid_level = 'Mid Level'
