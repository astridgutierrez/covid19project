from pydantic import BaseModel
from datetime import datetime


# Abbreviation - float
# Level - integer
# Description - string
# days of week - string
# start time - datetime
# end time - datetime
# Professor - string
# Students - list of students

class Classroom(BaseModel):
    abbreviation: float
    level: str
    description: str
    days_of_week: str
    start_time: datetime
    end_time: datetime
    professor: str
    students: list


print(Classroom.__fields__.keys())
if __name__ == "__main__":
    import json

    s1 = Classroom(first_name="z", last_name="z")
    x = 1
    with open(s1.file, "w") as fp:
        json.dump(s1.json(), fp)
