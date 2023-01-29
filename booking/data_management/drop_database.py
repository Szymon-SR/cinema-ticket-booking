from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


from booking.bookings.booking_models import Rezerwacja
from booking.clients.client_models import Klient
from booking.employees.employee_models import Pracownik

Base = declarative_base()

engine = create_engine('sqlite:///booking/cinema_base.db', echo=True)
Session = sessionmaker(bind=engine)

def delete_reservations():
    session = Session()

    try:
        num_rows_deleted = session.query(Rezerwacja).delete()
        session.commit()
    except:
        session.rollback()


def delete_clients():
    session = Session()

    try:
        num_rows_deleted = session.query(Klient).delete()
        session.commit()
    except:
        session.rollback()


def delete_employees():
    session = Session()

    try:
        num_rows_deleted = session.query(Pracownik).delete()
        session.commit()
    except:
        session.rollback()


if __name__ == "__main__":
    delete_reservations()
    delete_clients()
    delete_employees()
