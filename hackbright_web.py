"""A web application for tracking projects, students, and student grades."""

from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)


@app.route("/student", methods=["GET"])
def get_student():
    """Show information about a student."""

    github = request.args.get('github')

    first, last, github = hackbright.get_student_by_github(github)

    project_grades = hackbright.get_grades_by_github(github)

    return render_template("student_info.html",
                           first=first,
                           last=last,
                           github=github,
                           project_grades=project_grades)


@app.route("/student-search")
def get_student_form():
    """Show form for searching for a student."""

    return render_template("student_search.html")


@app.route("/add-student-form")
def add_student_form():
    """Show form for adding a student."""

    return render_template("add_student.html")


@app.route("/student-add", methods=['POST'])
def student_add():
    """Add a student."""

    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    github = request.form.get('github')

    hackbright.make_new_student(first_name, last_name, github)

    return render_template("added_student.html", 
                            first=first_name, 
                            last=last_name, 
                            github=github)


@app.route("/project-form")
def project_form():
    """Show form for searching for a project."""

    return render_template("project_form.html")


@app.route("/project")
def get_project_info():
    """Display project info."""

    title = request.args.get('title')

    project_info = hackbright.get_project_by_title(title)

    return render_template("project_desc.html", 
                            project_info=project_info)

if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True)
