import datetime
import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from flask import Flask, render_template, Blueprint, request, redirect, url_for, flash
import flask_login
from flask_mail import Mail, Message

# from booking.cinema.cinema_models import Seans
from booking.data_management.manage_form_data import (
    add_contact_form_to_database,
    send_email,
)
from booking.employees.employee_models import Pracownik
from booking.cinema.cinema_models import Formularz
from booking.bookings.booking_models import Rezerwacja


# from . import create_app
# app = create_app()

engine = create_engine("sqlite:///booking/cinema_base.db", echo=True)
Session = sessionmaker(bind=engine)


bp = Blueprint("booking", __name__)

mail = Mail()


@bp.route("/")
def main_page():
    shows_mocks = [
        {
            "title": "Matrix Zmartwychwstania",
            "date": "27 stycznia",
            "time": "19:00",
            "image": "/static/images/matrix.jpg",
            "description": "Podążaj za Neo, który prowadzi zwyczajne życie w San Francisco, gdzie jego terapeuta przepisuje mu niebieskie pigułki. Jednak Morfeusz oferuje mu czerwoną pigułkę i ponownie otwiera jego umysł na świat Matrix.",
        },
        {
            "title": "Avatar: Istota wody",
            "date": "28 stycznia",
            "time": "17:30",
            "image": "/static/images/avatar.jpg",
            "description": "Pandorę znów napada wroga korporacja w poszukiwaniu cennych minerałów. Jack i Neytiri wraz z rodziną zmuszeni są opuścić wioskę i szukać pomocy u innych plemion zamieszkujących planetę.",
        },
    ]

    return render_template("main.html", all_shows=shows_mocks)


@bp.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        form = request.form

        add_contact_form_to_database(form.get("Message"), form.get("Email"))

        return redirect("/")

    return render_template("contact_form.html")


@bp.route("/login")
def login():
    return render_template("user_login.html")


@bp.route("/login", methods=["GET", "POST"])
def login_post():
    session = Session()

    login_form = request.form.get("login")
    password_form = request.form.get("password")

    user = session.query(Pracownik).filter(Pracownik.Login == login_form).first()
    session.close()
    if user and (password_form == user.Hasło):
        flask_login.login_user(user)
        return redirect(url_for("booking.employee"))

    else:
        flash("Niepoprawne dane.", "error")
        return redirect(url_for("booking.login"))


@bp.route("/employee")
@flask_login.login_required
def employee():
    session = Session()
    current_user = flask_login.current_user.Id
    session.close()
    return render_template("employee_account.html", id=current_user)


@bp.route("/employee/contact")
@flask_login.login_required
def employee_contact_form():
    session = Session()
    contact_forms = session.query(Formularz).filter(Formularz.Odpowiedz == None).all()
    session.close()
    return render_template("contact_form_records.html", all_messages=contact_forms)


@bp.route("/employee/reservations")
@flask_login.login_required
def employee_reservations():
    session = Session()
    reservations = session.query(Rezerwacja).all()
    session.close()
    return render_template("reservations_records.html", all_reservations=reservations)


@bp.route("/employee/reservations", methods=["POST"])
@flask_login.login_required
def employee_reservations_post():
    if request.method == "POST":
        search_id = (int)(request.form.get("res_id"))
        if search_id != None:
            session = Session()
            search = (
                session.query(Rezerwacja).filter(Rezerwacja.Numer == search_id).first()
            )
            session.close()
            if search != None:
                return redirect(
                    url_for("booking.employee_reservation_details", id=search.Numer)
                )

            else:
                flash("Nie znaleziono rezerwacji o podanym numerze.", "error")
                return redirect(url_for("booking.employee_reservations"))
        else:
            flash("Nie znaleziono rezerwacji o podanym numerze.", "error")
            return redirect(url_for("booking.employee_reservations"))
    else:
        return redirect(url_for("booking.employee_reservations"))


@bp.route("/employee/reservations/update/<int:id>", methods=["GET", "POST"])
@flask_login.login_required
def employee_reservations_update(id):
    if request.method == "POST":
        value = request.form.get("status")
        session = Session()
        session.expire_on_commit = False

        search = session.query(Rezerwacja).filter(Rezerwacja.Numer == id).first()
        search.Status = value
        session.commit()
        session.close()
        return redirect(
            url_for("booking.employee_reservation_details", id=search.Numer)
        )

    else:
        flash("Status rezerwacji nie został zmieniony.", "error")
        return redirect(url_for("booking.employee_reservations"))


@bp.route("/employee/contact/answer/send/<int:id>", methods=["GET", "POST"])
@flask_login.login_required
def employee_answer_send(id):
    if request.method == "POST":
        text = request.form.get("odpowiedz")
        if text != None:
            session = Session()
            session.expire_on_commit = False
            search = session.query(Formularz).filter(Formularz.Id == id).first()
            search.Odpowiedz = text
            search.TerminOdpowiedzi = datetime.datetime.utcnow()
            send_email(email=search.KlientEmail, message=text)
            session.commit()
            session.close()

            flash("Wiadomość została wysłana.", "success")
            return redirect(url_for("booking.employee_contact_form"))

    else:
        flash("Wiadomość nie została wysłana. Spróbuj ponownie.", "error")
        return redirect(url_for("booking.employee_contact_form"))


@bp.route("/employee/contact/answer/<int:id>")
@flask_login.login_required
def employee_answer(id):
    session = Session()
    message = session.query(Formularz).filter(Formularz.Id == id).first()
    session.close()
    return render_template(
        "contact_form_answer.html",
        email=message.KlientEmail,
        data=message.TerminPrzeslania,
        tresc=message.Tresc,
        numer=message.Id,
    )


@bp.route("/employee/reservations/details/<int:id>")
@flask_login.login_required
def employee_reservation_details(id):
    session = Session()
    reservation = session.query(Rezerwacja).filter(Rezerwacja.Numer == id).first()
    session.close()
    tickets = random.randint(1, 6)
    return render_template(
        "reservation_details.html",
        numer=reservation.Numer,
        dane=reservation.KlientEmail,
        data=reservation.TerminZlozenia,
        status=reservation.Status,
        waznosc=reservation.TerminWaznosci,
        liczba=tickets,
    )


@bp.route("/employee/logout")
@flask_login.login_required
def logout():
    flask_login.logout_user()
    flash("Wylogowano.", "success")
    return redirect(url_for("booking.login"))
