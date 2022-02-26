""" 
WiCHacks 2022 Submission: down 2 hang scheduling solution

Anisha Latchman

Languages/Packages used:
    - Python 3.10
    - icalendar 4.0.9
    - datetime
    - pytz
"""
from icalendar import Calendar, Event
from datetime import datetime
from pytz import UTC # provides UTC timezone
from StudentCourse import Course, Student

def convert_ical_to_courses(filename: str) -> list[Course]:
    """Retrieve DESCRIPTION, DTSTART, DTEND for each BEGIN:VEVENT, 
    convert to Course objects, and return as list of Course objects.
    """
    courses_so_far = []
    sched = open(filename,'rb')
    sched_cal = Calendar.from_ical(sched.read())
    for component in sched_cal.walk():
        if component.name == "VEVENT":
            code = component.get('SUMMARY').split()[0]
            name = component.get('DESCRIPTION').split('\n')[0]
            start = component.get('DTSTART').dt
            end = component.get('DTEND').dt
        courses_so_far.append(Course(code, name, start, end))
    sched.close()
    return courses_so_far

def create_student(name: str, courses: list[Course]) -> Student:
    return Student(name, courses)