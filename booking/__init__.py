from flask import Flask
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

def create_app():
    app = Flask(__name__)
    
    app.config.from_envvar('BOOKING_SETTINGS', silent=True)

    from booking import db
    db.init_app(app)

    # apply blueprints
    from booking import booking
    app.register_blueprint(booking.bp)
    app.add_url_rule("/", endpoint="main")
    return app
