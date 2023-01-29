import unittest
import os
import datetime

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask_testing import TestCase
from flask import abort, url_for
from booking import create_app, db

from booking.cinema.cinema_models import Formularz
from booking.bookings.booking_models import Rezerwacja
from booking.clients.client_models import Klient
from booking.employees.employee_models import Pracownik

engine = create_engine("sqlite:///booking/test_base.db", echo=True)
Session = sessionmaker(bind=engine)


class TestBase(TestCase):
    def create_app(self):
        app = create_app()
        return app

    def setUp(self):
        """
        Will be called before every test
        """

        # create test form
        formularz_test = Formularz(
            Id=44,
            Tresc="Witam, chcialbym napisac ze aplikacja do rezerwacji bardzo mi sie podoba, pozdrwiam panstwa serdecznie",
            TerminPrzeslania=datetime.datetime(2023, 1, 14),
            KlientEmail="janek@wp.pl",
            PracownikId=50,
        )

        session = Session()
        session.query(Rezerwacja).delete()
        session.query(Klient).delete()
        session.query(Pracownik).delete()
        session.query(Formularz).delete()
        session.commit()

        # save form to database
        session.add(formularz_test)
        session.commit()

    def tearDown(self):
        """
        Will be called after every test
        """
        session = Session()
        session.query(Rezerwacja).delete()
        session.query(Klient).delete()
        session.query(Pracownik).delete()
        session.query(Formularz).delete()
        session.commit()



# class TestModels(TestBase):
#     def test_form_model(self):
#         """
#         Test number of records in Formularz table
#         """
#         session = Session()

#         self.assertEqual(session.query(Formularz).count(), 1)

#     def test_client_model(self):
#         """
#         Test number of records in Klient table
#         """

#         department = Klient(Email="example@wp.pl", Telefon="348794111", Imie="Jan", Nazwisko="Janek")

#         session = Session()

#         session.add(department)
#         session.commit()

#         self.assertEqual(session.query(Klient).count(), 1)



class TestViews(TestBase):
    def test_homepage_view(self):
        """
        Test that homepage is accessible without login
        """
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_contact_view(self):
        """
        Test that contact page is accessible without login
        """
        response = self.client.get("/contact")
        self.assertEqual(response.status_code, 200)

    def test_login_view(self):
        """
        Test that login page is accessible without login
        """
        response = self.client.get("/contact")
        self.assertEqual(response.status_code, 200)


class TestErrorPages(TestBase):

    def test_404_not_found(self):
        response = self.client.get("/nopage")
        self.assertEqual(response.status_code, 404)

        self.assertTrue("404 Not Found" in str(response.data))



if __name__ == "__main__":
    unittest.main()
