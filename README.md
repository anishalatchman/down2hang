# Down 2 Hang?
A modern solution to group scheduling at the University of Toronto. 🏙️

# The problem 🔴
Socialization is an important part of the university experience. Many freshman students build strong group relationships during frosh week, but hanging out in groups becomes a challenge when school starts and friends have different course schedules. It takes endless messaging back and forth to find a time when everyone in a group is free and down to hang out. Enter us.

# The solution 🟢
Down 2 hang is a one-stop scheduling solution for UofT students looking to organize group hangouts. The app can coordinate the course schedules of up to 20 students to find dates and times when any selection of people are out of class and free to hang out.

# The implementation 💻
The app reads .ical file formats (which can be exported from ACORN), stores each student’s schedule, and displays each student’s availability on the home page. The program has 2 input fields:
    1) To find when a specified group of people are collectively available.
    2) To find general availability at a specified date and time.
The program uses Python and Object Oriented Programing to store each schedule as a Student object and compare conflicts in everyone’s schedules.
