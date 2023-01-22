from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import datetime

from booking.cinema.cinema_models import Formularz




engine = create_engine('sqlite:///booking/cinema_base.db', echo=True)
Session = sessionmaker(bind=engine)

def add_contact_form_to_database():
    session = Session()

    session.add(
        Formularz()
    )

    session.commit()

