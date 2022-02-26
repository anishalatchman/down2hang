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

    def find_next_course(self) -> Course:
        """Return next most upcoming course from current time.

        Return None if there are no more courses scheduled for the day.

        For use in: Student is available! But hurry, their next course, CSC110H1, starts at 13:00.
        """
        current_time = datetime.datetime.now() # current time can also be passed in if necessary
        next_course_so_far = current_time
        for course in self.courses: # find next upcoming course in the day
            if course.start > current_time and course.start <= next_course_so_far:
                next_course_so_far = course
        if next_course_so_far == current_time: # if there are no upcoming courses in the day
            return None
        return course

    def is_next_course_soon(self, next_course = Course) -> bool:
        """Calculate time to next course and return whether next course is too close to current time.
        'Too close' means <= 30 minutes away
        
        Determines default or hurry message: 
        Student is available! Their next course, CSC110H1, starts at 13:00.
        Student is available, but their next course, CSC110H1, starts soon at 13:00.
        """
        current_time = datetime.datetime.now()
        time_difference = next_course.start - current_time
        if time_difference.hour == 0:
            return time_difference.minute <= 30
        return False

@dataclass
class Hangout:
    """ Class which holds data about a proposed hangout date/time, inviter, and invitees.
    """
    date: datetime
    inviter: Student
    invitees: list[Student]

    def does_course_conflict(self, course: tuple[datetime, datetime]) -> bool:
        """Return whether course conflicts with this potential hangout time.
        Return True if there is a conflict, False if there is not.
        
        Preconditions:
            - Hangout/course start and end must be on the same weekday (Mon = 0, Sun = 6)
            - Assume all courses start and end on a full hour
        """
        if self.date.weekday == course[0].weekday: # course occurs on same day
            course_time_range = set(range(course[1].hour, course[2].hour))
            return self.date.hour in course_time_range
        else:
            return False