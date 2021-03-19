from typing import List

from fastapi import APIRouter, HTTPException

from classroom.model import Classroom

router = APIRouter()


@router.get("/create")
def create_ep(color: str):
    students = Classroom(["john"], color)

    return students


@router.get("/read")
def read():
    return "there was an issue"


@router.get("/update")
def update_ep():
    return


@router.get("/students")
def students_ep():
    return


@router.get("/attendance")
def attendance_ep():
    return


@router.get("/enroll_student")
def enroll_student_ep():
    return


@router.get("/remove_student")
def remove_student_ep():
    return


@router.get("/delete")
def delete_ep():
    return
