from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import func
from sqlalchemy.orm import load_only
from flask_mail import Mail, Message

import random
import datetime

from booking.cinema.cinema_models import Formularz
from booking.employees.employee_models import Pracownik

# do not look-----
MIN_EMPLOYYE_ID = 4
MAX_EMPLOYEE_ID = 4
# do not look-----

engine = create_engine("sqlite:///booking/cinema_base.db", echo=True)
Session = sessionmaker(bind=engine)

mail = Mail()


def add_contact_form_to_database(message: str, email: str):
    session = Session()

    # a random employee is assigned to handle the contact btw
    randomly_assigned_employye_id = random.randint(MIN_EMPLOYYE_ID, MAX_EMPLOYEE_ID)
    session.add(
        Formularz(
            Tresc=message,
            TerminPrzeslania=datetime.datetime.utcnow(),
            KlientEmail=email,
            PracownikId=randomly_assigned_employye_id,
        )
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
