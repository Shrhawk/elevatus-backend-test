import csv
from typing import Dict

from models import Candidate
from schemas.candidates_schema import SearchKeySchema


def add_filters(candidate_filter: SearchKeySchema) -> Dict:
    filters = dict()
    if candidate_filter.first_name:
        filters[Candidate.first_name] = candidate_filter.first_name
    if candidate_filter.last_name:
        filters[Candidate.last_name] = candidate_filter.last_name
    if candidate_filter.email:
        filters[Candidate.email] = candidate_filter.email
    if candidate_filter.uuid:
        filters[Candidate.uuid] = candidate_filter.uuid
    if candidate_filter.career_level:
        filters[Candidate.career_level] = candidate_filter.career_level
    if candidate_filter.job_major:
        filters[Candidate.job_major] = candidate_filter.job_major
    if candidate_filter.years_of_experience:
        filters[Candidate.years_of_experience] = candidate_filter.years_of_experience
    if candidate_filter.degree_type:
        filters[Candidate.degree_type] = candidate_filter.degree_type
    if candidate_filter.skills:
        filters[Candidate.skills] = candidate_filter.skills
    if candidate_filter.nationality:
        filters[Candidate.nationality] = candidate_filter.nationality
    if candidate_filter.city:
        filters[Candidate.city] = candidate_filter.city
    if candidate_filter.salary:
        filters[Candidate.salary] = candidate_filter.salary
    if candidate_filter.gender:
        filters[Candidate.gender] = candidate_filter.gender
    return filters


def list_to_csv(data, filename):
    with open(filename, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)
