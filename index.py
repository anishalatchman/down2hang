""" 
WiCHacks 2022 Submission: down 2 hang scheduling solution

Anisha Latchman

Languages/Packages used:
    - Python 3.10
    - icalendar 4.0.9
    - datetime
    - pytz

Flask file (with HTML) to build front end of website
"""
from flask import Flask, render_template, wtf
import main
from forms import AddFriend

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", students = [main.Student("Anisha", []), main.Student("Bob", [])])

# @app.route("/add-friend")
# def add_friend():
#     form = AddFriend()
#     return render_template("forms")

# @app.route("/results")
# def results():
#     form = Results()
#     return render_template("forms")


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
