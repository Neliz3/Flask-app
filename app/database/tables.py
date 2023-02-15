from dependencies import db

class Users(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100))

    def __init__(self, name, email):
        self.name = name
        self.email = email
