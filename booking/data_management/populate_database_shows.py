# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker

# import datetime

# from cinema.cinema_models import Seans
# from booking.bookings.booking_models import Rezerwacja
# from booking.clients.client_models impo<rt Klient
# from booking.employees.employee_models import Pracownik


# engine = create_engine('sqlite:///booking/cinema_base.db', echo=True)
# Session = sessionmaker(bind=engine)


# def add_shows():
#     session = Session()

#     session.add(
#         Seans(Id=0, Termin=datetime.datetime(2023, 1, 27), Status="Zaplanowany", NumerSali=4, Film)
#     )

#     session.commit()


# def populate_database():
#     add_shows()


# if __name__ == "__main__":
#     populate_database()
