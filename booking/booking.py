import datetime

from flask import Flask, render_template, Blueprint, request, redirect
import flask_login

from booking.cinema.cinema_models import Seans
from booking.data_management.manage_form_data import add_contact_form_to_database
# from . import create_app
# app = create_app()

bp = Blueprint("booking", __name__)

@bp.route("/")
def main_page():
    shows_mocks = [
    {"title": "Matrix Zmartwychwstania", "date": "27 stycznia", "time": "19:00", "image": "/static/images/matrix.jpg", "description": "Podążaj za Neo, który prowadzi zwyczajne życie w San Francisco, gdzie jego terapeuta przepisuje mu niebieskie pigułki. Jednak Morfeusz oferuje mu czerwoną pigułkę i ponownie otwiera jego umysł na świat Matrix."},
    {"title": "Avatar: Istota wody", "date": "28 stycznia", "time": "17:30", "image": "/static/images/avatar.jpg", "description": "Pandorę znów napada wroga korporacja w poszukiwaniu cennych minerałów. Jack i Neytiri wraz z rodziną zmuszeni są opuścić wioskę i szukać pomocy u innych plemion zamieszkujących planetę."},
    ]

    

    return render_template('main.html', all_shows = shows_mocks)

@bp.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        form = request.form
        
        add_contact_form_to_database(form.get("Message"), form.get("Email"))
        
        return redirect('/')

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