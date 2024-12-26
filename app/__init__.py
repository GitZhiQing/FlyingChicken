import os
import logging
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


@app.before_request
def initialize_database():
    """初始化数据库"""
    from app.models import Admins

    if not os.path.exists(os.path.join(app.instance_path, "data.db")):
        db.create_all()
        admin_name = os.getenv("ADMIN_NAME")
        admin_password = os.getenv("ADMIN_PASSWORD")
        if admin_name and admin_password:
            admin_user = Admins(username=admin_name)
            admin_user.set_password_hash(admin_password)
            db.session.add(admin_user)
            db.session.commit()
            logging.info("管理员账户创建完成.")
        else:
            logging.warning("未设置管理员账户.")
