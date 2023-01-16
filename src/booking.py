from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('main.html')

@app.route("/contact")
def contact():
    return render_template('contact_form.html')
