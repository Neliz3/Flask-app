from flask import Blueprint, render_template, flash
from app.models import Users
from app import db

admin = Blueprint("admin", __name__, static_folder="static", template_folder="templates")

@admin.route("/view")
@admin.route("/")
def view():
    return render_template("admin/view.html", values=Users.query.all())

@admin.route("/delete/<name>")
def delete(name):
    # db
    found_user = Users.query.filter_by(name=name)
    if found_user.delete():
        db.session.commit()
        flash("This user was deleted!", "info")
    else:
        flash("This name isn't in db!", "info")

    return render_template("admin/view.html", values=Users.query.all())
