""" 
WiCHacks 2022 Submission: down 2 hang scheduling solution

Anisha Latchman

Contains classes to be imported into main.py
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

class Student:
    """ Class which holds data about a student's name, list of courses, and list of available times.

    Need to initialise with empty availability list, then update afterwards
    """
    name: str
    courses: list[Course]
    availabiltiy: set

    def __init__(self, name: str, courses: list[Course]) -> None:
        self.name = name
        self.courses = courses
        self.availabiltiy = self.find_available_times()

    def find_available_times(self) -> set[int]:
        """Return list of all hours between 8:00-10PM/22:00 where student is not in a class.

        Return an empty set if there are no free hours in the day.

        Hours are stored from 0-23, then converted to 12-hr time in main.convert_to_12_hour().
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

    def find_common_availability(self) -> list:
        """Return common times when all students in this group are available.

        Return empty list if there are no common availabilities.

        Hours are stored from 0-23, then converted to 12-hr time in main.convert_to_12_hour().
        """
        common_availability = []
        for index in range(len(self.students) - 1):
            avail_set = self.students[index].availabiltiy
            common_availability = avail_set.intersection(stud.availability for stud in self.students[index:])
            if common_availability != []:
                break
        return common_availability

@dataclass
class Hangout:
    """ Class which holds data about a proposed hangout date/time, inviter, and invitees.
    """
    date: datetime
    inviter: Student
    invitees: list[Student]
