from flask import Flask, render_template, Blueprint

# from . import create_app
# app = create_app()

bp = Blueprint("booking", __name__)

@bp.route("/")
def hello_world():
    shows_mocks = ["xd", "xd"]

    

    return render_template('main.html', all_shows = shows_mocks)

@bp.route("/contact")
def contact():
    return render_template('contact_form.html')

@bp.route("/login")
def login():
    return render_template('user_login.html')

@bp.route("/employee")
def employee():
    return render_template('employee_account.html')

@bp.route("/employee/contact")
def employee_contact_form():
    shows_mocks = ["xd", "xd"]
    return render_template('contact_form_records.html', all_messages = shows_mocks)

@bp.route("/employee/reservations")
def employee_reservations():
    shows_mocks = ["xd", "xd"]
    return render_template('reservations_records.html', all_reservations = shows_mocks)

@bp.route("/employee/contact/answer")
def employee_answer():
    return render_template('contact_form_answer.html')

@bp.route("/employee/reservations/details")
def employee_reservation_details():
    return render_template('reservation_details.html')
