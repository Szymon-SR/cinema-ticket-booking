from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import func
from sqlalchemy.orm import load_only

import datetime

from booking.cinema.cinema_models import Formularz
from booking.employees.employee_models import Pracownik


engine = create_engine('sqlite:///booking/cinema_base.db', echo=True)
Session = sessionmaker(bind=engine)


def add_contact_form_to_database(message: str, email: str):
    session = Session()

    # a random employee is assigned to handle the contact btw
    session.add(
        Formularz(Tresc=message, TerminPrzeslania=datetime.datetime.utcnow(
        ), KlientEmail=email, PracownikId=4)    # TODO change hardcoded lmao
    )

    session.commit()
