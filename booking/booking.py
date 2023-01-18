from flask import Flask, render_template, Blueprint

# from . import create_app
# app = create_app()

bp = Blueprint("booking", __name__)

@bp.route("/")
def hello_world():
    shows_mocks = ["xd", "xd"]

    

    return render_template('main.html', all_shows = shows_mocks)

@bp.route("/contact")
def contact():
    return render_template('contact_form.html')
