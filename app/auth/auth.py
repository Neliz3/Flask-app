from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from app import db
from app.models import Users
from config import admin

auth = Blueprint("auth", __name__, static_folder="static", template_folder="templates")

@auth.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        #db
        email = request.form["email"]
        found_user = Users.query.filter_by(email=email).first()
        if found_user:
            _password = request.form["pswd"]
            if _password == found_user.password:
                session.permanent = True
                user = found_user.name
                session["user"] = user
                flash("Login successful", "info")

                # Authorization
                if email == admin:
                    return redirect(url_for("admin.view"))
                else:
                    return redirect(url_for("general.users"))
            else:
                flash("You entered a wrong password. Try again, please.", "info")
                return redirect(url_for("auth.login"))
        else:
            flash("You are a new user. Welcome to registration page :)", "info")
            return redirect(url_for("auth.registration"))
    else:
        if "user" in session:
            # autocompleting
            return redirect(url_for("general.users"))
        return render_template("auth/login.html")


@auth.route("/signup", methods=['GET', 'POST'])
def registration():
    if request.method == "POST":
        # Try/except unique of name/...
        name = request.form["nm"]
        email = request.form["email"]
        password = request.form["pswd"]

        usr = Users(name, email, password)
        db.session.add(usr)
        db.session.commit()

        session.permanent = True
        session["user"] = name

        flash("Thanks for the registration!")
        if email == admin:
            return redirect(url_for("general.view"))
        else:
            return redirect(url_for("general.users"))
    else:
        return render_template("auth/signup.html")


@auth.route("/logout")
def logout():
    flash("You have been log out!", "info")
    session.pop("user", None)
    session.pop("email", None)
    session.pop("password", None)
    return redirect(url_for("auth.login"))
