from datetime import datetime, timedelta


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
        return {"student_id": self.student_id, "username": self.username}

    @property
    def status(self):
        now = datetime.now()
        if self.infection_date is None:
            return "healthy"
        if timedelta(days=14) < now - self.infection_date:
            return "vac"


if __name__ == "__main__":
    from loguru import logger

    u = User("username1")
    s = Student(1, "student1")
    s2 = Student(2, "student2")
    logger.info(u.to_upper())
    logger.warning(s.to_lower())
    logger.info(s.student_dictionary())
    logger.error(s2.student_dictionary())
    logger.debug(s.status)
