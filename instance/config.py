import os
import sys
from dotenv import load_dotenv
from sqlalchemy.pool import QueuePool

load_dotenv()
prefix = "sqlite:///" if sys.platform.startswith("win") else "sqlite:////"

SQLALCHEMY_DATABASE_URI = f"{prefix}{os.path.join(os.path.abspath(os.path.dirname(__file__)), 'data.db')}?check_same_thread=False&cache=shared"
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ENGINE_OPTIONS = {
    "poolclass": QueuePool,
    "pool_size": 4,
    "max_overflow": 10,
    "pool_timeout": 30,
    "pool_recycle": 1800,
}
SECRET_KEY = os.getenv("SECRET_KEY")
