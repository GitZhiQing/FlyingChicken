from app import db
import time

from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class Admins(db.Model, UserMixin):
    __tablename__ = "admins"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def set_password_hash(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Records(db.Model):
    __tablename__ = "records"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    phone = db.Column(db.String(11), nullable=False)
    check_in_time = db.Column(db.Integer, default=lambda: int(time.time()))


class Event(db.Model):
    __tablename__ = "event"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    date = db.Column(db.String(20), nullable=False)
    desc = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)

    @staticmethod
    def set_event(name, date, desc, location):
        db.session.query(Event).delete()
        new_event = Event(name=name, date=date, desc=desc, location=location)
        db.session.add(new_event)
        db.session.commit()
