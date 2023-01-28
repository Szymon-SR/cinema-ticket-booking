from flask import Flask
from sqlalchemy.ext.declarative import declarative_base
from flask_login import LoginManager
from flask_mail import Mail
# from booking.employees.employee_models import Pracownik
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

engine = create_engine('sqlite:///booking/cinema_base.db', echo=True)
Session = sessionmaker(bind=engine)
session = Session()
mail = Mail()

def create_app():
    app = Flask(__name__)
    
    app.config.from_envvar('BOOKING_SETTINGS', silent=True)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///booking/cinema_base.db'
    app.config['SECRET_KEY'] = 'super-secret'
    app.config['MAIL_SERVER']= 'smtp.gmail.com'
    app.config['MAIL_PORT'] = 465
    app.config['MAIL_USERNAME'] = 'kino.projekt.legit@gmail.com'
    app.config['MAIL_PASSWORD'] = 'haslo'
    app.config['MAIL_USE_TLS'] = False
    app.config['MAIL_USE_SSL'] = True
    mail = Mail(app)


    from booking import db
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'booking.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(Id):
        user = session.query(employees.employee_models.Pracownik).filter(employees.employee_models.Pracownik.Id == Id).first()
        session.close()
        return user

    # apply blueprints
    from booking import booking
    app.register_blueprint(booking.bp)
    app.add_url_rule("/", endpoint="main")
    return app
