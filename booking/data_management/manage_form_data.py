from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import func
from sqlalchemy.orm import load_only
from flask_mail import Mail, Message

import datetime

from booking.cinema.cinema_models import Formularz
from booking.employees.employee_models import Pracownik


engine = create_engine("sqlite:///booking/cinema_base.db", echo=True)
Session = sessionmaker(bind=engine)

mail = Mail()


def add_contact_form_to_database(message: str, email: str):
    session = Session()

    # a random employee is assigned to handle the contact btw
    session.add(
        Formularz(
            Tresc=message,
            TerminPrzeslania=datetime.datetime.utcnow(),
            KlientEmail=email,
            PracownikId=4,
        )  # TODO change hardcoded lmao
    )

    session.commit()


def send_email(email: str, message: str):
    msg = Message(
        "Kino Baszta",
        sender="kino.projekt.legit@gmail.com",
        recipients=["kino.projekt.legit@gmail.com"],
    )
    msg.body = message
    mail.send(msg)
