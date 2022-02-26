""" 
WiCHacks 2022 Submission: down 2 hang scheduling solution

Anisha Latchman

Contains classes to be imported into main.py
"""
from dataclasses import dataclass
from datetime import datetime
from StudentCourse import Course, Student, Students

@dataclass
class Hangout:
    """ Class which holds data about a proposed hangout date/time, inviter, and invitees.
    """
    date: datetime
    inviter: Student
    invitees: list[Student]

    def has_course_conflict(self, course: Course) -> bool:
        """Return whether course conflicts with this potential hangout time.
        Return True if there is a conflict, False if there is not.
        
        Preconditions:
            - Hangout/course start and end must be on the same weekday (Mon = 0, Sun = 6)
            - Assume all courses start and end on a full hour (0-23 hrs)
        """
        if self.date.weekday == course.start.weekday: # course occurs on same day
            course_time_range = set(range(course.start.hour, course.start.hour))
            return self.date.hour in course_time_range
        else:
            return False