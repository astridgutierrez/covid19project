from typing import Optional

from fastapi import FastAPI

from student.endpoints import router as student_router
from classroom.endpoints import router as classroom_router

app = FastAPI(title='COVID Tracking Project')

app.include_router(student_router, prefix="/student")
app.include_router(classroom_router, prefix="/classroom")


@app.get("/reset")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
