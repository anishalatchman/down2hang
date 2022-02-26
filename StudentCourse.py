""" 
WiCHacks 2022 Submission: down 2 hang scheduling solution

Anisha Latchman

Student and Course classes to be imported into main.py
"""
from dataclasses import dataclass
from datetime import datetime

@dataclass
class Course:
    """ Class which holds data about a course's code/summary, name/description, start date, and end date.
    """
    code: str
    name: str
    start: datetime
    end: datetime

@dataclass
class Student:
    """ Class which holds data about a student's name, list of courses, and list of available times.
    """
    name: str
    courses: list[Course]
    availabiltiy: list[datetime] # might not need this

@dataclass
class Hangout:
    """ Class which holds data about a proposed hangout date/time, inviter, and invitees.
    """
    date: datetime
    inviter: Student
    invitees: list[Student]

    def check_course_conflict(self, course: tuple[datetime, datetime]) -> bool:
        """Return whether course conflicts with this potential hangout time.
        Return True if there is a conflict, False if there is not.
        
        Precondition:
            - Hangout/course start and end must be on the same weekday (Mon = 0, Sun = 6)
            - Assume all courses start and end on a full hour
        """
        if self.date.weekday == course[0].weekday: # course occurs on same day
            course_time_range = set(range(course[1].hour, course[2].hour))
            return self.date.hour in course_time_range
        else:
            return False