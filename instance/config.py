import os
import sys
from dotenv import load_dotenv


load_dotenv()

prefix = "sqlite:///" if sys.platform.startswith("win") else "sqlite:////"

SQLALCHEMY_DATABASE_URI = (
    f"{prefix}{os.path.join(os.path.abspath(os.path.dirname(__file__)), 'data.db')}"
)
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = os.getenv("SECRET_KEY")
