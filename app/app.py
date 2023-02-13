from flask import Flask, render_template, request, redirect, url_for, session
from configs import config
from datetime import timedelta

app = Flask(__name__)

app.secret_key = config.secret_key
app.permanent_session_lifetime = timedelta(days=30)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        session.permanent = True
        user = request.form["nm"]
        session["user"] = user
        return redirect(url_for("users"))
    else:
        if "user" in session:
            return redirect(url_for("users"))

        return render_template("login.html")


@app.route("/user")
def users():
    if "user" in session:
        user = session["user"]
        return f"<h1>{user}</h1>"
    else:
        return redirect(url_for("login"))


@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))



if __name__ == '__main__':
    app.run(debug=True)
