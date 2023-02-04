import datetime
import uuid
from typing import Dict, List, Optional

from fastapi import APIRouter, HTTPException, status

from common.methods import add_filters, list_to_csv
from models import Candidate
from schemas.candidates_schema import (
    CandidateRequestSchema,
    CandidateResponseSchema,
    CandidateUpdateRequestSchema,
    SearchKeySchema,
)

router = APIRouter(
    prefix="/candidate",
    tags=["candidate"],
    responses={404: {"description": "Not found"}},
)


@router.post("/create", response_model=CandidateResponseSchema)
async def create_candidate(candidate: CandidateRequestSchema) -> Candidate:
    """Create Candidate."""
    candidate_check = await Candidate.find_one(Candidate.email == candidate.email)
    if candidate_check:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail="Email already exists"
        )
    user_data = candidate.dict()
    user_data["uuid"] = str(uuid.uuid4())
    return await Candidate(**user_data).create()


@router.get("/view/{candidate_id}", response_model=CandidateResponseSchema)
async def view_candidate(candidate_id: str) -> Candidate:
    """View Candidate."""
    candidate = await Candidate.find_one(Candidate.uuid == candidate_id)
    if not candidate:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Candidate does not exists"
        )
    return candidate


@router.put("/update/{candidate_id}", response_model=CandidateResponseSchema)
async def update_candidate(
    candidate_id: str, candidate: CandidateUpdateRequestSchema
) -> Optional[Candidate]:
    """Update Candidate data."""
    candidate_check = await Candidate.find_one(Candidate.uuid == candidate_id)
    if not candidate_check:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Candidate does not exists"
        )

    req = {k: v for k, v in candidate.dict().items() if v is not None}
    update_query = {"$set": {field: value for field, value in req.items()}}
    await candidate_check.update(update_query)
    return candidate_check


@router.delete("/delete/{candidate_id}")
async def delete_candidate(candidate_id: str) -> Dict:
    """Delete Candidate."""
    candidate = await Candidate.find_one(Candidate.uuid == candidate_id)
    if not candidate:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Candidate does not exists"
        )
    await candidate.delete()
    return {"message": "Record deleted successfully"}


@router.post("/all-candidates", response_model=List[CandidateResponseSchema])
async def view_all_candidate(candidate_filter: SearchKeySchema) -> [Candidate]:
    """View all Candidates."""
    filters = add_filters(candidate_filter)

    candidate = await Candidate.find(filters).to_list()
    if not candidate:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Candidate does not exists"
        )
    return candidate


@router.get("/generate-report")
async def generate_report() -> Dict:
    """Generate CSV reports."""
    candidates = await Candidate.find({}).to_list()
    if not candidates:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Candidate does not exists"
        )
    candidate_data = [candidate.dict() for candidate in candidates]
    file_name = f"{datetime.datetime.now()}_candidates_data.csv"
    list_to_csv(candidate_data, file_name)
    return {"Status": "Success"}
