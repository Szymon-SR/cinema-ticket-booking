import flask_login
from flask import Flask, render_template, Blueprint, request, flash, redirect, url_for

# from . import create_app
# app = create_app()
from booking import models, bcrypt

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

@bp.route("/login", methods=['POST'])
def login_post():
    login_form = request.form.get("login")
    password_form = request.form.get("password")

    user = models.Pracownik.query.filter_by(Login=login_form).first()
    if user and (password_form == user.Hasło):
        flask_login.login_user(user)

        return redirect(url_for("booking.employee"))
        flash("Zalogowano", 'success')
    else:
        # Wrong email and/or password

        return redirect(url_for("booking.login"))
        flash("Niepoprawne dane.", 'error')

@bp.route("/employee")
@flask_login.login_required
def employee():
    current_user = flask_login.current_user.Id
    return render_template('employee_account.html', id=current_user)

@bp.route("/employee/logout")
@flask_login.login_required
def logout():
    flask_login.logout_user()
    flash("Wylogowano", 'success')
    return redirect(url_for("booking.login"))


@bp.route("/employee/contact")
@flask_login.login_required
def employee_contact_form():
    # contact_forms = models.
    return render_template('contact_form_records.html', all_messages = shows_mocks)

@bp.route("/employee/reservations")
@flask_login.login_required
def employee_reservations():
    # shows_mocks = ["xd", "xd"]
    reservations = models.Rezerwacja.query.all()

    return render_template('reservations_records.html', all_reservations = reservations)

@bp.route("/employee/contact/answer")
@flask_login.login_required
def employee_answer():
    return render_template('contact_form_answer.html')

@bp.route("/employee/reservations/details")
@flask_login.login_required
def employee_reservation_details():
    return render_template('reservation_details.html')
