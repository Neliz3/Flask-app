from flask import Blueprint, render_template, session, flash, redirect, url_for

user = Blueprint("user", __name__, static_folder="static", template_folder="templates")


@user.route("/")
def users():
    if "user" in session:
        _user = session["user"]
        return render_template("user/user.html", user=_user)
    else:
        flash("You're not logged in", "info")
        return redirect(url_for("auth.login"))
