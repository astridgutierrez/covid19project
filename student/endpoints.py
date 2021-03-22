from datetime import datetime
from fastapi import APIRouter
from pydantic import BaseModel
from loguru import logger


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


@router.post("/read")
def create_ep(req: CreateStudentRequest):
    logger.info(f"{req.first_name} {req.last_name}")
    print()


@router.post("/update")
def create_ep(req: CreateStudentRequest):
    logger.info(f"{req.first_name} {req.last_name}")
    print()


@router.delete("/delete")
def create_ep(req: CreateStudentRequest):
    logger.info(f"{req.first_name} {req.last_name}")
    print()
