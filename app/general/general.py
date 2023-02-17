from flask import Blueprint, render_template

general = Blueprint("general", __name__, static_folder="static", template_folder="templates")

@general.route("/")
@general.route("/home")
def home():
    return render_template("general/index.html")
