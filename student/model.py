from datetime import datetime, timedelta

from loguru import logger


class User:
    def __init__(self, username):
        logger.info(f"creating a new user {username}")
        self.username: str = username

    def to_upper(self):
        return self.username.upper()

    def to_lower(self):
        return self.username.lower()


class Student(User):
    def __init__(self, student_id, username, *, infection_date=None):
        logger.debug("creating new student")
        super().__init__(username)
        logger.debug("finished calling super")
        self.username = username
        self.student_id = student_id
        self.infection_date = infection_date

    def student_dictionary(self):
        print({"student_id": self.student_id, "username": self.username})
        return 0


    @property
    def status(self):
        now = datetime.now()
        if self.infection_date is None:
            return "healthy"
        if timedelta(days=14) < now - self.infection_date:
            return "vac"


if __name__ == "__main__":
    import json

    s1 = Student(first_name="z", last_name="z")
    x = 1
    with open(s1.file, "w") as fp:
        json.dump(s1.json(), fp)
