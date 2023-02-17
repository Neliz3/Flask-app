from app.auth import auth
from app.admin import admin
from app.general import general
from app.user import user
from app import app, db

app.register_blueprint(general.general)
app.register_blueprint(auth.auth)
app.register_blueprint(admin.admin, url_prefix='/admin')
app.register_blueprint(user.user, url_prefix='/user')


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(port=5555)
