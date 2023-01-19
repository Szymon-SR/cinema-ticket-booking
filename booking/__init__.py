from flask import Flask
from sqlalchemy.ext.declarative import declarative_base
from flask_login import LoginManager


Base = declarative_base()

def create_app():
    app = Flask(__name__)
    
    app.config.from_envvar('BOOKING_SETTINGS', silent=True)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///booking/cinema_base.db'

    from booking import db
    db.init_app(app)

    # login_manager = LoginManager()
    # login_manager.login_view = 'booking.login'
    # login_manager.init_app(app)

    # apply blueprints
    from booking import booking
    app.register_blueprint(booking.bp)
    app.add_url_rule("/", endpoint="main")
    return app
