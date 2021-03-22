from datetime import datetime, timedelta
from http.client import HTTPException
from pydantic import BaseModel
from fastapi import APIRouter
import classroom
import student

router = APIRouter()


class CreateClassroomRequest(BaseModel):
    course_abbreviation: str
    level: int
    students = []


@router.get("/students")
def students(students: int, Student: int):
    return {"row_count": students, "rows": Student}


@router.post("/create")
def create_ep(course_abbreviation: str, level: int):
    # students = Classroom(course_abbreviation, level)
    students = [course_abbreviation, level]
    classroom = []
    if students not in classroom:
        classroom.append(students)
    return classroom


@router.post("/update_try_catch")
def update_ep(index: int, new_course_abbreviation: str, level: int, method: str = "add"):
    try:
        if new_course_abbreviation is not None:
            classroom[index].course_abbreviation = new_course_abbreviation
        if method == "add":
            classroom[index].classroom.append(level)

    except Exception:
        return "there was an issue"


@router.get("/update")
def update1_ep(index: int, new_course_abbreviation: str, level: int, method: str = "add"):
    if index > len(classroom):
        raise HTTPException(422, "index out of range")
    h = classroom[index]
    h.course_abbreviation = new_course_abbreviation
    if method == "add":
        h.level.append(level)
    return h


@router.post("/read")
def read():
    print(type(classroom[0]))
    return classroom


@router.get("/attendance")
def attendance(date: datetime, req: CreateClassroomRequest, status: str):
    d = {'present': [date],
         'online': [req.course_abbreviation],
         'sick': [status]

         }


@router.post("/enroll_student")
def enroll_student_ep():
    return


@router.post("/remove_student")
def remove_student_ep():
    return


@router.delete("/delete")
def read():
    return "there was an issue"
