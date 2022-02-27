from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, DateField, DateTimeField, FileField, SubmitField, Label
from wtforms.validators import DataRequired, regexp

class AddFriend(FlaskForm):
    student_name = StringField('Enter a name for this friend', validators=[DataRequired()])
    file = FileField("Upload an iCalender file", validators=regexp(u'^[^/\\]\.ics$'))
    selected_file_txt = Label("Selected file: f{file}")

class HomeForm(FlaskForm):
    question_1 = Label("1. Who would you like to hang out with?")
    question_2 = Label("1. Who would you like to hang out with?")

    def create_checkboxes(self, students):
        checkboxes = []
        for student in students:
            checkboxes.append(BooleanField("f{student.name}"))

    date = DateField('When would you like to hang out?')
    show_time = BooleanField("Specify time")
    datetime = DateTimeField("When would you like to hang out?")