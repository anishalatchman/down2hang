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
from StudentCourse import Course, Student, Students
from Hangout import Hangout

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

def convert_to_12_hour(hour: int) -> int:
    """Return converted 24-hour time to 12-hour time.

    AM and PM stamps are unneccsary and implied by time of use.

    Preconditons:
        - 0 <= hour <= 23
        - 1 <= Return value <= 12
    """
    hour += 1 # start index at 1 instead of 0
    if hour > 12:
        return hour - 12
    else:
        return hour

def ouput_group_availabilities(group: Students) -> None:
    """Return avaialble times for all students in group.

    Return empty list if every student has no availability.

    Hours are stored from 0-23, then converted to 12-hr time in convert_to_12_hour().
    """
    str_hours = ""
    for student in group.students:
        for hour in student.availabiltiy:
            str_hours += ', ' + convert_to_12_hour(hour)
        if str_hours == "":
            output = "Uh oh. f{student.name} has no available hours."
        else:
            output = "f{student.name} is available at f{str_hours}"

