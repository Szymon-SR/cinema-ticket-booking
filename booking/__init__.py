from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

bcrypt = Bcrypt()


def create_app():
    app = Flask(__name__)

    app.config.from_envvar('BOOKING_SETTINGS', silent=True)
    app.config['SECRET_KEY'] = 'super-secret'


    from booking import db
    db.init_app(app)
    # db = SQLAlchemy(app)

    login_manager = LoginManager()
    login_manager.login_view = 'booking.login'
    # login_manager.login_message = "Login or Change role."
    login_manager.init_app(app)
    from . import models
    @login_manager.user_loader
    def load_user(Id):
        return models.Pracownik.query.get(int(Id))

    # apply blueprints
    from booking import booking
    app.register_blueprint(booking.bp)
    app.add_url_rule("/", endpoint="main")
    return app