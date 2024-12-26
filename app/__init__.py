from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from app.filters import utc_timestamp_to_shanghai_datetime

app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile("config.py")

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = "login"


@login_manager.user_loader
def load_user(user_id):
    from app.models import Admins

    user = Admins.query.get(int(user_id))
    return user


app.add_template_filter(utc_timestamp_to_shanghai_datetime)


from app import routes, errors, commands  # noqa
