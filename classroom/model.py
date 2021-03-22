from loguru import logger


class Class:
    def __init__(self, course_abbreviation):
        logger.info(f"creating a new classroom {course_abbreviation}")
        self.course_abbreviation: str = course_abbreviation


class Classroom(Class):
    def __init__(self, course_abbreviation, level):
        logger.debug("creating new classroom")
        super().__init__(course_abbreviation)
        logger.debug("finished calling super")
        self.course_abbreviation = course_abbreviation
        self.level = level

    def classroom_dictionary(self):
        return {"course_abbreviation": self.course_abbreviation, "level": self.level}


if __name__ == "__main__":
    import json

    s1 = Classroom(course_abbreviation="z", level="z")
    x = 1
    with open(s1.file, "w") as fp:
        json.dump(s1.json(), fp)


