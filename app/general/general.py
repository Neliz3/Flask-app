from flask import Blueprint, render_template, session, flash, redirect, url_for

general = Blueprint("general", __name__, static_folder="static", template_folder="templates")

@general.route("/")
@general.route("/home")
def home():
    return render_template("general/index.html")


@general.route("/user")
def users():
    if "user" in session:
        user = session["user"]
        return render_template("general/user.html", user=user)
    else:
        flash("You're not logged in", "info")
        return redirect(url_for("auth.login"))
