from flask import Flask, render_template, Blueprint, request


from booking.data_management.manage_form_data import add_contact_form_to_database
# from . import create_app
# app = create_app()

bp = Blueprint("booking", __name__)

@bp.route("/")
def hello_world():
    shows_mocks = ["xd", "xd"]

    

    return render_template('main.html', all_shows = shows_mocks)

@bp.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        form = request.form
        
        add_contact_form_to_database()
        
        return redirect('/')

    return render_template('contact_form.html')
