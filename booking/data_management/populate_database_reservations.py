from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import datetime

from booking.bookings.booking_models import Rezerwacja
from booking.clients.client_models import Klient
from booking.employees.employee_models import Pracownik


engine = create_engine("sqlite:///booking/cinema_base.db", echo=True)
Session = sessionmaker(bind=engine)

example_client_data = [
    {
        "email": "jan.kowalski@pwr.edu.pl",
        "telefon": "675431941",
        "imie": "Jan",
        "nazwisko": "Kowalski",
    },
    {
        "email": "szymon.romanek@gmail.com",
        "telefon": "987654321",
        "imie": "Szymon",
        "nazwisko": "Romanek",
    },
    {
        "email": "216931@student.pwr.edu.pl",
        "telefon": "876456888",
        "imie": "Karol",
        "nazwisko": "Nowak",
    },
]

example_employee_data = [
    {
        "id": 4,
        "login": "janowski_4",
        "haslo": "password",
        "imie": "Robert",
        "nazwisko": "Janowski",
        "status": "aktywny",
        "telefon": "456 124 693",
        "czy_kierownik": 0,
    },
    {
        "id": 2,
        "login": "admin",
        "haslo": "admin",
        "imie": "Anna",
        "nazwisko": "Kowalska",
        "status": "aktywny",
        "telefon": "233 455 677",
        "czy_kierownik": 0,
    },
]

example_booking_data = [
    {
        "numer": "24",
        "status": "Potwierdzona",
        "termin_zlozenia": datetime.datetime.utcnow(),
        "termin_waznosci": datetime.datetime(2023, 1, 30),
        "klient_email": "jan.kowalski@pwr.edu.pl",
        "pracownik_id": 4,
    },
    {
        "numer": "26",
        "status": "Anulowana",
        "termin_zlozenia": datetime.datetime.utcnow(),
        "termin_waznosci": datetime.datetime(2023, 1, 20),
        "klient_email": "anna.n@o2.pl",
        "pracownik_id": 2,
    },
    {
        "numer": "27",
        "status": "Potwierdzona",
        "termin_zlozenia": datetime.datetime.utcnow(),
        "termin_waznosci": datetime.datetime(2023, 1, 22),
        "klient_email": "jan.kowalski@pwr.edu.pl",
        "pracownik_id": 4,
    },
]


def add_clients():
    session = Session()

    for data_dict in example_client_data:
        session.add(
            Klient(
                Email=data_dict.get("email"),
                Telefon=data_dict.get("telefon"),
                Imie=data_dict.get("imie"),
                Nazwisko=data_dict.get("nazwisko"),
            )
        )

    session.commit()


def add_employees():
    session = Session()

    for data_dict in example_employee_data:
        session.add(
            Pracownik(
                Id=data_dict.get("id"),
                Login=data_dict.get("login"),
                Hasło=data_dict.get("haslo"),
                Imie=data_dict.get("imie"),
                Nazwisko=data_dict.get("nazwisko"),
                Status=data_dict.get("status"),
                Telefon=data_dict.get("telefon"),
                czyKierownik=data_dict.get("czy_kierownik"),
            )
        )

    session.commit()


def add_bookings():
    session = Session()

    for data_dict in example_booking_data:
        session.add(
            Rezerwacja(
                Numer=data_dict.get("numer"),
                Status=data_dict.get("status"),
                TerminZlozenia=data_dict.get("termin_zlozenia"),
                TerminWaznosci=data_dict.get("termin_waznosci"),
                KlientEmail=data_dict.get("klient_email"),
                PracownikId=data_dict.get("pracownik_id"),
            )
        )

    session.commit()


def populate_database():
    add_clients()
    add_employees()
    add_bookings()


if __name__ == "__main__":
    populate_database()
