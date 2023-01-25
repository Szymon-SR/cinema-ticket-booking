from flask import Flask
from sqlalchemy.ext.declarative import declarative_base
from flask_login import LoginManager
# from booking.employees.employee_models import Pracownik
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

engine = create_engine('sqlite:///booking/cinema_base.db', echo=True)
Session = sessionmaker(bind=engine)
session = Session()

def create_app():
    app = Flask(__name__)
    
    app.config.from_envvar('BOOKING_SETTINGS', silent=True)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///booking/cinema_base.db'
    app.config['SECRET_KEY'] = 'super-secret'


    from booking import db
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'booking.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(Id):
        return session.query(employees.employee_models.Pracownik).filter(employees.employee_models.Pracownik.Id == Id).first()


    # apply blueprints
    from booking import booking
    app.register_blueprint(booking.bp)
    app.add_url_rule("/", endpoint="main")
    return app
