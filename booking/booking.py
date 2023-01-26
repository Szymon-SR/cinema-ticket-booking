import datetime
import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from flask import Flask, render_template, Blueprint, request, redirect, url_for, flash
import flask_login

# from booking.cinema.cinema_models import Seans
from booking.data_management.manage_form_data import add_contact_form_to_database
from booking.employees.employee_models import Pracownik
from booking.cinema.cinema_models import Formularz
from booking.bookings.booking_models import Rezerwacja



# from . import create_app
# app = create_app()

engine = create_engine('sqlite:///booking/cinema_base.db', echo=True)
Session = sessionmaker(bind=engine)
session = Session()

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

@bp.route("/login", methods=['GET', 'POST'])
def login_post():
    
    login_form = request.form.get("login")
    password_form = request.form.get("password")

    user = session.query(Pracownik).filter(Pracownik.Login == login_form).first()
    if user and (password_form == user.Hasło):
        flask_login.login_user(user)

        return redirect(url_for("booking.employee"))
        flash("Zalogowano", 'success')
    else:
        return redirect(url_for("booking.login"))
        flash("Niepoprawne dane.", 'error')

@bp.route("/employee")
@flask_login.login_required
def employee():
    current_user = flask_login.current_user.Id
    return render_template('employee_account.html', id = current_user)

@bp.route("/employee/contact")
@flask_login.login_required
def employee_contact_form():
    contact_forms = session.query(Formularz).filter(Formularz.Odpowiedz == None).all()
    return render_template('contact_form_records.html', all_messages = contact_forms)

@bp.route("/employee/reservations")
@flask_login.login_required
def employee_reservations():
    reservations = session.query(Rezerwacja).all()
    return render_template('reservations_records.html', all_reservations = reservations)

@bp.route("/employee/reservations", methods=['POST'])
@flask_login.login_required
def employee_reservations_post():
    if request.method == 'POST':
        search_id = (int)(request.form.get("res_id"))
        search = session.query(Rezerwacja).filter(Rezerwacja.Numer == search_id).first()
        if (search != None):
            flash("Znaleziono", 'success')
            return redirect(url_for("booking.employee_reservation_details", id = search.Numer))
            
        else:
            flash("Nie znaleziono", 'error')
            return redirect(url_for("booking.employee_reservations"))
    
    else:
        return redirect(url_for("booking.employee_reservations"))

@bp.route("/employee/contact/answer/<int:id>")
@flask_login.login_required
def employee_answer(id):
    message = session.query(Formularz).filter(Formularz.Id == id).first()
    return render_template('contact_form_answer.html', email = message.KlientEmail, data = message.TerminPrzeslania, tresc = message.Tresc)

@bp.route("/employee/reservations/details/<int:id>")
@flask_login.login_required
def employee_reservation_details(id):
    reservation = session.query(Rezerwacja).filter(Rezerwacja.Numer == id).first()
    tickets = random.randint(1, 6)
    return render_template('reservation_details.html', numer = reservation.Numer, dane = reservation.KlientEmail, data = reservation.TerminZlozenia,
             status = reservation.Status, waznosc = reservation.TerminWaznosci, liczba = tickets)


@bp.route("/employee/logout")
@flask_login.login_required
def logout():
    flask_login.logout_user()
    flash("Wylogowano", 'success')
    return redirect(url_for("booking.login"))