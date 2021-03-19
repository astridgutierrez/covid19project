from datetime import datetime

from fastapi import APIRouter
from loguru import logger
from pydantic import BaseModel

router = APIRouter(prefix="/student")


class CreateStudentRequest(BaseModel):
    first_name: str
    last_name: str
    email: str
    infection_date: datetime = None


@router.post("/create")
def create_ep(req: CreateStudentRequest):
    logger.info(f"{req.first_name} {req.last_name}")
    print()
