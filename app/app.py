from flask import render_template, request, redirect, url_for, session, flash
from dependencies import app, db
from database.tables import Users

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/view")
def view():
    return render_template("view.html", values=Users.query.all())


@app.route("/delete/<name>")
def delete(name):
    # db
    found_user = Users.query.filter_by(name=name)
    if found_user.delete():
        db.session.commit()
        flash("This user was deleted!", "info")
    else:
        flash("This name isn't in db!", "info")

    return render_template("view.html", values=Users.query.all())


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        session.permanent = True
        user = request.form["nm"]
        session["user"] = user

        #db
        found_user = Users.query.filter_by(name=user).first()
        if found_user:
            session["email"] = found_user.email
        else:
            usr = Users(user, "")
            db.session.add(usr)
            db.session.commit()

        flash("Login successful", "info")
        return redirect(url_for("users"))
    else:
        if "user" in session:
            flash("Already logged!", "info")
            return redirect(url_for("users"))

        return render_template("login.html")


@app.route("/user", methods=['GET', 'POST'])
def users():
    email = None
    if "user" in session:
        user = session["user"]
        if request.method == "POST":
            email = request.form["email"]
            session["email"] = email
            # db
            found_user = Users.query.filter_by(name=user).first()
            found_user.email = email
            db.session.commit()

            flash("Email was saved!", "info")
        else:
            if "email" in session:
                email = session["email"]
        return render_template("user.html", email=email, user=user)
    else:
        flash("You're not logged in", "info")
        return redirect(url_for("login"))


@app.route("/logout")
def logout():
    flash("You have been log out!", "info")
    session.pop("user", None)
    session.pop("email", None)
    return redirect(url_for("login"))


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
