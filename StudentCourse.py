""" 
WiCHacks 2022 Submission: down 2 hang scheduling solution

Anisha Latchman

Contains classes to be imported into main.py
"""
from dataclasses import dataclass
from datetime import datetime
from Hangout import Hangout

@dataclass
class Course:
    """ Class which holds data about a course's code/summary, name/description, start date, and end date.
    """
    code: str
    name: str
    start: datetime
    end: datetime

class Student:
    """ Class which holds data about a student's name, list of courses, and list of available times.

    Need to initialise with empty availability list, then update afterwards
    """
    name: str
    courses: list[Course]
    availabiltiy: list[datetime]

    def __init__(self, name: str, courses: list[Course]) -> None:
        self.name = name
        self.courses = courses
        self.availabiltiy = self.find_available_times()

    def is_available(self, hangout: Hangout) -> bool:
        """Return whether student is out of classes at given hangout time.
        """
        for course in self.courses:
            if hangout.has_course_conflict(hangout):
                return False
        return True

    def find_available_times(self) -> set[int]:
        """Return list of all hours between 8:00-10PM/22:00 where student is not in a class

        Hours are stored from 0-23, then converted to 12-hr time in main.convert_to_12_hour()
        """
        free_hours = set(range(0,24)) # range start inclusive, end exclusive
        for course in self.courses:
            course_hours = range(course.start.hour, course.end.hour)
            free_hours = free_hours.difference(course_hours)
        return free_hours

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
class Students:
    """ Class which holds a collection of Students.
    """
    students: list[Student]

    def find_whos_available(self, hangout: Hangout) -> list:
        """Return list of all students in self who are available at the given datetime.

        Return an empty list if no students are available.
        """
        available_students = []
        for student in self.students:
            if student.is_available_at(hangout):
                available_students.append(student)
        return available_students


